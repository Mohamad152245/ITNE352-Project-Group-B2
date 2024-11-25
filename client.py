import socket

#creating client socket 
client_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client to server connection 
try:
    client_Sock.connect(('192.168.0.1',5000))
except:
    print("connaction  faild")
    exit(0) 

while True:

    try:

        #main menu
        print("Choose the number of your option")
        print("1.Search headlines ")
        print("2.List of sources")
        print("3.Quit")
        option = input(int("your option is : "))

        #search headlines menu
        if option == "1":
            print("Choose the number of your option")
            print("1.search for key word")
            print("2.search for caregory")
            print("3.search for country")
            print("3.list all new headlines")
            print("4.back to the main menu")
            option2 = input(int("your option is : "))

        #list of sources menu
        elif option == "2":
            print("Choose the number of your option")
            print("1.search for caregory")
            print("2.search for country")
            print("3.search by language")
            print("4.list all")
            print("5.back to the main menu")
            option3 = input(int("your option is : "))
         
        #invalid option selection  
        else:
            print("Invalid option")


            

    
    
    except :    
        break
