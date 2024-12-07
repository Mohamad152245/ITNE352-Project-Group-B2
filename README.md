# ITNE352-Project-Group-B2

# Multithreaded News Client/Server Information System

**University of Bahrain**  
**College of Information Technology**  
**Department of Computer Engineering**  
**ITCE320: Network Programming, S1 2024-2025**  

**Submitted to:** Dr. Mohammed Almeer  
**Group:** B2 Section 2  
**Team Members:**  
- Ali Salman Ali (202103011)  
- Mohammad Hamzah Murad (202101456)  

---

## Table of Contents

1. [Project Description](#project-description)  
2. [Requirements](#requirements)  
   - [Install Required Libraries](#install-required-libraries)  
3. [System Architecture](#system-architecture)  
   - [Server Overview](#server-overview)  
   - [Client Overview](#client-overview)  
4. [Implementation Details](#implementation-details)  
   - [Server Functionalities](#server-functionalities)  
   - [Client Functionalities](#client-functionalities)  
5. [Packages and Modules](#packages-and-modules)  
   - [Server Modules](#server-modules)  
   - [Client Modules](#client-modules)  
6. [Additional Concept](#additional-concept)  
   - [Server-Side Setup](#server-side-setup)  
   - [Client-Side Setup](#client-side-setup)  
7. [Conclusion](#conclusion)  

---

## Project Description

This project focuses on creating a Python-based client-server system for exchanging news information using an API. It emphasizes the following key principles:  

- **Architecture**  
- **Network Communication**  
- **Multithreading**  
- **API Integration**  

The system supports multiple client connections simultaneously using multithreading.

---

## Requirements

### Install Required Libraries

The project requires the following external Python libraries:  

- **`requests`**: To handle API requests.  
  ```bash
  pip install requests

 - **`SSL certificates`**:requires SSL certificates
    ```bash
    openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes

### System Architecture

The system is designed with a client-server architecture, enabling communication between multiple clients and a single server. The architecture ensures secure data exchange, multithreading for handling multiple client connections, and integration with an external News API for retrieving news data.

#### Server Overview
The server acts as the central hub of the system, handling client requests and interacting with the News API. It performs the following key roles:
- Listens for incoming client connections using a secure SSL connection.
- Processes client requests for news headlines, sources, or specific search terms.
- Fetches relevant data from the News API and sends it back to the requesting client.
- Utilizes multithreading to handle multiple client connections simultaneously.

#### Client Overview
The client provides an interface for users to interact with the server. It performs the following roles:
- Connects securely to the server using SSL.
- Sends user-defined requests (e.g., retrieve news headlines, sources, or search results) to the server.
- Displays the server's responses (news data) to the user in a readable format.

### Implementation Details

#### Server Functionalities
- **Multi-Threaded Server**: The server spawns a new thread for each client connection, ensuring that multiple clients can interact with the server concurrently without blocking.
- **Request Processing**: The server processes three types of requests:
  - **Headlines**: Fetches the latest headlines from the News API.
  - **Sources**: Retrieves the list of news sources available on the API.
  - **Search**: Searches for news articles based on a keyword provided by the client.
- **Data Storage**: The server saves the retrieved news data locally as a JSON file for further use or debugging.

#### Client Functionalities
- **Menu-Driven Interface**: The client provides a user-friendly menu to select options such as retrieving headlines, sources, or searching for news articles.
- **Request Handling**: Based on the user's choice, the client sends the appropriate request to the server along with any necessary parameters (e.g., search keywords).
- **Response Display**: The client receives the server's response and displays the news data in a structured and readable format.

### Packages and Modules

#### Server Modules
- **socket**: Used to create a TCP server socket for communication with clients.
- **threading**: Enables multithreading to handle multiple client connections simultaneously.
- **ssl**: Used to establish a secure communication channel between the server and the clients.
- **requests**: Handles HTTP requests to the News API for retrieving news data.
- **json**: Parses and formats JSON responses from the News API.

#### Client Modules
- **socket**: Establishes a TCP connection to the server.
- **ssl**: Ensures secure communication with the server.

### Additional Concept

#### Server Side Setup
- The server sets up an SSL context to enable secure communication with clients.
- **SSL Context**:
  - `ssl.Purpose.CLIENT_AUTH`: Configures the server to authenticate clients.
  - `load_cert_chain(certfile, keyfile)`: Loads the server's SSL certificate (`server.crt`) and private key (`server.key`) for secure communication.

#### Client Side Setup
- The client creates an SSL context to establish a secure connection with the server.
- **SSL Context**:
  - `check_hostname = False`: Disables hostname verification for simplicity.
  - `verify_mode = ssl.CERT_NONE`: Skips verification of the server's certificate.

### Conclusion

In this project, we successfully developed a multithreaded client-server system that exchanges news information using Python. The system highlights the principles of client-server architecture, secure communication using SSL, multithreading for concurrent connections, and API integration for dynamic news retrieval. This implementation demonstrates the practical application of network programming concepts in a real-world scenario.
