#! /usr/bin/python
import os
import sys
import re

def calc(q):
    print("<head><title>calculator</title></head><body>")

    if not q:
        print("<form name='calculator' method='get'>a: <input type='text' name='a' value=''><br>b: <input type='text' name='b' value=''><br><select name='method'><option value='+'>+</option><option value='-'>-</option><option value='*'>*</option><option value='/'>/</option></select><input type='submit' value='Submit'></form>")
    else:
        mylist = q.replace('&', '=')
        mylist = mylist.split("=")
        mydict = dict(zip(mylist[::2], mylist[1::2])) # From pavpanchekha on StackOverFlow
        print("<form name='calculator' method='get'>a: <input type='text' name='a'><br>b: <input type='text' name='b'><br><select name='method'><option value='+'>+</option><option value='-'>-</option><option value='*'>*</option><option value='/'>/</option></select><input type='submit' value='Submit'></form>")

        # Attempt to Convert Number
        try:
            a = float(mydict['a'])
            b = float(mydict['b'])
        except Exception as e:
            print("Please Provide Valid Number</body>")
            return

        # Complete Calculation Based on Method
        if 'method' in mydict.keys():
            if mydict['method'] == "+" or mydict['method'] == "%2B":
                print(mydict['a'] + " + " + mydict['b'] + " = " + str(a + b))
            elif mydict['method'] == "-" or mydict['method'] == "%2D":
                print(mydict['a'] + " - " + mydict['b'] + " = " + str(a - b))
            elif mydict['method'] == "/" or mydict['method'] == "%2F":
                print(mydict['a'] + " / " + mydict['b'] + " = " + str(a / b))
            elif mydict['method'] == "*" or mydict['method'] == "%2A":
                print(mydict['a'] + " * " + mydict['b'] + " = " + str(a * b))
        else:
            print("Wrong Use!")

    print("</body>")

def gb(q):

    error = ""
    # Always Print
    print("<head><title>guestbook</title></head><body>")

    # Query Parameters
    if q:
        mylist = q.replace('+', " ")
        mylist = mylist.replace('&', '=')
        mylist = mylist.replace('<', '')
        mylist = mylist.replace('>', '')
        mylist = mylist.replace('%2C',',')
        mylist = mylist.split("=")
        mydict = dict(zip(mylist[::2], mylist[1::2])) # From pavpanchekha on StackOverFlow

        if 'name' in mydict.keys() and 'comment' in mydict.keys():
            with open('guestbook.txt', 'a') as f:
                if mydict['name'] == '':
                    error = "Please Provide Name <br>"
                elif mydict['comment'] == "":
                    error = "Please Provide Comment <br>"
                else:
                    f.write(mydict['name'] + ": " + mydict['comment'] + '<br>')
        else:
            error = "Please provide valid fields<br>"

    try:
        with open('guestbook.txt', 'r') as f:
            print(f.read())
            print("<br>")
    except Exception as e:
         with open('guestbook.txt','w+') as f:
             f.write("")


    print("<form id='usrform' name='guestbook' method='get'>Name: <input type='text' name='name'><input type='submit' value='Submit'></form><br><textarea rows='4' cols='50' name='comment' form='usrform'></textarea><br>")
    print(error)
    print("</body>")

# START MAIN
def main():

    print("Content-Type: text/html\n\n")
    print("<!DOCTYPE html>")

    # Initialize Variables
    path = os.getenv("PATH_INFO")
    query = os.getenv("QUERY_STRING")
    calculator = re.compile(r"^/calculator/?$")
    guestbook = re.compile(r"^/guestbook/?$")

    # Choose which page to show
    if not path:
        print("<head><title>Wrong Page</title></head><body>Please visit either /calculator or /guestbook. Thank you</body>")
    elif calculator.search(path):
        calc(query)
    elif guestbook.search(path):
        gb(query)
    else:
        print("<head><title>Wrong Page</title></head><body>Please visit either /calculator or /guestbook. Thank you</body>")

if __name__ == "__main__":
    main()



# Create Local Server on port 8080 with "python -m http.server --cgi 8080"
