import random
def motivation_quote():
    quotes=[
        "Keep going. Every line of code makes you better." ,
        "Mistakes help you learn and grow!",
        "Small progress is still progress.",
        "You're more than capable of doing more! Don't let anything hold you back!", 
        "The only thing standing between you and your dreams is your doubt! Work hard and keep going!"
    ]
    return random.choice(quotes)

# ======================================
# TO-DO LIST
# ======================================

def todo_list():
    tasks = []

    while True:
        print("TO-DO LIST")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit To-Do List")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks added yet.")
            else:
                print("\nYour Tasks:")
                for task in tasks:
                    print("-", task)

        elif choice == "3":
            print("Leaving To-Do List...")
            break
        else:
            print("Invalid option. Please try again.")