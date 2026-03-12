from utils.register import Registration

def main():
    """Entry Point to Restaurant Reservation Menu"""

    print('==== Restaurant Reservation Menu ====\n')

    while True:
        # --- Prompt User to Select Menu Option ---
        option = int(input("\nSelect Menu Option:\nRegister: (press 1)\nLogin: (press 2)\nExit (press 3)\nSelection: "))

        # --- Validate Option ---
        if option < 1 or option > 3:
            print(f"\n[ERROR]: {option} is invalid, please select a value from 1 - 3\n") # print error message
            continue

        # --- Match Option ---
        match option:
            case 1:
                r = Registration()
                r.start_registration()
            case 2:
                print("Logging in...")
            case 3:
                print("Exiting...")
                return  
            case _:
                pass
    


if __name__ == "__main__":
    main()
