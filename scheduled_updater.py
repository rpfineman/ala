#!/usr/bin/env python3
import update   # My script
import schedule
from datetime import datetime
import time


# What to run...
def job():
    # Hackernews
    update.hackernews_update_all_records()
    # Slashdot
    update.slashdot_update_all_records()
    # Reddit
    update.reddit_update_all_records()
    # Chan
    update.chan_update_all_records()



# Run it every...
schedule.every(15).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)


# One it once
job()
# Then run it in a loop
while True:
    schedule.run_pending()
    time.sleep(1) # Seconds


