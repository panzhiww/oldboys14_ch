import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1",8991))
msg, addr = sk.recvfrom(1024)
while 1:
    cmd = input(">>>")
    if cmd == "q":break
    sk.sendto(cmd.encode("utf-8"),addr)
    msg,addr = sk.recvfrom(1024)
    print(msg.decode("utf-8"))

sk.close()