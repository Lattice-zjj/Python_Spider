import requests
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
import re
if __name__ == "__main__":

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    url = 'http://www.biquge.info/32_32534/'
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text

    # 实例化
    soup = BeautifulSoup(page_text, 'lxml')
    dd_list = soup.select('.box_con > div > dl > dd')
    fp = open('./左道倾天.txt', 'w', encoding='utf-8')
    for dd in dd_list[400:]:
        title = dd.a.string
        fp.write(title+'\n\n')
        detail = url+dd.a['href']
        response_in = requests.get(url=detail, headers=headers)
        response_in.encoding = 'utf-8'
        get_text = response_in.text
        tree = etree.HTML(get_text)
        li_list = tree.xpath('/html/body/div/div[4]/div/div[3]')
        i = 0
        for li in li_list:
            content = li.xpath('./text()')
            for content_true in content:
                fp.write(content_true+'\n')
        fp.write('\n\n')
        print(title, '录入成功！！')
        sleep(5)
    fp.close()
