class Customers:
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age

    def __str__(self):
        return f"id:{self.id}, name:{self.name}, city:{self.city}, age:{self.age}"


class AllCustomers:
    def __init__(self):
        self.all_customers = []

    def add_a_new_customer(self):
        from first_init import write
        print("Ok, let's get the details of the new customer:")
        while True:
            try:
                id = int(input("enter customer id in numbers"))
            except ValueError:
                print("only numbers are valid, try again please:")
                print("\n")
                continue
            else:
                name = input("enter customer name")
                city = input("enter your city")
                while True:
                    try:
                        age = int(input("enter your age in numbers"))
                    except ValueError:
                        print("only numbers are valid, try again please:")
                        print("\n")
                        continue
                    else:
                        new_cust = Customers(id, name, city, age)
                        self.all_customers.append(new_cust)
                        write(self, "data_files/cust.data")
                        print(new_cust.id, new_cust.city, new_cust.age, new_cust.name)
                        print("\n")
                        print("the customer is added successfully")
                        break
            break

    def display_all_customers(self):
        for customer in self.all_customers:
            print(customer.name)
            print("\n")

    def find_customer_by_name(self):
        search_customer = input("please enter the customer name:")
        search_if_cust_exists = 0
        for cust in self.all_customers:
            if search_customer == cust.name:
                search_if_cust_exists += 1
                print("the customer is found, here's the details: ", cust)
                print("\n")
            else:
                pass
        if search_if_cust_exists == 0:
            print("the customer is not found, sorry!")
            print("\n")

    def remove_customer(self):
        from first_init import write
        cust_name = input("please enter the customer name you like to remove:")
        search_if_cust_exists = 0
        for index, cust in enumerate(self.all_customers):
            if cust_name == cust.name:
                search_if_cust_exists += 1
                self.all_customers.remove(cust)
                write(self, "data_files/cust.data")
                print("the customer removed successfully")
                print("\n")
            else:
                pass
        if search_if_cust_exists == 0:
            print("the customer you're looking for is not exist, sorry!")
            print("\n")
