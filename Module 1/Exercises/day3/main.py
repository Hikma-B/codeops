# main.py

from day3.utils import add_tax

price = float(input("Enter the product price: "))

final_price = add_tax(price)

print("Price with tax:", final_price)