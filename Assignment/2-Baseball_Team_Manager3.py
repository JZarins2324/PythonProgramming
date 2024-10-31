# Display Header
print("=================================================================")
print("                   Baseball Team Manager")
print("MENU OPTIONS)")
print("1 - Calculate batting average")
print("2 - Exit program")
print("=================================================================")

while True:
    # Get User Action
    user_action = input("Menu option: ")

    if user_action != "1" and user_action != "2":
        print("Please enter a valid menu option")
        print()

    if user_action == "1":
        # Display message
        print("Calculate batting average...")
        
        # Gather required data
        name = input("Player's name: ")
        num_at_bats = int(input("Official number of at bats: "))
        num_hits = int(input("Number of hits: "))

        # Calculate batting average
        avg = num_hits / num_at_bats

        # Output
        print(f"Batting average: {avg:.3f}")
        print()

    elif user_action == "2":
        print("Bye!")
        break
