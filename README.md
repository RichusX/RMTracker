# RMTracker
RoyalMail tracking with PushBullet integration

You will need...
- Python (2 or 3 should be fine)

**Dependencies**
- [pyPushBullet](https://github.com/Azelphur/pyPushBullet/)
- [dryscrape](https://github.com/niklasb/dryscrape/)

**Usage**

Get your PushBullet API Key from https://www.pushbullet.com/#settings/account

Get your PushBulelt Device ID:
  - Go to https://www.pushbullet.com/
  - Select the device from the device list
  - Look at the URL, it will be "https://www.pushbullet.com/#devices/xxxxxxxxxxxxxxxxxxxxxx"
  - Instead of x's you're going to see your device ID

Before using you need to edit the Python scripts user variables
```python
# USER VARIABLES START
trackingNumber = 'YOUR_TRACKING_NUMBER' # your RoyalMail tracking number
apiKey = 'YOUR_API_KEY' # your PushBullet API key
deviceId = 'YOUR_PUSHBULLET_DEVICE_ID' # your PushBullet device ID that you want to push status to
refreshRate = 30 # how often to check the status in minutes
# USER VARIABLES END
```

If you've done everything correctly just start the script (reccommended to run within a 'screen') and that's it!
If you have any issues / questions feel free to contact me by e-mail: me@richusx.me
