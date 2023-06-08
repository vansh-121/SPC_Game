#Stone paper scissor game 
print("Welcome to game of stone paper scissor:\n")
print('''Instructions:\n["1" refers to Stone\n"2" refers to Paper\n"3" refers to Scissor]''' )
print()
print("Press 0 to choose Stone")
print("Press 1 to choose Paper")
print("Press 2 to choose Scissor")
a = int(input("Enter any no bw 0-2 :" ))
if (a < 0 or a > 2):
    print("Invalid input !!!")
else:
    import random                
    comp = random.randint(0,2)
    print(f"The computer's choice is {comp}\nYour choice is {a}")
    if (comp == 0 and a == 0):
        print("The match tied")
    elif (comp == 0 and a == 1):
        print("The computer wins")
    elif(comp == 0 and a == 2):
        print("The computer wins")
    elif (comp == 1 and a == 0):
        print("You won")
    elif (comp == 1 and a == 1):
        print("The match tied")
    elif (comp == 1 and a == 2):
        print("You won")
    elif (comp == 2 and a == 0 ):
        print("You won")
    elif (comp == 2 and a == 1):
        print("The computer wins")
    elif (comp == 2 and a == 2):
        print("The match tied")

        
        


