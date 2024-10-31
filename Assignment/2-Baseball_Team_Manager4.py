def display_separator():
    print("=================================================================")

def display_title():
    print("                   Baseball Team Manager")

def display_menu():
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit program")

def calculate_average(num_hits, num_at_bats):
    return num_hits / num_at_bats

def main():
    # Display Header
    display_separator()
    display_title()
    display_menu()
    display_separator()

    while True:
        # Get User Action
        user_action = input("Menu option: ")

        if user_action != "1" and user_action != "2":
            print("Please enter a valid menu option")
            print()
            display_menu()
            print()
            
        if user_action == "1":
            # Display message
            print("Calculate batting average...")
            
            # Gather required data
            name = input("Player's name: ")
            num_at_bats = int(input("Official number of at bats: "))
            num_hits = int(input("Number of hits: "))

            # Calculate batting average
            avg = calculate_average(num_hits, num_at_bats)

            # Output
            print(f"Batting average: {avg:.3f}")
            print()

        elif user_action == "2":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
