import requests


def make_session():
    session = requests.session()
    #do the cookie thingies here
    return session