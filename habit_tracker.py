from db import JSONDatabase
import datetime


class Habit:
    """
  Define the constructor method and initialize the attributes name, routine,
  created_at and completions.
    """
    def __init__(self, name, routine, created_at=None, completions=None):
        self.name = name
        self.routine = routine  # routine may be "daily" or "weekly"
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.completions = completions or []

    def mark_complete(self):
        """
        sets habit to be completed by saving  current datetime.
        """
        self.completions.append(datetime.datetime.now().isoformat())

    def to_dict(self):
        """
        Changing the Habit object to a dictionary for JSON serialization.
        """
        return {
            "name": self.name,
            "routine": self.routine,
            "created_at": self.created_at,
            "completions": self.completions
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Habit object from a dictionary.
        """
        return Habit(
            name=data["name"],
            routine=data["routine"],
            created_at=data["created_at"],
            completions=data["completions"]
        )


class HabitTracker:
    """
   initializes the habit management  and handles load and saving  from/to Database.
    """

    def __init__(self, storage_file="data.json"):
        self.db = JSONDatabase(storage_file)
        self.habits = []
        self.load_habits()

    def load_habits(self):
        """
        Loads habits from the database.
        """
        data = self.db.load()
        self.habits = [Habit.from_dict(habit) for habit in data]

    def save_habits(self):
        """
        Saves habits to the database.
        """
        self.db.save([habit.to_dict() for habit in self.habits])

    def add_habit(self, name, routine):
        """
        Adds a new habit to the tracker.
        """
        new_habit = Habit(name=name, routine=routine)
        self.habits.append(new_habit)
        self.save_habits()

    def delete_habit(self, name):
        """
        Deletes a habit which is unrelated.
        """
        self.habits = [habit for habit in self.habits if habit.name != name]
        self.save_habits()

    def complete_habit(self, name):
        """
        Add the habit as completed by name.
        """
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete()
                self.save_habits()
                return
        print(f"There is no such habit with name'{name}' in the habit list.")

    def list_habits(self):
        """
        Returns the list of habits.
        """
        return self.habits
