import csv

PLAYERS = "players.csv"

def read_players():
    players = []
    with open(PLAYERS, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            players.append(row)

    return players

def write_players(players):
    with open(PLAYERS, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)