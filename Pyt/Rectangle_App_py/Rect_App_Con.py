# intro
print("Hello and welcome User!!")
print("this simple application is a small somewhat redundant calculator that "
      +"\nreturns both the area and parameter of any given rectangle!! ")

height = int (input("Firstly to begin, please enter the hight of your rectangle: " ))
width = int (input("And the width: "))

calculateArea = height * width
calculateParameter = (2*(height + width))

print(f"The area of your rectangle is: {calculateArea}")
print(f"and the Parameter is: {calculateParameter}")
