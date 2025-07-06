#let's calculate savings of user
#monthly income & expenses 
income = float(input("Enter your Monthly Income: "))
expense = float (input ("Enter your Monthly Expenses: "))
#savings calculation
saving = income - expense
print("Your Monthly Savings: ", saving)
#classification
if saving >= 10000:
    print ("Saving Well")
elif saving <=9999 and saving >=5000:
    print ("Saving Average")
elif saving <5000:
    print ("Try to Save")