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
for link in sector_links_a:
    print(link.get("title") +":" +  link.get("href"))
    # sector_request = s.get(link.get("href"))
    # sector_soup = BeautifulSoup(sector_request.text, "html.parser")
    # div_grid_content = sector_soup.select_one("div.grid-content")
    # grid_content_links = div_grid_content.find_all("a")
    # for link in grid_content_links:
    #     print(link.get("href"))
    #     counter+=1

print(counter)
print(s.cookies)
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://igod.gov.in/sector/GRNsIHQBsvhI6u6Q3tju/organizations",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "text/html, */*; q=0.01",
}

test_req = s.get("https://igod.gov.in/sector/GRNsIHQBsvhI6u6Q3tju/organizations_list_more/0/5", headers=HEADERS)
test_soup = BeautifulSoup(test_req.text, "html.parser")
print(test_soup.prettify())


