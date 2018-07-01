import Crypto
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


# Develop 16 byte key for AES encryption
def create_key():
   password = input('Encryption key: ' )
   hasher = SHA256.new(password.encode("utf-8"))
   return hasher.digest()

# Encrypt the message typed by client
def encrypt_message(message):
    message = str(message)
    key = create_key()
    # Initialization vector is needed for sender not receiver
    iv = get_random_bytes(16)
    # Key must be the same between sender and receiver 
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted_message = iv + cipher.encrypt(message.encode('utf-8'))
    return encrypted_message

# Decrypt message received
def decrypt_message(message):
    key = create_key()
    cipher = AES.new(key, AES.MODE_CFB)
    ready_message = cipher.decrypt(message)
    print('decrypted message: ', ready_message)


def main():
    message = encrypt_message()
    decrypt_message(message)

if __name__=="__main__":
    main()

