# daily_reminder.py

while True:
    # Prompt the user for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    print()  # Add spacing for readability

    # Provide a reminder using match-case for priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that needs to be done today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan it into your schedule.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task but still needs to be completed today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority entered. Please enter 'high', 'medium', or 'low'.")

    # Ask the user if they want to enter another task
    repeat = input("\nDo you want to enter another task? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Goodbye! Stay productive!")
        break

   
