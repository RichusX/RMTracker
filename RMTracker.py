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
import sys, getopt
import argparse
import requests
import time
from pushbullet.pushbullet import PushBullet

if 'linux' in sys.platform:
    dryscrape.start_xvfb()

refreshRate = 30 # how often to check the status in minutes

def checkArgs(apiK, devID, trackN):
    if len(trackN) < 7 and len(trackN) > 22:
        print "Invalid tracking number"
        return False
    elif len(apiK) < 20:
        print "Invalid API Key"
        return False
    elif len(devID) != 22:
        print "Invalid Device ID"
        return False
    else:
        return True

def usage():
    #print "Usage:\n-h, --help (displays this info)\n-a [YOUR_API_KEY], --apiKey [YOUR_API_KEY]\n-d [YOUR_PUSHBULLET_DEVICE_ID], --deviceID [YOUR_PUSHBULLET_DEVICE_ID]\n-t [YOUR_TRACKING_NUMBER], --trackingNumber [YOUR_TRACKING_NUMBER]\n\nNote: Arguments API Key, Device ID & tracking number are all required"
    parser.print_help()
    sys.exit(0)

def main(apiKey, deviceId, trackingNumber):
    prevStatus = ""
    p = PushBullet(apiKey)

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
        try:
            x = sess.at_xpath('//*[@class="status result-row padding20lr first"]')
            status = x.text()
        except AttributeError:
            try:
                x = sess.at_xpath('//*[@class="status result-row padding20lr first last"]')
                status = x.text()
            except AttributeError:
                print "Error"
                sys.exit(0)


        if (status != prevStatus):
            # push the status to PushBullet

            # if tracking not available then print out message
            if "Status: Please try again" in status:
                print "\n" + status
                print "Will countinue checking unless stopped (CTRL+C)"

            try:
                #p.pushNote(deviceId, 'RoyalMail Tracking', status)
                print ("Notification 'pushed': %s" % status)
            except requests.exceptions.HTTPError:
                print "Incorrect API Key or Device ID"
                usage()


            prevStatus = status

        # wait for 'refreshRate' minutes before checking again
        time.sleep(refreshRate * 60)

if __name__ == "__main__":
        try:
            parser = argparse.ArgumentParser(description='RoyalMail tracking with PushBullet integration.')
            parser.add_argument('-a','--apikey', help='Your PushBullet API key',required=True)
            parser.add_argument('-d','--deviceid', help='Your PushBullet device ID',required=True)
            parser.add_argument('-t','--tracknum', help='RoyalMail Tracking number you wish to track',required=True)
            args = parser.parse_args()

            a = args.apikey
            d = args.deviceid
            t = args.tracknum

            print ("API Key: %s" % len(args.apikey))
            print ("Device ID: %s" % len(args.deviceid))
            print ("Tracking Number: %s" % len(args.tracknum))

            if checkArgs(a,d,t):
                main(a, d, t)
            else:
                print "checkArgs() check FAILED\n"
                usage()
        except KeyboardInterrupt:
            print " RMTracker stopped"
            sys.exit(0)
