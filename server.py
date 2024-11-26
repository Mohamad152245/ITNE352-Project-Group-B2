import socket
import threading
import json
import requests

api_url = 'https://newsapi.org/'
api_key = '27d7c542059d496ba63e8330cd595bd6'

print('----------------Server is Online----------------')

article_headline = input('Enter an article headline:')
passive_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
passive_server_socket.bind('127.0.0.1', 1010)
print('----------------Server is Waiting----------------')
passive_server_socket.listen(3)

def handle_client(client_socket):
    client_name = client_socket.recv(2048)
    print('Client ', client_name.decode('ascii'), ' is connected to the server')

    param = {'key': api_key, 'headline': article_headline}

    response = requests.get(api_url,param)

    if response.status_code == 200:
        requested_data = response.json()
        with open('b2.json', 'w') as file:
            json.dump(requested_data, file, indent=4)

    else:
        print('Something went wrong in proccessing your request:', response.text)
        print('Error code:', response.status_code)

while True:

    active_server_socket, address = passive_server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(active_server_socket,address))
    thread.start()

def handle_headlines(client_socket, client_name):
    headline_url = 'https://newsapi.org/v2/everything?q=business+OR+entertainment+OR+general+OR+health+OR+science+OR+sports+OR+technology&apiKey=27d7c542059d496ba63e8330cd595bd6'