import csv
from objects import Player

PLAYERS = "players.csv"

def read_players():
    players = []
    with open(PLAYERS, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            player = Player()

            player.first_name = row[0]
            player.last_name = row[1]
            player.position = row[2]
            player.at_bats = row[3]
            player.hits = row[4]

            players.append(player)

    return players

def write_players(players):
    new_players = []

    for player in players:
        new_player = []

        new_player.append(player.first_name)
        new_player.append(player.last_name)
        new_player.append(player.position)
        new_player.append(player.at_bats)
        new_player.append(player.hits)

        new_players.append(new_player)

    with open(PLAYERS, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_players)