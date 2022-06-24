from collections import defaultdict
from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message, MessageSegment
import os
import base64
from src.libraries.tool import hash
from src.libraries.maimaidx_music import *
from src.libraries.image import *
from src.libraries.maimai_best_40 import generate
from src.libraries.maimai_best_50 import generate50
import re
import random

from collections import defaultdict

from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message, MessageSegment, GroupMessageEvent, PrivateMessageEvent

from src.libraries.tool import hash
from src.libraries.maimaidx_music import *
from src.libraries.image import *
from src.libraries.maimai_best_40 import *

from src.libraries.maimai_plate import *

import re
import datetime
import time

from nonebot.permission import Permission
from nonebot.log import logger
import requests
import json
import random
from urllib import parse
import asyncio
from nonebot.rule import to_me

driver = get_driver()

@driver.on_startup
def _():
    logger.info("aya Kernel -> Load \"DX\" successfully")


def song_txt(music: Music):
    return Message([
        {
            "type": "text",
            "data": {
                "text": f"{music.id}. {music.title}\n"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://www.diving-fish.com/covers/{get_cover_len4_id(music.id)}.png"
            }
        },
        {
            "type": "text",
            "data": {
                "text": f"\n{'/'.join(music.level)}"
            }
        }
    ])

def img_4630_text():
    pic_path = "/home/aya/images/4630/"
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


def inner_level_q(ds1, ds2=None):
    result_set = []
    diff_label = ['Bas', 'Adv', 'Exp', 'Mst', 'ReM']
    if ds2 is not None:
        music_data = total_list.filter(ds=(ds1, ds2))
    else:
        music_data = total_list.filter(ds=ds1)
    for music in sorted(music_data, key = lambda i: int(i['id'])):
        for i in music.diff:
            result_set.append((music['id'], music['title'], music['ds'][i], diff_label[i], music['level'][i]))
    return result_set


inner_level = on_command('inner_level ', aliases={'定数查歌 '})


@inner_level.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(" ")
    if len(argv) > 2 or len(argv) == 0:
        await inner_level.finish("命令格式为\n定数查歌 <定数>\n定数查歌 <定数下限> <定数上限>")
        return
    if len(argv) == 1:
        result_set = inner_level_q(float(argv[0]))
    else:
        result_set = inner_level_q(float(argv[0]), float(argv[1]))
    if len(result_set) > 50:
        await inner_level.finish(f"彩彩找到的结果太多了呢...（{len(result_set)} 条），请缩小搜索范围~")
        return
    s = ""
    for elem in result_set:
        s += f"{elem[0]}. {elem[1]} {elem[3]} {elem[4]}({elem[2]})\n"
    await inner_level.finish(s.strip())


spec_rand = on_regex(r"^随个(?:dx|sd|标准)?[绿黄红紫白]?[0-9]+\+?")


@spec_rand.handle()
async def _(bot: Bot, event: Event, state: T_State):
    level_labels = ['绿', '黄', '红', '紫', '白']
    regex = "随个((?:dx|sd|标准))?([绿黄红紫白]?)([0-9]+\+?)"
    res = re.match(regex, str(event.get_message()).lower())
    try:
        if res.groups()[0] == "dx":
            tp = ["DX"]
        elif res.groups()[0] == "sd" or res.groups()[0] == "标准":
            tp = ["SD"]
        else:
            tp = ["SD", "DX"]
        level = res.groups()[2]
        if res.groups()[1] == "":
            music_data = total_list.filter(level=level, type=tp)
        else:
            music_data = total_list.filter(level=level, diff=['绿黄红紫白'.index(res.groups()[1])], type=tp)
        if len(music_data) == 0:
            rand_result = "彩彩没有找到没有这样的乐曲哦。"
        else:
            rand_result = song_txt(music_data.random())
        await spec_rand.send(rand_result)
    except Exception as e:
        print(e)
        await spec_rand.finish("随机命令错误，请检查语法")


mr = on_regex(r".*maimai.*什么")


@mr.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await mr.finish(song_txt(total_list.random()))

