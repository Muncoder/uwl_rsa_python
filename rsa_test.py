import rsa

# Generate RSA key pair
def generate_key_pair():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

print(f"Public Key: { generate_key_pair()[0]}")
print("=======================================================")
print("=======================================================")
print("=======================================================")
print(f"Private Key: { generate_key_pair()[1]}")
