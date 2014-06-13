import urllib
import urllib2
import json

def getFromURL(url):
    response = urllib2.urlopen(url);
    return response.read();

def getMeta(path):
    return getFromURL("http://169.254.169.254"+path);
    
def getInstanceIdentity(name):
    instanceIdentity = getMeta("/latest/dynamic/instance-identity/document/")
    instanceIdentityObject = json.loads(instanceIdentity)
    return instanceIdentityObject[name]

def getUserData(name):
    userData = getMeta("/latest/user-data")
    userDataObject = json.loads(userData)
    return userDataObject[name]
    
def getRegion():
    return getInstanceIdentity("region")
    
  