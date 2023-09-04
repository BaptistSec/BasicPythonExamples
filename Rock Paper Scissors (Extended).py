import random

Game = 1
tie = 0
player_score = 0
cpu_score = 0


def cpu_choice():
    cpu_index = ["rock", "paper", "scissors"]
    cpu_decision = random.randint(0, 2)
    cpu_word = cpu_index[cpu_decision]
    print("The CPU chose", cpu_word)
    return cpu_decision


def player_choice():
    while True:
        player_decision = input("rock, paper or scissors? ")
        if player_decision == "rock":
            player_decision = 0
            break
        elif player_decision == "paper":
            player_decision = 1
            break
        elif player_decision == "scissors":
            player_decision = 2
            break
        else:
            print("Enter a valid option")
    return player_decision


while Game < 4 + tie:
    print()
    print("You are on Game ", Game)
    player_move = player_choice()
    cpu_move = cpu_choice()
    if cpu_move == player_move:
        print("It's a tie!")
        tie += 1
    elif player_move == 0:
        if cpu_move == 1:
            print("You have lost")
            cpu_score += 1
        else:
            print("You have won!")
            player_score += 1
    elif player_move == 1:
        if cpu_move == 2:
            print("You have lost")
            cpu_score += 1
        else:
            print("You have won!")
            player_score += 1
    elif player_move == 2:
        if cpu_move == 0:
            print("You have lost")
            cpu_score += 1
        else:
            print("You have won!")
            player_score += 1
    Game += 1
    print("You have ", player_score, " point(s) against the CPU's ", cpu_score, "point(s)")

print("Game over")
if player_score > cpu_score:
    print("Player WINS with ", player_score, "against ", cpu_score)
elif cpu_score > player_score:
    print("CPU WINS with ", cpu_score, "against ", player_score)
else:
    print("It is a tie")
