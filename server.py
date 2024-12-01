import socket
import threading
import json
import requests

api_key = '27d7c542059d496ba63e8330cd595bd6'

print('----------------Server is Online----------------')
passive_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
passive_server_socket.bind(('127.0.0.1', 1010))

print('----------------Server is Waiting----------------')
passive_server_socket.listen(3)

def handle_client(client_socket):
    client_name = client_socket.recv(2048).decode('ascii')
    print('Client', client_name, 'is connected.')

    # Receive client request type
    client_request = client_socket.recv(2048).decode('ascii')  
    print('Received the request:', client_request)

    params = {'apiKey': api_key, 'limit': 15}

    if client_request == 'headlines':
        #Retrieve headlines filtered by country, category, and language
        params['country'] = input('Choose a country (au, ca, jp, ae, sa, kr, us, ma):')
        params['category'] = input('Choose a category (business, entertainment, general, sports, science, technology, health):')
        params['language'] = input('Choose a language (en, ar):')
        response = requests.get('https://newsapi.org/v2/everything?q=business+OR+entertainment+OR+general+OR+health+OR+science+OR+sports+OR+technology&apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)

    elif client_request == 'sources':
        #Retrieve sources filtered by country, category, and language
        params['country'] = input('Choose a country (au, ca, jp, ae, sa, kr, us, ma):')
        params['category'] = input('Choose a category (business, entertainment, general, sports, science, technology, health):')
        params['language'] = input('Choose a language (en, ar):')
        response = requests.get('https://newsapi.org/v2/top-headlines/sources?apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)

    elif client_request == 'search':
        # Search for news articles by keyword
        params['q'] = input('Enter keyword for searching articles:')
        params['language'] = input('Choose a language (en, ar):')
        params['country'] = input('Enter a specific country:')
        response = requests.get('https://newsapi.org/v2/everything?apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)

    else:
        print('Invalid request')

    # Process and save response
    if  response.status_code == 200:
        requested_data = response.json()
        filename = client_name,'_',client_request,'.json'
        with open(filename, 'w') as f:
            client_socket.send(json.dump(requested_data, f, indent=4).encode('ascii'))
        print('requested data saved to' , filename)

    else:
        print('Error in processing your request:', response.text)
        print('Error code:', response.status_code)

    client_socket.close()

#Multithreading
while True:
    active_server_socket, address = passive_server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(active_server_socket,address))
    thread.start()
