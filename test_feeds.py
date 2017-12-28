#!/usr/bin/env python3
#NOTE: This script tests the scraping results (run it manually)
#      Once it looks good, implement it in project
import os
import sys
from django.utils import timezone
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ala.settings")
import django
django.setup()
from feeds.models import Reddit, Slashdot, Hackernews
import pprint
import subprocess

pp = pprint.PrettyPrinter(indent=4)

#REDDIT_URL='https://www.reddit.com/r/Python/search.json?q=&sort=comments&restrict_sr=on&t=day'
REDDIT_URL='https://www.reddit.com/r/Python/search.json?q=&sort=new&restrict_sr=on&t=all&count=999'
SLASHDOT_URL='http://rss.slashdot.org/Slashdot/slashdotMain'
HACKERNEWS_URL='https://hnrss.org/newest?comments=100&count=100'
CHAN_URL='https://a.4cdn.org/g/index.rss'


from collections import OrderedDict
import os ,sys ,re ,uuid ,subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import uuid
from lxml import html
import requests
import time


def test_hackernews(all=False):
    print('HACKERNEWS_URL: ', HACKERNEWS_URL, '\n')
    import re
    from bs4 import BeautifulSoup
    import urllib3
    import feedparser
    import lxml
    import re

    feed = feedparser.parse(HACKERNEWS_URL)

    for data in feed["entries"]:
        if all == True:
            pprint.pprint(data)
        else:
            t=data['title']
            u=data['comments']
            d=data['published']
            a=data['author']

            from urllib.request import urlopen
            from bs4 import BeautifulSoup
            html = data['summary']
            bsObj = BeautifulSoup( html, 'lxml')
            nameList = bsObj. findAll( "p")
            for name in nameList:
                if '# Comments' in name.get_text():
                    n_line=name.get_text()

            n=re.findall('\d+', n_line)
            n=n[0]
            print('----------')
            print('title: ', t)
            print('url: ', u)
            print('num_comemnts: ', n)
            print('date(utc): ', d)
            print('author: ', a)

    print('\n', len(feed['entries']), ' records found')



def test_slashdot(all=False):
    from django.utils import dateparse
    from django.utils.timezone import localtime

    print('SLASHDOT_URL: ', SLASHDOT_URL, '\n')
    import feedparser

    feed=feedparser.parse(SLASHDOT_URL)

    count = str(feed).count('slash_comments')

    if count != 15:
        prRed('=========================================================================')
        prRed('===============ERROR SLASHDOT data["slash_comments"] not found===========')
        prRed('=========================================================================')
        return
    else:
        for data in feed['items']:
            if all == True:
                pprint.pprint(data)
            else:
                t=data['title']
                u=data['link']
                n=data['slash_comments']
                d=data['updated']
                a=data['author']

                print('----------')
                print('title: ', t)
                print('url: ', u)
                print('num_comments: ', n)
                print('date(EST`): ', localtime(dateparse.parse_datetime(d)))
                print('author: ', a)

    print('\n', "slash_comments:", count, ' ', len(feed['items']), ' records found')



def test_reddit(all=False):
    import datetime
    print('REDDIT_URL: ', REDDIT_URL, '\n')
    import json
    from bs4 import BeautifulSoup
    import urllib3

    http = urllib3.PoolManager()
    # Get url
    r = http.request('GET', REDDIT_URL)
    # Decode data into dict/string
    json_dict = json.loads(r.data.decode('utf-8'))
    json_str = json.dumps(json_dict)
    # Records are the children in the dict
    records = json_dict['data']['children']

#    for data in records:
    for data in records:
        if all == True:
            pprint.pprint(data)
        else:
            t=data['data']['title']
            u='https://www.reddit.com'+data['data']['permalink']
            n=data['data']['num_comments']
            d=data['data']['created']
            a=data['data']['author']

            print('----------')
            print('title: ', t)
            print('url: ', u)
            print('num_comments: ', n)
            print('date(UTC): ', datetime.datetime.fromtimestamp(float(d)))
            print('author: ', a)

    print('\n', len(records), 'records found')






def main():
    if len(sys.argv) == 1:
        print('pass a paramater: c/ca, r/ra, s/sa, h/ha')
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'c': test_chan()
        elif sys.argv[1] == 'ca': test_chan(all=True)
        elif sys.argv[1] == 'r': test_reddit()
        elif sys.argv[1] == 'ra': test_reddit(all=True)
        elif sys.argv[1] == 's': test_slashdot()
        elif sys.argv[1] == 'sa': test_slashdot(all=True)
        elif sys.argv[1] == 'h': test_hackernews()
        elif sys.argv[1] == 'ha': test_hackernews(all=True)
        else:
            print('bad param, choose c,r,s,h')
    else:
        print('bad param, choose c,r,s,h')

if __name__ == "__main__":
    main()



