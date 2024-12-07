import socket
import ssl

#SSL certificates
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Creating client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client to server connection
try:
    client_socket.connect(('192.168.100.176', 1010))
except:
    print("Connection failed")
    exit(0)

def print_data(data):
    data = data.decode('utf-8')
    print(data)

    

while True:
    try:
        # Main menu
        print("\nChoose the number of your option:")
        print("1. Search headlines")
        print("2. List of sources")
        print("3. Quit")
        option = input("Your option is: ")

        # Search headlines menu
        if option == "1":

            while True:
                print("\nChoose the number of your option:")
                print("1. Search for a keyword")
                print("2. Search by category")
                print("3. Search by country")
                print("4. List all new headlines")
                print("5. Back to the main menu")
                option2 = input("Your option is: ")

                if option2 == "1":  # Search for a specific keyword
                    client_socket.send("search".encode('ascii'))  # Send request type to server
                    keyword = input("Enter a keyword to search for: ")
                    client_socket.send(keyword.encode('ascii'))
                    
                    # Send additional info based on search options
                   
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))

                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))
                    print("Keyword search request sent to the server.")
                    data = client_socket.recv(2048)  # Receive the response
                    print_data(data)
                    

                elif option2 == "2":
                    # Search by category
                    client_socket.send("headlines".encode('ascii'))  # Send request type to server
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    country = input("Enter a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language
                    print("Category search request sent to the server.")
                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    

                elif option2 == "3":
                    # Search by country
                    client_socket.send("headlines".encode('ascii'))  # Send request type to server
                    country = input("Choose a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language
                    print("Country search request sent to the server.")

                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    
                elif option2 == "4":
                    # List all new headlines
                    client_socket.send("headlines".encode('ascii'))  # Send request type to server
                    country = input("Enter a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language
                    print("Request to list all headlines sent to the server.")

                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    
                elif option2 == "5":
                    # Back to the main menu
                    break

                else:
                    print("Invalid option. Please try again.")

        # List of sources menu
        elif option == "2":

            while True:
                print("\nChoose the number of your option:")
                print("1. Search by category")
                print("2. Search by country")
                print("3. Search by language")
                print("4. List all sources")
                print("5. Back to the main menu")
                option3 = input("Your option is: ")

                if option3 == "1":
                    # Search by category
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    country = input("Enter a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language

                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Category filter request sent to the server.")

                elif option3 == "2":
                    # Search by country
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    country = input("Choose a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language
                    print("Country filter request sent to the server.")
                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    

                elif option3 == "3":
                    # Search by language
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language
                    country = input("Enter a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    print("Language filter request sent to the server.")
                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    

                elif option3 == "4":
                    # List all sources
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    country = input("Enter a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))  # Send country
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))  # Send category
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))  # Send language
                    print("Request to list all sources sent to the server.")
                    # Receive and display data
                    data = client_socket.recv(2048)
                    print_data(data)
                    

                elif option3 == "5":
                    # Back to the main menu
                    break

                else:
                    print("Invalid option. Please try again.")

        # Quit option
        elif option == "3":
            print("Quitting...")
            print("Connection is closed.")
            client_socket.close()
            break

        # Invalid option selection
        else:
            print("Invalid option. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")
        break
