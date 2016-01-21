#! /usr/bin/python
import socket
import sys
import re
from urlparse import urlparse

# Set Variables
URL    = sys.argv[2]
METHOD = str(sys.argv[1])
HOST   = str(urlparse(URL).hostname)
PATH   = '/'
PORT   = 80
RECV_SIZE = 1024

# Change port number if provided
if urlparse(URL).port:
    PORT = int(urlparse(URL).port)
if urlparse(URL).path:
    PATH = str(urlparse(URL).path)

# Create TCP Connection to Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

# Create and Send HTTP Message
message = METHOD + " " + PATH + " HTTP/1.1" + "\nHost: " + HOST + "\nConnection: close" +"\n\n"
client.send(message)

# Recieve response from server
response = current = client.recv(RECV_SIZE)
while len(current) > 0:
    current = client.recv(RECV_SIZE)
    response += current

# Print Final Response
print(response)

# Close Connection to Server
client.close()

# # Grab the Response Status
# first_line = response.split('\n')[0]
# status = re.search(r'\d\d\d.*', first_line)
# print(first_line[status.start():status.end()])
# # Grab the redirected location
# redirect = re.search(r'Location:', response)
# print(response[redirect.start():].split('\n')[0])
