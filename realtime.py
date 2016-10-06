from users import Users
import re
import time


class RealTime:
    sc = None
    users = None

    def __init__(self, slackclient):
        self.sc = slackclient
        self.users = Users(self.sc)

        if self.sc.rtm_connect():
            while True:
                self.event(self.sc.rtm_read())
                time.sleep(1)
        else:
            print("Connection Failed, invalid token?")

    def event(self, event):
        if event:
            if "subtype" in event[0]:
                if event[0]["subtype"] == "message_changed":
                    return
            elif event[0]["type"] == "message":
                self.process_message(event[0])

    def process_message(self, message):
        print(message)
        user = self.users.info(message["user"])
        text = message["text"]

        print("{}: {}".format(user["name"], text))

        if re.search(r'TEST-\d*(?=\s)|TEST-\d*$', text):
            print(" Found possible ticket id")
            newtext = re.sub(r'(TEST-\d*(?=\s)|TEST-\d*$)', r'http://www.google.com/\1', text)
            self.update_message(message, newtext)

    def update_message(self, message, text):
        response = self.sc.server.api_call("chat.update", ts=message["ts"], channel=message["channel"], text=text)