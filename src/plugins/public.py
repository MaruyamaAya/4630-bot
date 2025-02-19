import random
import re

from PIL import Image
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot, MessageSegment
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
from src.libraries.food import food_list, shitang
from src.libraries.image import *
from src.libraries.bilibili_search import *
from random import randint
import requests
from pixivpy3 import *
from bilibili_api import sync
import os
from src.libraries.Thursday import *




aapi = AppPixivAPI()

def img_aya_text():
    pic_path = "/home/aya/images/aya/"
    file_list = os.listdir(pic_path)
    idx = random.randint(0, len(file_list) - 1)
    f_path = pic_path + file_list[idx]
    f_ = open(f_path, 'rb')
    img_data = f_.read()
    b64_data = base64.b64encode(img_data)
    b64_data = b64_data.decode('utf-8')
    b64_data = "base64://" + b64_data
    print(b64_data)
    return Message([MessageSegment.image(b64_data)])


@event_preprocessor
async def preprocessor(bot, event, state):
    if hasattr(event, 'message_type') and event.message_type == "private" and event.sub_type != "friend":
        raise IgnoredException("not reply group temp message")

thur = on_command("疯狂星期四")
@thur.handle()
async def _(bot: Bot, event: Event, state: T_State):
    res__ = return_thur()
    await thur.finish(res__)

dog = on_command("舔狗日记")
@dog.handle()
async def _(bot: Bot, event: Event, state: T_State):
    url_ = 'https://cloud.qqshabi.cn/api/tiangou/api.php'
    response = requests.get(url_,).text
    response = response.replace('你', '彩彩')
    await dog.finish(response)

find_shitang = on_command("吃啥食堂", aliases={'吃什么食堂', '吃哪个食堂', '随个食堂'}, priority=1)
@find_shitang.handle()
async def _(bot: Bot, event: Event, state: T_State):
    len_ = len(shitang)
    idx_ = random.randint(0, len_ - 1)
    food_ = shitang[idx_]
    await find_shitang.finish("彩彩建议你吃{}呢！".format(food_))

# find_shitang2 = on_regex("吃什么食堂", priority=2)
# @find_shitang2.handle()
# async def _(bot: Bot, event: Event, state: T_State):
#     len_ = len(shitang)
#     idx_ = random.randint(0, len_ - 1)
#     food_ = food_list[idx_]
#     await find_shitang2.finish("彩彩建议你吃{}呢！".format(food_))

find_food = on_regex("吃啥", priority=2)
@find_food.handle()
async def _(bot: Bot, event: Event, state: T_State):
    len_ = len(food_list)
    idx_ = random.randint(0, len_ - 1)
    food_ = food_list[idx_]
    await find_food.finish("彩彩建议你吃{}呢！".format(food_))

find_food2 = on_regex("吃什么", priority=2)
@find_food2.handle()
async def _(bot: Bot, event: Event, state: T_State):
    len_ = len(food_list)
    idx_ = random.randint(0, len_ - 1)
    food_ = food_list[idx_]
    await find_food2.finish("彩彩建议你吃{}呢！".format(food_))

