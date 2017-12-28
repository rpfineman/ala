#!/usr/bin/env python3
# Misc
from pprint import pprint
import ipdb
# ipdb.set_trace(context=55)
# Core
import os
import sys
# Time
from django.utils import timezone
import time
from datetime import datetime
# Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ala.settings")
import django
django.setup()
from feeds.models import Chan, Reddit, Slashdot, Hackernews
# Misc
from pprint import pprint
import html2text
import ipdb  # ipdb.set_trace(context=55)
# Chan
import json
from bs4 import BeautifulSoup
import urllib3
# Hakernews
import re
import urllib3
import feedparser
import lxml


def prRed(prt):
    print("\033[31m{}\033[00m" .format(prt))
def prGreen(prt):
    print("\033[32m{}\033[00m" .format(prt))
def prYellow(prt):
    print("\033[33m{}\033[00m" .format(prt))
def prLightGray(prt):
    print("\033[37m{}\033[00m" .format(prt))


REDDIT_URL = 'https://www.reddit.com/r/Python/search.json?q=&sort=new&restrict_sr=on&t=all&count=999'
HACKERNEWS_URL = 'https://hnrss.org/newest?comments=100&count=100'
SLASHDOT_URL = 'http://rss.slashdot.org/Slashdot/slashdotMain'
SLASHDOT_DEVELOPER_URL = 'http://rss.slashdot.org/Slashdot/slashdotDevelopers'
# SLASHDOT_LINUX_URL='http://rss.slashdot.org/Slashdot/slashdotLinux'
CHAN_URL_PREFIX = 'http://boards.4chan.org/g/thread/'
CHAN_CATALOG_URL = 'http://a.4cdn.org/g/catalog.json'
# CHAN_ARCHIVE_URL='http://a.4cdn.org/g/archive.json'


def delete_all_records(my_board):
    '''Deletes all records in given board'''
    all_records = my_board.objects.all()
    record_count = my_board.objects.count()
    all_records.delete()
    prRed('%d records deleted' % record_count)


def chan_update_all_records():
    '''Update all records found at the url:

       http://a.4cdn.org/g/catalog.json
    '''
    print('\n\n\n==============================================================')
    print(datetime.now().strftime('%m/%d  %I:%M%P') + ' - Updating Chan')
    print('==============================================================')

    http = urllib3.PoolManager()
    r = http.request('GET', CHAN_CATALOG_URL)
    resp = json.loads(r.data.decode('utf-8'))

    total_record_count = 0
    new_record_count = 0
    updated_record_count = 0

    for j in resp:
        for i in j['threads']:
            u = CHAN_URL_PREFIX + str(i['no'])
            d = i['time']
            n = int(i['replies'])
            
            try:
                m = i['md5']
            except:
                m=0

            # Our 'title' is their 'sub' field
            try:
                t = i['sub']
            # No title, just use the first line of 'comment' field as title
            except :
                comment = i['com']
                t = html2text.html2text(comment)
                t = t.splitlines()
                t = t[0]
            # Our 'subject' is their 'com' field
            try:
                s = i['com']
                s = html2text.html2text(s)
            # Empty comment field, store empty string
            except :
                s = ''

            total_record_count += 1

            try:
                obj = Chan.objects.get(md5=m)
                # Record exists, num_comments has changed, lets upate our
                # record
                if obj.num_comments != n:
                    prYellow('Record exists, updating...')
                    obj.num_comments = n
                    obj.save(update_fields=['num_comments'])
                    updated_record_count += 1
                # Recod exists and hasn't changed, nothing to do
                else:
                    pass
            # Record doesn't exist, lets create it
            except Chan.DoesNotExist:
                prGreen('Record does not exist, creating...')
                new_record = Chan(
                    title=t,
                    url=u,
                    num_comments=n,
                    date=d,
                    md5=m,
                    subject=s
                )
                new_record.save()
                new_record_count += 1

    print('records found:   ', total_record_count)
    if updated_record_count:
        print('records updated: ', updated_record_count)
    if new_record_count:
        print('records created: ', new_record_count)
    print('')


def hackernews_update_all_records():
    '''Update all records found at the url:

       https://hnrss.org/newest?comments=100&count=100
    '''
    print('\n\n\n==============================================================')
    print(datetime.now().strftime('%m/%d  %I:%M%P') + ' - Updating Hackernews')
    print('==============================================================')
    feed = feedparser.parse(HACKERNEWS_URL)

    total_record_count = 0
    new_record_count = 0
    updated_record_count = 0
    for data in feed["entries"]:
        t = data['title']
        u = data['comments']
        d = data['published']
        a = data['author']

        # This is where we have to scrape a html block to get num_comments
        html = data['summary']
        bsObj = BeautifulSoup(html, 'lxml')
        nameList = bsObj. findAll("p")
        # We index over each record and get num_comments
        for name in nameList:
            n_line = ''
            # If the json item exists, then we just grab it
            if '# Comments' in name.get_text():
                n_line = name.get_text()
                # Extract the numerical part
                n_text = re.findall('\d+', n_line)
                # The num_comments value is always the firt item
                n = n_text[0]
            # If the json item doesn't exist yet, set num_comments to 0
            else:
                n = 0

        total_record_count += 1

        # Now we have all values needed to create record
        # Get record's title, an exception means !exist
        try:
            obj = Hackernews.objects.get(title=t)
            if obj.num_comments != int(n):
                prYellow('Record exists, updating...')
                obj.num_comments = n
                obj.save(update_fields=['num_comments'])
                updated_record_count += 1
            else:
                pass
        # Record !exist, lets create it
        except Hackernews.DoesNotExist:
            prGreen('Record does not exist, creating...')
            new_record = Hackernews(
                title=t,
                url=u,
                num_comments=n,
                date=d,
                author=a
            )
            new_record.save()
            new_record_count += 1

    print('records found:   ', total_record_count)
    if updated_record_count:
        print('records updated: ', updated_record_count)
    if new_record_count:
        print('records created: ', new_record_count)
    print('')


