from slackclient import SlackClient
from realtime import RealTime


def init():
    sc = SlackClient(load_token())
    realtime = RealTime(sc)


def load_token():
    file = open('./token.txt', 'r')
    txt = file.read()
    file.close()
    return txt


init()
