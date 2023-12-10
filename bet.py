player1 = input("Player1:")
player2 = input("Player2:")
import random
total=0
for i in range(1,7):
    user = int(input("swing bat: "))
    print("its a ",user)
    machine = random.randint(1,6)
    if user!=machine:
        total = total + user
    elif user==machine and user==6:
        print ("bet at ",machine)
        print ("you are catch out at ",total)
        break
    elif user==machine and user!=6:
        print ("bet at ",machine)
        print ("you are run out")
        break   
    else:
        print("error")
    print ("bet at ",machine)

print ("total of ", player1," is ",total)


total_2 = 0
for i in range(1,7):
    user = int(input("swing bat: "))
    print("its a ",user)
    machine = random.randint(1,6)
    if user!=machine:
        total_2 = total_2 + user
    elif user==machine and user==6:
        print ("bet at ",machine)
        print ("you are catch out at ",total_2)
        break
    elif user==machine and user!=6:
        print ("bet at ",machine)
        print ("you are run out")
        break   
    else:
        print("error")
    print ("bet at ",machine)

print ("total of ",player2," is ",total_2)


if total > total_2:
       print(player1,"won with score of",total)
else:
       print(player2,"won with score of",total_2)
