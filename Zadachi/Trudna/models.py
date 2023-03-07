import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="libraries_and_books"
)
mycursor = mydb.cursor()

class Library:
    def __init__(self, pk):
        '''
        Initialising Library class
        :param pk: Library id
        :param args: Library name , Library address
        '''
        self.pk = pk

    @staticmethod
    def show_libraries():
        sql = "SELECT * FROM libraries"
        mycursor.execute(sql)
        libraries = mycursor.fetchall()
        for library in libraries:
            print(f"{library[0]}) {library[1]}, Address: \"{library[2]}\"")

    def show_books(self):
        '''
        Method to show all books in Library
        :param pk: int
        :return: str
        '''
        sql = "SELECT * FROM books WHERE library_id = %s"
        mycursor.execute(sql, [self.pk])
        books = mycursor.fetchall()
        if books:
            for book in books:
                print(f"Cat.No: -> ({book[0]}) - {book[1]}")


class Book:
    def __init__(self, pk, title, author, genre, publisher, library_id):
        self.pk = pk
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.library_id = library_id

    @staticmethod
    def get_book(pk):
        sql = "SELECT * FROM books WHERE id = %s"
        mycursor.execute(sql, [pk])
        book_instance = mycursor.fetchone()
        if book_instance:
            return Book(*book_instance)

    def add_book(self):
        '''
        Method to add new book in library
        :return:
        '''
        sql = "INSERT INTO books(id, title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.pk, self.title, self.author, self.genre, self.publisher, self.library_id)
        mycursor.execute(sql, val)
        mydb.commit()

    @staticmethod
    def edit_book(pk):
       user_input_edit_option = input(
                "1) for title, 2) for author, 3) for genre, 4) for publisher, 5) for library ID\n"
                ">> ")
       if user_input_edit_option == "1":
          new_title = input("Enter new Title: ")
          sql = "UPDATE books SET title = %s WHERE id = %s"
          val = (new_title, pk)
          mycursor.execute(sql, val)
          mydb.commit()
       if user_input_edit_option == "2":
          new_author = input("Enter new Author: ")
          sql = "UPDATE books SET author = %s WHERE id = %s"
          val = (new_author, pk)
          mycursor.execute(sql, val)
          mydb.commit()
       if user_input_edit_option == "3":
          new_genre = input("Enter new Genre: ")
          sql = "UPDATE books SET genre = %s WHERE id = %s"
          val = (new_genre, pk)
          mycursor.execute(sql, val)
          mydb.commit()
       if user_input_edit_option == "4":
          new_publisher = input("Enter new Publisher: ")
          sql = "UPDATE books SET publisher = %s WHERE id = %s"
          val = (new_publisher, pk)
          mycursor.execute(sql, val)
          mydb.commit()
       if user_input_edit_option == "5":
          new_library_id = input("Enter new Library id: ")
          sql = "UPDATE books SET library_id = %s WHERE id = %s"
          val = (new_library_id, pk)
          mycursor.execute(sql, val)
          mydb.commit()
       else:
           return "Book not edited!"


    @staticmethod
    def delete_book(pk):
        sql = "DELETE FROM books WHERE id = %s"
        mycursor.execute(sql, [pk])
        mydb.commit()

    @staticmethod
    def book_details(pk):
        sql = "SELECT * FROM books WHERE id = %s"
        mycursor.execute(sql, [pk])
        book = mycursor.fetchone()
        if book:
            print(f"Title: {book[1]}\nAuthor: {book[2]}\nGenre: {book[3]}\nPublisher: {book[4]}\nCatalogue № :"
                  f" ({book[0]}) in Library ID {book[5]}")
# print(book)")
            # return [f"Title: {book[1]}",f"Author: {book[2]}",f"Genre: {book[3]}",f"Publisher: {book[4]}",f"Cat. № : ({book[0]})"]

    @staticmethod
    def get_elements_from_table(pk, table, field):
        sql = f"SELECT * FROM {table} WHERE {field} = %s"
        mycursor.execute(sql, [pk])
        book_instance = mycursor.fetchall()
        return book_instance


    @staticmethod
    def show_last_catalogue_number():
        sql = "SELECT MAX(id) FROM books;"
        mycursor.execute(sql)
        last_number = mycursor.fetchone()
        # print(f"The last Catalogue number is: {str(last_number).replace(',', '')}",
        #       f"use ({int(str(last_number).replace(',', '').replace('(','').replace(')', '')) + 1})!")
        next_number = int(str(last_number).replace(',', '').replace('(','').replace(')', '')) + 1
        return next_number





# a = Book(25, "impulse - Why we do what we do without knowing why we do it", "Dr. David Lewis", "Neuroscience", "rh Books", 2)
#
# a.add_book()
#
# for i in Book.book_details(23):
#    print(i)

# #
# a = Library(1)
# a.show_libraries()
# print(type(a.show_libraries()))
# #
# print(Book.show_last_catalogue_number())

#
# c = Book(24, "Fundamentals of Wavelets", "Goswami, Jaideva", "signal_processing", "Wiley", 1 )
# c.edit_book()
#
# Book.delete_book(25)



