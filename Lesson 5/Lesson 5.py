import json
import csv
import re


def task_1():
    # Читаем все строки из файла "traders.txt" и создаем список
    with open("traders.txt", "r") as f:
        inns = f.read().splitlines()

    # Открываем файл "traders.json" и загружаем его содержимое в переменную all_traders
    with open("traders.json", "r") as f:
        all_traders = json.load(f)

    # Создаем список traders, содержащий только те элементы из all_traders, которые имеют inn из списка inns
    traders = [trader for trader in all_traders if trader['inn'] in inns]

    # Записываем данные из списка traders в файл "traders.csv"
    with open('traders.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for trader in traders:
            writer.writerow([trader['inn'], trader['ogrn'], trader['address']])

def task_2():
    # Открываем файл "1000_efrsb_messages.json" и загружаем его содержимое в переменную msgs
    with open("1000_efrsb_messages.json", "r") as f:
        msgs = json.load(f)

    # Создаем регулярное выражение для поиска email
    email_pattern = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')

    # Создаем словарь, где ключи - email, а значения - список уникальных ИНН организаций, которые связаны с данным email.Все email приведены в нижний регистр.
    result = {}
    for msg in msgs:
        emails = set(re.findall(email_pattern, msg['msg_text'].lower()))
        for email in emails:
            inn = msg['publisher_inn']
            result.setdefault(email, []).append(inn)

    # Записываем результаты в файл "emails.json"
    with open('emails.json', "w") as f:
        json.dump(result, f)


# Вызываем функции
task_1()
task_2()