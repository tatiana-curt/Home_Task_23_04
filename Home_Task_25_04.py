
from pprint import pprint

def get_data_from_json():
    import json
    with open('newsafr.json', encoding="utf-8") as new:
        move = json.load(new)
        items_list = move['rss']['channel']['items']
        word_list_json =[]
        for item in items_list:
            # print(item['description'].split( ))# отладочный принт
            for word in item['description'].split( ):
                if len(word) > 6:
                    word_list_json.append(word)
    work_with_word_list(word_list=word_list_json)

def work_with_word_list(word_list):
    sort_word_list = sorted(word_list) # отсортировали список слов из файла
    # pprint(sort_word_list) # отладочный принт

    word_dict = {} # словарь для повторяющихся слов Формат - {слово: кол-во раз}
    counter = 1
    for i in range(0, len(sort_word_list) - 1):
        if sort_word_list[i] == sort_word_list[i + 1]:
            counter += 1
            word_dict[sort_word_list[i]] = counter
        else:
            counter = 1
    # print(word_dict) # отладочный принт

    # для сортировки словоря по значению создаем кортеж из пары (ключ, значение) и сортируем кортежи по второму значению с применением reverse
    word_list_new = list(word_dict.items())
    # print(word_list_new) # отладочный принт
    word_list_new.sort(key=lambda i: i[1],  reverse=True)
    # print(word_list_new) # отладочный принт

    # вывод значений на экран
    counter = 1
    for i in word_list_new:
        if counter <= 10:
            print('Слово "{}" - {} раз'.format(i[0],i[1] ))
            counter += 1
# get_data_from_json()


# Задача 2____________________________________________________________________________________________
def get_data_from_xml():
    import xml.etree.ElementTree as ET
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    xml_description = root.findall("channel/item/description")
    # print(len(xml_description))# отладочный принт
    word_list_xml = []
    for description in xml_description:
        for word in description.text.split( ):
            if len(word) > 6:
                word_list_xml.append(word)
    work_with_word_list(word_list=word_list_xml)
# get_data_from_xml()


def main():
    while True:
        user_input = input('Введите команду (j or x): ')
        if user_input == 'j':
            get_data_from_json()
        elif user_input == 'x':
            get_data_from_xml()

main()

