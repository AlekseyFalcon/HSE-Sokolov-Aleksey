import json
import os
import csv
import codecs
import re
import pickle

# Найдите информацию об организациях:
# Получите список ИНН из файла «traders.txt»;
# Найдите информацию об организациях с этими ИНН в файле «traders.json»;
# Сохраните информацию об ИНН, ОГРН и адресе организаций из файла «traders.txt» в файл «traders.csv».





def writeCsv(path):
    f = open('traders.txt', 'r', newline='')
    trInn = (f.readlines())


    l = open('traders.json', 'r')
    data = json.load(l)

    c = 0


    os.remove(path)
    header = ['ИНН', 'ОГРН', 'Адрес']

    with open(path, 'a', encoding='UTF-32', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()

    while (c <= len(trInn) - 1):
        for i in data:

            if int(i['inn']) == int(trInn[c]):
                csvF = []
                csvF.append(i['inn'])
                csvF.append(i['ogrn'])
                csvF.append(i['address'])
                with open(path, 'a', encoding="UTF-32", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(csvF)
                    file.close()


        c += 1



    with open(path, 'r') as file:
        csvreader = csv.reader(codecs.open(path, 'rU', 'utf-32'))
        for row in csvreader:
            print(row)



#writeCsv('D:/Studying/Uni/traders.csv')






#2Напишите регулярное выражение для поиска email-адресов в тексте.
def findEmail(text):
    email_pattern = r'\S+@\S+\.\S+[^\W]'
    emails = re.findall(email_pattern, text)
    return set(emails)



def findAllEmail(path):
    l = open(path, 'r')
    data = json.load(l)

    emailsSet = {}

    for i in data:
        em = findEmail(i["msg_text"])
        emailsSet[i["publisher_inn"]] = em
    print(emailsSet)



findAllEmail('efrsb_messages.json')


