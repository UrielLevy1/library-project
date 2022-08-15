import pickle
from books import Books, AllBooks
from customers import Customers, AllCustomers
from loans import Loans, AllLoans

# this is the program initialization module - and it runs only once at the run beginning,
# in order to generate the data data_files in the program


# this func creating and writing to a data file in the program


def write(object_to_save, filename):
    with open(filename, "wb") as my_file:
        pickle.dump(object_to_save, my_file)


# this func returning an exists data file


def read(filename):
    with open(filename, "rb") as my_file:
        return pickle.load(my_file)


# this func is reading a csv file and returning a books objects list


def read_books_from_file():
    all_my_books = []
    with open(r"data_files/Books.csv") as books_file:
        header = books_file.readline()
        for line in books_file:
            temp_list = line.split(",")
            book = Books(author_name=temp_list[0],
                         book_id=int(temp_list[1]),
                         year_pub=int(temp_list[2]),
                         book_type=int(temp_list[3]),
                         book_name=temp_list[4][:-1])
            all_my_books.append(book)
    return all_my_books


# this func is reading a csv file and returning a customers objects list


def read_cust_from_file():
    all_cust = []
    with open(r"data_files/Customers.csv") as cust_file:
        header = cust_file.readline()
        for line in cust_file:
            temp_list = line.split(",")
            cust = Customers(id=temp_list[3],
                             name=temp_list[2],
                             city=temp_list[1],
                             age=int(temp_list[0]))
            all_cust.append(cust)
    return all_cust


def read_loans_from_file():
    all_loans = []
    with open(r"data_files/Loans.csv") as loans_file:
        header = loans_file.readline()
        for line in loans_file:
            temp_list = line.split(",")
            loan = Loans(return_date=temp_list[0],
                         loan_date=temp_list[1],
                         customer=temp_list[2],
                         book_id=int(temp_list[3]))
            all_loans.append(loan)
    return all_loans

# Here is the call to the functions above, and this is where the data_files are created in the program:


def first_time_books_data_read():
    all_books = read_books_from_file()
    main_books_class = AllBooks()
    main_books_class.all_books = all_books
    write(main_books_class, "data_files/books.data")


def first_time_cust_data_read():
    all_cust = read_cust_from_file()
    main_cust_class = AllCustomers()
    main_cust_class.all_customers = all_cust
    write(main_cust_class, "data_files/cust.data")


def first_time_loans_data_read():
    all_loans = read_loans_from_file()
    main_loans_class = AllLoans()
    main_loans_class.all_loans = all_loans
    write(main_loans_class, "data_files/loans.data")


def first_time_init_all():
    run_over_data = input("are you sure you want to run over data? yes/no")
    if run_over_data == "yes":
        first_time_cust_data_read()
        first_time_books_data_read()
        first_time_loans_data_read()

