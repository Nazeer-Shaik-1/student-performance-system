# Student Performance Management System using Dictionary

# Initialize empty dictionary to store student records
students = {}

# Function to add a new student
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Student Name: ")
    students[roll] = {'name': name, 'marks': {}}
    print(f"Student {name} added successfully.")

# Function to add marks to an existing student
def add_marks():
    roll = input("Enter Roll Number: ")
    if roll not in students:
        print("Student not found.")
        return
    subject = input("Enter Subject Name: ")
    marks = int(input("Enter Marks: "))
    students[roll]['marks'][subject] = marks
    print(f"Marks added for {subject}.")

# Function to update marks
def update_marks():
    roll = input("Enter Roll Number: ")
    if roll not in students:
        print("Student not found.")
        return
    subject = input("Enter Subject to Update: ")
    if subject not in students[roll]['marks']:
        print("Subject not found.")
        return
    marks = int(input("Enter New Marks: "))
    students[roll]['marks'][subject] = marks
    print(f"Marks updated for {subject}.")

# Function to delete a student
def delete_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

# Function to display all students
def display_students():
    if not students:
        print("No records found.")
        return
    for roll, details in students.items():
        print(f"Roll No: {roll}, Name: {details['name']}, Marks: {details['marks']}")

# Function to find topper in a subject
def subject_topper():
    subject = input("Enter Subject: ")
    topper = None
    top_marks = -1
    for student in students.values():
        marks = student['marks'].get(subject)
        if marks is not None and marks > top_marks:
            top_marks = marks
            topper = student['name']
    if topper:
        print(f"Topper in {subject}: {topper} with {top_marks} marks.")
    else:
        print("No marks found for this subject.")

# Function to find overall topper
def overall_topper():
    topper = None
    max_total = -1
    for student in students.values():
        total = sum(student['marks'].values())
        if total > max_total:
            max_total = total
            topper = student['name']
    if topper:
        print(f"Overall Topper: {topper} with total {max_total} marks.")
    else:
        print("No records found.")

# Function to show average marks per student
def average_marks():
    for student in students.values():
        marks = student['marks'].values()
        if marks:
            avg = sum(marks) / len(marks)
            print(f"{student['name']}'s Average: {avg:.2f}")
        else:
            print(f"{student['name']} has no marks entered.")

# Function to sort students by total marks
def sort_by_total():
    totals = {}
    for roll, student in students.items():
        totals[roll] = sum(student['marks'].values())
    sorted_students = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    print("Students sorted by total marks:")
    for roll, total in sorted_students:
        print(f"Roll: {roll}, Name: {students[roll]['name']}, Total Marks: {total}")

# Main Menu
def main_menu():
    while True:
        print("\n===== Student Management Menu =====")
        print("1. Add Student")
        print("2. Add Marks")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Topper in Subject")
        print("7. Overall Topper")
        print("8. Average Marks")
        print("9. Sort by Total Marks")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_marks()
        elif choice == '3':
            update_marks()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_students()
        elif choice == '6':
            subject_topper()
        elif choice == '7':
            overall_topper()
        elif choice == '8':
            average_marks()
        elif choice == '9':
            sort_by_total()
        elif choice == '0':
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice, try again.")

#  Run the program
if __name__ == "__main__":
    main_menu()
