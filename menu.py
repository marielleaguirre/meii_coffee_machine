class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

#     METHOD get_items():
#         SET options to an empty string
#         FOR each item in the menu:
#             ADD item name and a slash to options
#         RETURN options

#     METHOD find_drink(order_name):
#         FOR each item in the menu:
#             IF item name matches order_name:
#                 RETURN that item
#         PRINT "Sorry that item is not available."
