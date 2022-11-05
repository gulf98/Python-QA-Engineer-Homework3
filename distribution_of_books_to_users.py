import csv
import json

'''Reading books.csv, saving books with desired attributes to a variable'''
with open('books.csv') as books_file:
    file_reader = csv.DictReader(books_file)
    book_list = []
    for row in file_reader:
        book = {'title': row['Title'], 'author': row['Author'], 'pages': row['Pages'], 'genre': row['Genre']}
        book_list.append(book)

'''Reading users.json, saving data to a variable'''
with open('users.json', 'r') as users_file:
    user_list = json.load(users_file)

'''Counting an equal number of books per user, counting the number of bonus books'''
users_count = len(user_list)
books_count = len(book_list)
books_to_user_count = books_count // users_count
surplus_books_left_count = books_count % users_count

'''The distribution of books among users is as even as possible. Saving data with desired attributes to a variable'''
output_list = []
for user in user_list:
    books_to_user = []
    # Each user gets the same number of books
    for i in range(books_to_user_count):
        book_to_user = book_list.pop(0)
        books_to_user.append(book_to_user)
    # As long as there are bonus books, the user of the current iteration gets a bonus book
    if surplus_books_left_count > 0:
        book_to_user = book_list.pop(0)
        books_to_user.append(book_to_user)
        surplus_books_left_count -= 1
    # Each user's data and books are saved as json and added to the list
    json_user_with_books = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": books_to_user
    }
    output_list.append(json_user_with_books)

'''Writing the final list to a json file'''
with open('result.json', 'w') as output_file:
    json.dump(output_list, output_file, indent=4)
