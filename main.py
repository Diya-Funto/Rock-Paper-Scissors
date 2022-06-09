
import random

print("Welcome to ROCK PAPER SCISSORS")
print(" ")

Game_options = ['R', 'P', 'S']
Options_dict = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

Player_name = input("Enter player ID: ")
print("Welcome " + Player_name + ". These are your options: ")
print ("Enter R for Rock | Enter P for Paper | Enter S for Scissors")

while True:
    Player_choice = input("Enter choice: ").upper()
    CPU = random.choice(Game_options)

#while Player_choice in Game_options:
    #continue

    while (Player_choice not in Game_options):
        print("Error, value entered is not an option. Try again")
        print ("Enter R for Rock | Enter P for Paper | Enter S for Scissors")
        Player_choice = input("Enter choice: ").upper()

        print("  ")

        print ("Player:",(Player_choice), ":",  "CPU:",(CPU) )


    while CPU == Player_choice:
        print("It's a tie. Try again.")
        print ("Enter R for Rock | Enter P for Paper | Enter S for Scissors")
        Player_choice = input("Enter choice: ").upper()
        CPU_choice = random.choice(Game_options)

    if CPU == 'S'and Player_choice == 'P':
        print("Computer wins. Better luck next time")
        break
    elif CPU == 'S' and Player_choice == 'R':
        print(Player_name, "wins!")
        break
    elif CPU == 'P' and Player_choice == 'S':
        print(Player_name, "wins!")
        break
    elif CPU == 'P'and Player_choice == 'R':
        print("Computer wins. Better luck next time")
        break
    elif CPU == 'R' and Player_choice == 'S':
        print("Computer wins. Better luck next time")
        break
    elif CPU == 'R'and Player_choice == 'P':
        print(Player_name, "wins!")
        break

    else:
        print("Error. Close game")












#elif
