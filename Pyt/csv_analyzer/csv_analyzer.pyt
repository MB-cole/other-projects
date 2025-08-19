import pandas
import os

running = True

while running:
    try: 
        user_csv_file = input("Please enter the name of your file: ")
        
        if not user_csv_file.endswith (".csv"):
            user_csv_file += ".csv" 
        
        print("1) View all file contents")
        print("2) View specific file entries")
        print()
        
        choice = int (input("What would you like to do with this file?: "))
        
        csv_file = pandas.read_csv(user_csv_file)
        if choice == 1: 
            print(csv_file)
            break
        elif choice == 2:
            print("How would you like the contents sorted?")
            print("The values are: ",csv_file.columns.values)
    except FileNotFoundError:
        print("Error, file not found: ")
    
#file = pandas.read_csv("csv_analyzer\expenses.csv")
    #print(file)
    #print("the total spent is: ",file['amount'].sum(axis=0))