#!/usr/bin/env python

# RM Tracker - RoyalMail tracking with PushBullet integration
# Copyright (C) 2016  Ritvars Timermanis (RichusX)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import dryscrape
import sys
import getopt
import time
from pushbullet.pushbullet import PushBullet

if 'linux' in sys.platform:
    dryscrape.start_xvfb()

# USER VARIABLES START
trackingNumber = 'YOUR_TRACKING_NUMBER'
apiKey = 'YOUR_API_KEY'
deviceId = 'YOUR_PUSHBULLET_DEVICE_ID'
refreshRate = 30 # how often to check the status in minutes
# USER VARIABLES END

def usage():
    print "Usage:\n-h, --help (displays this info)\n-a [YOUR_API_KEY], --apiKey [YOUR_API_KEY]\n-d [YOUR_PUSHBULLET_DEVICE_ID], --deviceID [YOUR_PUSHBULLET_DEVICE_ID]\n-t [YOUR_TRACKING_NUMBER], --trackingNumber [YOUR_TRACKING_NUMBER]\n\nNote: Arguments API Key, Device ID & tracking number are all required" 

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:d:t:", ["help","apiKey","deviceID","trackingNumber"]) # h (help), a (api key), d (device ID), t (tracking number)
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            usage()
            sys.exit()
        #elif opt in ("-a", "--apiKey"):
            #nothin   
      
#    p = PushBullet(apiKey)
#
#    # set up a web scraping session
#    sess = dryscrape.Session(base_url = 'https://www.royalmail.com')
#
#    # we don't need images
#    sess.set_attribute('auto_load_images', False)
#
#    while True:
#        # visit the tracking page and lookup the tracking number
#        sess.visit('/track-your-item')
#        q = sess.at_xpath('//*[@name="tracking_number"]')
#        q.set(trackingNumber)
#        q.form().submit()
#
#        # extract the tracking status
#        try:
#            x = sess.at_xpath('//*[@class="status result-row padding20lr first"]')
#            status = x.text()
#        except AttributeError:
#            x = sess.at_xpath('//*[@class="status result-row padding20lr first last"]')
#            status = x.text()
#        
#        if (status != prevStatus):
#            # push the status to PushBullet
#            # if you would like to push to more than one device then just copy the line below and change the device ID
#            p.pushNote(deviceId, 'RoyalMail Tracking', status)
#            
#            prevStatus = status
#        
#        # wait for 'refreshRate' minutes before checking again
#        time.sleep(refreshRate * 60)

if __name__ == "__main__":
        usage()
        #main(sys.argv[1:])