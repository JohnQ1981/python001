print("""
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/


""")
todo = []
done = []
while True :
    print("*"*40)
    user = input("Enter a command. Type 'h' for help: \n > ")
    if user == "h" or user == "H":
        print('''
        TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number''')
    elif user =="q" or user =="Q":
        print(f"Your Todo list is:{todo}\nand Today you have completed {done}")
        for j in todo:
            print(f"You have {j} to do")
        for k in done:
            print(f"Today you have completed {len(done)} todos: {k}")
        break
    elif (user !="q" or user !="Q") and (not user.strip().isdigit()):
    
         todo.append(user)
        
    elif int(user)-1 in range(0,len(todo)):
        done.append(todo.pop(int(user)-1))
        print(f"You have completed:{done}")
    elif int(user)-1 not in range(0,len(todo)):
        print(f"I do not know that {int(user)} todo number!")
 
    for c in range(len(todo)) :
        print(f"{c+1} ) {todo[c]} ")