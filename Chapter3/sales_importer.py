#! /usr/bin/env/ python3

print()
print("SALES DATA IMPORTER")

print()
print("Enter sales data")

# Variable to accumulate the total sales amount
total = 0.0
sales_number = 1

# Start loop to get sales data
again = "y"

while again == "y":
    amount = float(input("Amount:     "))
    year = int(input("Year:       "))
    month = int(input("Month:      "))
    day = int(input("Day:        "))
    print()

    # Add sales to total
    total += amount

    # Get quarter based on month
    if month >= 1 and month <= 3:
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    else:
        quarter = 4

    #Display Sales Info
    print(f"{sales_number}.\t\t{year}-{month}-{day}\t",f"Quarter {quarter}\t${amount}\n")

    # Increment sales number
    sales_number +=1

    # Check if there are more sales
    again = input("Enter more sales (y/n): ").lower()
    print()


# Display the total
print("Total Sales")
print()
print(f"${total}\n")

print("Bye")
