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
CONSUMER_KEY = '********Your Consumer Key********'
CONSUMER_SECRET = '********Your Consumer Secret********'
ACCESS_KEY = '********Your Access Key********'
ACCESS_SECRET = '********Your Access Secret********'

cgitb.enable()

form=cgi.FieldStorage()

text=form["post"].value


with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.start_preview()
	time.sleep(2)
	camera.capture(photo_name)
	camera.stop_preview()
	camera.close()
	
overlay_image = "composite -geometry +31+105 hackiowa.png " + photo_name + " \combined.jpg"
print overlay_image
call ([overlay_image], shell=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_with_media(photo_path, status=cgi.escape(text))


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
