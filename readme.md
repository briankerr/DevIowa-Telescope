# Dev/Iowa Telescope

The Dev/Iowa Telescope is a child of the first ever [Dev/Iowa Hackathon](http://www.deviowa.org/hackathon/). Via an HTML Page take an image, overlay the Dev/Iowa logo, it then uploads the photo to a twitter account (In the case of the Hackathon it was [@telescopeia](http://www.twitter.com/telescopeia)) and reloads the webpage to show you the photo you just took.

It has the following requirements:

1. A Raspberry Pi with camera module and network connection.
2. Knowledge of python or williness to learn.
3. [ImageMagick](http://imagemagick.org/) Dependences installed on your Raspberry Pi.
4. The use of the [Python Tweepy Library](https://pypi.python.org/pypi/tweepy/3.3.0) for help with interacting with the Twitter API.
4. A [Twiiter Developer account](https://dev.twitter.com/apps) for API uploading.

The Telescope can be ran locally on the Pi or the Raspberry Pi can be ran as a local network web server if you run the following command on the directiory:

```
python -m CGIHTTPServer
```

This makes the Telescope fantastic for having others on the network take picture.

For any questions or help please contact me via Twitter [@thebriankerr](http://www.twitter.com/thebriankerr)
