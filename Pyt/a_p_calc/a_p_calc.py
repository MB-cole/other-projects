import math

running = True
while running:
    try:
        print("Please select a shape to calculate the dimensions of (units must be standard).")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. End")
    
        choice = int (input("----> "))
    
        if choice == 1: 
            #input
            side = float(input("Please enter the Length or Width of your object: "))
            #math
            area = (side**2)
            perimeter = (4 * side)
            #out
            print(" ")
            print(f"The Area of your object is {area:.2f} and the Perimeter is {perimeter:.2f}.")
            print(" ")
        elif choice == 2:
            #input
            length = float(input("Please enter the Length of your object: "))
            width = float(input("Please enter the Width of your object: "))
            #math
            area = (length * width)
            perimeter = (2*length + 2*width)
            #out
            print(" ")
            print(f"The Area of your object is {area:.2f} and the Perimeter is {perimeter:.2f}.")
            print(" ")
        elif choice == 3:
            try:
                #input
                base = float(input("Please enter the Base of your object: "))
                height = float(input("Please enter the Height of your object: "))
                a,b,c = map(float,input("Please enter the Length of each side for your object separated by spaces or commas: ").replace(',',' ').split())
                #math
                area = (.5 * base * height)
                perimeter = (a + b + c)
                #out
                print(" ")
                print(f"The Area of your object is {area:.2f} and the Perimeter is {perimeter:.2f}.")
                print(" ")
            except ValueError:
                print("Error, Bad logic/Invalid input.")
        elif choice == 4:
            #input
            radius = float(input("Please enter the Radius of your object: "))
            #math
            area = (math.pi * radius**2)
            circumference = (2 * math.pi * radius)
            #out
            print(" ")
            print(f"The Area of your object is {area:.2f} and the Circumference is {circumference:.2f}.")
        elif choice == 5:
            running = False
    except ValueError:
        print(" ")
        print("Invalid input.")