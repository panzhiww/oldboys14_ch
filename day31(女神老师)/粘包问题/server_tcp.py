# 基于 tcp 实现远程执行命令
# 在 server 下发命令

# import socket
#
# sk = socket.socket()
# sk.bind(("127.0.0.1", 8091))
# sk.listen()
# conn, addr = sk.accept()
# conn.send(b"dir;ls")
# ret = conn.recv(1024).decode("utf-8")
# print(ret)
# conn.close()
# sk.close()


import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8091))
sk.listen()
conn, addr = sk.accept()
while True:
    cmd = input(">>>")
    conn.send(cmd.encode("utf-8"))
    ret = conn.recv(1024).decode("utf-8")
    print(ret)
conn.close()
sk.close()
