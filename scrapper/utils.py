from scrapper.models import ScrapperConfig
import requests
from bs4 import BeautifulSoup


def scrape_all_links():
    links_l = list()
    # while True:
    configs = ScrapperConfig.objects.all()
    for config in configs:
        response = requests.get(config.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links_l.append({"name": config.name, "value": soup.find_all("a")})
    return links_l
    # time.sleep(60)