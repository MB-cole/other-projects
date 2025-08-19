import random

print("Hello and welcome to your very own Digital 8 ball application!")
print("This application works just like how a normal 8 ball would")
print("just ask a question to have your fortune told, if you dare...")

while True:
    random_num = random.randint(1,8)
    input()
    if random_num == 1:
        print("Absolutely not!")
    elif random_num == 2:
        print("Of course not silly")
    elif random_num == 3:
        print("Yes")
    elif random_num == 4:
        print("Theres no way it'll not happen")
    elif random_num == 5:
        print("Ask me later...")
    elif random_num == 6:
        print("its possible")
    elif random_num == 7:
        print("ehh")
    elif random_num == 8:
        print("I can't say for certain")
    
    end = input("Would you like to test fate again? y/n ").lower() 
    if end == 'n':
        break 

    
      
      