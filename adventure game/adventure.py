name=input("Type your name: ")
print("Welcome", name, "to this game")
answer=input("You are on a dirt road, it has come to an end you can go ,left or right, which way do you want to go?  ").lower()
if answer== "left":
    answer= input("you have come to a river, you can walk around it or swim across?  ")
    if answer=="swim":
        print("You swam across and got eaten by a crocodile")
    elif answer=="walk":
        print("You walked for many miles and lacked water")
    else:
        print("Invalid option")


elif answer == "right":
    answer=input("You come to a bridge, Do you want to cross or go back? (back/cross) ")
    if answer=="back":
        print("You go back and loose")
    elif answer=="cross":
        answer=input("You cross the bridge and meet a stranger, do you talk to them (Yes/No)")
        if answer == "Yes":
            print("You talk to the stranger and they give you gold, You win!")
        elif answer== "No" :
            print("You ignore the stranger and they feel offended now, You loose!")  
        else:
            print("Invalid option ")  
    else:
        print("Invalid option, You loose")



else:
    print("Invalid choice.You loose")
