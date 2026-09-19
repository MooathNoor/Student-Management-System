name = input("Enter your name: ")
age = int(input("Enter your age: "))
specialization = input("Enter your specialization: ")

mark1 = float(input("Enter your mark1: "))
mark2 = float(input("Enter your mark2: "))
mark3 = float(input("Enter your mark3: "))
mark4 = float(input("Enter your mark4: "))
mark5 = float(input("Enter your mark5: "))

average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

if average >= 50:
    status = "Passed"
else:
    status = "Failed"

student = {
    "Name": name,
    "Age": age,
    "Specialization": specialization,
    "Average": average,
    "Status": status,
    "Marks": [mark1, mark2, mark3, mark4, mark5]
}

highest_mark = max(student["Marks"])
lowest_mark = min(student["Marks"])
number_of_marks = len(student["Marks"])
sorted_marks = sorted(student["Marks"])

student["Highest Mark"] = highest_mark
student["Lowest Mark"] = lowest_mark
student["Number of Marks"] = number_of_marks
student["Sorted Marks"] = sorted_marks

print("\nStudent Information:")

for key in student:
    print(key, ":", student[key])