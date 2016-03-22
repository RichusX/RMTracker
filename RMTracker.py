#!/usr/bin/env python
import dryscrape
import sys
import time
from pushbullet.pushbullet import PushBullet

if 'linux' in sys.platform:
    dryscrape.start_xvfb()

trackingNumber = 'YOUR_TRACKING_NUMBER'
apiKey = 'YOUR_API_KEY'
p = PushBullet(apiKey)
refreshRate = 30 # how often to check the status in minutes

# set up a web scraping session
sess = dryscrape.Session(base_url = 'https://www.royalmail.com')

# we don't need images
sess.set_attribute('auto_load_images', False)

while True:
    # visit the tracking page and lookup the tracking number
    sess.visit('/track-your-item')
    q = sess.at_xpath('//*[@name="tracking_number"]')
    q.set(trackingNumber)
    q.form().submit()

    # extract the tracking status
    x = sess.at_xpath('//*[@class="status result-row padding20lr first"]')
    status = x.text()
    prevStatus = ''
    
    if (status != prevStatus):
        # push the status to PushBullet
        p.pushNote("YOUR_DEVICE_IDENT", 'RoyalMail Tracking', status)
        prevStatus = status
    
    # wait for 'refreshRate' minutes before checking again
    time.sleep(refreshRate * 60)
