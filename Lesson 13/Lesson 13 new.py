import requests
from bs4 import BeautifulSoup
import os
import csv


class ParserCBRF:
    def __init__(self):
        self.url = 'https://www.cbr.ru/hd_base/KeyRate/'
        self.key_rate_data = {}

    def start(self):
        self._fetch_data()
        self._parse_data()
        self._save_data()

    def _fetch_data(self):
        response = requests.get(self.url)

        if response.status_code != 200:
            raise Exception(f"Не удалось получить страницу, код состояния: {response.status_code}")

        self.page_content = response.content

    def _parse_data(self):
        soup = BeautifulSoup(self.page_content, 'html.parser')
        table = soup.find('table', {'class': 'data'})

        if not table:
            raise Exception("Не удалось найти таблицу данных в содержимом страницы")

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            date = columns[0].get_text(strip=True)
            rate = columns[1].get_text(strip=True)
            self.key_rate_data[date] = rate

    def _save_data(self):
        file_path = os.path.join(os.getcwd(), 'key_rate_data.csv')

        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Дата', 'Ставка'])

            for date, rate in self.key_rate_data.items():
                writer.writerow([date, rate])


if __name__ == '__main__':
    parser = ParserCBRF()
    parser.start()
    print("Данные получены и сохранены в key_rate_data.csv")
