msgTemplate = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Justin", website='cfe.sh')

def formatMsg(myName="Justin", myWebsite="cfe.sh"):
    myMsg = msgTemplate.format(name=myName, website=myWebsite)
    return myMsg
