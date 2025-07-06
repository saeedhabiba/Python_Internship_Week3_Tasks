#let's create calculator 
num1 = (float(input ("Enter first number: ")))
num2 = (float(input ("Enter second number: ")))
operator = input("Enter any operator: ")

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '/':
    if num2 != 0:
      print (num1/num2)
    else:
      print("Error")
elif operator == '*':
    print(num1 * num2)
elif operator== '':
    print (num1 ** num2)
elif operator == '//':
    print(num1 // num2)
elif operator == '%':
    print (num1 % num2)