test_4630 = on_command("4630", aliases={'wht'})
@test_4630.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await test_4630.finish(img_4630_text())


search_music = on_regex(r"^查歌.+")


@search_music.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "查歌(.+)"
    name = re.match(regex, str(event.get_message())).groups()[0].strip()
    if name == "":
        return
    res = total_list.filter(title_search=name)
    if len(res) == 0:
        await search_music.send("没有找到这样的乐曲。")
    elif len(res) < 50:
        search_result = ""
        for music in sorted(res, key = lambda i: int(i['id'])):
            search_result += f"{music['id']}. {music['title']}\n"
        await search_music.finish(Message([
            {"type": "text",
                "data": {
                    "text": search_result.strip()
                }}]))
    else:
        await search_music.send(f"结果过多（{len(res)} 条），请缩小查询范围。")


query_chart = on_regex(r"^([绿黄红紫白]?)id([0-9]+)")


@query_chart.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "([绿黄红紫白]?)id([0-9]+)"
    groups = re.match(regex, str(event.get_message())).groups()
    level_labels = ['绿', '黄', '红', '紫', '白']
    if groups[0] != "":
        try:
            level_index = level_labels.index(groups[0])
            level_name = ['Basic', 'Advanced', 'Expert', 'Master', 'Re: MASTER']
            name = groups[1]
            music = total_list.by_id(name)
            chart = music['charts'][level_index]
            ds = music['ds'][level_index]
            level = music['level'][level_index]
            file = f"https://www.diving-fish.com/covers/{get_cover_len4_id(music['id'])}.png"
            if len(chart['notes']) == 4:
                msg = f'''{level_name[level_index]} {level}({ds})
TAP: {chart['notes'][0]}
HOLD: {chart['notes'][1]}
SLIDE: {chart['notes'][2]}
BREAK: {chart['notes'][3]}
谱师: {chart['charter']}'''
            else:
                msg = f'''{level_name[level_index]} {level}({ds})
TAP: {chart['notes'][0]}
HOLD: {chart['notes'][1]}
SLIDE: {chart['notes'][2]}
TOUCH: {chart['notes'][3]}
BREAK: {chart['notes'][4]}
谱师: {chart['charter']}'''
            await query_chart.send(Message([
                {
                    "type": "text",
                    "data": {
                        "text": f"{music['id']}. {music['title']}\n"
                    }
                },
                {
                    "type": "image",
                    "data": {
                        "file": f"{file}"
                    }
                },
                {
                    "type": "text",
                    "data": {
                        "text": msg
                    }
                }
            ]))
        except Exception:
            await query_chart.send("未找到该谱面")
    else:
        name = groups[1]
        music = total_list.by_id(name)
        try:
            file =f"https://www.diving-fish.com/covers/{get_cover_len4_id(music['id'])}.png"
            await query_chart.send(Message([
                {
                    "type": "text",
                    "data": {
                        "text": f"{music['id']}. {music['title']}\n"
                    }
                },
                {
                    "type": "image",
                    "data": {
                        "file": f"{file}"
                    }
                },
                {
                    "type": "text",
                    "data": {
                        "text": f"艺术家: {music['basic_info']['artist']}\n分类: {music['basic_info']['genre']}\nBPM: {music['basic_info']['bpm']}\n版本: {music['basic_info']['from']}\n难度: {'/'.join(music['level'])}"
                    }
                }
            ]))
        except Exception:
            await query_chart.send("未找到该乐曲")


wm_list = ['拼机', '推分', '越级', '下埋', '夜勤', '练底力', '练手法', '打旧框', '干饭', '抓绝赞', '收歌']


jrwm = on_command('aya 今日舞萌', aliases={'aya 今日mai', 'aya 今日运势'})


