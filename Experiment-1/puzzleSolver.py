import hashlib
import time

def solve_crypto_puzzle(data, difficulty):
    # 1. Define the 'Target' (e.g., "0000")
    target = "0" * difficulty
    nonce = 0
    
    print(f"--- PUZZLE START ---")
    print(f"Data: {data}")
    print(f"Difficulty: {difficulty} (Target prefix: '{target}')")
    
    start_time = time.time()

    while True:
        # 2. Combine data + nonce
        input_str = data + str(nonce)
        
        # 3. Generate SHA-256 hash
        result_hash = hashlib.sha256(input_str.encode()).hexdigest()
        
        # 4. Check if the hash 'solves' the puzzle
        if result_hash.startswith(target):
            end_time = time.time()
            
            # --- Results ---
            print(f"\nPUZZLE SOLVED!")
            print(f"Nonce: {nonce}")
            print(f"Hash:  {result_hash}")
            print(f"Time:  {end_time - start_time:.4f} seconds")
            return nonce, result_hash
        
        # 5. Increment nonce to try a new 'ticket'
        nonce += 1

# --- Perform the Experiment ---
user_data = "Transaction: Alice pays Bob 5 BTC"
level = int(input("Enter Puzzle Difficulty (Try 4 or 5): "))

solve_crypto_puzzle(user_data, level)