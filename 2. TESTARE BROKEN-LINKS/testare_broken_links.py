from bs4 import BeautifulSoup
import requests




sitemap_urls = [
    'https://www.mosionroata.ro/sitemap.xml',
    'https://www.olx.ro/sitemap.xml',
    'https://www.raijucarii.ro/sitemap.xml',
    'https://tazz.ro/sitemap.xml',
    'https://www.google.ro/sitemap.xml',
]

def fetch_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'xml')
    urls = [loc.text for loc in soup.find_all('loc')]
    return urls

def check_link_for_404(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 404:
            print(f"Status 404 - Link nefunctional: {url}")
            return True
    except requests.RequestException as e:
        print(f"Verificare eroare {url}: {e}")
    return False

def main(sitemap_urls):
    for sitemap_url in sitemap_urls:
        print(f"Se proceseaza:{sitemap_url}")
        urls = fetch_urls_from_sitemap(sitemap_url)
        found_broken = False
        for url in urls:
            if check_link_for_404(url):
                found_broken = True
        if not found_broken:
            print(f"Nu s-a/s-au gasit link/link-uri nefunctional/e in:{sitemap_url}.")
        print("Status: 200")

main(sitemap_urls)