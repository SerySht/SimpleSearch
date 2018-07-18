from bs4 import BeautifulSoup
from . import indexer
import time
import requests
#from queue import Queue
#from reppy.cache import RobotsCache


class Crawler(object):
    def __init__(self, start_url):
        self.start_url = start_url
        self.sites_num = 0
        self.queue = set()

    def crawl(self):
        current_page_url = self.start_url
        self.queue.add(current_page_url)

        while self.queue:
            if self.sites_num < 500:  #lol
                self.__download_pages_in_queue()
            else:
                return

    def __download_pages_in_queue(self):
        current_page_url = self.queue.pop()
        while current_page_url.find(self.start_url[8:]) == -1:
            current_page_url = self.queue.pop()


        # robot = RobotsCache()
        # if (robot.allowed(current_page_url, "*")):

        print (" --- Now downloading -  " + str(current_page_url) + " №" + str(self.sites_num))

        if len(current_page_url) < 10:   #lol
            return

        # getting links on other pages
        current_page_html = download_page_by_url(current_page_url)

        bs = BeautifulSoup(current_page_html, "html.parser")
        title_id = current_page_html.find("<title>")
        title_id2 = current_page_html.find("</title>")
        title = current_page_html[title_id:title_id2].replace("<title>", "")

        links = bs.find_all('a', href=True)
        post_links = [link['href'] for link in links]

        # print("---------------------------")
        # print(post_links)
        # print("---------------------------")
        #


        for post_link in post_links:
            # if len(post_link) < 10:
            #     continue
            # if str(post_link).find('http') != 0:
            #     post_link = str(self.start_url) + str(post_link)
            self.queue.add(post_link)
        self.sites_num += 1

        indexer.add_document(current_page_url, get_text_from_html(bs), title)

        # else:
        #     print "Page can't be indexed because of the rules in ROBOTS.TXT"


def download_page_by_url(url):
    if url:
        headers = {'User-Agent': 'Searching Engine bot version 2'}
        try:
            r = requests.get(url, headers=headers)
        except:
            print("Download FAILED ", url)
            return ""
        if r.status_code != 200:
            time.sleep(2)
        # raise Exception("TOO FAST!!!!!")
        return r.text


def get_text_from_html(soup):
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text
