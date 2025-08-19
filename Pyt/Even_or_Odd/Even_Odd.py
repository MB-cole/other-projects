print("Hello and welcome, this app will determine if your # input is either even or odd!")

while True:
    try:
        user_num = int(input("Please enter a value: "))
        if (user_num % 2) ==0:
            print(f"{user_num} is even!")
        else:
            print(f"{user_num} + is odd!")
            break
    except ValueError:
        print("Please enter a proper value.")