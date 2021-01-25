from pprint import pprint
import csv
import re


with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)

# pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ

tel_pattern = re.compile('(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})[-\s]?\(?(доб\.)?\s*(\d{4})?\)?')
name_pattern = re.compile('^(\w+)[,\s]?(\w+)[\s]?(\w+)?')

full_names_list = list()

for contact in contacts_list[1:]:
    tel = contact[5]
    tel_res = tel_pattern.sub(r'+7(\2)\3-\4-\5 \6\7', tel)
    contact[5] = tel_res
    name = ','.join(contact[0:2])
    name_res = name_pattern.sub(r'\1,\2,\3', name)
    full_name = name_res.split(',')
    del(full_name[3:])
    contact[0:2] = full_name
    del(contact[3])


result = list()
result.append(contacts_list[0])

for contact_1 in contacts_list[1:]:
    for i1, contact_2 in enumerate(contacts_list[1:]):
        if contact_1[0] == contact_2[0]:
            for i2, element in enumerate(contact_2):
                if element not in contact_1:
                    contact_1[i2] = element
    if contact_1 not in result:
        result.append(contact_1)

pprint(result)


# TODO 2: сохраните получившиеся данные в другой файл

with open('phonebook.csv', 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
