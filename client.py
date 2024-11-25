import socket

client_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_Sock.connect(('192.168.0.1',5000))
except:
    print("connaction  faild")
    exit(0) 
