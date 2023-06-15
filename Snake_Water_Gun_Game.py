# Snake, Water and Gun Game...

comp_points = 0
player_points = 0

print("Welcome to Snake, Water and Gun Game...")


def game():
    import random
    print("Computer's Turn: Chosen...")
    choise_list = ["s", "w", "g"]
    comp = random.choice(choise_list)
    player = input(
        "Player's Turn: Choose from Snake(s), Water(w) or Gun(g)...\n")

    if ((comp == "s" and player == "w") or (comp == "w" and player == "g") or (comp == "g" and player == "s")):
        global comp_points
        comp_points += 1
        if comp == "s":
            print("Computer chose Snake, You lose...")
        elif comp == "w":
            print("Computer chose Water, You lose...")
        elif comp == "g":
            print("Computer chose Gun, You lose...")

    elif ((comp == "w" and player == "s") or (comp == "g" and player == "w") or (comp == "s" and player == "g")):
        global player_points
        player_points += 1
        if comp == "s":
            print("Computer chose Snake, You Win...")
        elif comp == "w":
            print("Computer chose Water, You Win...")
        elif comp == "g":
            print("Computer chose Gun, You Win...")

    else:
        if comp == "s":
            print("Computer also chose Snake, It's a Tie...")
        elif comp == "w":
            print("Computer also chose Water, It's a Tie...")
        elif comp == "g":
            print("Computer also chose Gun, It's a Tie...")


t = int(input("How many times you want to play...\n"))
u = 1
while u <= t:
    u += 1
    print("\nLet's Play...")
    game()
else:
    print(
        f"Your points are {player_points} and Computers points are {comp_points}...\nThanks for playing...")
    if player_points < comp_points:
        print("Computer Won...")
    elif player_points > comp_points:
        print("You Win...")
    else:
        print("It's a tie...")
