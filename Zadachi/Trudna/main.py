# Трудна:
# Използвайки данните които си добавихте от предната задача преобразувайте първата
# като този път използвайте данните от базата. Отново програмата да пита потребителя за
# библиотека, като възможните избори да бъдат показани от базата, след което да има
# възможност да покаже наличните книги, да добави книга и да изтрие книга. За да е
# по-лесно на потребителя номерирайте възможните имена на библиотеки и очаквайте от
# конзолата input като (1,2,3,4,5) ако потребителят въведе 0 трябва програмата да
# приключи. След като потребителя избере библиотека да се покаже текст с възможните
# команди (Покажи книги, добави книга, изтрий книга) при първата опция да се покажат
# всички книги. При втората опция трбва да се пкажат кои са полетата които потребителя
# трябва да попълни и той да ги въведе на един ред разделени със запетая. Да има
# помощен текст в какъв формат трябва да се въведът). При третата опция да се покажат
# всички книги номерирани и да се очаква input от потребителя коя книга да изтрие.
# Когато се покажат всички книги при първата оция трябва да можем да изберем някоя от
# книгите въвеждайки съответния и номер. Когато я изберем трябва да има опция за
# редактиране и да можем да редактираме някое от нейните полета.
# В задачата е дадено примерна последователност на фукционалсттта на програмата.
# Имате свободата да направите интерфейса и по ваше усмотрение стига да е приятен за
# използване от потребителя. Важно е да има фукционалсотите да могат да се виждат
# книгите от дадена библиотека, да се добавят нови, да се изтриват или да променяме
# данните в тях.
# Помощ: За да номерирате книгите може да използвате техните ID-та, и да очаквате от
# потребителя да въведе ID на книгата.
# За въпроси относно условието на задачите можете да ме питате на лично съобщение в
# дискорд -> Galin#2073

from models import Library, Book
import time

while True:
    print("="*27, "List of Libraries","="*27)
    Library.show_libraries()
    print("="*20, "Select library number from list", "="*20,)
    selected_library = input("(0 to exit program)>> ")
    if selected_library == "0":
        print("Exit successfull!")
        break
    if selected_library not in "1,2,3,4,5":
        print("Library not found!")
        continue
    if selected_library:
        # library = Library(selected_library)
        books_in_library = Book.get_elements_from_table(selected_library, "books", "library_id")
        print("=" * 23, f"List of books in Library:", "=" * 23)
        # library.show_books()
        [print(f"Cat.No -> {book[0]} - {book[1]}, {book[2]}", end='\n') for book in books_in_library]
        print("="*19, "Select option from the menu below", "="*19)
    while True:
        book_option = input(
            ">> Cat.No -> for details\n"
            ">> NEW for new book\n"
            ">> DEL to delete book\n"
            ">> EDIT to edit book\n"
            "(0 exit to Libraries)>> ")
        if book_option == "0":
            print("Now exiting to main menu...")
            time.sleep(1)
            break
        if book_option.isdigit():
            print("=" * 30, "Book details", "=" * 30)
            if Book:
                Book.book_details(int(book_option))
            else:
                print("Book not found!")
            print("=" * 28, "END book details", "=" * 28)
            time.sleep(2)
        elif book_option == "NEW":
            try:
                print(f"Current Library ID -> {selected_library}")
                new_book = input("Enter book details separated by comma: Title, Author, Genre, Publisher, Library ID\n"
                                 "(0 to exit)>> ")
                if new_book:
                    new_book_details = new_book.split(',')
                    new_book_to_add = Book(Book.show_last_catalogue_number(), new_book_details[0], new_book_details[1],
                                           new_book_details[2], new_book_details[3],new_book_details[4])
                    new_book_to_add.add_book()
                    print(f"Adding book \"{new_book_details[0]}\" to library - {new_book_details[3]}!")
                    time.sleep(2)
                    print("Book added succefully!")
                    time.sleep(1)
            except IndexError:
                print("Error adding new book! Try again!")
                continue
        elif book_option == "DEL":
            books_in_library = Book.get_elements_from_table(selected_library, "books", "library_id")
            [print(f"Cat.No -> {book[0]} - {book[1]}", end='\n') for book in books_in_library]
            book_to_delete = input("Enter book Cat.No to DELETE: ")
            if book_to_delete.isdigit():
                confirm = input("ARE YOU SURE? Y/N\n"
                                ">> ")
                if confirm == "Y":
                    print("Deleting book...")
                    Book.delete_book(int(book_to_delete))
                    time.sleep(2)
                    print("Book deleted!")
                    time.sleep(1)
                elif confirm == "N":
                    print("Book not deleted!")
            else:
                print("Book not deleted")
        elif book_option == "EDIT":
            try:
                books_in_library = Book.get_elements_from_table(selected_library, "books", "library_id")
                [print(f"Cat.No -> {book[0]} - {book[1]}", end='\n') for book in books_in_library]
                book_to_edit = input("Enter book Cat.No to edit details:\n"
                                     ">> ")
                Book.book_details(int(book_to_edit))
                Book.edit_book(book_to_edit)
                print("="*20,"Book edited successfully!","="*20)
            except ValueError:
                print("Book not edited! Try again!")
                continue
        else:
            print("Error! Try again!")
            continue

        # print("Editing...")
        # time.sleep(2)




