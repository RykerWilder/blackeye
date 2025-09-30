import requests
from colorama import Style, Fore

def print_welcome_message():
    print(f"""
        ██████╗ ██╗      █████╗  ██████╗██╗  ██╗███████╗██╗   ██╗███████╗
        ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝
        ██████╔╝██║     ███████║██║     █████╔╝ █████╗   ╚████╔╝ █████╗  
        ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══╝  
        ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗███████╗   ██║   ███████╗
        ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                         {Fore.BLUE}Coded by: RykerWilder{Style.RESET_ALL}""")

def get_local_ip():
    """Ottiene l'IP locale della macchina per accesso dalla rete locale"""
    try:
        # Connessione a un IP pubblico per determinare l'interfaccia di default
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return "localhost"

def cleanup():
    global server_process
    if server_process:
        try:
            server_process.terminate()
            server_process.wait(timeout=5)
            print(f"{Fore.GREEN}[✓] Server fermato con successo{Style.RESET_ALL}")
        except subprocess.TimeoutExpired:
            server_process.kill()
            print(f"{Fore.YELLOW}[!] Server terminato forzatamente{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Errore durante la pulizia: {e}{Style.RESET_ALL}")
        server_process = None