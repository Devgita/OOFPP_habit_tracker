from habit_tracker import HabitTracker
from analytics import longest_streak, habits_by_routine

def main():
    tracker = HabitTracker()

    while True:
        print("List  of habit Tracker:")
        print("1. Add Habit:")
        print("2. Complete Habit:")
        print("3. Delete Habit:")
        print("4. List Habits:")
        print("5. Analyze Habits:")
        print("6. Exit")

        choice = input("choose the option display on list:")

        if choice == "1":
            name = input("Enter the name of habit:")
            routine = input("Enter the routine which may be on (daily/weekly) on:")
            tracker.add_habit(name, routine)
            print(f"Habit '{name}' added.")

        elif choice == "2":
            name = input("Enter the habit name which you completed:")
            tracker.complete_habit(name)

        elif choice == "3":
            name = input("Enter the habit name to delete:")
            tracker.delete_habit(name)

        elif choice == "4":

            print("\nList of Habits:")
            if tracker.habits:
                for habit in tracker.habits:
                    print(f"- {habit.name} ({habit.routine})")
            else:
                print("No habits found")

        elif choice == "5":
            print("\nAnalyze Habits:")
            print("1. longest streak for a habit")
            print("2. List habits by routine")
            sub_choice = input(" select an analysis option: ")


            if sub_choice == "1":
                name = input("enter habit name:")
                habit = next(( h for h in tracker.habits if h.name == name), None)
                if habit:
                    streak = longest_streak(habit)
                    print(f"Longest streak for '{habit.name}': {streak} days.")
                else:
                    print(f"Habit '{name}' not found.")

            elif sub_choice == "2":
                routine = input ("Enter routine '(daily/weekly'):")
                if routine in ["daily", "weekly"]:
                    filtered_habits = habits_by_routine(tracker.habits, routine)
                    if filtered_habits:
                        print(f"The habits for the '{routine}' routine:")
                        for habit in filtered_habits:
                            print(f"- {habit.name}")
                    else:
                        print(f" No habits found with '{routine}' routine.")
                else:
                    print("Invalid routine. please put the  'daily' or 'weekly'")

        elif choice == "6":
            print("Exiting Habit Tracker, Goodbye!")
            break

        else:

            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()
