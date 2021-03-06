from core.socket_client import MySocketClient
class Auth:
    __instance = False
    def __new__(cls, *args, **kwargs):
        '''单例模式'''
        if not cls.__instance:
            obj = object.__new__(cls)
            obj.socket = MySocketClient()
            obj.username = None
            cls.__instance = obj
        return cls.__instance
    # def __init__(self):
    #     self.socket = MySocketClient()
    #     self .username = None

    def login(self):
        username = input("username: ")
        password = input("password: ")
        if username.strip() and password.strip():
            self.socket.mysend({"username: ":username,"passworf":password,"operation":"login"})
        ret = self.socket.sk.recv(1024)    # 登录的结果

    def register(self):
        username = input("username: ")
        password1 = input("password: ")
        password2 = input("password_ensure: ")
        if username.strip() and password1.strip() and password1 == password2:
            self.socket.mysend({"username: ": username, "passworf": password1,"operation":"register"})
        ret = self.socket.sk.recv(1024)   # 注册的结果