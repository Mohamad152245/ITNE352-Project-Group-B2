import socket
import threading
import json
import requests
import ssl
import os

api_key = '27d7c542059d496ba63e8330cd595bd6'

print('----------------Server is Online----------------')

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
current_dir = os.path.dirname(os.path.abspath(__file__))
cert_path = os.path.join(current_dir, 'server.crt')
key_path = os.path.join(current_dir, 'server.key')
context.load_cert_chain(certfile= cert_path, keyfile= key_path)

passive_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
passive_server_socket.bind(('192.168.100.176', 1010))

print('----------------Server is Waiting----------------')
passive_server_socket.listen(3)

def handle_client(client_socket):
    # Receive the client request type (headlines, sources, or search)
    client_request = client_socket.recv(2048).decode('ascii')
    print('Received the request:', client_request)
    
    # Ensure valid request
    if client_request not in ['headlines', 'sources', 'search']:
        print(f"Invalid request: {client_request}")
        client_socket.send(f"Invalid request: {client_request}".encode('ascii'))
        client_socket.close()
        return

    params = {'apiKey': api_key, 'limit': 15}

    # Depending on the request type, handle accordingly
    if client_request == 'headlines':
        category = client_socket.recv(2048).decode('ascii')  # Receive category
        country = client_socket.recv(2048).decode('ascii')  # Receive country
        language = client_socket.recv(2048).decode('ascii')  # Receive language

        params['language'] = language  # Always set language

    # Check if we are using /top-headlines or /everything
        if country:  # If country is specified, we should use /top-headlines
                params['country'] = country
                response = requests.get('https://newsapi.org/v2/top-headlines?apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)
        else:  # If no country is specified, use /everything and only use keywords and language
                params['q'] = category  # Use category as search keywords for /everything
                response = requests.get('https://newsapi.org/v2/everything?apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)

    elif client_request == 'sources':
        category = client_socket.recv(2048).decode('ascii')  # Receive category
        country = client_socket.recv(2048).decode('ascii')  # Receive country
        language = client_socket.recv(2048).decode('ascii')  # Receive language

        params['category'] = category
        params['country'] = country
        params['language'] = language

        response = requests.get('https://newsapi.org/v2/top-headlines/sources?apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)

    elif client_request == 'search':
        keyword = client_socket.recv(2048).decode('ascii')  # Receive keyword for searching
        language = client_socket.recv(2048).decode('ascii')  # Receive language
        country = client_socket.recv(2048).decode('ascii')  # Receive country

    # Set up parameters for the /everything endpoint
        params['q'] = keyword  # The keyword for the search
        params['language'] = language  # Language for filtering

    # Only add country to params if it's provided, but note that it's not supported in /everything endpoint
        if country:
             print("Country parameter is not supported in /everything. It will be ignored.")

    # Perform the request to /everything endpoint, without including the 'country' parameter
        response = requests.get('https://newsapi.org/v2/everything?apiKey=27d7c542059d496ba63e8330cd595bd6', params=params)
    else:
        print(f"Invalid request: {client_request}")
        client_socket.send(f"Invalid request: {client_request}".encode('ascii'))
        client_socket.close()
        return

    # Process and save response
    if response.status_code == 200:
        requested_data = response.json()
        filename = f"client_data_{client_request}.json"
        with open(filename, 'w') as f:
            json.dump(requested_data, f, indent=4)
        print(f'Data saved to {filename}')
        
        # Send back data to the client
        client_socket.send(json.dumps(requested_data, indent=4).encode('ascii'))
    else:
        error_message = f"Error in processing your request: {response.text}, Error code: {response.status_code}"
        print(error_message)
        client_socket.send(error_message.encode('ascii'))

    client_socket.close()

# Multithreading
while True:
    active_server_socket, address = passive_server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(active_server_socket,))
    thread.start()