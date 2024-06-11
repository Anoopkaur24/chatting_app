import socket
import threading
import tkinter as tk
from tkinter import simpledialog

# Client setup
HOST = '127.0.0.1'
PORT = 12345

# Function to receive messages from the server
def receive_messages(client_socket, chat_box):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_box.config(state=tk.NORMAL)
                chat_box.insert(tk.END, message + '\n')
                chat_box.config(state=tk.DISABLED)
                chat_box.yview(tk.END)
        except:
            break

# Main function to start the client
def start_client():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Get username
    username = simpledialog.askstring("Username", "Please choose a username")
    client.send(f"/username {username}".encode('utf-8'))

    # Set up GUI
    root = tk.Tk()
    root.title("Chat Application")

    chat_frame = tk.Frame(root)
    scrollbar = tk.Scrollbar(chat_frame)
    chat_box = tk.Text(chat_frame, height=15, width=50, yscrollcommand=scrollbar.set, state=tk.DISABLED)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
    chat_box.pack()
    chat_frame.pack()

    entry_field = tk.StringVar()
    entry_box = tk.Entry(root, textvariable=entry_field)
    entry_box.bind("<Return>", lambda event: send_message(entry_field))
    entry_box.pack()

    send_button = tk.Button(root, text="Send", command=lambda: send_message(entry_field))
    send_button.pack()

    # Start thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(client, chat_box))
    thread.start()

    root.mainloop()

    client.close()

# Function to send messages to the server
def send_message(entry_field):
    message = entry_field.get()
    entry_field.set("")
    client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
