first_name  = str (input("1). Please enter your first name: "))
last_name = str (input("2). Please enter your last name: "))
t_sales = int(input("3). please enter the total sales amount: "))
 
employee = first_name + " " + last_name

#base tax %
amount_rec = .07
fed_tax = .18
ss_tax = .06
retirement_funds = .10

#spacing
print("")

print(employee+ "'s" + " Deductions")
print("-----------------")
print(f"Sales:  {t_sales:.2f}")

Amr = t_sales * amount_rec 
print(f"Amount received: {t_sales * amount_rec:.2f}")

Ft = t_sales * amount_rec * fed_tax
print(f"Federal tax: {t_sales * amount_rec * fed_tax:.2f}")

Ss = t_sales * amount_rec * ss_tax
print(f"Social Security: {t_sales * amount_rec * ss_tax:.2f}")

Rf = t_sales * amount_rec * retirement_funds
print(f"Retirement fund: {t_sales * amount_rec * retirement_funds:.2f}")

print("")
print("Total take home pay: " + str(Amr - Ft - Ss - Rf))