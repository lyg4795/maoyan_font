from fontTools.ttLib import TTFont
from maoyan.get_html import get_html
from maoyan.covv import covv
font = TTFont('./1.woff')  # 读取woff文件
url = 'https://maoyan.com/films/1218273'
# 请求网址并保存字体文件到font_new.woff
html=get_html(url)
font_new=TTFont('font_new.woff')
# 获取新的数字映射关系
num_dict_new=covv(font,font_new)
# 将数字转化为集合，如果长度小于10，则表示有重复，出现识别问题
print(len(set(num_dict_new.values())))