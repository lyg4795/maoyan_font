import HeadersToDict
import requests
import re
def get_html(url):
    # 请求网址并保存字体文件到font_new.woff
    headers=HeadersToDict.fromFile('maoyan_detail_headers')
    res=requests.get(url,headers=headers).text
    font_link=re.search(r'font-face[\s\S]*?url\(\'(.*?woff)\'\)',res).group(1)
    font_new_data=requests.get('http:'+font_link,headers=headers).content
    with open('font_new.woff','wb')as f:
        f.write(font_new_data)
    return res