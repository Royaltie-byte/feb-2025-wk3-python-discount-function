#The function that calculates the discount.
def calculate_discount(price , discount_percentage):
    if discount_percentage < 20.0:
        result= price
    else:
        discount= price * (discount_percentage/100.0)
        result=price - discount
    return result


#user input
price= float(input( "Enter the original price of the item : "))
discount=float(input("Enter the discount percentage  for the item : "))
print("Final price :" ,calculate_discount(price , discount))
