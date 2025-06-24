# CLASS CoffeeMaker:
#     METHOD __init__():
#         SET initial resources: water = 1000ml, milk = 1000ml, coffee = 500g

#     METHOD report():
#         PRINT current amount of water, milk, and coffee

#     METHOD is_resource_sufficient(drink):
#         SET can_make to True
#         FOR each ingredient in drink:
#             IF required amount > available amount:
#                 PRINT "Sorry there is not enough [ingredient]"
#                 SET can_make to False
#         RETURN can_make

#     METHOD make_coffee(order):
#         FOR each ingredient in order:
#             SUBTRACT required amount from resources
#         PRINT cup art with "Here's your [drink name]. Enjoy!"