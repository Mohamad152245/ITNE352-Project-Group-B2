import socket
import threading
import json
import pip._vendor.requests

api_url = 'https://newsapi.org/'
api_key = '27d7c542059d496ba63e8330cd595bd6'

print('----------------Server is Online----------------')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind('127.0.0.1', 1010)
print('----------------Server is ----------------')
server_socket.listen(3)

def handle_client(client)