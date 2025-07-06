#let's code a billing system 
product = int(input("No. Of Products: "))
price = float(input ("Total Price: "))
#now apply discount 
if price > 1000 and product > 3:
    discount = price * 0.15
    final_price = price - discount 
    print ("You got 15% OFF")
    print ("Final Price after Discount = ", final_price)
elif  price > 500:
    discount = price * 0.10
    final_price = price - discount 
    print ("You got 10% OFF ")
    print ("Final Price after Discount = ", final_price)
else: 
    
    print ("No Discount applied ", price)