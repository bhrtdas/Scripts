from encapsulate_message import send_message
import socket
import sys
import signal
from Crypto.Cipher import AES
from Crypto import Random
from encrypt import decrypt_message
import pickle
import ast

message = ""

message_template = {
     "server": "",
     "port": "",
     "message": ""
}

current_message = message

def sigint_handler(signal,frame):
        print("transmission ended")
        sys.exit()

def connect_to_resist(ip, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ip, int(port)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)    
    sock.listen(5)   
    # Accept socket connection
    conn, client_address = sock.accept()
    print('connection from', client_address)
    while True:
        try: 
            while True:
                global message
                # Receive the data in byte-sized chunks, decrypt and convert to ascii
                data = conn.recv(4096) 
                if data:
                    message = pickle.loads(data)
                    # print('type of message received', type(message))
                    # # message = message.decode('ascii')
                    # # print('type of message after decode', type(message))                                                         
                    # print('message is: ', message) 
                    message = message['message']
                    if type(message) == dict:
                        # print('message test is:', type(message['message']))
                        # print('we have unwrapped a layer of message')
                        # print('New message to send is:', message)                    
                        send_message(message)
                        print('sending messasge to: {}:{}}'.format(message['server'], message['port']))
                    else:
                        print(message)
                        return message

                else:
                    break 
        finally:
            # End the particular session with the client (but keep listening)
            conn.close()

if __name__=="__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    connect_to_resist(sys.argv[1], sys.argv[2])
    