#calculate percentage and assign grades
sub1 = float(input ("Enter Maths marks: "))
sub2 = float(input ("Enter English marks: "))
sub3 = float(input ("Enter Biology marks: "))
Total_marks = sub1 + sub2 + sub3
print("Total marks = ", Total_marks)
Percentage = (Total_marks / 300) * 100
print ("Percentage Obtained = " , Percentage)
#now let's assign grades 
if Percentage >= 85:
    print("Grade A")
elif Percentage >= 70:
    print ("Grade B")
elif Percentage >= 50:
    print ("Grade C")
else:
    print ("Grade F")