play = input("Do you want to play a game? ").lower()


if play == "yes":


 while play == "yes":
    name = input("Tell me your name:")
    print("Welcome", name, "to the adventure of a lifetime!")
    

    answer = input("You are on a dirt road, it has come to an end you can go left ir right. Which way would you like to go? ").lower()

    if answer == "left":
        q2 = input("You come to a river. You can walk around it or swim accross. Type walk to walk around and swim to swim accross: ").lower()

        if q2 == "swim":
            print("You swam accros and got eaten by a croc!.")
        elif q2 == "walk":
             print("You walked for miles, ran out of water and lost the game!.")
        else:
            print("Not a valid option. You lose")
    elif answer == "right":
        q2 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

        if q2 == "back":
             print("You made the right choise and win the game!.")
        elif q2 == "cross":
             q3 = input("You cross the bridge and meet a stranger. Do you tak to them (yes/no)? ").lower()

             if q3 == "yes":
                    print("You talk to the stranger and he gives you a pot of gold. You win!")
             elif q3 == "no":
                    print("You ignore the stranger and never get the reward, You lose!")
             else:
                    print("Not a valid option. You lose")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")

    break
else:
    quit
