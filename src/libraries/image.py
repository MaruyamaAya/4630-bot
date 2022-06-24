import base64
import asyncio

import re
import aiohttp
from io import BytesIO

from PIL import ImageFont, ImageDraw, Image


path = 'src/static/high_eq_image.png'
fontpath = "src/static/msyh.ttc"


def draw_text(img_pil, text, offset_x):
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(fontpath, 48)
    width, height = draw.textsize(text, font)
    x = 5
    if width > 390:
        font = ImageFont.truetype(fontpath, int(390 * 48 / width))
        width, height = draw.textsize(text, font)
    else:
        x = int((400 - width) / 2)
    draw.rectangle((x + offset_x - 2, 360, x + 2 + width + offset_x, 360 + height * 1.2), fill=(0, 0, 0, 255))
    draw.text((x + offset_x, 360), text, font=font, fill=(255, 255, 255, 255))


def text_to_image(text):
    font = ImageFont.truetype(fontpath, 24)
    padding = 10
    margin = 4
    text_list = text.split('\n')
    max_width = 0
    for text in text_list:
        w, h = font.getsize(text)
        max_width = max(max_width, w)
    wa = max_width + padding * 2
    ha = h * len(text_list) + margin * (len(text_list) - 1) + padding * 2
    i = Image.new('RGB', (wa, ha), color=(255, 255, 255))
    draw = ImageDraw.Draw(i)
    for j in range(len(text_list)):
        text = text_list[j]
        draw.text((padding, padding + j * (margin + h)), text, font=font, fill=(0, 0, 0))
    return i


def image_to_base64(img, format='PNG'):
    output_buffer = BytesIO()
    img.save(output_buffer, format)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str

# async def get_jlpx(jl, px, bottom):
#     data = {
#         'id': jl,
#         'zhenbi': '20191123',
#         'id1': '9007',
#         'id2': '18',
#         'id3':  '#0000FF',
#         'id4':  '#FF0000',
#         'id5': '10',
#         'id7': bottom,
#         'id8': '9005',
#         'id10': px,
#         'id11': 'jiqie.com_2',
#         'id12': '241'
#     }
#     async with aiohttp.request(method='POST', url="http://jiqie.zhenbi.com/e/re111.php", data=data) as resp:
#         t = await resp.text()
#         regex = '<img src="(.+)">'
#         return re.match(regex, t).groups()[0]


async def get_jlpx(index, jl, px, bottom):
    data = {
        'id': jl,
        'zhenbi': '20191123',
        'id2': '18',
        'id5': '10',
        'id7': bottom,
    }
    if index == '盘旋':
        subfix = '111'
        data['id1'] = '9007'
        data['id3'] = '#0000FF'
        data['id4'] = '#FF0000'
        data['id8'] = '9005'
        data['id10'] = px
        data['id11'] = 'jiqie.com_2'
        data['id12'] = '241'
    elif index == '飞升':
        subfix = '111'
        data['id1'] = '9005'
        data['id3'] = '#00FF00'
        data['id4'] = '#FFFF00'
        data['id8'] = '9008'
        data['id10'] = px
        data['id11'] = 'jiqie.com_1'
        data['id12'] = '505'
    elif index == '酷炫':
        subfix = '102'
        data['id1'] = '9005'
        data['id3'] = '#CDE374'
        data['id4'] = '#4CA3CF'
        data['id8'] = '9007'
    else:
        return None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36', 'Content-type': 'application/x-www-form-urlencoded'}
    async with aiohttp.request(method='POST', url=f"http://jiqie.zhenbi.com/e/re{subfix}.php", headers=headers, data=data) as resp:
        t = await resp.text()
        regex = r'<img src="(.+)">'
        return re.match(regex, t).groups()[0]