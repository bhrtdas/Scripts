import random
import Crypto
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import socket
import pickle 

known_servers = (
    {
        "host": "127.0.0.1",
        "port": 5555,
        "message": []
    },
    {
        "host": "127.0.0.1",
        "port": 5556,
        "message": []
    },
    {
        "host": "127.0.0.1",
        "port": 5558,
        "message": []
    },
    {
        "host": "127.0.0.1",
        "port": 5559,
        "message": []
    }
    )

def encrypt_message(message):
    message = str(message)
    # Key must be the same between sender and receiver 
    key = b'Sixteen byte key'
    # Initialization vector is needed for sender not receiver
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_message = iv + cipher.encrypt(message.encode('utf-8'))
    return encrypted_message

def decrypt_message(message):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_CFB)
    ready_message = cipher.decrypt(message)
    print('decrypted message: ', ready_message)

def acquire_random_servers():
    hosts = random.sample(known_servers, ENCRYPTION_LEVEL)
    return hosts

ENCRYPTION_LEVEL = 4

message = ""

message_template = {
     "server": "",
     "port": "",
     "message": ""
}

current_message = message

def message():
    global message
    rfid = input("What is your resistance fighter id? ")
    message = rfid + ": " + input("Type your message: ")
    print("Here is the message that will be transmitted:", message)

def build_onion(hosts):
    global current_message
    current_message = message
    print('current message is:', current_message)
    for x in range(ENCRYPTION_LEVEL):
        current_layer = dict(message_template)
        current_layer['message'] =  current_message
        current_layer['server'] = hosts[x]['host']
        current_layer['port'] = hosts[x]['port']
        current_message = current_layer
        
    print('Final Message:', current_message)

def send_message(message):
    hosts = acquire_random_servers()
    # user_decide = input('Transmit message to first port: %s ? (yes or no)' % message['port'])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        while True:
            # if user_decide == 'yes':
            sock.connect((message['server'],message['port']))
            transmission = pickle.dumps(message)
            sock.send(transmission)          
    finally:
        sock.close()

def unwrap_onion(message):
    print('next port is:', message['port']  )
    if (isinstance(message['message'], dict)):
        unwrap_onion(message['message'])
    
    return message['server']
    return message['port']

def main():
    hosts = acquire_random_servers()
    message()
    build_onion(hosts)


if __name__=="__main__":
    main()
    send_message(current_message)
    # unwrap_onion(current_message)
    




 