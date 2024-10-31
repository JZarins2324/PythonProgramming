def display_separator():
    print("=================================================================")

def display_title():
    print("                   Baseball Team Manager")

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")

def display_positions():
    print()
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

def add_player(players):
    # Get Player Number
    number = 1

    if len(players) != 0:
        for player in players:
            if player[0] == number:
                number = player[0] + 1

    # Get Name and Stats
    name = input("Name: ")
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)

    # Add Player to List
    players.append([number, name, position, at_bats, hits])
    print(f"{name} was added.\n")

def get_player_position():
    while True:
        position = input("Position: ")

        if position not in valid_positions:
            print("Enter a valid position.")
        else:
            return position
            

def get_at_bats():
    while True:
        at_bats = int(input("At bats: "))

        if at_bats < 0:
            print("Value must be greater than 0.")
        else:
            return at_bats

def get_hits(at_bats):
    while True:
        hits = int(input("Hits: "))

        if hits > at_bats or hits < 0:
            print(f"Value must be between 0 and {at_bats}.")
        else:
            return hits

def get_lineup_number(players, prompt):
    while True:
        lineup_number = int(input(prompt))

        if lineup_number >= 1 and lineup_number <= 10:
            return lineup_number

def delete_player(players):
    lineup_number = get_lineup_number(players, "Enter the Player's Number: ")
    
    for index, player in enumerate(players):
        if player[0] == lineup_number:
            players.pop(index)
            return
        

def move_player(players):
    # Initialize Variables
    lineup_number = get_lineup_number(players, "Enter the Player's Number: ")
    lineup_position = int(input("Where do you want to move the player (1-9): "))
    selected_player = []
    selected_index = 0

    # Get Player and remove it from players List
    for index, player in enumerate(players):
        if player[0] == lineup_number:
            selected_index = index
            selected_player = players.pop(index)
            break

    # Reorder List
    temp_players = []

    i = 0
    while i < lineup_position - 1:
        temp_players.append(players[i])
        i += 1

    temp_players.append(selected_player)

    while i < len(players):
        temp_players.append(players[i])
        i += 1

    # Return new List
    return temp_players
    

def edit_player_position(players):
    lineup_number = get_lineup_number(players, "Enter the Player's Number: ")
    selected_player = []

    # Get Player
    for player in players:
        if player[0] == lineup_number:
            selected_player = player
            break

    # Get new Position
    while True:
        new_position = input("Enter New Position: ")

        if new_position in valid_positions:
            selected_player[2] = new_position
            return

        print("Enter a valid position.")

def edit_player_stats(players):
    lineup_number = get_lineup_number(players, "Enter the Player's Number: ")
    selected_player = []

    # Get Player
    for player in players:
        if player[0] == lineup_number:
            selected_player = player
            break

    # Get new stats
    while True:
        stat = input("Enter Stat to Edit: ").lower()
        if stat == "ab":
            player[3] = get_at_bats()
            return
        elif stat == "h":
            player[4] = get_hits(player[3])
            return
                    
        print("Please Enter 'AB' or 'H': ")
                    

def display_lineup(players):
    print("\tPlayer\t\tPOS\tAB\tH\tAVG")
    print("---------------------------------------------------")
    for player in players:
        num = player[0]
        name = player[1]
        position = player[2]
        at_bats = player[3]
        hits = player[4]

        print(f"{num}.\t{name}\t{position}\t{at_bats}\t{hits}\t{get_batting_avg(at_bats, hits):.3f}")

def get_batting_avg(at_bats, hits):
    return hits / at_bats


def main():
    players = []
    
    # Display Header
    display_separator()
    display_title()
    display_menu()
    display_positions()
    display_separator()
    
    while True:
        # Get User Action
        print()
        user_action = input("Menu option: ")

        # Execute User Action
        if user_action == "1":
            display_lineup(players)
            
        elif user_action == "2":
            add_player(players)

        elif user_action == "3":
            delete_player(players)

        elif user_action == "4":
            players = move_player(players)

        elif user_action == "5":
            edit_player_position(players)

        elif user_action == "6":
            edit_player_stats(players)

        elif user_action == "7":
            print("Bye!")
            break
        else:
            print("Enter a valid option (1-7).")

if __name__ == "__main__":
    valid_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    
    # Run Program
    main()
