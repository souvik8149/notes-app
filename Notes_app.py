"""
Notes App
---------

A simple command-line notes application written in Python.
Users can add notes and view all saved notes, which are stored in a local text file (notes.txt).

Features:
- Add new notes
- View all saved notes with numbering
- Handles missing file gracefully
- Input validation for menu choice

Author: [Souvik]
"""


def notes_app():
    """
    Command-line Notes App.

    Displays a menu with options to:
    1. Add a note: saves user input to 'notes.txt' (appending).
    2. View notes: reads and displays all notes from 'notes.txt'.
    3. Exit the app.

    Ensures input validation and handles missing notes file gracefully.
    """
    
    print("Welcome to Notes App!")
    print("1. Add a note")
    print("2. View notes")
    print("3. Exit")

    while True:
        while True:
            try:
                choice = int(input("Choose an option 1/2/3: "))
                break
            except ValueError:
                print("Invalid choice!...Please choose a number \n")

        if choice == 1:
            note = input("Enter the note: ").strip()
            with open("notes.txt" , "a") as f:
                f.write(note + "\n")
            print("✅ Note saved!\n")
        
        elif choice == 2:
            print("\nYour notes:")
            try:
                with open("notes.txt" , "r") as f:
                    lines = f.readlines()
                    if not lines:
                        print("📭 No notes yet.")
                    else:
                        for idx , line in enumerate(lines , start=1):
                            print(f"{idx}. {line.strip()}")
            except FileNotFoundError:
                print("📭 No notes yet. (File not found)")
            print()

        elif choice == 3:
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice.Please enter 1/2/3 . \n")


if __name__ == "__main__":
    notes_app()
