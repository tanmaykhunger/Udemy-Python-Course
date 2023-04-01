# TanmayPizza.py
number_of_pizzas = eval(input("How many pizzas do you want? "))
cost_per_pizza = eval(input("How much does each pizza cost? "))
subtotal = number_of_pizzas * cost_per_pizza
pay_for_delivery = eval(input("What is the cost of delivery? "))
payment = subtotal + pay_for_delivery
print("The total cost you have to pay is ₹", payment)