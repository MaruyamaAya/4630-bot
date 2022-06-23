'''复读姬'''
from collections import defaultdict
from nonebot import on_message
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot, MessageSegment


class CACHE:
    REPEAT_AFTER = 5

    last_msg = defaultdict(Message)
    msg_count = defaultdict(int)


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


repeater = on_message(priority=10, block=False)


@repeater.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if getattr(event, 'message_type', None) != 'group':
        return
    group_id = getattr(event, 'group_id', None)
    if not group_id:
        return

    msg1 = CACHE.last_msg[group_id]
    msg2 = event.get_message()
    if checkMsgEqual(msg1, msg2):
        CACHE.msg_count[group_id] += 1
        if CACHE.msg_count[group_id] == CACHE.REPEAT_AFTER:
            await repeater.send(msg2)
    else:
        CACHE.last_msg[group_id] = msg2
        CACHE.msg_count[group_id] = 1
