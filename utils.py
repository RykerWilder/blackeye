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

def get_ip_info(ip):
    ip_data = {}
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        ip_data = {
            "country": response.get("country", "N/A"),
            "country-code": response.get("countryCode", "N/A"),
            "region": response.get("regionName", "N/A"),
            "city": response.get("city", "N/A"),
            "latitude": response.get("lat", "N/A"),
            "longitude": response.get("lon", "N/A"),
            "timezone": response.get("timezone", "N/A"),
            "organization": response.get("org", "N/A"),
            "as": response.get("as", "N/A"),
            "isp": response.get("isp", "N/A")
        }
        return ip_data
    except Exception as e:
        print(f"Error retrieving IP information: {e}")