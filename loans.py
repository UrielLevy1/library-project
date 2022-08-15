class Loans:
    def __init__(self, customer, book_id, loan_date, return_date):
        self.customer = customer
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def __str__(self):
        return f"customer:{self.customer}, book_id:{self.book_id}," \
         f" loan_date:{self.loan_date}, return_date:{self.return_date}"


class AllLoans:
    def __init__(self):
        self.all_loans = []

    def display_all_loans(self):
        for loans in self.all_loans:
            print(loans.customer)
            print("\n")


