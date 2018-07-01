import random
import socket
import sys
import signal
from Crypto.Cipher import AES
from Crypto import Random
from encapsulate_message import encrypt_message, acquire_random_servers, message, build_onion, send_message

ENCRYPTION_LEVEL = 4

known_servers = (
    {
        "host": "127.0.0.1",
        "port": 5555
    },
    {
        "host": "127.0.0.1",
        "port": 5556
    }
    )

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
    
def main():
    hosts = acquire_random_servers()
    message()
    build_onion(hosts)

if __name__=="__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    main()
    send_message(current_message)
    # unwrap_onion(current_message)