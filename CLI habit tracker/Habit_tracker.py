from Habits import Habit


def main():

    # User input
    file_path = "Habits.txt"
    habit = user_input()
    # Save into file txt
    saving_into_file(habit, file_path)
    # Return a summary (read the file after appending)
    summary_output(file_path)


def user_input():
    print("Starting (User input!🎯)")
    habit_name = input("Enter your daily habit: ")
    habit_times = input("How many times you do it daily:")
    categories = [
        "Health & Wellness 💪🏼",
        "Productivity & Success 💰",
        "Social & Relationships ❤️",
    ]
    print("Category select:")
    for i, category in enumerate(categories):
        print(f"{i+1}.{category}")
    while True:

        num_range = f"(1 - {len(categories)})"

        try:
            entered_index = int(input(f"Enter category number {num_range}:")) - 1
            if entered_index in range(len(categories)):
                habit_category = categories[entered_index]
                new_habit = Habit(
                    name=habit_name, times=habit_times, category=habit_category
                )
                return new_habit
            else:
                print("Invalid number ,Try again please!")
        except ValueError:
            print("Error:wrong type of input!,Try again please! ")


def saving_into_file(habit: Habit, file_path):
    print("Starting (Saving into file!🎯)")
    with open(file_path, "a", encoding=("UTF-8")) as fname:
        fname.write(f"{habit.name},{habit.times},{habit.category}\n")


def summary_output(file_path):
    print("Starting (Summary output!🎯)")
    print("-" * 40)
    with open(file_path, "r", encoding=("UTF-8")) as f:
        for i, line in enumerate(f):
            name, times, category = line.strip().split(",")
            print(f"{i+1}.{name} , {times} x Day -{category}")
    print("-" * 40)


# its a special function to stop calling main function unless we run it
if __name__ == "__main__":
    main()
