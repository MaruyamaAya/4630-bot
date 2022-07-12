'''复读姬'''
from collections import defaultdict
from nonebot import on_message
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot, MessageSegment
import time
import random
import re


class CACHE:
    REPEAT_AFTER = 4  # 在于第(REPEAT_AFTER+1)位复读
    NUM_MEMO = 3  # 最多复读连续NUM_MEMO条消息组合 a.k.a. 间隔(NUM_MEMO-1)条消息无法打断复读

    last_msg = defaultdict(lambda: [Message() for _ in range(CACHE.NUM_MEMO)])
    msg_count = defaultdict(lambda: [0] * CACHE.NUM_MEMO)
    msg_time = defaultdict(lambda: [0] * CACHE.NUM_MEMO)


class BREAKER:
    # 概率
    P_PRONOUN = 0.1

    # 代词替换
    PNLIST = [
        '我俺咱',
        '你您恁',
        '他她它',
    ]
    PNALL = ''.join(PNLIST)
    PN_GREP = re.compile('[' + PNALL + ']')

    def _pronoun_switch(self, msg):
        # 一二人称
        while 1:
            rep_i = random.randrange(3)
            rep_you = random.randrange(3)
            if rep_i != rep_you and (rep_i != 0 or rep_you != 1):
                break
        # 第三人称
        rep_them = {k: random.choice(self.PNALL) for k in self.PNLIST[2]}

        # 替换
        def _sub(p):
            p = p.group()
            if p in self.PNLIST[0]:
                return random.choice(self.PNLIST[rep_i])
            if p in self.PNLIST[1]:
                return random.choice(self.PNLIST[rep_you])
            return rep_them.get(p, p)

        for seg in msg:
            if seg.type != 'text':
                continue
            seg.data['text'] = self.PN_GREP.sub(_sub, seg.data['text'])

    def __call__(self, msg):
        if random.random() < self.P_PRONOUN:
            self._pronoun_switch(msg)


BREAKER = BREAKER()


def checkMsgEqual(msg1, msg2):
    if len(msg1) != len(msg2):
        return False
    for s1, s2 in zip(msg1, msg2):
        if s1.type != s2.type:
            return False
        if s1.type == 'image':
            if s1.data.get('file') != s2.data.get('file'):
                return False
        elif s1.data != s2.data:
            return False
    return True


repeater = on_notice(priority=10, block=False)


@repeater.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if getattr(event, 'message_type', None) != 'group':
        return
    group_id = getattr(event, 'group_id', None)
    if not group_id:
        return

    msg = event.get_message()
    msg_memo = CACHE.last_msg[group_id]
    cnt_memo = CACHE.msg_count[group_id]
    time_memo = CACHE.msg_time[group_id]

    # 尝试复读
    for i in range(CACHE.NUM_MEMO):
        last_msg = msg_memo[i]
        if checkMsgEqual(msg, last_msg):
            cnt_memo[i] += 1
            if cnt_memo[i] == CACHE.REPEAT_AFTER:
                BREAKER(msg)
                await repeater.send(msg)
            return

    # 尝试替换
    i_lru = min(range(CACHE.NUM_MEMO), key=lambda i: time_memo[i])
    msg_memo[i_lru] = msg
    cnt_memo[i_lru] = 1
    time_memo[i_lru] = time.time()
