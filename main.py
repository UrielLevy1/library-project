from print_func import print_to_the_screen
from first_init import first_time_init_all, read
# call this func only in the first running,
# then, put her in a comment:

# first_time_init_all()

# here we create variables that contain all data from data files,
# which we will work on them during the program:

main_books_class = read("data_files/books.data")
main_cust_class = read("data_files/cust.data")
main_loans_class = read("data_files/loans.data")

# first, a user receives a print to the screen with all possible options (calling by func):

print_to_the_screen()

# then, he's entering his choice by an input:

while True:
    try:
        command = int(input("please enter your choice using the numbers 1 - 9, or 0 to end:"))
    except ValueError:
        print("only numbers are valid, try again please:")
        continue
    else:
        if command == 1:
            main_books_class.display_all_books()
        elif command == 2:
            main_cust_class.display_all_customers()
        elif command == 3:
            main_loans_class.display_all_loans()
        elif command == 4:
            main_cust_class.add_a_new_customer()
        elif command == 5:
            main_books_class.add_a_new_book()
        elif command == 6:
            main_books_class.find_book_by_name()
        elif command == 7:
            main_cust_class.find_customer_by_name()
        elif command == 8:
            main_books_class.remove_book()
        elif command == 9:
            main_cust_class.remove_customer()
        elif command == 0:
            print("\n")
            print("thank you for using our library system!" "\n"
                  "we're really hope to see you soon :)")
            break
        else:
            print("invalid number, sorry, choose number between 0 - 9")
            print("\n")
