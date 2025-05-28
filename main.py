from utils import print_welcome_message, get_ip_info

def main():
    print_welcome_message()

    while True:

        print(""" 
            [1] Amazon
            [2] Ebay
            [3] Linkedin
            [4] Netflix
        """)

        choice = input("Insert your choice: ")

        if choice == "1":
            print("you choose Amazon")
        elif choice == "2":
            print("you choose Ebay")
        elif choice == "3":
            print("you choose Linkedin")
        elif choice == "4":
            print("you choose Netflix")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()