
print("Hello and welcome to the BMI calculator User!\n"
      "This app will calculate your BMI based on the factors below!\n"
     )

user_height_in = float(input("1). Please enter your height in inches: "))
user_weight = float(input("2). Please enter your weight in pounds: "))

print("")

user_bmi = (user_weight / (user_height_in * user_height_in ) * 703.0)

if user_bmi < 18.5:
    print(f"Your BMI is {user_bmi:.2f}, you are currently in the 'Under Weight' weight class.")
elif 18.5 <= user_bmi <= 24.9:
    print(f"Your BMI is {user_bmi:.2f}, you are currently in the 'Normal' weight class.")
elif 25 <= user_bmi <= 29.9:
    print(f"Your BMI is {user_bmi:.2f}, you are currently in the 'Over Weight' weight class.")
else:
    print(f"Your BMI is {user_bmi:.2f}, you are currently in the 'Obese' weight class.")