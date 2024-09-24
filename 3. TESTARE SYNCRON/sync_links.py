from bs4 import BeautifulSoup
import requests




def get_links():
    sitemap_url = "https://www.mosionroata.ro/sitemap.xml"

    response = requests.get(sitemap_url)

    soup = BeautifulSoup(response.content, "xml")
    locations = soup.find_all("loc")

    xml_locations = [l.text for l in locations]

    print(xml_locations)
    all_xml_links = []

    for xml in xml_locations:
        xml_response = requests.get(xml)
        xml_soup = BeautifulSoup(xml_response.content, "xml")
        xml_links = xml_soup.find_all("loc")
        inner_xml_locations = [l.text for l in xml_links]
        all_xml_links.extend(inner_xml_locations)

    return all_xml_links

if __name__ == "__main__":
    all_links = get_links()
    print("Am gasit", len(all_links), "link-uri.")
    with open("sync_links_cdn.txt", "w") as fwriter:
        n = 1
        for l in all_links:
            if "gomagcdn" in l:
                fwriter.write(f"{n}{l}\n")
                n += 1

    with open("sync_links.txt", "w", encoding='utf-8') as fwriter:
        n = 1
        for l in all_links:
            if "gomagcdn" not in l:
                fwriter.write(f"{l}\n")
                n += 1