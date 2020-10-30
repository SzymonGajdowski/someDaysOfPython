import sys
import requests
from datetime import datetime

from formatting import formatMsg
from sendMail import sendMail


def send(name, website=None, toEmail=None, verbose=False):
    assert toEmail != None
    if website != None:
        msg = formatMsg(myName=name, myWebsite=website)
    else:
        msg = formatMsg(myName=name)
    if verbose:
        print(name, website, toEmail)
    try:
        sendMail(text=msg, toEmails=[toEmail])
        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, toEmail=email, verbose=True)
    print(response)