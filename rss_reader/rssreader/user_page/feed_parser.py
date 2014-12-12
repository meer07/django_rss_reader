#coding:utf-8
import feedparser
import time

class feed_passer():
    feed_list = []
    def __init__(self, feed_url):
        feed = feedparser.parse(feed_url)
        self.get_feed_list(feed)

    def get_feed_list(self, feed):
        self.feed_list = []

        for e in feed.entries:
            # タイトルは日本語含むのでunicodeに変換
            title = unicode(e.title)
            date = time.strftime('%Y/%m/%d', e.updated_parsed)
            link = e.link

            list_item = [title, date, link]
            self.feed_list.append(list_item)

        #print self.feed_list

# テスト用
"""
if __name__ == '__main__':
    url = 'http://rss.dailynews.yahoo.co.jp/fc/rss.xml'
    passer = feed_passer(feed_url=url)

"""