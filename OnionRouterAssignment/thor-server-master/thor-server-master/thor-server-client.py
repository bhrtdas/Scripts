from onion_message import send_message, known_servers, known_resistance_fighters, message, message_template  
import socket # Can establish socket, listen on server and connect with client
import sys # Can pass arguments from terminal into functions 
import signal # Can build exception handler for keyboard interupt
from Crypto.Cipher import AES # Do symmetric encryption of message
from Crypto.Hash import SHA256 # Can turn any password into 16 byte key
from Crypto import Random # Use to acquire random bytes for IV 
from encrypt import decrypt_message 
import pickle # Will convert dictionary into byte stream and back 
from _thread import * # Can spawn thread for socket connection and allow socket to still listen

# Handle exception when ctrl + c is pressed in terminal
def sigint_handler(signal,frame):
        print("transmission ended")
        sys.exit()

# Do all work on a particular instance of socket connection then close instance.
def threaded_client(conn):
    while True:
        global message
        # Receive the data
        data = conn.recv(4096) 
        if data:
            # convert the bite stream
            message = pickle.loads(data)
            # Unwrap the top layer
            message = message['message']
            # Send to the next node
            if type(message) == dict:             
                print("received", message)
                send_message(message)
                print('sending messasge to: {}:{}'.format(message['server'], message['port']))
            # Decrypt and print if not dictionary 
            else:
                print('decrypting ...  ', message)
                message = decrypt_message(message)
                print(message)
                return message

        else:
            print("connection to the resistance was broken")
            break
    # Close this particular instance of socket connection
    conn.close()


# Establish socket 
def listen_on_socket(ip, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port and listen for incoming traffic
    server_address = ip, int(port)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)    
    sock.listen(5)   
    while True:
        # Accept instance of socket connection and pass to thread for work 
        conn, client_address = sock.accept()
        print('connection from', client_address)
        start_new_thread( threaded_client, (conn,))

if __name__=="__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    listen_on_socket(sys.argv[1], sys.argv[2])
    