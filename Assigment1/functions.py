import socket
import re
from urlparse import urlparse

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
RECV_SIZE = 1024

# Send HTTP Message
def sendMessage(method, url, client):
    # Set Initial Values
    host = str(urlparse(url).hostname)
    path = '/'
    port = 80

    # Change port number if provided
    if urlparse(url).port:
        port = int(urlparse(url).port)
    if urlparse(url).path:
        path = str(urlparse(url).path)

    # Create TCP Connection to Server
    client.connect((host,port))

    # Create HTTP Message
    message = method + " " + path + " HTTP/1.1" + "\nHost: " + host + "\nConnection: close" +"\n\n"

    # Attempt to Send HTTP Message
    try:
        client.send(message)
        return 1
    except Exception as e:
        return 0

# Recieve HTTP Response
def getResponse(client):
    # Recieve response from server
    resp = current = client.recv(RECV_SIZE)
    while len(current) > 0:
        current = client.recv(RECV_SIZE)
        resp += current
    # Return Final Response
    return resp

# Get return Status for return value
def getStatusCode(response_string):
    if re.search(r'HTTP/1\.1\s2\d\d\s.*',response_string):
        return 0
    elif re.search(r'HTTP/1\.1\s3\d\d\s.*',response_string):
        return 3
    elif re.search(r'HTTP/1\.1\s4\d\d\s.*',response_string):
        return 4
    elif re.search(r'HTTP/1\.1\s5\d\d\s.*',response_string):
        return 5
    else:
        return 1
