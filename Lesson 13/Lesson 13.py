import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.parse import urljoin


class ParserCBRF:
    def __init__(self, base_url, target_dir):
        self._base_url = base_url
        self._target_dir = target_dir
        self._data = {}

    def start(self):
        page_content = self._get_page_content(self._base_url)
        links = self._extract_links(page_content)
        for link in links:
            self._download_file(link)

    def _get_page_content(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content

    def _extract_links(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        links = [urljoin(self._base_url, a['href']) for a in soup.find_all('a', href=True) if
                 a['href'].endswith(('.xls', '.xlsx', '.pdf', '.csv'))]
        return links

    def _download_file(self, url):
        file_name = os.path.join(self._target_dir, url.split('/')[-1])
        urllib.request.urlretrieve(url, file_name)


parser = ParserCBRF('https://www.cbr.ru/analytics/?CF.Search=&CF.TagId=&CF.Date.Time=LastMonth&CF.Date.DateFrom=&CF.Date.DateTo=', 'C:/1')
parser.start()
