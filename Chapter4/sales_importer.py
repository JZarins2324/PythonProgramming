#! /usr/bin/env/ python3

import sales

def display_title():
    print()
    print("SALES DATA IMPORTER")

    print()
    print("Enter sales data")

def display_total(total):
    # Display the total
    print("Total Sales")
    print()
    print(f"${total:.2f}\n")

def get_quarter(month):
    # Get quarter based on month
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

def main():
    display_title()

    # Variable to accumulate the total sales amount and sale number
    total = 0.0
    sales_number = 1

    # Start loop to get sales data
    again = "y"

    while again == "y":
        amount = sales.get_amount()
        year = sales.get_year()
        month = sales.get_month()
        day = sales.get_day()
        print()

        # Add sales to total
        total += amount

        # Get quarter
        quarter = get_quarter(month)

        #Display Sales Info
        print(f"{sales_number}.\t\t{year}-{month}-{day}\t",f"Quarter {quarter}\t${amount:.2f}\n")

        # Increment sales number
        sales_number +=1

        # Check if there are more sales
        again = input("Enter more sales (y/n): ").lower()
        print()

    display_total(total)
    print("Bye!")

if __name__ == "__main__":
    main()
        

