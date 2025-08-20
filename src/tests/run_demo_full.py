import os
import json
from datetime import datetime
import random
import uuid

# Folder logs
REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_PATH = os.path.join(REPO_PATH, "logs")

if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH)

# Fungsi generate demo transaksi
def generate_demo_transactions(num=5):
    transactions = []
    for _ in range(num):
        txn = {
            "transaction_id": str(uuid.uuid4()),
            "account_number": f"1000{random.randint(100000,999999)}",
            "amount": random.randint(10000, 500000),
            "channel": random.choice(["qris", "virtual_account", "ewallet"]),
            "status": random.choice(["success", "failed", "expired"]),
            "timestamp": datetime.now().isoformat()
        }
        transactions.append(txn)

        # Print ringkas di terminal
        print(f"Generated txn: {txn['transaction_id']} | {txn['channel']} | {txn['amount']}")

    # Simpan ke file JSON
    log_file = os.path.join(LOGS_PATH, f"demo_txn_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(log_file, "w") as f:
        json.dump(transactions, f, indent=2)

    print(f"\nAll transactions saved to {log_file}\n")
    return transactions

# Main
if __name__ == "__main__":
    print("Running demo transactions...")
    generate_demo_transactions(num=5)
