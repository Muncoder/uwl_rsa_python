import rsa
import os
import glob

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
    with open(file_path, 'rb') as file:
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

#Main Menu
def main_menu():
    # os.system('clear')
    # return "hello"
    print('---------------------------------------------------------------------------------------------------')
    print('* Module / Code : Applied Cryptography / CP5SA87E       |     Assignment 1 : Crypto RSA by Python *')
    print('* Module Leader : Dr. Waqar Asif                        |     Developed by : Group7               *')
    print('* ----------------------------------------------------------------------------------------------- *')
    print('* Student ID/Name : 21575537, MOHAMMAD MUNIR UDDIN                                                *')
    print('* Student ID/Name : 21577165, MOHAMED CHARIF CHAIRI BENAICHA                                      *')
    print('* Student ID/Name : 21588720, ABU BAKARR KARGBO                                                   *')
    print('* Student ID/Name : 21580794, SABA SULTANA                                                        *')
    # print('* --------------------------------------------------------------------------------------------- *')
    print('********************************************** M E N U ********************************************')
    print('* [ 1 ] Show available txt files                                                                  *')
    print('* [ 2 ] Encrypt a file                                                                            *')
    print('* [ 3 ] Decrypt the encrypted file                                                                *')
    print('* [ 4 ] Show file content before encryption                                                       *')
    print('* [ 5 ] Show file content after encryption                                                        *')
    print('* [ 6 ] Show file content after decryption                                                        *')
    print('* [ 0 ] Exit                                                                                      *')
    print('***************************************************************************************************')
    print("")

# main method for:
# -------------------------------------------------------
# 1. generate public and private keys
# 2. save public and private keys on the current folder
# 3. txt files available to encrypt on the folder "files"
# 4. encrypt file on the folder "files"
# 5. decrypt file on the folder "files"
def main():
    encrypted_file_path = ''
    file_to_encrypt = ''
    encrypted_file_path = ''
    decrypted_file_path = ''

    # # Check RSA key pair files exit
    if not os.path.isfile('public_key.pem') or not os.path.isfile('private_key.pem'):
        # Generate new key pair if files do not exist.
        public_key, private_key = generate_key_pair() 
        save_key_pair(public_key, private_key)
        print("Generated RSA key pair and saved on the current folder.")
    
    # Load RSA key pair from files
    public_key, private_key = load_key_pair()
    print("Loaded RSA key pair.")

    # os.system('clear')

    while True:
        main_menu()

        user_input = input("Select your option: ")
        if user_input == '1':
            txtfiles = []
            for file in glob.glob("files/*.txt"):
                txtfiles.append(os.path.basename(file))

            if (len(txtfiles) > 0):
                # main_menu()
                for file_name in txtfiles:
                    f = file_name.split(".")        
                    if len(f) <= 2:
                        print(f[0] + "." + f[1])
            else:
                print("No txt file found.")

        if user_input == '2':
            # Encrypt file
            file_to_encrypt = input("Enter text file name to encrypt: ")

            file_to_encrypt = os.path.join("files/", file_to_encrypt)

            if os.path.isfile(file_to_encrypt) == True:
                print("Text File exists")

                encrypted_file_path = encrypt_file(file_to_encrypt, public_key)
                print(f"File encrypted successfully. Encrypted file: {encrypted_file_path}")
            elif file_to_encrypt == '0':
                break
            else:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("Text File is not exists")
                print("----------------------------------------------------------------------------------------------------------------------")
                print()
                print()
        elif user_input == '3':
            if encrypted_file_path != '':
                # Decrypt file
                decrypted_file_path = decrypt_file(encrypted_file_path, private_key)
                print(f"File decrypted successfully. Decrypted file: {decrypted_file_path}")
            else:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("No file encrypted yet. Need to encrypt the file first to decrypt.")
                print("----------------------------------------------------------------------------------------------------------------------")
                print()
                print()
        elif user_input == '4':
            if file_to_encrypt != '':
                # Show txt file content
                if os.path.isfile(file_to_encrypt) == True:
                    f = open(file_to_encrypt, 'r')
                    file_contents = f.read()
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print (file_contents)
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("")
            else:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("No txt file selected yet. Select the txt file first")
                print("----------------------------------------------------------------------------------------------------------------------")
                print()
                print()
        elif user_input == '5':
            if file_to_encrypt != '':
                # Show encrypted file content
                if os.path.isfile(file_to_encrypt) == True:
                    # f = open(encrypted_file_path, 'r')
                    # file_contents = f.read()
                    command = "cat " + encrypted_file_path
                    os.system(command)
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    # print (file_contents)
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("")
            else:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("No txt file selected yet. Select the txt file first")
                print("----------------------------------------------------------------------------------------------------------------------")
                print()
                print()
        elif user_input == '6':
            if decrypted_file_path != '':
                # Show decrypted file content
                if os.path.isfile(decrypted_file_path) == True:
                    f = open(decrypted_file_path, 'r')
                    file_contents = f.read()
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("")
                    print (file_contents)
                    print("----------------------------------------------------------------------------------------------------------------------")
                    print("")
            else:
                print("----------------------------------------------------------------------------------------------------------------------")
                print("No File Decrypted Yet. Decrypt a file first to view its content.")
                print("----------------------------------------------------------------------------------------------------------------------")
                print()
                print()
        elif user_input == '0':
            print("###########################################################")
            print("#                                                         #")
            print("#  Thank you for using this program, Crypto RSA by Python #")
            print("#  Developed by  : Group7                                 #")
            print("#  Module        : Applied Cryptography / CP5SA87E        #")
            print("#  Module Leader : Dr. Waqar Asif                         #")
            print("#                                                         #")
            print("###########################################################")
            break

if __name__ == '__main__':
    main()
