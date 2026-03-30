# Function to determine grade based on marks
def grade(marks):
    """
    This function takes marks as input
    and returns the corresponding grade.
    """

    # Validate marks range (basic input validation)
    if marks < 0 or marks > 100:
        return "Invalid marks"

    # Check conditions for grading
    if marks >= 90:
        return "A"   # Grade A for 90 and above
    elif marks >= 75:
        return "B"   # Grade B for 75–89
    elif marks >= 50:
        return "C"   # Grade C for 50–74
    else:
        return "Fail"  # Fail for below 50


# ---------------- MAIN PROGRAM ----------------

# Take input from user
marks = int(input("Enter marks: "))

# Call the function and store result
result = grade(marks)

# Display the grade
print("Grade:", result)