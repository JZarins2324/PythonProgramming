import sales
import db
import csv

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
    print("import - Import Sales from File")
    print("Save - Save Sales to File")
    print("menu - Show Menu")
    print("exit - Exit Program")
    print()

def view_sales(sales_list):
    if len(sales_list) == 0:
        print("No sales to view")
    else:
        total = 0
        print(f"\tDate\t\t Quarter\t\tAmount")
        print("-------------------------------------------------------")
        for num, data in enumerate(sales_list, start=1):
            amount = data[0]
            month = data[1]
            day = data[2]
            year = data[3]
            quarter = data[4]

            total += amount

            #Display Sales Info
            print(f"{num}.\t{month}-{day}-{year}\t",f"{quarter}\t\t\t${amount:.2f}\n")

        print("-------------------------------------------------------")
        print(f"TOTAL:\t\t\t\t\t\t${total:.2f}\n")

def add_sales(sales_list):
    amount = sales.get_amount()
    month = sales.get_month()
    day = sales.get_day(month)
    year = sales.get_year()
    print()

    quarter = db.get_quarter(month)

    data = [amount, month, day, year, quarter]
    sales_list.append(data)

    print(f"Sales for {month}-{day}-{year} added.\n")

def import_sales(sales_list):
    filename = input("Enter name of file to be imported: ")
    print()

    if db.already_imported(filename):
        print(f"File '{filename}' has already been imported\n")
    else:
        imported_sales = db.import_sales(filename)
        view_sales(imported_sales)

        if len(imported_sales) > 0:
            sales_list += imported_sales
            print("Imported Sales added to list")
            db.add_imported_file(filename)

def main():
    display_title()
    display_menu()

    sales_list = db.get_all_sales()

    # Start loop to handle commands
    while True:
        command = input("Enter a command: ").lower()
        if command == "view":
            view_sales(sales_list)
        elif command == "add":
            add_sales(sales_list)
        elif command == "import":
            import_sales(sales_list)
        elif command == "save":
            db.save_all_sales(sales_list)
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
        

