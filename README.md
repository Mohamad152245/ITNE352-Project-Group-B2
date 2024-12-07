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
