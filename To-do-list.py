todolist=[]
while True:
    print("\n--- TO-DO-LIST ---")
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Exit")
    choice=input("Enter your choice(1-4): ")
    if choice=='1':
        task=input("Enter task:")
        todolist.append(task)
        print("Task added successfully.")
    elif choice == '2':
        if not todolist:
            print("No tasks found.")
        else:
            print("\n Your tasks:")
            for i,t in enumerate(todolist,start=1):
                print(f"{i}. {t}")
    elif choice == '3':
        if not todolist:
            print("No tasks to delete.")
        else:
            try:
                task_num=int(input("Enter task number to delete: "))
                if 1<= task_num<=len(todolist):
                    removed= todolist.pop(task_num-1)
                    print(f"{removed} deleted")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice,please try again.")