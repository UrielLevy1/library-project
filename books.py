class Books:

    def __init__(self, book_id, book_name, author_name, year_pub, book_type):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
        self.year_pub = year_pub
        self.book_type = book_type

    def __str__(self):
        return f"book_id:{self.book_id}, book_type:{self.book_type}" \
               f"year_pub:{self.year_pub}, author:{self.author_name}, name:{self.book_name}"


class AllBooks:

    def __init__(self):
        self.all_books = []

    def add_a_new_book(self):
        from first_init import write
        print("Ok, let's get the details of the new book:")
        while True:
            try:
                book_id = int(input("enter book id in numbers"))
            except ValueError:
                print("only numbers are valid, try again please:")
                print("\n")
                continue
            else:
                book_name = input("enter a book name")
                author_name = input("enter author name")
                while True:
                    try:
                        year_pub = int(input("enter year published in numbers"))
                    except ValueError:
                        print("only numbers are valid, try again please:")
                        print("\n")
                        continue
                    else:
                        while True:
                            try:
                                book_type = int(input("enter type (1,2,3)"))
                            except ValueError:
                                print("only numbers are valid, try again please:")
                                print("\n")
                                continue
                            else:
                                new_book = Books(book_id, book_name, author_name, year_pub, book_type)
                                self.all_books.append(new_book)
                                write(self, "data_files/books.data")
                                print(new_book.book_id, new_book.book_name, new_book.author_name,
                                      new_book.year_pub, new_book.book_type)
                                print("\n")
                                print("the book is added successfully")
                                break
                    break
            break

    def display_all_books(self):
        for my_book in self.all_books:
            print(my_book.book_name)
            print("\n")

    def find_book_by_name(self):
        search_book = input("please enter a book name:")
        search_if_book_exists = 0
        for my_book in self.all_books:
            if search_book == my_book.book_name:
                search_if_book_exists += 1
                print("the book is found, here's the details: ", my_book)
                print("\n")
            else:
                pass
        if search_if_book_exists == 0:
            print("the book is not found, sorry!")
            print("\n")

    def remove_book(self):
        from first_init import write
        book_name = (input("please enter the book name you like to remove:"))
        search_if_book_exists = 0
        for index, book in enumerate(self.all_books):
            if book_name == book.book_name:
                search_if_book_exists += 1
                self.all_books.remove(book)
                write(self, "data_files/books.data")
                print("the book removed successfully")
                print("\n")
            else:
                pass
        if search_if_book_exists == 0:
            print("the book you're required is not found, sorry!")
            print("\n")



