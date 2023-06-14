import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

class ParserCBRF:
    def __init__(self):
        self.url = 'https://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01010&UniDbQuery.From=27.05.2023&UniDbQuery.To=03.06.2023'

    def start(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.find('table')

        df = pd.read_html(str(table))[0]
        print(df.head())  # Показать первые несколько строк, чтобы увидеть структуру фрейма данных.

        # Проверка существует ли столбец "дата" и является ли его тип данных строкой
        if 'date' in df.columns and df['date'].dtype == object:
            df['date'] = pd.to_datetime(df['date'], errors='coerce', format='%d.%m.%Y').dt.strftime('%Y-%m-%d')

        # Преобразование данных в словарь
        data_dict = df.to_dict(orient='records')

        # Сериализация данных
        self.serialize(data_dict)

    def serialize(self, data):
        # Убедиться, что каталог «parsed_data» существует
        os.makedirs('parsed_data', exist_ok=True)

        # Сериализировать данные в JSON и сохранить в файл
        with open(os.path.join('parsed_data', 'data.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

parser = ParserCBRF()
parser.start()
