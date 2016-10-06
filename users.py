import json


class Users:

    sc = None

    def __init__(self, slackclient):
        self.sc = slackclient

    def info(self, userid):
        return json.loads(self.sc.server.api_call("users.info", user=userid))["user"]