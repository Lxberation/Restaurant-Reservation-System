import os
from utils.config import PROJECT_ROOT

class CancelReservation:

    def __init__(self, email):
        self.email = email
        self.data_path = os.path.join(PROJECT_ROOT, "user_data", "user_reservation.txt")

    def start_cancel(self):
        print("\n===== Cancel Reservation =====\n")

        if not os.path.exists(self.data_path):
            print("No reservation found")
            return

        with open(self.data_path, "r") as f:
            content = f.read().strip()

        if content == "":
            print("No reservation found")
            return

        all_blocks = content.split("----------------------")
        user_blocks = [b for b in all_blocks if f"Email: {self.email}" in b]

        if not user_blocks:
            print("No reservation found")
            return

        for i, block in enumerate(user_blocks, 1):
            print(f"Reservation {i}:")
            print(block.strip())
            print("----------------------")

        while True:
            try:
                choice = int(input(f"\nSelect reservation to cancel (1-{len(user_blocks)}): "))
                if 1 <= choice <= len(user_blocks):
                    break
                print(f"[ERROR]: Please enter a number between 1 and {len(user_blocks)}")
            except ValueError:
                print("[ERROR]: Please enter a valid number.")

        selected = user_blocks[choice - 1]

        confirm = input("\nAre you sure you want to cancel this reservation? (Y to confirm): ").strip().lower()

        if confirm != "y":
            print("\nCancellation aborted.")
            return

        for i, block in enumerate(all_blocks):
            if block == selected:
                all_blocks[i] = ""
                break

        with open(self.data_path, "w") as f:
            for block in all_blocks:
                if block.strip():
                    f.write("----------------------\n")
                    f.write(block.strip() + "\n")

        print("\nReservation cancelled successfully!\n")
