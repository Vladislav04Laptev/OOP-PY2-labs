BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id, name, pages):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id: индекс книги
        :param name: название книги
        :param pages: количество страниц в книге

        """
        #проверки передаваемых переменных на коректность типа данных
        if not isinstance(id, (int,float)):
            raise TypeError("Id не типа int или float")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Name должна быть строкой")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Pages должно быть целочисленно")
        self.pages = pages

    def __str__(self) -> list:
        return f'Книга "{self.name}"'

    def __repr__(self) -> list:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
