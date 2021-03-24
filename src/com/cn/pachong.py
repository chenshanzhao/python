'''
Created on 2019年11月6日
爬虫入门
@author: chensz
'''

import os

from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import json


class Fitness:
    host = 'https://www.hiyd.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    def __init__(self):
        self.conn = sqlite3.connect('fitness_test.db')
        self.create_db()

    def get_pages(self, url):
        r = requests.get(url, headers=self.headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for x in soup.find_all("div", class_="cont"):
            self.get_info(self.host + x.a.get('href'))
        next_page_url = str(soup.find("a", rel="next").get('href'))
        if next_page_url is not None and next_page_url != "/dongzuo/?page=3":
            self.get_pages(self.host + next_page_url)
        else:
            self.close_db()

    def get_info(self, url):
        r = requests.get(url, headers=self.headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        text = str(soup.find_all("script")[-1])
        data = json.loads(re.search(r'e.init\((.+?)\);', text).group(1))
        self.download(data['name'], data['video_url'])
        self.save_db([data['name'], data['muscle_name'], data['description'], data['video_url']])
        print("done " + data['name'])

    def download(self, name, url):
        if os.path.exists("./video") is False:
            os.makedirs("./video")
        with requests.get(url, stream=True) as response:
            with open("./video/" + name + ".mp4", "wb") as file:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)

    def create_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS fitness (id INTEGER PRIMARY KEY, "
                          "name TEXT, "
                          "muscle_name TEXT, "
                          "description TEXT, "
                          "video_url TEXT);")

    def save_db(self, data):
        self.conn.execute("INSERT INTO fitness (name, muscle_name, description, video_url) VALUES(?, ?, ?, ?)", data)

    def close_db(self):
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    fitness = Fitness()
    fitness.get_pages('https://www.hiyd.com/dongzuo/')