#!/usr/bin/env python
import cgi
import cgitb
import sys
import tweepy
import time
from subprocess import call
import picamera
photo_name = 'cgi-bin/test.jpg'
photo_path = 'combined.jpg'

# Twitter API Information

CONSUMER_KEY = '********Your Consumer Key********'
CONSUMER_SECRET = '********Your Consumer Secret********'
ACCESS_KEY = '********Your Access Key********'
ACCESS_SECRET = '********Your Access Secret********'

# For Syncing with index.html to capture the fields

cgitb.enable()

form=cgi.FieldStorage()

text=form["post"].value

# Capturing the picture

with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.start_preview()
	time.sleep(2)
	camera.capture(photo_name)
	camera.stop_preview()
	camera.close()

# Overlaying the image, in this case named hackiowa.jpg creating an an
# image named combined.jpg
	
overlay_image = "composite -geometry +31+105 hackiowa.png " + photo_name + " \combined.jpg"
print overlay_image
call ([overlay_image], shell=True)

# Posting to twitter with picture and status entered from webpage

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_with_media(photo_path, status=cgi.escape(text))

# Handles redirect back to main webpage by printing an HTML page
# Please note the IP adddress will change depending on the Pi

print "Content-type: text/html\n"
print "<!doctype html>"
print "<head>"
print '<script type="text/javascript">'
print "var delay;"
print "function wait (){"
print "delay = window.setTimeout(foo, 5000);"
print "}"
print ""
print 'function foo (){'
print 'window.location.href = "http://192.168.1.60:8000";'
print '}'
print "window.onload= wait;"
print "</script>"
print "</head>"
print '<body>'
print "<h1>Awesome! Picture sucessful. Please wait while we load it...</h1>"
print "<script>"
print "</script>"
print "</body>"
print "</html>"
