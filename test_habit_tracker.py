import unittest
import os
from datetime import datetime, timedelta
from habit_tracker import Habit, HabitTracker
from analytics import longest_streak, habits_by_routine


class TestHabitTracker(unittest.TestCase):

    def setUp(self):
        """Set up a temporary HabitTracker with a test file."""
        self.test_file = "test_data.json"
        self.tracker = HabitTracker(self.test_file)

        # Cleans up any test file data that already exists.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Cleaning up test file after each testing."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_habit(self):
        """Test create new habit."""
        self.tracker.add_habit("Drink Water", "daily")
        self.assertEqual(len(self.tracker.habits), 1)
        self.assertEqual(self.tracker.habits[0].name, "Drink Water")
        self.assertEqual(self.tracker.habits[0].routine, "daily")

    def test_complete_habit(self):
        """Test mark a habit which  was done."""
        self.tracker.add_habit("Exercise", "daily")
        self.tracker.complete_habit("Exercise")
        self.assertEqual(len(self.tracker.habits[0].completions), 1)

        # Verify the completion of given time is recent
        completion_time = datetime.fromisoformat(self.tracker.habits[0].completions[0])
        self.assertTrue(datetime.now() - completion_time < timedelta(seconds=5))

    def test_delete_habit(self):
        """Test delete a habit which is unrelated."""
        self.tracker.add_habit("Read book", "weekly")
        self.tracker.add_habit("Run", "daily")
        self.tracker.delete_habit("Read book")

        self.assertEqual(len(self.tracker.habits), 1)
        self.assertEqual(self.tracker.habits[0].name, "Run")

    def test_longest_streak(self):
        """Test calculates the longest streak for a habit."""
        habit = Habit("cleaning house", "weekly")
        habit.completions = [
            (datetime.now() - timedelta(days=i)).isoformat()
            for i in range(5)  # Five consecutive days
        ]

        streak = longest_streak(habit)
        self.assertEqual(streak, 5)

        # create a gap to break the streak
        habit.completions.append((datetime.now() - timedelta(days=7)).isoformat())
        streak = longest_streak(habit)
        self.assertEqual(streak, 5)  # The streak should remain 5

    def test_habits_by_routine(self):
        """Test separating the  habits by routine."""
        self.tracker.add_habit("exercise", "daily")
        self.tracker.add_habit("plan week", "weekly")
        self.tracker.add_habit("Drink Water", "daily")

        daily_habits = habits_by_routine(self.tracker.habits, "daily")
        weekly_habits = habits_by_routine(self.tracker.habits, "weekly")

        self.assertEqual(len(daily_habits), 2)
        self.assertEqual(len(weekly_habits), 1)

    def test_load_and_save_habits(self):
        """Test loading and saving  given habits."""
        self.tracker.add_habit("Code", "daily")
        self.tracker.save_habits()

        # instantiate a new instance of for loading test.
        new_tracker = HabitTracker(self.test_file)
        self.assertEqual(len(new_tracker.habits), 1)
        self.assertEqual(new_tracker.habits[0].name, "Code")


if __name__ == "__main__":
    unittest.main()
