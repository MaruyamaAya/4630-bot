from bilibili_api.utils.utils import get_api
from bilibili_api.utils.network import request
from enum import Enum
import asyncio
import json
import os

API = open(os.path.join(os.path.dirname(__file__), 'search.json'), "r")
API = json.loads(API.read())

class SearchObjectType(Enum):
    """
    搜索对象。
    + VIDEO : 视频
    + BANGUMI : 番剧
    + FT : 影视
    + LIVE : 直播
    + ARTICLE : 专栏
    + TOPIC : 话题
    + USER : 用户
    """
    VIDEO = "video"
    BANGUMI = "media_bangumi"
    FT = "media_ft"
    LIVE = "live"
    ARTICLE = "article"
    TOPIC = "topic"
    USER = "bili_user"

async def web_search(keyword: str, page: int=1):
    """
    只指定关键字在 web 进行搜索，返回未经处理的字典
    Args:
        keyword (str): 搜索关键词
        page (int)   : 页码
    Returns:
        调用 api 返回的结果
    """
    api = API["search"]["web_search"]
    params = {
        "keyword": keyword,
        "page": page
    }
    return await request('GET', url=api["url"], params=params)

async def web_search_by_type(keyword: str, search_type: SearchObjectType, page: int=1):
    """
    指定关键字和类型进行搜索，返回未经处理的字典
    类型：视频(video)、番剧(media_bangumi)、影视(media_ft)、直播(live)、专栏(article)、话题(topic)、用户(bili_user)
    Args:
        keyword     (str): 搜索关键词
        search_type (str): 搜索类型
        page        (int): 页码
    Returns:
        调用 api 返回的结果
    """
    api = API["search"]["web_search_by_type"]
    params = {
        "keyword": keyword,
        "search_type": search_type.value,
        "page": page
    }
    return await request('GET', url=api["url"], params=params)

if __name__ == "__main__":
    res = asyncio.run(web_search_by_type('丸山彩', SearchObjectType.VIDEO, 1))
    print(res['result'][0])