import hashlib

def build_merkle_tree(transactions):
    # 1. Initial Hashed Transactions
    current_level = [hashlib.sha256(t.encode()).hexdigest() for t in transactions]
    print(f"Initial Hashes: {current_level}\n")

    level = 1
    while len(current_level) > 1:
        # If odd, duplicate the last element
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])
        
        new_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i+1]
            new_level.append(hashlib.sha256(combined.encode()).hexdigest())
        
        current_level = new_level
        print(f"Level {level} Hashes: {current_level}")
        level += 1

    return current_level[0]

# Execution
tx = ["Alice -> Bob : $800", "Bob -> Dave : $540", "Dave -> Eve : $100", "Eve -> Alice : $500", "Roo -> Bob : $680"]
root = build_merkle_tree(tx)
print(f"\nMerkle Root: {root}")