@jrwm.handle()
async def _(bot: Bot, event: Event, state: T_State):
    qq = int(event.get_user_id())
    h = hash(qq)
    rp = h % 100
    wm_value = []
    for i in range(11):
        wm_value.append(h & 3)
        h >>= 2
    s = f"今日人品值：{rp}\n"
    for i in range(11):
        if wm_value[i] == 3:
            s += f'宜 {wm_list[i]}\n'
        elif wm_value[i] == 0:
            s += f'忌 {wm_list[i]}\n'
    s += "Pastel*Palettes的应援就拜托大家了哦~\n彩彩今天为你推荐这首歌！"
    music = total_list[h % len(total_list)]
    await jrwm.finish(Message([
        {"type": "text", "data": {"text": s}}
    ] + song_txt(music)))


# music_aliases = defaultdict(list)
# f = open('src/static/aliases.csv', 'r', encoding='utf-8')
# tmp = f.readlines()
# f.close()
# for t in tmp:
#     arr = t.strip().split('\t')
#     for i in range(len(arr)):
#         if arr[i] != "":
#             music_aliases[arr[i].lower()].append(arr[0])
#
#
# find_song = on_regex(r".+是什么歌")
#
#
# @find_song.handle()
# async def _(bot: Bot, event: Event, state: T_State):
#     regex = "(.+)是什么歌"
#     name = re.match(regex, str(event.get_message())).groups()[0].strip().lower()
#     if name not in music_aliases:
#         await find_song.finish("未找到此歌曲\n舞萌 DX 歌曲别名收集计划：https://docs.qq.com/sheet/DQ0pvUHh6b1hjcGpl")
#         return
#     result_set = music_aliases[name]
#     if len(result_set) == 1:
#         music = total_list.by_title(result_set[0])
#         await find_song.finish(Message([{"type": "text", "data": {"text": "彩彩为你找到了"}}] + song_txt(music)))
#     else:
#         s = '\n'.join(result_set)
#         await find_song.finish(f"彩彩觉得可能是以下歌曲中的其中一首：\n{ s }")


query_score = on_command('aya 分数线')


@query_score.handle()
async def _(bot: Bot, event: Event, state: T_State):
    r = "([绿黄红紫白])(id)?([0-9]+)"
    argv = str(event.get_message()).strip().split(" ")
    if len(argv) == 1 and argv[0] == '帮助':
        s = '''此功能为查找某首歌分数线设计。
命令格式：分数线 <难度+歌曲id> <分数线>
例如：分数线 紫799 100
命令将返回分数线允许的 TAP GREAT 容错以及 BREAK 50落等价的 TAP GREAT 数。
以下为 TAP GREAT 的对应表：
GREAT/GOOD/MISS
TAP\t1/2.5/5
HOLD\t2/5/10
SLIDE\t3/7.5/15
TOUCH\t1/2.5/5
BREAK\t5/12.5/25(外加200落)'''
        await query_score.send(Message([{
            "type": "image",
            "data": {
                "file": f"base64://{str(image_to_base64(text_to_image(s)), encoding='utf-8')}"
            }
        }]))
    elif len(argv) == 2:
        try:
            grp = re.match(r, argv[0]).groups()
            level_labels = ['绿', '黄', '红', '紫', '白']
            level_labels2 = ['Basic', 'Advanced', 'Expert', 'Master', 'Re:MASTER']
            level_index = level_labels.index(grp[0])
            chart_id = grp[2]
            line = float(argv[1])
            music = total_list.by_id(chart_id)
            chart: Dict[Any] = music['charts'][level_index]
            tap = int(chart['notes'][0])
            slide = int(chart['notes'][2])
            hold = int(chart['notes'][1])
            touch = int(chart['notes'][3]) if len(chart['notes']) == 5 else 0
            brk = int(chart['notes'][-1])
            total_score = 500 * tap + slide * 1500 + hold * 1000 + touch * 500 + brk * 2500
            break_bonus = 0.01 / brk
            break_50_reduce = total_score * break_bonus / 4
            reduce = 101 - line
            if reduce <= 0 or reduce >= 101:
                raise ValueError
            await query_chart.send(f'''{music['title']} {level_labels2[level_index]}
分数线 {line}% 允许的最多 TAP GREAT 数量为 {(total_score * reduce / 10000):.2f}(每个-{10000 / total_score:.4f}%),
BREAK 50落(一共{brk}个)等价于 {(break_50_reduce / 100):.3f} 个 TAP GREAT(-{break_50_reduce / total_score * 100:.4f}%)''')
        except Exception:
            await query_chart.send("格式错误，输入“分数线 帮助”以查看帮助信息")

