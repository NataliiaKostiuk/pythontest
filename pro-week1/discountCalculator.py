# Discount Calculator
# Write a Python function that takes a customer's age and total purchase'
# ' amount as input. Apply discounts based on the following conditions:
# If the customer is a senior citizen (age 60 or above), apply a 15% discount.
# If the purchase amount is above £100 and the customer is not a senior citizen, apply a 10% discount.
# If both conditions apply, only apply the higher discount.

   
def checkDiscount(age, totalPurchase):
    if age >= 60:
      print("Your discount is 15%")
    elif totalPurchase >= 100:
      print("Your discount is 10%")
    else:
      print("Enter correct data") 


age = int(input("Enter your age:  "))
totalPurchase = int(input("Enter your total purchase:  "))

checkDiscount(age, totalPurchase)