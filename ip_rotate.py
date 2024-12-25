import requests

JOB_POST = "machine-learning-internship"

proxies = [
    # Enter Proxy IP's
    # IP:PORT:USERNAME:PASSWORD
]


def check_ip_rotation():
    url = f"https://internshala.com/internships_ajax/{JOB_POST}"  
    for proxy in proxies:
        ip, port, username, password = proxy.split(":")
        
        proxy_url = f"http://{username}:{password}@{ip}:{port}"
        
        proxy_dict = {
            "http": proxy_url,
            "https": proxy_url
        }
        
        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                ip_info = response.json()
                return ip_info
                #print("yayy")
                #print(ip_info['internship_list_html'])
                #raw_string = ip_info['internship_list_html']

                #print(f"IP for proxy {ip}:{port} - {ip_info['origin']}")
                
            else:
                print("Ouch")
                print(f"Failed with proxy {proxy_url}, status code: {response.status_code}")
                print("Trying with another proxy")
                continue
        except requests.RequestException as e:
            print(f"Error with proxy {proxy_url}: {e}")
            print("Trying with another proxy")
            continue

        print("Tried All IP Proxies")


