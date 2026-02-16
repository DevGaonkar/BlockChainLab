import hashlib
import time

def mine_new_block(input_data, difficulty):
    # The 'target' is a string of zeros (e.g., "00" or "000")
    target_prefix = "0" * difficulty
    nonce = 0
    
    print(f"Target: {target_prefix}... (Looking for {difficulty} leading zeros)")
    start_time = time.time()

    while True:
        # 1. Combine data and nonce into one string
        content = input_data + str(nonce)
        
        # 2. Generate the SHA-256 hash
        current_hash = hashlib.sha256(content.encode()).hexdigest()
        
        # 3. Check if the hash meets the target
        if current_hash.startswith(target_prefix):
            end_time = time.time()
            print(f"\nSUCCESS! Block Mined.")
            print(f"Final Nonce: {nonce}")
            print(f"Final Hash: {current_hash}")
            print(f"Time taken: {end_time - start_time:.4f} seconds")
            break
        
        # 4. If not, increment nonce and try again
        nonce += 1

# --- Run the Experiment ---
my_data = input("Enter transaction data: ")
diff = int(input("Enter difficulty (e.g., 1 to 5): "))

mine_new_block(my_data, diff)