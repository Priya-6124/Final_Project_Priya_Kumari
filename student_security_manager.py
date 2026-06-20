import os

FILE_NAME = "students.txt"


# ==========================
# FILE HANDLING FUNCTIONS
# ==========================

def load_students():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 6:
                    students.append({
                        "id": data[0],
                        "name": data[1],
                        "branch": data[2],
                        "email": data[3],
                        "score": int(data[4]),
                        "status": data[5]
                    })

    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"{student['id']}|"
                f"{student['name']}|"
                f"{student['branch']}|"
                f"{student['email']}|"
                f"{student['score']}|"
                f"{student['status']}\n"
            )


# ==========================
# MODULE 1 ADD STUDENT
# ==========================

def add_student(students):

    print("\nADD STUDENT")

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    email = input("Enter Email: ")

    student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "email": email,
        "score": 0,
        "status": "Not Assessed"
    }

    students.append(student)

    save_students(students)

    print("Student Added Successfully!")


# ==========================
# MODULE 2 VIEW STUDENTS
# ==========================

def view_students(students):

    print("\nALL STUDENTS")

    if len(students) == 0:
        print("No Records Found")
        return

    for student in students:

        print("-" * 40)
        print("ID      :", student["id"])
        print("Name    :", student["name"])
        print("Branch  :", student["branch"])
        print("Email   :", student["email"])
        print("Score   :", student["score"])
        print("Status  :", student["status"])


# ==========================
# MODULE 3 SEARCH STUDENT
# ==========================

def search_student(students):

    print("\nSEARCH STUDENT")

    choice = input("Search By (1-ID / 2-Name): ")

    keyword = input("Enter Search Value: ")

    found = False

    for student in students:

        if choice == "1" and student["id"] == keyword:
            found = True

        elif choice == "2" and student["name"].lower() == keyword.lower():
            found = True

        else:
            continue

        print("\nRecord Found")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Email:", student["email"])

    if not found:
        print("Student Not Found")


# ==========================
# MODULE 4 DELETE STUDENT
# ==========================

def delete_student(students):

    student_id = input("Enter Student ID to Delete: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            print("Student Deleted Successfully")
            return

    print("Student Not Found")


# ==========================
# MODULE 5 SECURITY ASSESSMENT
# ==========================

def security_assessment(students):

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            score = 0

            mfa = input("Is MFA Enabled? (yes/no): ")

            if mfa.lower() == "yes":
                score += 30

            password_length = int(
                input("Password Length: ")
            )

            if password_length >= 12:
                score += 30
            elif password_length >= 8:
                score += 20

            update = input(
                "System Updated? (yes/no): "
            )

            if update.lower() == "yes":
                score += 20

            antivirus = input(
                "Antivirus Installed? (yes/no): "
            )

            if antivirus.lower() == "yes":
                score += 20

            if score >= 90:
                status = "Excellent"

            elif score >= 70:
                status = "Good"

            elif score >= 50:
                status = "Moderate"

            else:
                status = "Poor"

            student["score"] = score
            student["status"] = status

            save_students(students)

            print("\nSecurity Score:", score)
            print("Status:", status)

            return

    print("Student Not Found")


# ==========================
# MODULE 6 REPORT
# ==========================

def generate_report(students):

    print("\nSECURITY REPORT")

    total_students = len(students)

    total_score = 0

    poor_students = []

    for student in students:

        total_score += student["score"]

        if student["status"] == "Poor":
            poor_students.append(student["name"])

    average_score = 0

    if total_students > 0:
        average_score = total_score / total_students

    print("Total Students :", total_students)
    print("Average Score  :", round(average_score, 2))

    print("\nStudents With Poor Security:")

    if len(poor_students) == 0:
        print("None")

    else:
        for name in poor_students:
            print(name)


# ==========================
# CYBER SECURITY FEATURE 1
# PASSWORD CHECKER
# ==========================

def password_strength_checker():

    password = input("Enter Password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if score == 4:
        print("Strong Password")

    elif score >= 2:
        print("Medium Password")

    else:
        print("Weak Password")


# ==========================
# CYBER SECURITY FEATURE 2
# USERNAME GENERATOR
# ==========================

def username_generator():

    name = input("Enter Full Name: ")

    username = name.lower().replace(" ", "") + "123"

    print("Generated Username:", username)


# ==========================
# CYBER SECURITY FEATURE 3
# LOGIN VALIDATION
# ==========================

def login_validation():

    username = "admin"
    password = "Admin123"

    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:
        print("Login Successful")

    else:
        print("Invalid Credentials")


# ==========================
# MAIN MENU
# ==========================

def main():

    students = load_students()

    while True:

        print("\n")
        print("=" * 35)
        print(" STUDENT SECURITY MANAGER ")
        print("=" * 35)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Security Assessment")
        print("6. Generate Report")
        print("7. Password Strength Checker")
        print("8. Username Generator")
        print("9. Login Validation")
        print("10. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            security_assessment(students)

        elif choice == "6":
            generate_report(students)

        elif choice == "7":
            password_strength_checker()

        elif choice == "8":
            username_generator()

        elif choice == "9":
            login_validation()

        elif choice == "10":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


main()
