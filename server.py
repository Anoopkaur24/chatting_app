import socket
import threading
import datetime

# Server setup
HOST = '127.0.0.1'
PORT = 12345

clients = []
usernames = {}

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message.startswith('/username '):
                    username = message.split(' ')[1]
                    usernames[client_socket] = username
                    broadcast(f"{username} has joined the chat!", client_socket)
                else:
                    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    username = usernames.get(client_socket, "Unknown")
                    formatted_message = f"[{timestamp}] {username}: {message}"
                    print(formatted_message)
                    broadcast(formatted_message, client_socket)
                    client_socket.send(f"Server: Message received at {timestamp}".encode('utf-8'))
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(connection):
    if connection in clients:
        username = usernames.get(connection, "Unknown")
        clients.remove(connection)
        del usernames[connection]
        broadcast(f"{username} has left the chat.", connection)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {addr}")

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