def slashdot_update_all_records():
    '''Update all records found at the url:

       http://rss.slashdot.org/Slashdot/slashdotMain
    '''
    print('\n\n\n==============================================================')
    print(datetime.now().strftime('%m/%d  %I:%M%P') + ' - Updating Slashdot')
    print('==============================================================')

    for i in [SLASHDOT_URL, SLASHDOT_DEVELOPER_URL]:
        total_record_count = 0
        new_record_count = 0
        updated_record_count = 0

        print('--------------------    ')
        print('url: ', i)
        print('--------------------    ')
        feed = feedparser.parse(i)

        for data in feed['items']:
            t = data['title']
            u = data['link']
            # try, cathch indexing error, assign null if missing
            d = data['updated']
            a = data['author']
            try:
                n = data['slash_comments']
            except :
                n = 0

            total_record_count += 1

            try:
                obj = Slashdot.objects.get(title=t)
                # Update when num_comments differ
                if obj.num_comments != int(n):
                    prYellow('Record exists, updating...')
                    obj.num_comments = n
                    obj.save(update_fields=['num_comments'])
                    updated_record_count += 1
                else:
                    pass
            # !exits so make new record
            except Slashdot.DoesNotExist:
                prGreen('Record does not exist, creating...')
                new_record = Slashdot(
                    title=t,
                    url=u,
                    num_comments=n,
                    date=d,
                    author=a)
                new_record.save()
                new_record_count += 1

        print('\n', len(feed['items']), ' records found\n\n')

        time.sleep(30)


def reddit_update_all_records():
    '''Update all records found at the url:

       https://www.reddit.com/r/Python/search.json?q=&sort=new&restrict_sr=on&t=all&count=999
    '''
    print('\n\n\n==============================================================')
    print(datetime.now().strftime('%m/%d  %I:%M%P') + ' - Updating Reddit')
    print('==============================================================')

    http = urllib3.PoolManager()
    r = http.request('GET', REDDIT_URL)

    json_dict = json.loads(r.data.decode('utf-8'))
    json_str = json.dumps(json_dict)
    records = json_dict['data']['children']

    total_record_count = 0
    new_record_count = 0
    updated_record_count = 0
    for data in records:
        t = data['data']['title']
        u = 'https://www.reddit.com' + data['data']['permalink']
        n = data['data']['num_comments']
        d = data['data']['created']
        a = data['data']['author']

        total_record_count += 1

        try:
            obj = Reddit.objects.get(title=t)
            if obj.num_comments != n:
                prYellow('Record exists, updating...')
                obj.num_comments = n
                obj.save(update_fields=['num_comments'])
                updated_record_count += 1
            # Recod exists and hasn't changed, nothing to do
            else:
                pass
        except Reddit.DoesNotExist:
            prGreen('Record does not exist, creating...')
            new_record = Reddit(
                title=t,
                url=u,
                num_comments=n,
                date=d,
                author=a)
            new_record.save()
            new_record_count += 1

    print('records found:   ', total_record_count)
    if updated_record_count:
        print('records updated: ', updated_record_count)
    if new_record_count:
        print('records created: ', new_record_count)
    print('')


def main():
    if len(sys.argv) == 1:
        print('pass a paramater: cu/cd, ru/rd, su/sd, hu/hd')
    elif len(sys.argv) == 2:

        # Chan
        if sys.argv[1] == 'cu':
            chan_update_all_records()
        elif sys.argv[1] == 'cd':
            delete_all_records(Chan)

        # Reddit
        if sys.argv[1] == 'ru':
            reddit_update_all_records()
        elif sys.argv[1] == 'rd':
            delete_all_records(Reddit)

        # Slashdot
        elif sys.argv[1] == 'su':
            slashdot_update_all_records()
        elif sys.argv[1] == 'sd':
            delete_all_records(Slashdot)

        # Hackernews
        elif sys.argv[1] == 'hu':
            hackernews_update_all_records()
        elif sys.argv[1] == 'hd':
            delete_all_records(Hackernews)

    else:
        print('bad param, choose cu/cd, ru/rd, su/sd, hu/hd')


if __name__ == "__main__":
    main()
