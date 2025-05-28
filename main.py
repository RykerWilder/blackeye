from utils import print_welcome_message, get_ip_info

def main():
    print_welcome_message()

    while True:
        get_ip_info("ip_address")

if __name__ == "__main__":
    main()