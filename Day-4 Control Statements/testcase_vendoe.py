# Q.4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

# //Code

# Sub function with parametrs
def calculate_discount(product_code, order_amount):
    discount = 0
    # if condition to check the every condition
    if product_code == 1 and order_amount > 1000:
        discount = 0.1
    elif product_code == 2 and order_amount > 100:
        discount = 0.05
    elif product_code == 3 and order_amount > 500:
        discount = 0.1
    # Substracting the total amount with discounted amount
    discounted_amount = order_amount - (order_amount * discount)
    return discounted_amount

# MAin Function
def main():
    # Taking an input 
    product_code = int(input("Enter product code (1 for Battery Based Toys, 2 for Key-based Toys, 3 for Electrical Charging Based Toys): "))
    order_amount = float(input("Enter order amount in Rs.: "))
    # Calling the function
    net_amount = calculate_discount(product_code, order_amount)
    # print the result
    print("Net amount after discount: Rs.", net_amount)

main()