class Book:
    __id = 0
    __name = ''
    __author = []
    __publisher = ''
    __year = 0
    __num_of_pages = 0
    price = 0
    type_of_binding = ''
    __count = 0

    def __init__(self, id, name, author, publisher, year, num_of_pages, price, type_of_binding):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__publisher = publisher
        self.__year = year
        self.__num_of_pages = num_of_pages
        self.__price = price
        self.__type_of_binding = type_of_binding
        Book.__count += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def get_year(self):
        return self.__year

    def get_num_of_pages(self):
        return self.__num_of_pages

    def get_price(self):
        return self.__price

    def get_type_of_binding(self):
        return self.__type_of_binding

    def get_all(self):
        print("Id - "+str(self.__id),
              ", название - ", self.__name,
              ", автор - ", self.__author,
              ", издательство - ", self.__publisher,
              ", год издания - ", self.__year,
              ", количество страниц - ", self.__num_of_pages,
              ", цена - ", self.__price, " рублей",
              ", тип переплета - ", self.__type_of_binding)

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name =  name

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_year(self, year):
        self.__year = year

    def set_num_of_pages(self, num_of_pages):
        self.__num_of_pages = num_of_pages

    def set_price(self, price):
        self.__price = price

    def set_type_of_binding(self, type_of_binding):
        self.__type_of_binding = type_of_binding


books = [
    Book(1, 'Алиса в стране чудес', 'Льюис Кэррол', 'Народная асвета', 2018, 124, 15, 'мягкий переплет'),
    Book(2, 'Винни Пух', 'Алан Милн', 'Аверсэв', 2015, 67, 25, 'твердый переплет'),
    Book(3, 'Золушка', 'Алан Милн', 'Аверсэв', 2019, 114, 9, 'мягкий переплет'),
    Book(4, 'Охота на Снарка', 'Льюис Кэррол', 'Народная асвета', 2014, 78, 8, 'мягкий переплет'),
    Book(5, 'Принц кролик', 'Алан Милн', 'Аверсэв', 2014, 45, 21, 'твердый переплет'),
    Book(6, 'Принцесса Несмеяна', 'Алан Милн', 'Аверсэв', 2015, 89, 13, 'мягкий переплет'),
    Book(7, 'Белоснежка', 'Братья Гримм', 'Народная асвета', 2012, 34, 7, 'твердый переплет'),
    Book(8, 'Бременские музыканты', 'Братья Гримм', 'Народная асвета', 2010, 101, 13, 'мягкий переплет')
]


def books_of_author():
    print("Книги какого автора вы хотите увидеть? ")
    author = {}
    j = 1
    for i in range(len(books)):
        if books[i].get_author() not in author.values():
            author[j] = str(books[i].get_author())
            print(str(j) + " - " + books[i].get_author() + "")
            j += 1
    a = int(input())
    count = 0
    for i in range(len(books)):
        if books[i].get_author() == author.get(a):
            books[i].get_all()
            count += 1
    if count == 0:
        print("Таких книг нет")
    print("\n")


def books_under_year():
    print("Книги, выпущенные после какого года, вы хотите увидеть? ")
    a = int(input())
    count = 0
    for i in range(len(books)):
        if books[i].get_year() > a:
            books[i].get_all()
            count += 1
    if count == 0:
        print("Таких книг нет")
    print("\n")


while True:
    print("-----------------------меню--------------------------------\n" +
          "Что вы хотите сделать:\n" +
          " 1 - Вывести список определенного автора\n"
          " 2 - Вывести список книг, выпущенных после определенного года\n" +
          " 3 - Выход\n" +
          "------------------------------------------------------------")
    a = int(input())
    if a == 1:
        books_of_author()
    elif a == 2:
        books_under_year()
    elif a == 3:
        break
    else:
        print("Введите верное значение")
        continue
