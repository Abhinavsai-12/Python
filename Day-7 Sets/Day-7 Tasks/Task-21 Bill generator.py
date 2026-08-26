
print("====================================")
print("       SUPER MARKET")
print("      BILL GENERATION")
print("====================================")


# Customer Details

customer_name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")

print("\nWelcome", customer_name)


# Product List

products = [
    ("Rice", 60),
    ("Sugar", 45),
    ("Milk", 30),
    ("Bread", 40),
    ("Oil", 120)
]


# Display Products

print("\nAvailable Products")
print("----------------------------")

for i in range(len(products)):
    print(i + 1, products[i][0], "- Rs.", products[i][1])


# Shopping Cart

cart = []

while True:

    print("\nEnter 0 to finish shopping")

    choice = int(input("Enter product number: "))

    if choice == 0:
        break

    if choice < 1 or choice > len(products):
        print("Invalid product number")
        continue

    product_name = products[choice - 1][0]
    price = products[choice - 1][1]

    quantity = int(input("Enter quantity: "))

    total = price * quantity

    cart.append((product_name, price, quantity, total))

    print(product_name, "added to cart")


# Generate Bill

print("\n")
print("==============================================")
print("              SUPER MARKET BILL")
print("==============================================")

print("Customer Name :", customer_name)
print("Mobile Number :", mobile)

print("----------------------------------------------")
print("Product\tPrice\tQty\tTotal")
print("----------------------------------------------")


grand_total = 0

for item in cart:

    product_name = item[0]
    price = item[1]
    quantity = item[2]
    total = item[3]

    print(product_name, "\t", price, "\t", quantity, "\t", total)

    grand_total = grand_total + total


# Discount

if grand_total >= 1000:
    discount = grand_total * 10 / 100
elif grand_total >= 500:
    discount = grand_total * 5 / 100
else:
    discount = 0


# Final Amount

final_amount = grand_total - discount


# Bill Summary

print("----------------------------------------------")

print("Grand Total :", grand_total)
print("Discount    :", discount)
print("Final Amount:", final_amount)

print("----------------------------------------------")

print("Thank you", customer_name)
print("Visit Again!")

print("==============================================")