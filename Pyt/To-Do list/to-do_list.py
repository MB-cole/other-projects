import os
proj_dir = os.path.join(os.path.dirname(__file__))
os.makedirs(proj_dir,exist_ok=True)
running = True

while running:
    print("1. Pull list")
    print("2. Create list")
    print("3. Delete list")
    print("4. End")
    
    option = int(input("---> "))
    
    if option == 1:
        try:
            print("Please enter the name of your list.")
            list_name = input("List name: ").strip()
            if not list_name.endswith(".txt"):
                list_name += ".txt"
                
            print()
            
            path = os.path.join(proj_dir,list_name)
            with open(path,"r") as f:
                if os.stat(path).st_size == 0:
                    print("This To-Do List has no content..")
                    print()
                else:
                    print("----Task----")
                    print(f.read())
                    option = input("Would you like to edit your list?(Y/N)").strip().upper()
                    if option == "Y":
                        print
                    elif option == "N":
                        print("Thank you for using this program!")
                        break
        except FileNotFoundError:
            print(" file Could not be found or Quote Error")
    
    elif option == 2:
        print("What would you like to name your To-Do List? (.txt is default if type not specified,)")
        
        try:   
            list_name = input("List name: ")
            if not list_name.endswith(".txt"):
                list_name += ".txt"
            directory = os.path.dirname(__file__)
            path = os.path.join(directory,list_name)
            
            with open(path,"x") as f:
                print("Your list was created")
                option = str (input("Would you like to add task to your To-Do List?(Y/N): ").strip().upper())
        
                if option == "Y":
                   
                elif option == 'N':
                    running = False  
                           
        except FileExistsError:
            print("This list already exist please choose another name.")
            
    elif option == 3:
        try:
            print("Please enter the name of the list you'd like to remove.")
            list_name = input("List name: ")
            if not list_name.endswith(".txt"):
                list_name += ".txt"
                path = os.path.join(proj_dir,list_name)
                os.remove(path)
                print("ToDo List deleted")
        except FileNotFoundError:
            print("this list does not exist")
            
    elif open == 4:
        running = False