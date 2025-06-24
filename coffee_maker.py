class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 500,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

#     METHOD make_coffee(order):
#         FOR each ingredient in order:
#             SUBTRACT required amount from resources
#         PRINT cup art with "Here's your [drink name]. Enjoy!"