Python Chat Application
=======================

Overview
--------
This Python Chat Application allows multiple clients to communicate with each other through a server. 
The application supports basic functionalities such as user authentication, message timestamps, and 
a graphical user interface (GUI) using `tkinter`. Each message sent by a client is acknowledged by the server.

Features
--------
- User Authentication: Each client can set a unique username.
- Message Timestamps: Messages include timestamps indicating when they were sent.
- Graphical User Interface: A user-friendly GUI using `tkinter`.
- Message Acknowledgment: The server acknowledges each message received from the clients.

Requirements
------------
- Python 3.x
- `tkinter` library (usually included with Python)

Installation
------------
1. Clone the repository or download the source code:
git clone https://github.com/your-repository/chat-app.git
cd chat-app

css
Copy code

2. Navigate to the project directory:
cd chat-app

markdown
Copy code

Usage
-----
### Start the Server
1. Open a terminal or command prompt.
2. Navigate to the directory where `server.py` is located.
3. Run the server using the command:
python server.py

markdown
Copy code
4. The server will start and listen for incoming connections on `127.0.0.1:12345`.

### Start the Client
1. Open another terminal or command prompt.
2. Navigate to the directory where `client.py` is located.
3. Run the client using the command:
python client.py

markdown
Copy code
4. A prompt will appear asking for a username. Enter a username and press Enter.
5. The chat window will appear, allowing you to send and receive messages.

### Chatting
- **Send Messages**: Type your message in the entry field and press Enter or click the "Send" button.
- **Receive Messages**: Messages from other clients and acknowledgments from the server will appear in the chat box.

### Exiting
- **Client**: To exit the client, simply close the GUI window.
- **Server**: To stop the server, use `Ctrl+C` in the terminal where the server is running.

Code Overview
-------------
### Server Code (`server.py`)
The server handles incoming connections, manages client threads, broadcasts messages, and sends acknowledgments.
Key functionalities include:
- **Client Handling**: A separate thread is created for each client to manage their messages.
- **Broadcasting**: Messages from a client are broadcast to all other connected clients.
- **Acknowledgment**: The server sends an acknowledgment back to the client for each received message.

### Client Code (`client.py`)
The client connects to the server, sets up the GUI, and handles sending and receiving messages.
Key functionalities include:
- **User Authentication**: The client prompts for a username upon starting.
- **GUI Setup**: Uses `tkinter` for a graphical interface, allowing easy message sending and receiving.
- **Message Handling**: The client can send messages to the server and display messages from the server and other clients.

Example
-------
### Starting the Server
$ python server.py
Server started on 127.0.0.1:12345
Connection established with ('127.0.0.1', 56789)

shell
Copy code

### Starting the Client
$ python client.py

less
Copy code
- A prompt appears asking for a username.
- Enter a username (e.g., `User1`).

Write anything that you want and it will be outputted in the command prompt
