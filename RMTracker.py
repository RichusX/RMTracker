#!/usr/bin/env python
import dryscrape
import sys
from pushbullet.pushbullet import PushBullet

if 'linux' in sys.platform:
    dryscrape.start_xvfb()

trackingNumber = 'YOUR_TRACKING_NUMBER_HERE'
apiKey = 'YOUR_PUSHBULLET_API_KEY_HERE'
p = PushBullet(apiKey)

# set up a web scraping session
sess = dryscrape.Session(base_url = 'https://www.royalmail.com')

# we don't need images
sess.set_attribute('auto_load_images', False)

# visit the tracking page and lookup the tracking number
sess.visit('/track-your-item')
q = sess.at_xpath('//*[@name="tracking_number"]')
q.set(trackingNumber)
q.form().submit()

#extract the tracking status
x = sess.at_xpath('//*[@class="status result-row padding20lr first"]')
status = x.text()

print status
p.pushNote("YOUR_DEVICE_IDEN_HERE", 'RoyalMail Tracking Status', status)
