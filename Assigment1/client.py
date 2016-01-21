#! /usr/bin/python
import sys
import re
import socket
from functions import getResponse, sendMessage, getStatusCode, getBody

# Set Variables
METHOD = str(sys.argv[1])
URL    = sys.argv[2]
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
REDIRECT_COUNT = 0

# Send Request and Recieve Response
sendMessage(METHOD, URL, CLIENT)
response = getResponse(CLIENT)
CLIENT.close()

# If Redirected (301,302,303,307)
while re.search(r'^HTTP\/1\.1\s3\d[1-3]\s.*|HTTP\/1\.1\s3\d[7]\s.*',response) and REDIRECT_COUNT < 5 and METHOD != "HEAD":
    print("REDIRECTED")
    REDIRECT_COUNT += 1

    # Get New Location
    location = re.search(r'Location:\s', response)
    new_url = response[location.end():].split('\n')[0].rstrip()
    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Re-send the Message to new location
    sendMessage(METHOD, new_url, CLIENT)
    response = getResponse(CLIENT)
    CLIENT.close()

# Print Final Response
getStatusCode(response)
print(getBody(response))

# https://docs.python.org/2/library/httplib.html
