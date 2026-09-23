# CLI Habit Tracker 🎯

A lightweight, interactive Command Line Interface (CLI) application built in Python to help you log and track your daily habits. 

This project was built to practice core Python concepts, including Object-Oriented Programming (OOP), file I/O operations, and robust error handling.

## ✨ Features

* **Interactive Prompts:** Easily log the name, frequency, and category of your daily habits.
* **Pre-defined Categories:** Categorize habits into specific areas like Health, Productivity, or Social.
* **Data Persistence:** Automatically saves your habits to a local `Habits.txt` file so nothing is lost when the app closes.
* **Crash-Resistant:** Includes `try/except` error handling to gracefully catch invalid user inputs (like typing text when a number is expected) without crashing the program.
* **Clean Formatting:** Reads the raw data from the text file and formats it into a clean, human-readable summary in the terminal.

## 🛠️ Project Structure

* `Habit_tracker.py` - The main script containing the CLI logic, user input handling, and file reading/writing.
* `Habits.py` - Contains the `Habit` class definition to structure the habit data.
* `Habits.txt` - The local text file where the habit data is stored.

## 🚀 How to Run

1. Make sure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.
2. Clone this repository or download the files.
3. Open your terminal or command prompt and navigate to the folder containing the project files.
4. Run the main script:
   ```bash
   python Habit_tracker.py
   ```
5. Follow the on-screen prompts to add a new habit and view your updated list!

## 💡 Future Improvements

* Implement duplicate checking to prevent the same habit from being added twice.
* Upgrade from `.txt` storage to a relational database like SQLite.
* Add a feature to mark habits as "completed" for the current day.