self_search = on_command("彩彩自搜")
@self_search.handle()
async def _(bot: Bot, event: Event, state: T_State):
    f_ = open('/home/aya/images/self_search.png', 'rb')
    img_data = f_.read()
    b64_data = base64.b64encode(img_data)
    b64_data = b64_data.decode('utf-8')
    b64_data = "base64://" + b64_data
    await self_search.send(Message([MessageSegment.image(b64_data)]))
    # await self_search.send("唔唔，让我来搜一下大家都是怎么看我的呢...")
    # res1 = asyncio.run(web_search_by_type('丸山彩', SearchObjectType.VIDEO, 1))['result']
    api = API["search"]["web_search_by_type"]
    keywords_ = ['丸山彩', '前岛亜美', '丸山彩', '前岛亜美', '丸山彩', '前岛亜美', '劈瓦', '修车']
    idx0 = random.randint(0, len(keywords_) - 1)
    pg_ = random.randint(1, 2)
    params = {
        "keyword": keywords_[idx0],
        "search_type": SearchObjectType.VIDEO.value,
        "page": pg_
    }
    res1 = await request('GET', url=api["url"], params=params)
    res1 = res1['result']
    len_ = len(res1)
    idx = random.randint(0, len_ - 1)
    tar_video = res1[idx]
    type_name = '\n分类：' + tar_video['typename']
    author = '\n作者：' + tar_video['author']
    url_ = '\n链接：' + tar_video['arcurl']
    title_ = '\n标题：' + tar_video['title']
    title_ = title_.replace('<em class="keyword">', '').replace('</em>', '')
    pic_ = "https:" + tar_video['pic']
    res_ = Message([MessageSegment.image(pic_),
                   MessageSegment.text(title_),
                   MessageSegment.text(author),
                   MessageSegment.text(type_name),
                   MessageSegment.text(url_)])
    await self_search.finish(res_)

nopig = on_regex('不是猪', priority=1)
@nopig.handle()
async def _(bot: Bot, event: Event, state: T_State):
    # await pig.finish(Message([MessageSegment.text("[CQ:at,qq=1525014054]彩彩觉得是这位呢！")]))
    await nopig.finish(Message([MessageSegment.at(1525014054), MessageSegment.text("彩彩觉得反正不是这位呢!")]))

pig = on_regex('是猪', priority=2,)
@pig.handle()
async def _(bot: Bot, event: Event, state: T_State):
    # await pig.finish(Message([MessageSegment.text("[CQ:at,qq=1525014054]彩彩觉得是这位呢！")]))
    await pig.finish(Message([MessageSegment.at(1525014054), MessageSegment.text("彩彩觉得是这位呢!")]))

pig2 = on_regex('猪呢', priority=2,)
@pig2.handle()
async def _(bot: Bot, event: Event, state: T_State):
    # await pig.finish(Message([MessageSegment.text("[CQ:at,qq=1525014054]彩彩觉得是这位呢！")]))
    await pig2.finish(Message([MessageSegment.at(1525014054), MessageSegment.text("彩彩觉得是这位呢!")]))
help = on_command('help')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''可用命令如下：
彩彩自搜 慌不择路的自我检索者
aya 今日舞萌 查看今天的舞萌运势
（北京限定） 吃啥/吃什么
（PKU限定）随个食堂/吃啥食堂/吃什么食堂
（credit to kiba）今日雀魂
（credit to kiba）mjxp
（credit to kiba）[歌曲等级][完成度]进度
（credit to kiba）牌子进度
（credit to kiba）低情商[]高情商[]
（credit to kiba）gocho [内容1] [内容2]
（credit to kiba）金龙盘旋/金龙飞升
[那个数字] 随机迫害wht
XXXmaimaiXXX什么 随机一首歌
随个[dx/标准][绿黄红紫白]<难度> 随机一首指定条件的乐曲
查歌<乐曲标题的一部分> 查询符合条件的乐曲
[绿黄红紫白]id<歌曲编号> 查询乐曲信息或谱面信息
<歌曲别名>是什么歌 查询乐曲别名对应的乐曲
定数查歌 <定数>  查询定数对应的乐曲
定数查歌 <定数下限> <定数上限>
分数线 <难度+歌曲id> <分数线> 详情请输入“分数线 帮助”查看'''
    await help.send(Message([{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        }
    }]))


async def _group_poke(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


poke = on_notice(rule=_group_poke, priority=10, block=True)


@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if event.__getattribute__('group_id') is None:
        event.__delattr__('group_id')
    await poke.send(img_aya_text())
    await poke.send("まんまるお山に彩りを!丸山彩でーす!")
    await poke.send(Message([{
        "type": "poke",
        "data": {
            "qq": f"{event.sender_id}"
        }
    }]))

