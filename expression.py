# for inline
# any
# sum

class Pizza:

    def __init__(self, name, price):
        self.name = name
        self.price = price


pizzas = [
    Pizza("Test", 12),
    Pizza("Test2", 13),
    Pizza("Test3", 19)
]

"""list_pizzas = []
    for pizza in pizzas:
        list_pizzas.append(pizza.name)"""

# ITERATE IN  1 LINE USING for loop
list_pizzas = [pizza.name for pizza in pizzas]
print(list_pizzas)

# VERIFY IF ELEMENT IS True or False USING ANY
expensive_pizzas = any([pizza.price > 13 for pizza in pizzas])
print(expensive_pizzas)

# COUNT SUM OF ELEMENT IN LIST -- SUM OF PIZZAS > 13$
sum_pizzas = sum([1 for pizza in pizzas if pizza.price > 13])
print(sum_pizzas)
print(sum([10, 10, 10]))
