# https://stackoverflow.com/questions/2466401/how-to-generate-ssh-key-pairs-with-python
# Generate RSA key pair
def generate_key_pair():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

#Save RSA key pair to files
def save_key_pair(public_key, private_key):
    with open('public_key.pem', 'w') as file:
        file.write(public_key.save_pkcs1().decode())
    with open('private_key.pem', 'w') as file:
        file.write(private_key.save_pkcs1().decode())

#Load RSA key pair from files
def load_key_pair():
    with open('public_key.pem', 'r') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read().encode())
    with open('private_key.pem', 'r') as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read().encode())
    return public_key, private_key

#Encrypt file using RSA
def encrypt_file(file_path, public_key):
    with open('file_path', 'rb') as file:
        file_data = file.read()
        encrypted_data = rsa.encrypt(file_data, public_key)
    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    return encrypted_file_path

#Decrypt file using RSA
def decrypt_file(encrypted_file_path, private_key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        decrypted_data = rsa.decrypt(encrypted_data, private_key)
    decrypted_file_path = encrypted_file_path.replace(".encrypted", "_decrypted.txt")
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
        return decrypted_file_path

# Example usage
def main():
    # Check RSA key pair files exit
    if not os.path.isfile('public_key.pem') or not os.path.isfile('private_key.pem'):
        public_key, private_key = generate_key_pair() 
        save_key_pair(public_key, private_key)
        print("Generated RSA key pair.")
    
    # Load RSA key pair from files
    public_key, private_key = load_key_pair()
    print("Loaded RSA key pair.")

    # Encrypt file
    file_path = r"D:\Code\python\testrsa.txt"
    encrypted_file_path = encrypt_file(file_path, public_key)
    print(f"File encrypted successfully. Encrypted file: {encrypted_file_path}")

    # Decrypt file
    decrypted_file_path = decrypt_file(encrypted_file_path, private_key)
    print(f"File decrypted successfully. Decrypted file: {decrypted_file_path}")

if __name__ == '__main__':
    main()
