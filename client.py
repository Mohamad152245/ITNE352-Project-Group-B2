import socket

client_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_Sock.connect(('192.168.0.1',5000))
except:
    print("connaction  faild")
    exit(0) 



while True:
    try:

        print("Choose the number of your option")
        print("1.Search headlines ")
        print("2.List of sources")
        print("3.Quit")
        option = input(int("your option is : "))
    
    
    except :    
        break
