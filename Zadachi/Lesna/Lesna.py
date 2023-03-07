# Лесна:
#
# Напишете програма която да пази информация за библиотеки и техните книги.
# Библиотеката трябва да има номер, име, адрес, и книги. Всяка книга трябва да има номер,
# автор, заглавие, жанр, и издател. Програмата трябва да попита потребителя коя
# библиотека иска да провери (Като му изкара съобщение със всички бибилиотеки и
# техните номера) и да му изкара информация за книгите в нея показвайки само заглавията
# и съответния номер. След което да го попита дали иска са подробна информация за
# някоя книга и ако избере нейния номер за да се покаже подробната информация. В
# противен случай програмата да приключи.
# Данните за книгите и библиотеките да се съхраняват в кода в типове по ваш избор.

libraries = {1: ["Casper-Waters","8 Vermont Avenue"],
             2: ["Lehner Williamson and Weimann","9515 Scofield Terrace"],
             3: ["Murray Group","00467 Londonderry Avenue"],
             4: ["McKenzie, Green and Ryan","32343 Dixon Alley"],
             5: ["Waelchi-Casper","3 Drewry Center"]

             }

books = [   [1, "Fundamentals of Wavelets", "Goswami, Jaideva", "signal_processing", "Wiley", 1],
            [2, "Data Smart", "Foreman, John","data_science","Wiley",2],
            [3, "God Created the Integers", "Hawking, Stephen","mathematics","Penguin",4],
            [4, "Superfreakonomics", "Dubner, Stephen","economics","HarperCollins",5],
            [5, "Orientalism","Said, Edward", "history", "Penguin", 2],
            [6, "Nature of Statistical Learning Theory", "The, Vapnik, Vladimir", "data_science", "Springer", 3],
            [7, "Integration of the Indian States", "Menon, V P", "history", "Orient Blackswan", 2],
            [8, "Drunkard's Walk, The", "Mlodinow, Leonard", "science", "Penguin", 5],
            [9, "Image Processing & Mathematical Morphology", "Shih, Frank", "signal_processing", "CRC", 3],
            [10, "How to Think Like Sherlock Holmes","Konnikova, Maria", "psychology", "Penguin", 2],
            [11, "Data Scientists at Work", "Sebastian Gutierrez", "data_science", "Apress", 5],
            [12, "Slaughterhouse Five", "Vonnegut, Kurt", "fiction", "Random House", 2],
            [13, "Birth of a Theorem", "Villani, Cedric", "mathematics", "Bodley Head", 1],
            [14, "Structure & Interpretation of Computer Programs", "Sussman, Gerald", "computer_science", "MIT Press", 2],
            [15, "Age of Wrath, The", "Eraly, Abraham", "history", "Penguin", 3],
            [16, "Trial, The","Kafka, Frank","fiction","Random House", 4],
            [17, "Statistical Decision Theory", "Pratt, John", "data_science", "MIT Press", 5],
            [18, "Data Mining Handbook","Nisbet, Robert","data_science", "Apress", 2],
            [19, "New Machiavelli, The", "Wells, H. G.", "fiction", "Penguin", 1],
            [20, "Physics & Philosophy", "Heisenberg, Werner", "science", "Penguin", 2],
            [21, "Making Software", "Oram, Andy", "computer_science", "O'Reilly", 3],
            [22, "Analysis, Vol I", "Tao, Terence", "mathematics", "HBA", 4]
        ]


def get_libraries():
    try:
        all_libs = list(libraries.items())
        return list(all_libs)
    except ValueError:
        print("Library not found!")



def get_catalog(library_id):
    books_in_library = [x for x in books[::][::-1] if int(library_id) in x]
    return books_in_library



def get_book_details(book_id):
    if book_id == "exit":
        print("Exiting now...")
        exit()
    if book_id.isdigit():
        book = [y for y in books[:][0:] if int(book_id) == y[0]]
        return book

print("="*25,"Libraries",25*"=")

for library in get_libraries():
    print(f"No:-> {library[0]}) {library[1][0]} Address: {library[1][1]}")

while True:
    try:
        library_id = input("\nPlease enter Library number: ")
        for book in get_catalog(library_id):
            print(f"Book Cat.No:-> {book[0]}) Title: {book[1]}")
    except ValueError:
        print("Lirary not found!")
        continue
    try:
        book_id = input("\nPlease enter Book Cat.No or exit: ")
        book_details = list(get_book_details(book_id))
        for detail in book_details:
            print(f"Title: {detail[1]}\nAuthor: {detail[2]}\nGenre: {detail[3]}\nPublisher: {detail[4]}\n"
                  f"In Library ID: {detail[5]}\n")
    except ValueError:
        print("Book not found!")

















