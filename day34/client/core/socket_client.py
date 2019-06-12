import socket
import json
from conf import settings
class MySocketClient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(settings.addr)
    def mysend(self,msg):
        ret_json = json.dumps(msg)
        self.sk.send(ret_json.encode(settings.code))