# TASK 1.
# A fitness tracker recorded the number of steps taken over 10 days.
# The data is stored in a NumPy array:
import numpy as np
# Determine the dimensionality of the array and its shape.
# Retrieve the number of steps taken on the first day and on the last day.
# Find all days when the user walked more than 8000 steps.
steps = np.array([5230, 8120, 4300, 9100, 10020, 6500, 7200, 4000, 11000, 9800])

print(f"Array dimension: {steps.ndim}")
print(f"Array shape: {steps.shape}")
print(f"Number of steps on first day: {steps[0]} ; last day: {steps[-1]}")
print(f"Days when user walked more than 8k steps: {steps[steps > 8000]}")

# TASK 2
# The array contains students exam scores:
# grades = np.array([45, 78, 82, 59, 91, 67, 73, 50, 88]).
# Find all scores greater than 80.
# Create a new array containing the scores of students who passed the exam (score ≥ 60).
# Find the indexes of the students who failed the exam (score < 60).
# Retrieve the scores of the first four students.
grades = np.array([45, 78, 82, 59, 91, 67, 73, 50, 88])

print(f"All scores greater than 80: {grades[grades > 80]}")
print(f"New array of students passing exams: {grades[grades > 60]}")
print(f"Indexes of failed students: {np.where(grades < 60)}")
print(f"Scores of first 4 students: {grades[0:4]}")
# TASK 3
# The array contains sales data for three stores over five days:
sales = np.array([[200, 220, 210, 240, 260], [180, 190, 200, 210, 230], [150, 160, 170, 180, 190]])
# Retrieve the sales of the first store for all days.
print(sales[0])
print(sales[0][:])
print(sales[0][::])
print(sales[0][0:5])
# Find the total sales that greater than 220.
print(sales[sales > 220])
# Retrieve the sales of all stores on the first day.
print(sales[:,0])
# Retrieve the sales of the second store for the last two days.
print(sales[:,3:5])