HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

studentStatus = str(input('Your Status: '))

# Prints an Error Message if status isn't UG, G, or DL. Otherwise, it reads scores from input
if studentStatus != "UG" and studentStatus != "G" and studentStatus != "DL":
    print("Error: student status must be UG, G or DL")
else:
    homeworkPoints = float(input("Homework Score: "))
    quizPoints = float(input("Quiz Score: "))
    midtermScore = float(input("Midterm Score: "))
    finalScore = float(input("Final Exam Score: "))

# This calculates the average as a percentage
HW_Average = homeworkPoints / HOMEWORK_MAX * 100
QP_Average = quizPoints / QUIZZES_MAX * 100
MS_Average = midtermScore / MIDTERM_MAX * 100
FS_Average = finalScore / FINAL_MAX * 100

# This defaults the average to 100 if it is over 100
if HW_Average > 100:
    HW_Average = 100
if QP_Average > 100:
    QP_Average = 100
if MS_Average > 100:
    MS_Average = 100
if FS_Average > 100:
    FS_Average = 100

# This dictionary is representing the table so I can pull values from it
UG_dict = {'Homework': 0.2, "Quizzes": 0.2, "Midterm": 0.3, "Final": 0.3}
G_dict = {'Homework': 0.15, "Quizzes": 0.05, "Midterm": 0.35, "Final": 0.45}
DL_dict = {'Homework': 0.05, "Quizzes": 0.05, "Midterm": 0.40, "Final": 0.50}

# This calculates the course average for each student status
if studentStatus == "UG":
    UG_HW = HW_Average * UG_dict["Homework"]
    UG_QP = QP_Average * UG_dict["Quizzes"]
    UG_MS = MS_Average * UG_dict["Midterm"]
    UG_FS = FS_Average * UG_dict["Final"]
    UG_Average = UG_FS + UG_MS + UG_QP + UG_HW
elif studentStatus == "G":
    G_HW = HW_Average * G_dict["Homework"]
    G_QP = QP_Average * G_dict["Quizzes"]
    G_MS = MS_Average * G_dict["Midterm"]
    G_FS = FS_Average * G_dict["Final"]
    G_Average = G_FS + G_MS + G_QP + G_HW
elif studentStatus == "DL":
    DL_HW = HW_Average * DL_dict["Homework"]
    DL_QP = QP_Average * DL_dict["Quizzes"]
    DL_MS = MS_Average * DL_dict["Midterm"]
    DL_FS = FS_Average * DL_dict["Final"]
    DL_Average = DL_FS + DL_MS + DL_QP + DL_HW

# This prints out the values
print(f"Homework: {HW_Average:.1f}%")
print(f"Quizzes: {QP_Average:.1f}%")
print(f"Midterm: {MS_Average:.1f}%")
print(f"Final: {FS_Average:.1f}%")

# This prints a letter grade depending on what the average was for each student status
if studentStatus == "UG":
    print(f"UG Average: {UG_Average:.1f}%")
    if UG_Average >= 90:
        print('Course Grade: A')
    elif UG_Average >= 80 and UG_Average < 90:
        print('Course Grade: B')
    elif UG_Average >= 70 and UG_Average < 80:
        print('Course Grade: C')
    elif UG_Average >= 60 and UG_Average < 70:
        print('Course Grade: D')
    else:
        print("Course Grade: F")
elif studentStatus == "G":
    print(f"G Average: {G_Average:.1f}%")
    if G_Average >= 90:
        print('Course Grade: A')
    elif G_Average >= 80 and G_Average < 90:
        print('Course Grade: B')
    elif G_Average >= 70 and G_Average < 80:
        print('Course Grade: C')
    elif G_Average >= 60 and G_Average < 70:
        print('Course Grade: D')
    else:
        print("Course Grade: F")
elif studentStatus == "DL":
    print(f"DL Average: {DL_Average:.1f}%")
    if DL_Average >= 90:
        print('Course Grade: A')
    elif DL_Average >= 80 and DL_Average < 90:
        print('Course Grade: B')
    elif DL_Average >= 70 and DL_Average < 80:
        print('Course Grade: C')
    elif DL_Average >= 60 and DL_Average < 70:
        print('Course Grade: D')
    else:
        print("Course Grade: F")


