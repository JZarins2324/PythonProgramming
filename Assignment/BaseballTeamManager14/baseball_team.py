import db
from objects import Player
from datetime import date, datetime

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def add_player(players):
    player = Player()

    player.first_name = input("First Name: ").title()
    player.last_name = input("Last Name: ").title()
    player.position = get_player_position()
    player.at_bats = get_at_bats()
    player.hits = get_hits(player.at_bats)
    
    players.append(player)

    db.write_players(players)

    print(f"{player.fullName()} was added.\n")

def get_player_position():
    while True:
        position = input("Position: ").upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_positions()

def get_at_bats():
    while True:
        at_bats = int(input("At bats: "))
        if at_bats < 0 or at_bats > 10000:    
            print("Invalid entry. Must be from 0 to 10,000.")
        else:
            return at_bats

def get_hits(at_bats):
    while True:
        hits = int(input("Hits: "))
        if hits < 0 or hits > at_bats:        
            print(f"Invalid entry. Must be from 0 to {at_bats}.")
        else:
            return hits

def get_lineup_number(players, prompt):
    while True:
        number = int(input(prompt))
        if number < 1 or number > len(players):
            print("Invalid player number. Please try again.")
        else:
            return number

def delete_player(players):
    number = get_lineup_number(players, "Number: ")
    player = players.pop(number-1)

    db.write_players(players)
    print(f"{player.fullName()} was deleted.\n")

def move_player(players):
    old_number = get_lineup_number(players, "Current lineup number: ") 
    print(f"{players[old_number-1].fullName()} was selected.")
    new_number = get_lineup_number(players, "New lineup number: ")

    player = players.pop(old_number-1)
    players.insert(new_number-1, player)

    db.write_players(players)
    print(f"{player.fullName()} was moved.\n")

def edit_player_position(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players[number-1]
    print(f"You selected {player.fullName()} POS={player.position}")
    
    position = get_player_position()
    player.position = position

    db.write_players(players)
    print(f"{player.fullName()} was updated.\n")

def edit_player_stats(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players[number-1]
    print(f"You selected {player.fullName()} AB={player.at_bats} H={player.hits}")
    
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    player.at_bats = at_bats
    player.hits = hits

    db.write_players(players)
    print(f"{player.fullName()} was updated.\n")

def display_lineup(players):
    if players == None:
        print("There are currently no players in the lineup.")
    else:
        print("\tPlayer\t\tPOS\tAB\tH\tAVG")
        print("----------------------------------------------------------------")
        for i, player in enumerate(players, start=1):
            name = player.fullName()
            position = player.position
            at_bats = player.at_bats
            hits = player.hits
            #get_batting_avg(at_bats, hits)
            avg = player.battingAvg()

            print("Batting average:","{:.3f}".format(round(avg, 3)))
            print(f"{i}\t{name}\t\t{position}\t{at_bats}\t{hits}\t","{:.3f}".format(round(avg, 3)))
    print()

def get_batting_avg(at_bats, hits):
    avg = int(hits) / int(at_bats)
    return round(avg, 3)

def display_separator():
    print("================================================================")

def display_title():
    print("                   Baseball Team Manager")

def display_menu():
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 – Show Menu")
    print("8 - Exit program")
    print()

def display_positions():
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

def display_dates():
    print()

    date_format = "%Y-%m-%d"
    now = datetime.now()    
    current_date = datetime(now.year, now.month, now.day)
    print(f"CURRENT DATE:    {current_date.strftime(date_format)}")

    while True:
        game_date_str = input("GAME DATE:       ")
        if game_date_str == "":
            print()
            return

        try:
            game_date = datetime.strptime(game_date_str, date_format)
        except ValueError:
            print("Incorrect date format. Please try again.")
            continue
        
        time_span = game_date - current_date

        if time_span.days > -1:
            print(f"DAYS UNTIL GAME: {time_span.days}")
        print()
        break    

def main():
    display_separator()
    display_title()
    display_dates()
    display_menu()
    display_positions()
    display_separator()

    players = db.read_players()
    while True:
        option = int(input("Menu option: "))
            
        if option == 1:
            display_lineup(players)
        elif option == 2:
            add_player(players)
        elif option == 3:
            delete_player(players)
        elif option == 4:
            move_player(players)
        elif option == 5:
            edit_player_position(players)
        elif option == 6:
            edit_player_stats(players)
        elif option == 7:
            display_menu()
        elif option == 8:
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()
