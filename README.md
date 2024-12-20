 # Habit Tracker Project
 
 
 

## Overview

As the name implies, this is a Python Application Project with the primary purpose of tracking the habits. 
It has features to add habits, mark habits as complete, delete habits, and slice and dice streak records and routines. 
This project saves all data to a JSON file so that the user's habits and completions are not lost between sessions.



## Core Functionality


### 1. Add Habit: 
- Enter a new habit, name and schedule it daily/weekly.

### 2.Complete Habit:
- Check off a habit for today/now.

### 3.Delete Habit:
- Delete a habit from the tracker.

### 4.List Habits:
- Get all habits, their names and routines.

### 5.Analyze Habits:

  - Longest Streak: Find out how long you haven’t missed a habit in a row.

   - By Routine: shows all habits categorized by the routine type (Daily or Weekly).

### 6 Data Persistence:

- JSON Database: The JSON file saves all data, and it is persistent and accessible.
### 7. Exit:
- saves the progress and close the application if unwanted.
 # File Structure

## Main Components

- ```habit_tracker.py:```it has the main logic for habit manage and database interaction.

- ```analytics.py:```it utilizes functions to get the longest streak and filtering habits by routine.

- ```db.py:``` it provides functions for dealing with JSON files where we can save and load habit data.

- ```main.py:```it provides the list of habit tracker for user interaction.

- ```data.json:```it is default file where the habit data is stored.

- ```test_habit_tracker.py:``` it contains unit tests and checks that the application behaves as expected.

# How to Run the Project
## Prerequisites:
1. Installation
``` pip install -r requirements.txt```
2. Run the application:
  ```python habit_tracker.py```
3. Follow the on - screen menu options to interact with the Habit Tracker.



# Testing

The project contains unit tests in ```test_habit_tracker. py```files to check availability. 
  
### ```Key test cases include:```
1. Test create new habit.
2. Test mark a habit was done.
3. Test delete a habit which is unrelated.
4. Test separating the habits by routine.
5. Test loading and saving given habit.
6. Test calculates the longest streak and routine  for a habit.
# To run the tests:

 Type the command :```python -m unittest test_habit_tracker. py```

## Example Usage: 
1. Add a habit:
  Habit Name : "Read book",
  Routine: "daily"
2. Mark Habit which was completed:
  Habit Name: "Read book"
3. Analyze Habits:

  - View the longest streak for "read book": display the streak in days.
  
  - View habits by routine " daily": displays all the habits with is on daily routine.





 

# Future Enhancements


- Creates custom routine Where users can set intervals of their own.

- Develops the reminders or notification for uncompleted habits.

## Contact 
For questions or feedback, please open an issue on the repository.

Email: ```prince.devendra1989@gmail.com```
