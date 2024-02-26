#iterative approach
import random  # Import the random module for shuffling the chocolates
def iterative(chocolates, students):
    # Get the counts of chocolates and students
    chocolate_count = len(chocolates)
    student_count = len(students)

    # Check if there are enough chocolates for all students
    if chocolate_count < student_count:
        print("Not enough chocolates to distribute to all students.")
        return None

    # Make a copy of chocolates list to avoid modifying the original list
    chocolates_copy = chocolates[:]  # Use list slicing to create a shallow copy

    # Shuffle chocolates to ensure random distribution
    random.shuffle(chocolates_copy)  # Shuffle the chocolates randomly

    # Iterate through students and assign each a distinct chocolate
    for i, student in enumerate(students):  # Use enumerate to get both index and value
        if i < chocolate_count:  # Check if there are enough chocolates for all students
            print(f"{student} gets chocolate: {chocolates_copy[i]}")
        else:
            print(f"{student} gets no chocolate.")  # Print if no chocolates are left


# Test the iterative distribution function
# Test case 1: Small chocolate and student lists
chocolates_1 = [("Dark", 50, 2), ("Milk", 30, 1)]
students_1 = ["Shaikha", "Maryam"]
iterative(chocolates_1, students_1)

# Test case 2: Equal number of chocolates and students
chocolates_2 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
students_2 = ["Shaikha", "Maryam", "Alex"]
iterative(chocolates_2, students_2)

# Test case 3: More students than chocolates
chocolates_3 = [("Dark", 50, 2), ("Milk", 30, 1)]
students_3 = ["Shaikha", "Maryam", "Alex", "Lyla", "Hourya"]
iterative(chocolates_3, students_3)



#recursive
def recursive(chocolates, students, choco_index=0, student_index=0):
    # Get the counts of chocolates and students
    chocolate_count = len(chocolates)
    student_count = len(students)

    # Base case: If all students have received chocolates
    if student_index >= student_count:
        return

    # Print the distribution of chocolate to the current student
    if choco_index < chocolate_count:  # If there are chocolates left
        print(f"{students[student_index]} gets chocolate: {chocolates[choco_index]}")
    else:
        print(f"{students[student_index]} gets no chocolate.")

    # Recursive call to distribute chocolates to the next student and chocolate
    recursive(chocolates, students, choco_index + 1, student_index + 1)


# Test case 1: Small chocolate and student lists
chocolates_1 = [("Dark", 50, 2), ("Milk", 30, 1)]
students_1 = ["Hessa", "Noura"]
recursive(chocolates_1, students_1)

# Test case 2: Equal number of chocolates and students
chocolates_2 = [("Dark", 50, 2), ("Milk", 30, 1), ("White", 40, 3)]
students_2 = ["Hessa", "Noura", "Hind"]
recursive(chocolates_2, students_2)

# Test case 3: More students than chocolates
chocolates_3 = [("Dark", 50, 2), ("Milk", 30, 1)]
students_3 = ["Hessa", "Noura", "Hind", "Aysha", "Maryam"]
recursive(chocolates_3, students_3)

