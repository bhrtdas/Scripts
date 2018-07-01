from encrypt import encrypt_message, create_key
import random
import Crypto
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import socket
import pickle

ENCRYPTION_LEVEL = 4

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


known_resistance_fighters = (
    {
        'rfid': 'luke',    
        'device_ip': '127.0.0.1',
        'port': 5600
    }
)


def acquire_random_servers():
    hosts = random.sample(known_servers, ENCRYPTION_LEVEL)
    return hosts

# Use global variable to maintain current message as it is being wrapped
message = ""
current_message = message

# Use message template to add and populate next layer of onion
message_template = {
     "server": "",
     "port": "",
     "message": ""
}

def message():
    global message
    global rfid
    rfid = input('What is your resistance fighter id?')
    user_message = input("Type your message: ") +  "-" + rfid
    message = message_template
    message['server'] = known_resistance_fighters['device_ip']
    message['port'] = known_resistance_fighters['port']
    message['message'] = encrypt_message(user_message)
    print("Here is the message that will be transmitted:", message)
    print('encrypting...')
    print('sending ... ')
    print('done')

def build_onion(hosts):
    global current_message
    current_message = message
    print('current message is:', current_message)
    for x in range(ENCRYPTION_LEVEL):
        current_layer = dict(message_template)
        current_layer['message'] = current_message
        current_layer['server'] = hosts[x]['host']
        current_layer['port'] = hosts[x]['port']
        current_message = current_layer
        print(current_message)
        
    
    print('Final Message:', current_message)

def send_message(message):
    hosts = acquire_random_servers()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((message['server'],message['port']))
    try:
        transmission = pickle.dumps(message)
        sock.send(transmission)
        print("transmission sent ya know")          
    except KeyboardInterrupt:
        sock.close()
    
    return message

def main():
    hosts = acquire_random_servers()
    message()
    build_onion(hosts)


if __name__=="__main__":
    main()
    send_message(current_message)

