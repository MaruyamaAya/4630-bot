import random
import re

from PIL import Image
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot, MessageSegment
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
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

pig = on_command('谁是猪')
@pig.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await pig.finish(Message([MessageSegment.text("[CQ:at,qq=1525014054]彩彩觉得是这位呢！")]))
        
help = on_command('help')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''可用命令如下：
[那个数字] 随机迫害wht
彩彩自搜 慌不择路的自我检索者
今日舞萌 查看今天的舞萌运势
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

