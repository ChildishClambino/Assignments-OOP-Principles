# starting point
from book import Book
from electronic import Electronic
from clothing import Clothing

def main():
    book = Book("20,000 Leagues Under the Sea", 20, "Jules Verne")
    electronic = Electronic("Tablet", 399, "A2342DF")
    clothing = Clothing("Pants", 40, "L")

    print(book.show_details())
    print(electronic.show_details())
    print(clothing.show_details())

if __name__ == "__main__":
    main()