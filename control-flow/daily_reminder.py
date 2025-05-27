# daily_reminder.py

# Function to get valid priority input
def get_priority():
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            return priority
        else:
            print("Please enter a valid priority: high, medium, or low.")

# Function to get valid time-bound input
def get_time_bound():
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ["yes", "no"]:
            return time_bound
        else:
            print("Please answer with 'yes' or 'no'.")

# Get user input
task = input("Enter your task: ")
priority = get_priority()
time_bound = get_time_bound()

# Generate customized reminder
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to address it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that still needs to be done today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to work on it when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task, but since it's time-bound, complete it today!")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")

