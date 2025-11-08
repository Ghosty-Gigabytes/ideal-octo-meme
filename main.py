import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import os
import json
s = requests.Session()
output_dir = "output_json"
os.makedirs(output_dir, exist_ok=True)
request = s.get("https://igod.gov.in/sectors")
soup = BeautifulSoup(request.text, "html.parser")
div_sector_container = soup.select_one("div.sector-container")
sector_links_a = div_sector_container.find_all("a")
sector_links = []
counter = 0

def extract_sector_id(url: str) -> str:
    """
    Extracts the sector ID from an IGOD sector URL.
    Example:
      https://igod.gov.in/sector/GRNsIHQBsvhI6u6Q3tju/organizations_list_more/270/5
      -> GRNsIHQBsvhI6u6Q3tju
    """
    path = urlparse(url).path.strip("/")  # get only the path part
    parts = path.split("/")               # split into segments
    try:
        idx = parts.index("sector")       # find "sector" in path
        return parts[idx + 1]             # return the piece after it
    except Exception:
        return None

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://igod.gov.in/sector/GRNsIHQBsvhI6u6Q3tju/organizations",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "text/html, */*; q=0.01",
}

for link in sector_links_a:
    print(link.get("title") +":" +  link.get("href"))
    limit_counter = 0
    sector_id = extract_sector_id(link.get("href"))
    while True:
        url = f"https://igod.gov.in/sector/{sector_id}/organizations_list_more/{limit_counter}/5"
        req= s.get(url, headers=HEADERS)
        soup = BeautifulSoup(req.text, "html.parser")
        website_links = soup.find_all("a")
        print(len(website_links))
        for link in website_links:
            print(link.get("href"))
            counter+=1
        limit_counter+=5
        if len(website_links) == 0:
            break

    # div_grid_content = sector_soup.select_one("div.grid-content")
    # grid_content_links = div_grid_content.find_all("a")
    # for link in grid_content_links:
    #     print(link.get("href"))
    #     counter+=1
print(counter)
print(s.cookies)


test_req = s.get("https://igod.gov.in/sector/GRNsIHQBsvhI6u6Q3tju/organizations_list_more/270/5", headers=HEADERS)
# print(test_soup.prettify())


test_soup = BeautifulSoup(test_req.text, "html.parser")