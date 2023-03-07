# Средна:
#
# Напишете скрипт който да чете csv файлове и да ги импортна във база данни като
# направи правилно връзката между тях. В books.csv се съхраняват книги които трябва да
# се прочетат и импортнат в MySQL база данни за която трябва да си създадете структурата
# в скрипта преди да бъдат импортнати. В файла libraries.csv има библиотеки които трябва
# да имат връзка с книги. Обърнете вниманите, че едната таблица зависи от другата и
# трбява да има връзка с нея.



import csv
import mysql.connector

def load_data_from_csv(file_path):

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return list(reader)


connector = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=3306,
)

cursor = connector.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS libraries_and_books')
cursor.execute('USE libraries_and_books')
cursor.execute('''
CREATE TABLE IF NOT EXISTS libraries(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    location VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(50) NOT NULL,
    genre VARCHAR(50),
    publisher VARCHAR(50),
    library_id INT NOT NULL,
    PRIMARY KEY (id)
);

''')

cursor.execute('''
ALTER TABLE books
ADD FOREIGN KEY (library_id) REFERENCES libraries(id)
;
''')


libraries = load_data_from_csv('libraries.csv')
sql = "INSERT INTO libraries (id, name, location) VALUES (%s, %s, %s)"
cursor.executemany(sql, libraries)
connector.commit()

books = load_data_from_csv('books.csv')
sql = "INSERT INTO books (id, title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(sql, books)
connector.commit()

