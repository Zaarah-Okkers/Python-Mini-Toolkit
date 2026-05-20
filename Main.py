from Helpers import motivation_quote

# My Study planner/ Motivation generator
def study_planner():
    subject = input("Subject: ")
    try:
        hours = int(input("Hours to study: "))
    except ValueError:
        print("Please enter a valid number of hours.")
        return

    print("My Study Plan")
    print(f"Subject: {subject}")
    print(f"Study Hours: {hours}")
    if hours >= 5:
        print("Excellent dedication! You're doing amazing")
    elif hours >= 2:
        print("You're doing amazing! Keep up the good work!")
    else:
        print("Taking breaks and starting slow is OK!!! Study a little longer next time.")

# Daily Motivation Generator
def motivation_generator():
    print("Daily Motivation Generator")
    print(motivation_quote())

# To-Do List
def todo_list():
    print("To-Do List")
    print("This feature is under construction. Check back later.")

# ======================================
# MAIN MENU
# ======================================

while True:
    print("PYTHON MINI TOOLKIT")
    print("1. Study Planner")
    print("2. Daily Motivation Generator")
    print("3. To-Do List")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        study_planner()
    elif choice == "2":
        motivation_generator()
    elif choice == "3":
        todo_list()
    elif choice == "4":
        print("Thank you for using the Python Mini Toolkit!")
        break
    else:
        print("Invalid choice. Please try again.")