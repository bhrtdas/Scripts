import Crypto
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_message():
    # Get the message
    message = input("Type your secret message:")
    # Key must be the same between sender and receiver 
    key = b'Sixteen byte key'
    # Initialization vector is needed for sender not receiver
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_message = iv + cipher.encrypt(message.encode('utf-8'))
    print('encrypted message: ', encrypted_message)
    return encrypted_message

def decrypt_message(message):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_CFB)
    ready_message = cipher.decrypt(message)
    print('decrypted message: ', ready_message)

# def create_message(message):
#     rfid = input("What is your resistance fighter id? ")
#     destination = 
#     destination = input("Which resistance fighter are you sending this message to? ")
#     message = input("Type your message: ")
#     rfid = 'Luke'
#     message = 'on my way'
#     hosts = acquire_random_servers()
#     transmission = "From " + rfid + ": " + message
#     # your onion is essentially the nested list below
#     encapsulated_message = {
#         'destination': hosts[0],
#         'message': transmission
#     }
#     # turn dictionary into string and encode as bytes because the cipher will only accept bytes
#     bitten_transmission = str(encapsulated_message).encode('utf-8')
#     encapsulated_message = (
#     {"destination": destination,
#     "message": transmission },
#     {"destination": hosts[0],
#     "message": transmission },
#     {"destination": hosts[1],
#     "message": transmission}    
#     )
#     encrypt the nested list

def main():
    message = encrypt_message()
    decrypt_message(message)

if __name__=="__main__":
    main()

