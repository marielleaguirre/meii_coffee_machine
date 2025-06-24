class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

# CLASS Menu:
#     METHOD __init__():
#         CREATE a list of MenuItem objects: latte, espresso, cappuccino

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
