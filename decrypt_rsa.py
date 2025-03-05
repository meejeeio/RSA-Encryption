from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def load_private_key(filename):
    """Load the private key from a file"""
    with open(filename, 'r') as key_file:
        return RSA.import_key(key_file.read())

def decrypt_data(private_key):
    """Decrypt data from encrypted_data.txt and save to file"""
    with open("encrypted_data.txt", "r") as enc_file:
        encrypted_data = enc_file.read()
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher_rsa.decrypt(base64.b64decode(encrypted_data))
    decoded_decrypted_data = decrypted_data.decode('utf-8')

    with open("decrypted_data.txt", "w") as dec_file:
        dec_file.write(decoded_decrypted_data)

    return decoded_decrypted_data

if __name__ == "__main__":
    private_key = load_private_key("J:\PYTHON\Encryption_RSA\private.pem")  # Load existing private key
    
    try:
        decrypted = decrypt_data(private_key)
        print("\nDecrypted Data saved to decrypted_data.txt")
    except Exception as e:
        print("\nDecryption failed:", str(e))
