import socket

#creating client socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client to server connection 
try:
    client_socket.connect(('127.0.0.1',1010))
except:
    print("connaction  faild")
    exit(0) 

def print_data(data):
    Data = data.decode('utf-8')
    print(Data)

while True:

    try:

        #main menu
        print("Choose the number of your option")
        print("1.Search headlines ")
        print("2.List of sources")
        print("3.Quit")
        option = input("your option is : ")

        #search headlines menu
        if option == "1":

            while True:

                print("Choose the number of your option")
                print("1.search for key word")
                print("2.search for caregory")
                print("3.search for country")
                print("4.list all new headlines")
                print("5.back to the main menu")
                option2 = input("your option is : ")

                if option2 == "1":
                    # Search for a specific keyword
                    client_socket.send("search".encode('ascii'))  # Send request type to server
                    keyword = input("Enter a keyword to search for: ")
                    client_socket.send(keyword.encode('ascii'))
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Keyword search request sent to the server.")
                   
                elif option2 == "2":
                    # Search by category
                    client_socket.send("headlines".encode('ascii'))  # Send request type to server
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Category search request sent to the server.")
                    
                elif option2 == "3":
                    # Search by country
                    client_socket.send("headlines".encode('ascii'))  # Send request type to server
                    country = input("Choose a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Country search request sent to the server.")
                    
                elif option2 == "4":
                    # List all new headlines
                    client_socket.send("headlines".encode('ascii'))  # Send request type to server
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Request to list all headlines sent to the server.")

                elif option2 == "5":
                    # Back to the main menu
                    break
                else :
                    print("Invalid option")
            

        #list of sources menu
        elif option == "2":

            while True:

                print("Choose the number of your option")
                print("1.search for caregory")
                print("2.search for country")
                print("3.search by language")
                print("4.list all")
                print("5.back to the main menu")
                option3 = input("your option is : ")

                if option3 == "1":
                     # Search by category
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    category = input("Choose a category (business, entertainment, general, sports, science, technology, health): ")
                    client_socket.send(category.encode('ascii'))
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Category filter request sent to the server.")
                    
                elif option3 == "2":
                    # Search by country
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    country = input("Choose a country (au, ca, jp, ae, sa, kr, us, ma): ")
                    client_socket.send(country.encode('ascii'))
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Country filter request sent to the server.")
                    
                elif option3 == "3":
                    # Search by language
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    language = input("Choose a language (en, ar): ")
                    client_socket.send(language.encode('ascii'))
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Language filter request sent to the server.")
                    
                elif option3 == "4":
                    # List all sources
                    client_socket.send("sources".encode('ascii'))  # Send request type to server
                    data = client_socket.recv(2048)
                    print_data(data)
                    print("Request to list all sources sent to the server.")

                elif option3 == "5":
                    # Back to the main menu
                    break
                else :
                    print("Invalid option")

        elif option == "3":
            print("Quitting") 
            print("connection is closed")
            client_socket.close() 
            break

         
        #invalid option selection  
        else:
            print("Invalid option")


            

    
    
    except :    
        print("error")
        break
