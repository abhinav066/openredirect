
import requests
from multiprocessing import Pool
from tqdm import tqdm

def get_wayback_urls(domain):
    # Use requests to fetch the Wayback Machine URL
    wayback_url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&fl=original&collapse=urlkey&limit=100000"
    response = requests.get(wayback_url)
    if response.status_code == 200:
        # Parse the JSON response and extract URLs
        json_data = response.json()
        urls = [url[0] for url in json_data[1:]]
        return urls
    else:
        print("Error fetching  URLs")
        return []

def check_vulnerability(url):
    try:
        # Send a HEAD request to the URL and check if 'evil.com' is in response headers
        response = requests.head(url, allow_redirects=True)
        if 'evil.com' in response.headers.get('location', ''):
            return True
    except Exception as e:
        pass
    return False

def check_url(url):
    if 'http' in url.lower() and check_vulnerability(url):
        return url

def print_ascii_art():
    # ASCII art to display before asking for domain
    ascii_art = r"""
                            _______                    ________     __________________ 
__  __ \______________________  __ \__________  /__(_)___________________  /_
_  / / /__  __ \  _ \_  __ \_  /_/ /  _ \  __  /__  /__  ___/  _ \  ___/  __/
/ /_/ /__  /_/ /  __/  / / /  _, _//  __/ /_/ / _  / _  /   /  __/ /__ / /_  
\____/ _  .___/\___//_/ /_//_/ |_| \___/\__,_/  /_/  /_/    \___/\___/ \__/  
       /_/@abhinav066
"""
    print(ascii_art)

def main():
    print_ascii_art()  # Print ASCII art
    domain = input("Enter a url: ")
    urls = get_wayback_urls(domain)
    if urls:
        with Pool() as pool:
            vulnerable_urls = list(tqdm(pool.imap(check_url, urls), total=len(urls), desc="Checking URLs", unit="URL"))
            vulnerable_urls = [url for url in vulnerable_urls if url]
            if vulnerable_urls:
                for url in vulnerable_urls:
                    print(f"{url} \033[0;31mVulnerable\n")
            else:
                print("No vulnerable URLs found.")
    else:
        print("No URLs found for the domain.")

if __name__ == "__main__":
    main()