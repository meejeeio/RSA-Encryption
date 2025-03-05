from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def load_public_key(filename):
    """Load the public key from a file"""
    with open(filename, 'r') as key_file:
        return RSA.import_key(key_file.read())

def encrypt_data(data, public_key):
    """Encrypt data and save to file"""
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher_rsa.encrypt(data.encode('utf-8'))
    encoded_encrypted_data = base64.b64encode(encrypted_data).decode('utf-8')

    with open("encrypted_data.txt", "w") as enc_file:
        enc_file.write(encoded_encrypted_data)

    return encoded_encrypted_data

if __name__ == "__main__":
    public_key = load_public_key("public.pem")  # Load existing public key
    
    data = input("Enter data to encrypt: ")  # Get data from user
    encrypted = encrypt_data(data, public_key)
    
    print("\nEncrypted Data saved to encrypted_data.txt")
