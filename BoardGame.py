# Homework 3 - Board Game System
# Name:Gavin Grow
# Date:4/5/26

import random

def load_game(file_name):
    players = {}
    events = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                position, name = line.split(": ")
                position = int(position)

                if "Player" in name:
                    num = int(name.replace("Player", ""))
                    players[num] = position
                else:
                    events[position] = name

    return players, events


def display_board(players, events):
    print("\n--- Current Game State ---")

    print("\nPlayers:")
    for num, pos in sorted(players.items()):
        print(f"Player {num} is at position {pos}")

    print("\nEvents on Board:")
    for pos, event in events.items():
        print(f"Position {pos}: {event}")


def move_player(players, player_num, steps):
    players[player_num] += steps


def check_event(players, events, player_num):
    pos = players[player_num]

    if pos in events:
        event = events[pos]
        print(f"Player {player_num} landed on {event}!")

        if event == "Goblin":
            players[player_num] -= 2
            print("Goblin attack! Move back 2 spaces.")
        elif event == "Treasure":
            players[player_num] += 3
            print("Treasure found! Move forward 3 spaces.")
        elif event == "Potion":
            players[player_num] += 1
            print("Found a potion! Move forward 1 space.")
        elif event == "Trap":
            players[player_num] -= 1
            print("Fell into a trap! Move back 1 space.")
        elif event == "Bonus":
            players[player_num] += 2
            print("Bonus! Move forward 2 spaces.")
        elif event == "Penalty":
            players[player_num] -= 2
            print("Penalty! Move back 2 spaces.")
        elif event == "Lucky":
            players[player_num] += 3
            print("Lucky! Move forward 3 spaces.")
        elif event == "Unlucky":
            players[player_num] -= 3
            print("Unlucky! Move back 3 spaces.")
        elif event == "Warp":
            new_pos = random.randint(1, 30)
            players[player_num] = new_pos
            print(f"Warped to position {new_pos}!")


def main():
    players, events = load_game("events.txt")

    while True:
        display_board(players, events)

        player_input = input("\nEnter player number (e.g., 1, player 1, Player1) or 'quit': ")

        if player_input.lower() == "quit":
            print("Game ended.")
            break

        player_num = None
        try:
            player_num = int(player_input)
        except ValueError:
            if player_input.lower().startswith('player'):
                try:
                    num_str = player_input.lower().replace('player', '').strip()
                    player_num = int(num_str)
                except ValueError:
                    pass

        if player_num is None or player_num not in players:
            print("Invalid player number.")
            continue

        # Roll dice
        steps = random.randint(1, 6)
        print(f"Rolled a {steps}!")

        move_player(players, player_num, steps)
        check_event(players, events, player_num)

        if players[player_num] > 30:
            print(f"Player {player_num} has reached beyond position 30 and wins!")
            break


# Run the game
main()
