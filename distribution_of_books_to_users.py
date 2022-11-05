import csv
import json

'''Чтение файла books.csv, сохранение книг с нужными атрибутами в переменную'''
with open('books.csv', encoding='utf-8') as books_file:
    file_reader = csv.DictReader(books_file, delimiter=',')
    book_list = []
    for row in file_reader:
        book = {'title': row['Title'], 'author': row['Author'], 'pages': row['Pages'], 'genre': row['Genre']}
        book_list.append(book)

'''Чтение файла users.json, сохранение данных в переменную'''
with open('users.json', 'r') as users_file:
    user_list = json.load(users_file)

'''Подсчет равного количества книг на каждого пользователя, подсчет количества лишних книг'''
users_count = len(user_list)
books_count = len(book_list)
books_to_user_count = books_count // users_count
surplus_books_left_count = books_count % users_count

'''Распределение книг по пользователям максимально поровну. Сохранение данных с нужными атрибутами в переменную'''
output_list = []
for user in user_list:
    books_to_user = []
    # Каждому пользователю достается одинаковое количество книг
    for i in range(books_to_user_count):
        book_to_user = book_list.pop(0)
        books_to_user.append(book_to_user)
    # Пока есть лишние книги - пользователю текущей итерации достается бонусная книга
    if surplus_books_left_count > 0:
        book_to_user = book_list.pop(0)
        books_to_user.append(book_to_user)
        surplus_books_left_count -= 1
    # Данные и книги каждого пользователя сохраняются в виде json и добавляются в список
    json_user_with_book = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": books_to_user
    }
    output_list.append(json_user_with_book)

'''Запись итогового списка в json фойл'''
with open('result.json', 'w') as output_file:
    json.dump(output_list, output_file, indent=4)
