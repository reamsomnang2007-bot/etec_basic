print("----------[ Input ]----------")
code = input("Enter code: ")
product_name = input("Enter Product_Name: ")
qty = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))
print("-----------------------------")

total = qty * price
discount = 0
if total < 10:
    discount = 0
elif total < 20:
    discount = 5
elif total < 30:
    discount = 10
elif total < 40:
    discount = 20
elif total > 40:
    discount = 30

payment = total - (total * discount / 100)

print("----------[ Output ]----------")
print(f"Code: {code}")
print(f"Product_Name: {product_name}")
print(f"Quantity: {qty}")
print(f"Price : {price}")
print(f"Total: {total}")
print(f"Discount: {discount}")
print(f"Payment: {payment}")
print("------------------------------")