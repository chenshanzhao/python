'''
Created on 2019年11月7日

@author: chensz
'''


import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = requests.get("http://image.baidu.com/wisehomepage/feeds")
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find('div',"hotPic"):
        title=item.find_all('div', calss='hotPicImg')
        print(title)
        