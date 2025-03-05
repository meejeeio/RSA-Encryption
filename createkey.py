from Crypto.PublicKey import RSA

def generate_and_save_keys():
    """Generate RSA key pair and save them to private.pem and public.pem"""
    key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    
    # Save Private Key
    private_key = key.export_key()
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)
    
    # Save Public Key
    public_key = key.publickey().export_key()
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)

    print("✅ Keys generated and saved successfully!")
    print("\n🔑 Private Key saved in 'private.pem'")
    print("🔓 Public Key saved in 'public.pem'")

if __name__ == "__main__":
    generate_and_save_keys()
