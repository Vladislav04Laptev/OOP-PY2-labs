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

# TODO написать класс Library
class Library:
    def __init__(self, books=[]):
        """
         Создание и подготовка к работе объекта "Книга"

        :param books: список книг

        """
        if not isinstance(books, list):
            raise TypeError("Передаваться должен список книг")
        self.books = books
    def get_next_book_id(self) -> int:
        """
        Функция возвращающяя идентификатор для добавления новой книги в библиотеку

        :return: идентификатор для новой книги

        """
        return len(self.books) + 1

    def get_index_by_book_id(self, id_search: int) -> int:
        """
        Функция возвращающая индекс книги в списке, через индекс книги, находящийся в атрибуте класса

        :return: возвращаем индекс книги в списке

        :raise ValueError: Если книги с запрашиваемым id не существует, то вызываем ошибку

        """
        #проверяем на соответствие передаваемой переменной типу данных
        if not isinstance(id_search, (int, float)):
            raise TypeError("Id не типа int или float")
        self.id_search = id_search

        for b in self.books: #перебор всех элементов списков
            if b.id == id_search: #епроверка совпадения id элемента класса Book с искомым
                return self.books.index(b)
        raise ValueError("Книги с запрашиваемым id не существует")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
