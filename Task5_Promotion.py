#let's promote students 
percentage = float(input("Enter your Attendance Percentage: "))
final_marks = float(input("Enter your Final Marks: "))
#criteria tu promote
if percentage >= 75 and final_marks >=50:
    print("..Congratulations! You are promoted to Next Semester..")
else: 
    print ("Promotion Denied ")