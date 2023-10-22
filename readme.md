# AnyProxy
A proxy which allows you to send a request to ANY website. The only catch is,
you have to host it yourself.

This proxy is designed to be hosted only for yourself. Because allowing any url's for
any proxies in general could be dangerous.

It's also designed to be modified to your liking.

# Setup
First, make sure you have python installed. And install those 3 packages using pip (if you haven't already)
Flask, waitress, python_dotenv.

Now, you gotta clone this repo. Run this on your terminal to do so. `git clone https://github.com/geometrical1/anyproxy.git`
Go to the cloned repo. And rename `.template.env` to -> `.env`
Open it, you may want to configure it
You should find these options:
1. api_key
2. prod
3. port

Change api_key to a strong password. You don't need to change it if you don't plan to deploy it for production.
The prod value is basically if to host the proxy on your local IP (127.0.0.1) or on an open IP (0.0.0.0).
Set this to 1 if you will be using it for production. Any value other than "1" will host the proxy on your local IP.
The port value is self explainatory. What port do you wanna use for your proxy?

Now, to run it, just type `py .` in the terminal. and tada! it should run now.

# Usage
Now, the proxy should be running. But how can I use it?
So far, only GET requests and POST requests are implemented. You can fork the proxy to add more request methods.
## GET requests
For this example, We will try to get a request from https://icanhazdadjoke.com/ via the proxy.
So:
\-\-proxy url\-\-/request/get?url=https://icanhazdadjoke.com/
Headers:
x-api-key:\-yourapikeyhere\-
Content-Type:application/json (you can also use text/plain)

If you got an "Unauthorized access" message from the proxy, Make sure you
put your api-key in the headers correctly.

It works, but how would I pass parameters or headers to the url itself too?

\-\-proxy url\-\-/request/get?url=https://icanhazdadjoke.com/&params={"WhateverParamUGot": "xyz", "anotherParam": "xy2"}
Headers:
x-api-key:\-yourapikeyhere\-
Content-Type:application/json (you can also use text/plain)
headers:{"yourheaderhere": "x", "anothaone": "y"}

they are in the json format, if you couldn't realize.
## POST requests
Its extremely identical to GET requests. except,
you replace the url with:
\-\-proxy url\-\-/request/post .. and so on

That is it. Fork it if you need to add more features.