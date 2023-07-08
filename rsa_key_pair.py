# https://stackoverflow.com/questions/2466401/how-to-generate-ssh-key-pairs-with-python
# Generate RSA key pair
def generate_key_pair():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

