#! /usr/bin/env/ python3

import sales

def display_title():
    print()
    print("SALES DATA IMPORTER")

    print()
    print("Enter sales data")
    print()
    
def display_menu():
    print("COMMAND MENU")
    print("view - View all Sales")
    print("add - Add Sales")
    print("menu - Show Menu")
    print("exit - Exit Program")
    print()


def get_quarter(month:int):
    # Get quarter based on month
    print(f"{month}")
    if month >= 1 and month <= 3:
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    elif month >= 10 and month <= 12:
        quarter = 4
    else:
        quarter = 0

    return quarter

def view_sales(sales_list):
    if len(sales_list) == 0:
        print("No sales to view")
    else:
        total = 0
        print(f"\tDate\t\t Quarter\t\tAmount")
        print("-------------------------------------------------------")
        for num, data in enumerate(sales_list, start=1):
            amount = data[0]
            year = data[1]
            month = data[2]
            day = data[3]
            quarter = data[4]

            total += amount

            #Display Sales Info
            print(f"{num}.\t{day}-{month}-{year}\t",f"{quarter}\t\t\t${amount:.2f}\n")

        print("-------------------------------------------------------")
        print(f"TOTAL:\t\t\t\t\t\t${total:.2f}\n")

def add_sales(sales_list):
    amount = sales.get_amount()
    year = sales.get_year()
    month = sales.get_month()
    day = sales.get_day(month)
    print()

    quarter = get_quarter(month)

    data = [amount, year, month, day, quarter]
    sales_list.append(data)

    print(f"Sales for {month}-{day}-{year} added.\n")
    
def main():
    display_title()
    display_menu()

    sales_list = []
    

    # Start loop to handle commands
    while True:
        command = input("Enter a command: ").lower()
        if command == "view":
            view_sales(sales_list)
        elif command == "add":
            add_sales(sales_list)
        elif command == "menu":
            print()
            display_menu()
        elif command == "exit":
            print()
            break
        else:
            print("Invalid command")
            display_menu()

    print("Bye!")

if __name__ == "__main__":
    main()
        

