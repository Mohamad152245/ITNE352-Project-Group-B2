import socket

#creating client socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client to server connection 
try:
    client_socket.connect(('127.0.0.1',1010))
except:
    print("connaction  faild")
    exit(0) 

def retrieve_data(data):
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
                print("3.list all new headlines")
                print("4.back to the main menu")
                option2 = input("your option is : ")

                if option2 == "1":

                    pass
                elif option2 == "2":

                    pass
                elif option2 == "3":

                    pass
                elif option2 == "4":
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

                    pass
                elif option3 == "2":

                    pass
                elif option3 == "3":

                    pass
                elif option3 == "4":

                    pass
                elif option3 == "5":
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
