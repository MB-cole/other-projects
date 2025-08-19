
running = True
PAYED = 33.56
while running:
    
    choice = str (input("Would you like to leave a Tip? Y/N: ").strip().upper())
     
    if choice == "Y":
        
        print("Choose one of the following...")
        print("1. 5%")
        print("2. 10%")
        print("3. 15%")
        print("4. 20%")
        print("5. Custom")
        
        option = int(input("----> "))
        try:
            if option == 1:
                tip_amount = .05
                tip = PAYED * tip_amount
                total = (tip + PAYED)
                print(f"Your total is: ${total:.2f}")
                break
            elif option == 2:
                tip_amount = .1
                tip = PAYED * tip_amount
                total = (tip + PAYED)
                print(f"Your total is: ${total:.2f}")
                break
            elif option == 3:
                tip_amount = .15
                tip = PAYED * tip_amount
                total = (tip + PAYED)
                print(f"Your total is: ${total:.2f}")
                break
            elif option == 4:
                tip_amount = .2
                tip = PAYED * tip_amount
                total = (tip + PAYED)
                print(f"Your total is: ${total:.2f}")
                break
            elif option == 5:
                try:
                    tip_amount = float(input("Please enter tip amount in cash: "))
                    total = (PAYED + tip_amount)
                    print(f"Your total is: ${total:.2f}")
                    break
                except ValueError:
                    print("Please enter amount in cash")
        except ValueError:
            print("Invalid input, please choose one of the above.")
        
    elif choice == "N":
        print(f"Your total is: ${PAYED:.2f}")
        print("Thank you for your patronage.")
        running = False
    else:
        print("Invalid input, please choose on of the above 'Y/N'.")