replace_score = on_command("b40", aliases={'mai b40'})
replace_score.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await replace_score.finish("如果想让彩彩帮你查询的话，请使用aya b40哦~")

best_40_pic = on_command('aya b40')


@best_40_pic.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await best_40_pic.send("彩彩正在帮你查询喔")
    username = str(event.get_message()).strip()
    if username == "":
        payload = {'qq': str(event.get_user_id())}
    else:
        payload = {'username': username}
    img, success = await generate(payload)
    if success == 400:
        await best_40_pic.send("未找到此玩家，请确保此玩家的用户名和查分器中的用户名相同。")
    elif success == 403:
        await best_40_pic.send("该用户禁止了其他人获取数据。")
    else:
        await best_40_pic.send(Message([
            {
                "type": "image",
                "data": {
                    "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                }
            }
        ]))

best_50_pic = on_command('aya b50')


@best_50_pic.handle()
async def _(bot: Bot, event: Event, state: T_State):
    username = str(event.get_message()).strip()
    if username == "":
        payload = {'qq': str(event.get_user_id()),'b50':True}
    else:
        payload = {'username': username,'b50':  True}
    img, success = await generate50(payload)
    if success == 400:
        await best_50_pic.send("未找到此玩家，请确保此玩家的用户名和查分器中的用户名相同。")
    elif success == 403:
        await best_50_pic.send("该用户禁止了其他人获取数据。")
    else:
        await best_50_pic.send(Message([
            {
                "type": "image",
                "data": {
                    "file": f"base64://{str(image_to_base64(img), encoding='utf-8')}"
                }
            }
        ]))


plate = on_regex(r'^([真超檄橙暁晓桃櫻樱紫菫堇白雪輝辉熊華华爽舞霸])([極极将舞神者]舞?)进度\s?(.+)?')

@plate.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "([真超檄橙暁晓桃櫻樱紫菫堇白雪輝辉熊華华爽舞霸])([極极将舞神者]舞?)进度\s?(.+)?"
    comboRank = 'fc fc+ ap ap+'.split(' ')
    combo_rank = 'fc fcp ap app'.split(' ')
    syncRank = 'fs fs+ fdx fdx+'.split(' ')
    sync_rank = 'fs fsp fdx fdxp'.split(' ')
    res = re.match(regex, str(event.get_message()).lower())
    diffs = 'Basic Advanced Expert Master Re:Master'.split(' ')
    nickname = event.sender.nickname
    mt = event.message_type
    db = get_driver().config.db
    c = await db.cursor()
    if f'{res.groups()[0]}{res.groups()[1]}' == '真将':
        await plate.finish(f"▿ To {nickname} | Plate Error\n请您注意: 真系 (maimai & maimaiPLUS) 没有真将成就。")
        return
    if not res.groups()[2]:
        if mt == "guild":
            await c.execute(f'select * from gld_table where uid="{event.user_id}"')
            data = await c.fetchone()
            if data is None:
                await plate.send(f"▿ To {nickname} | Plate - 错误\n在频道内，免输入用户名的前提是需要将您的 QQ 进行绑定。您尚未将您的 QQ 绑定到小犽，请进行绑定或输入用户名再试一次。\n")
                return
            else:
                payload = {'qq': str(data[0])}
        else:
            payload = {'qq': str(event.get_user_id())}
    else:
        payload = {'username': res.groups()[2].strip()}
    if res.groups()[0] in ['舞', '霸']:
        payload['version'] = list(set(version for version in plate_to_version.values()))
    if res.groups()[0] in ['真']:
        payload['version'] = [plate_to_version['真1'], plate_to_version['真2']]
    else:
        payload['version'] = [plate_to_version[res.groups()[0]]]
    player_data, success = await get_player_plate(payload)
    if success == 400:
        await plate.send(f"▿ To {nickname} | Plate - 错误\n您输入的玩家 ID 没有找到。\n请检查一下您的用户名是否输入正确或有无注册查分器系统？如您没有输入ID，请检查您的QQ是否与查分器绑定正确。\n若需要确认设置，请参阅:\nhttps://www.diving-fish.com/maimaidx/prober/")
    elif success == 403:
        await plate.send(f'▿ To {nickname} | Plate - 被禁止\n 不允许使用此方式查询牌子进度。\n如果是您的账户，请检查您的QQ是否与查分器绑定正确后，不输入用户名再试一次。\n您需要修改查分器设置吗？请参阅:\nhttps://www.diving-fish.com/maimaidx/prober/')
    else:
        song_played = []
        song_remain_expert = []
        song_remain_master = []
        song_remain_re_master = []
        song_remain_difficult = []
        if res.groups()[1] in ['将', '者']:
            for song in player_data['verlist']:
                if song['level_index'] == 2 and song['achievements'] < (100.0 if res.groups()[1] == '将' else 80.0):
                    song_remain_expert.append([song['id'], song['level_index']])
                if song['level_index'] == 3 and song['achievements'] < (100.0 if res.groups()[1] == '将' else 80.0):
                    song_remain_master.append([song['id'], song['level_index']])
                if res.groups()[0] in ['舞', '霸'] and song['level_index'] == 4 and song['achievements'] < (100.0 if res.groups()[1] == '将' else 80.0):
                    song_remain_re_master.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        elif res.groups()[1] in ['極', '极']:
            for song in player_data['verlist']:
                if song['level_index'] == 2 and not song['fc']:
                    song_remain_expert.append([song['id'], song['level_index']])
                if song['level_index'] == 3 and not song['fc']:
                    song_remain_master.append([song['id'], song['level_index']])
                if res.groups()[0] == '舞' and song['level_index'] == 4 and not song['fc']:
                    song_remain_re_master.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        elif res.groups()[1] == '舞舞':
            for song in player_data['verlist']:
                if song['level_index'] == 2 and song['fs'] not in ['fsd', 'fsdp']:
                    song_remain_expert.append([song['id'], song['level_index']])
                if song['level_index'] == 3 and song['fs'] not in ['fsd', 'fsdp']:
                    song_remain_master.append([song['id'], song['level_index']])
                if res.groups()[0] == '舞' and song['level_index'] == 4 and song['fs'] not in ['fsd', 'fsdp']:
                    song_remain_re_master.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        elif res.groups()[1] == "神":
            for song in player_data['verlist']:
                if song['level_index'] == 2 and song['fc'] not in ['ap', 'app']:
                    song_remain_expert.append([song['id'], song['level_index']])
                if song['level_index'] == 3 and song['fc'] not in ['ap', 'app']:
                    song_remain_master.append([song['id'], song['level_index']])
                if res.groups()[0] == '舞' and song['level_index'] == 4 and song['fc'] not in ['ap', 'app']:
                    song_remain_re_master.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        total_music_num = 0
        for music in total_list:
            if music.version in payload['version']:
                total_music_num += 1
                if [int(music.id), 2] not in song_played:
                    song_remain_expert.append([int(music.id), 2])
                if [int(music.id), 3] not in song_played:
                    song_remain_master.append([int(music.id), 3])
                if res.groups()[0] in ['舞', '霸'] and len(music.level) == 5 and [int(music.id), 4] not in song_played:
                    song_remain_re_master.append([int(music.id), 4])
        song_remain_expert = sorted(song_remain_expert, key=lambda i: int(i[0]))
        song_remain_master = sorted(song_remain_master, key=lambda i: int(i[0]))
        song_remain_re_master = sorted(song_remain_re_master, key=lambda i: int(i[0]))
        for song in song_remain_expert + song_remain_master + song_remain_re_master:
            music = total_list.by_id(str(song[0]))
            if music.ds[song[1]] > 13.6:
                song_remain_difficult.append([music.id, music.title, diffs[song[1]], music.ds[song[1]], music.stats[song[1]].difficulty, song[1]])
        expcomplete = 100 - (len(song_remain_expert) / total_music_num * 100)
        mascomplete = 100 - (len(song_remain_master) / total_music_num * 100)
        msg = f'''▾ To {nickname} | {res.groups()[0]}{res.groups()[1]}当前进度\n{"您" if not res.groups()[2] else res.groups()[2]}的剩余歌曲数量如下：
Expert | 已完成 {expcomplete:.2f}%, 待完成 {len(song_remain_expert)} 首 / 共 {total_music_num} 首
Master | 已完成 {mascomplete:.2f}%, 待完成 {len(song_remain_master)} 首 / 共 {total_music_num} 首
'''
        song_remain = song_remain_expert + song_remain_master + song_remain_re_master
        song_record = [[s['id'], s['level_index']] for s in player_data['verlist']]
        if res.groups()[0] in ['舞', '霸']:
            remascomplete = 100 - (len(song_remain_re_master) / total_music_num * 100)
            msg += f'Re:Master | 已完成 {remascomplete:.2f}%, 待完成 {len(song_remain_re_master)} 首 / 共 {total_music_num} 首\n'
        if len(song_remain_difficult) > 0:
            if len(song_remain_difficult) < 11:
                if res.groups()[0] in ['真']:
                        msg += "\n注意: 真系不需要游玩ジングルベル(以下简称\"圣诞歌\")。受技术限制，真系查询仍包括圣诞歌，您可以忽略此歌曲。如您的真系进度只剩下圣诞歌，则您已达成条件。\n"
                msg += '\n剩余的 13+ 及以上的谱面如下：\n'
                for s in sorted(song_remain_difficult, key=lambda i: i[3]):
                    self_record = ''
                    if [int(s[0]), s[-1]] in song_record:
                        record_index = song_record.index([int(s[0]), s[-1]])
                        if res.groups()[1] in ['将', '者']:
                            self_record = str(player_data['verlist'][record_index]['achievements']) + '%'
                        elif res.groups()[1] in ['極', '极', '神']:
                            if player_data['verlist'][record_index]['fc']:
                                self_record = comboRank[combo_rank.index(player_data['verlist'][record_index]['fc'])].upper()
                        elif res.groups()[1] == '舞舞':
                            if player_data['verlist'][record_index]['fs']:
                                self_record = syncRank[sync_rank.index(player_data['verlist'][record_index]['fs'])].upper()
                    if res.groups()[0] in ['真'] and s[0] == 70:
                        continue
                    msg += f'Track {s[0]} > {s[1]} | {s[2]}\n定数: {s[3]} 相对难度: {s[4]} {"当前达成率: " if self_record else ""}{self_record}'.strip() + '\n\n'
            else: msg += f'还有 {len(song_remain_difficult)} 个等级是 13+ 及以上的谱面，加油推分捏！\n'
        elif len(song_remain) > 0:
            if len(song_remain) < 11:
                msg += '\n剩余曲目：\n'
                for s in sorted(song_remain, key=lambda i: i[3]):
                    m = total_list.by_id(str(s[0]))
                    self_record = ''
                    if [int(s[0]), s[-1]] in song_record:
                        record_index = song_record.index([int(s[0]), s[-1]])
                        if res.groups()[1] in ['将', '者']:
                            self_record = str(player_data['verlist'][record_index]['achievements']) + '%'
                        elif res.groups()[1] in ['極', '极', '神']:
                            if player_data['verlist'][record_index]['fc']:
                                self_record = comboRank[combo_rank.index(player_data['verlist'][record_index]['fc'])].upper()
                        elif res.groups()[1] == '舞舞':
                            if player_data['verlist'][record_index]['fs']:
                                self_record = syncRank[sync_rank.index(player_data['verlist'][record_index]['fs'])].upper()
                    if res.groups()[0] in ['真'] and s[0] == 70:
                        continue
                    msg += f'Track {m.id} > {m.title} | {diffs[s[1]]}\n定数: {m.ds[s[1]]} 相对难度: {m.stats[s[1]].difficulty} {"当前达成率: " if self_record else ""}{self_record}'.strip() + '\n\n'
            else:
                msg += '已经没有大于 13+ 的谱面了,加油清谱吧！\n'
        else: msg += f'{res.groups()[0]}{res.groups()[1]} 所需的所有歌曲均已达到要求，恭喜 {"您" if not res.groups()[2] else res.groups()[2]} 达成了 {res.groups()[0]}{res.groups()[1]}！'
        msg += '\n credit to Killua-Blitz/Kiba \n'
        await plate.send(msg.strip())

levelprogress = on_regex(r'^([0-9]+\+?)\s?(.+)进度\s?(.+)?')

@levelprogress.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "([0-9]+\+?)\s?(.+)进度\s?(.+)?"
    res = re.match(regex, str(event.get_message()).lower())
    scoreRank = 'd c b bb bbb a aa aaa s s+ ss ss+ sss sss+'.lower().split(' ')
    levelList = '1 2 3 4 5 6 7 7+ 8 8+ 9 9+ 10 10+ 11 11+ 12 12+ 13 13+ 14 14+ 15'.split(' ')
    comboRank = 'fc fc+ ap ap+'.split(' ')
    combo_rank = 'fc fcp ap app'.split(' ')
    syncRank = 'fs fs+ fdx fdx+'.split(' ')
    sync_rank = 'fs fsp fdx fdxp'.split(' ')
    achievementList = [50.0, 60.0, 70.0, 75.0, 80.0, 90.0, 94.0, 97.0, 98.0, 99.0, 99.5, 100.0, 100.5]
    nickname = event.sender.nickname
    db = get_driver().config.db
    c = await db.cursor()
    mt = event.message_type
    if res.groups()[0] not in levelList:
        await levelprogress.finish(f"▿ To {nickname} | 参数错误\n最低是1，最高是15，您这整了个{res.groups()[0]}......故意找茬的吧？")
        return
    if res.groups()[1] not in scoreRank + comboRank + syncRank:
        await levelprogress.finish(f"▿ To {nickname} | 参数错误\n输入有误。\n1.请不要随便带空格。\n2.等级目前只有D/C/B/BB/BBB/A/AA/AAA/S/S+/SS/SS+/SSS/SSS+\n3.同步相关只有FS/FC/FDX/FDX+/FC/FC+/AP/AP+。")
        return
    if not res.groups()[2]:
        if mt == "guild":
            await c.execute(f'select * from gld_table where uid="{event.user_id}"')
            data = await c.fetchone()
            if data is None:
                await levelprogress.send(f"▿ To {nickname} | 等级清谱查询 - 错误\n在频道内，免输入用户名的前提是需要将您的 QQ 进行绑定。您尚未将您的 QQ 绑定到小犽，请进行绑定或输入用户名再试一次。\n")
                return
            else:
                payload = {'qq': str(data[0])}
        else:
            payload = {'qq': str(event.get_user_id())}
    else:
        payload = {'username': res.groups()[2].strip()}
    payload['version'] = list(set(version for version in plate_to_version.values()))
    player_data, success = await get_player_plate(payload)
    if success == 400:
        await levelprogress.send(f"▿ To {nickname} | 等级清谱查询 - 错误\n您输入的玩家 ID 没有找到。\n请检查一下您的用户名是否输入正确或有无注册查分器系统？如您没有输入ID，请检查您的QQ是否与查分器绑定正确。\n若需要确认设置，请参阅:\nhttps://www.diving-fish.com/maimaidx/prober/")
        return
    elif success == 403:
        await levelprogress.send(f'▿ To {nickname} | 等级清谱查询 - 被禁止\n 不允许使用此方式查询牌子进度。\n如果是您的账户，请检查您的QQ是否与查分器绑定正确后，不输入用户名再试一次。\n您需要修改查分器设置吗？请参阅:\nhttps://www.diving-fish.com/maimaidx/prober/')
        return
    else:
        song_played = []
        song_remain = []
        if res.groups()[1].lower() in scoreRank:
            achievement = achievementList[scoreRank.index(res.groups()[1].lower()) - 1]
            for song in player_data['verlist']:
                if song['level'] == res.groups()[0] and song['achievements'] < achievement:
                    song_remain.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        elif res.groups()[1].lower() in comboRank:
            combo_index = comboRank.index(res.groups()[1].lower())
            for song in player_data['verlist']:
                if song['level'] == res.groups()[0] and ((song['fc'] and combo_rank.index(song['fc']) < combo_index) or not song['fc']):
                    song_remain.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        elif res.groups()[1].lower() in syncRank:
            sync_index = syncRank.index(res.groups()[1].lower())
            for song in player_data['verlist']:
                if song['level'] == res.groups()[0] and ((song['fs'] and sync_rank.index(song['fs']) < sync_index) or not song['fs']):
                    song_remain.append([song['id'], song['level_index']])
                song_played.append([song['id'], song['level_index']])
        for music in total_list:
            for i, lv in enumerate(music.level[2:]):
                if lv == res.groups()[0] and [int(music.id), i + 2] not in song_played:
                    song_remain.append([int(music.id), i + 2])
        song_remain = sorted(song_remain, key=lambda i: int(i[1]))
        song_remain = sorted(song_remain, key=lambda i: int(i[0]))
        songs = []
        for song in song_remain:
            music = total_list.by_id(str(song[0]))
            songs.append([music.id, music.title, diffs[song[1]], music.ds[song[1]], music.stats[song[1]].difficulty, song[1]])
        msg = ''
        if len(song_remain) > 0:
            if len(song_remain) < 50:
                song_record = [[s['id'], s['level_index']] for s in player_data['verlist']]
                msg += f'▼ To {nickname} | 清谱进度\n以下是 {"您" if not res.groups()[2] else res.groups()[2]} 的 Lv.{res.groups()[0]} 全谱面 {res.groups()[1].upper()} 的剩余曲目：\n'
                for s in sorted(songs, key=lambda i: i[3]):
                    self_record = ''
                    if [int(s[0]), s[-1]] in song_record:
                        record_index = song_record.index([int(s[0]), s[-1]])
                        if res.groups()[1].lower() in scoreRank:
                            self_record = str(player_data['verlist'][record_index]['achievements']) + '%'
                        elif res.groups()[1].lower() in comboRank:
                            if player_data['verlist'][record_index]['fc']:
                                self_record = comboRank[combo_rank.index(player_data['verlist'][record_index]['fc'])].upper()
                        elif res.groups()[1].lower() in syncRank:
                            if player_data['verlist'][record_index]['fs']:
                                self_record = syncRank[sync_rank.index(player_data['verlist'][record_index]['fs'])].upper()
                    if self_record == "":
                        self_record = "暂无"
                    msg += f'Track {s[0]} > {s[1]} | {s[2]}\nBase: {s[3]} 相对难度: {s[4]} 当前达成率: {self_record}'.strip() + '\n\n'
            else:
                await levelprogress.finish(f'▾ To {nickname} | 清谱进度\n{"您" if not res.groups()[2] else res.groups()[2]} 还有 {len(song_remain)} 首 Lv.{res.groups()[0]} 的曲目还没有达成 {res.groups()[1].upper()},加油推分吧！\n credit to Killua-Blitz/Kiba \n')
        else:
            await levelprogress.finish(f'▾ To {nickname} | 清谱完成\n恭喜 {"您" if not res.groups()[2] else res.groups()[2]} 达成 Lv.{res.groups()[0]} 全谱面 {res.groups()[1].upper()}！\n credit to Killua-Blitz/Kiba \n')
        msg += '\n credit to Killua-Blitz/Kiba \n'
        await levelprogress.send(MessageSegment.image(f"base64://{image_to_base64(text_to_image(msg.strip())).decode()}"))
