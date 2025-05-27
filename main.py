from utils import print_logo

print_logo()

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        return {
            "country": response.get("country", "N/A"),
            "city": response.get("city", "N/A"),
            "isp": response.get("isp", "N/A")
        }
    except:
        return {"country": "N/A", "city": "N/A", "isp": "N/A"}