import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# Display Banner
def display_banner():
    print("**************************************")
    print("*    Udemy Link Extractor            *")
    print("*    Extract Udemy Coupons Easily    *")
    print("*                                    *")
    print("*    Join Telegram:                  *")
    print("*    https://t.me/Udemydeath         *")
    print("*    https://t.me/English_chating0   *")
    print("*                                    *")
    print("*    WhatsApp:                       *")
    print("*    https://whatsapp.com/channel/0029VaCBM8AKGGG9l6g6Lz0b *")
    print("**************************************\n")

# Extract Udemy links from a webpage
def extract_udemy_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []

        # Find all <a> tags
        for a_tag in soup.find_all('a', href=True):
            if "udemy.com" in a_tag['href']:
                full_url = urljoin(url, a_tag['href'])
                links.append(full_url)

        return list(set(links))  # Return unique links
    except Exception as e:
        print(f"[ERROR] Failed to scrape {url}: {e}")
        return []

# Recursive scraper
def scrape_links(base_url, max_depth, current_depth=0, visited=None):
    if visited is None:
        visited = set()

    if current_depth > max_depth:
        return []

    print(f"[INFO] Scraping at depth {current_depth}...")

    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"[ERROR] Failed to fetch {base_url}: {e}")
        return []

    visited.add(base_url)
    udemy_links = extract_udemy_links(base_url)

    # Find all internal links to scrape further
    for a_tag in soup.find_all('a', href=True):
        next_url = urljoin(base_url, a_tag['href'])
        if next_url not in visited and base_url in next_url:
            visited.add(next_url)
            udemy_links.extend(scrape_links(next_url, max_depth, current_depth + 1, visited))
            time.sleep(1)  # Delay to avoid being rate-limited

    return list(set(udemy_links))  # Return unique links

def main():
    display_banner()

    # Input URL and depth
    base_url = input("Enter the website URL (e.g., https://coursevania.com): ").strip()
    max_depth = int(input("Enter the maximum scraping depth (1-6): ").strip())

    print(f"\n[INFO] Scraping {base_url} for Udemy links up to depth {max_depth}...\n")

    udemy_links = scrape_links(base_url, max_depth)

    print("\n==================================================")
    print("[RESULTS] Scraping Completed!")
    print(f"[STATS] Total Udemy Links Found: {len(udemy_links)}")
    print("==================================================\n")

    for idx, link in enumerate(udemy_links, start=1):
        print(f"{idx:02d}. {link}")

if __name__ == "__main__":
    main()
