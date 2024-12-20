from datetime import datetime
def longest_streak(habit):
    """calculates a current streak for a habit.
    """

    if not habit.completions:
        return 0 # No completions, so streak is 0


# convert completion time series into datetime objects and sort them for easier analysis.
    completions = sorted([datetime.fromisoformat(dt) for dt in habit.completions])
    streak = 1
    max_streak = 1

    for i in range(1, len(completions)):
        # check if the current completion is next day of the previous completion.
        if (completions[i] - completions[i-1]).days <=1:
            streak += 1
            max_streak = max(max_streak, streak )
        else:
            streak = 1
    return max_streak

def habits_by_routine(habits, routine):
    """separates the habits according  to the routine.
    """
    return[habit for habit in habits if habit.routine == routine]