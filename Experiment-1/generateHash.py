import hashlib

def generate_sha256(input_string):
    # 1. Convert the string to bytes (SHA-256 needs bytes, not just text)
    encoded_string = input_string.encode()
    
    # 2. Create a SHA-256 hash object
    hash_object = hashlib.sha256(encoded_string)
    
    # 3. Convert the hash into a readable hexadecimal string
    hex_dig = hash_object.hexdigest()
    
    return hex_dig

user_input = input("Enter a String: ")
result = generate_sha256(user_input)

print(f"Input: {user_input}")
print(f"SHA-256 Hash: {result}")