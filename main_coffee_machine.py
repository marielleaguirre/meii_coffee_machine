from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep
import pygame

# INITIALIZE pygame mixer and play background classical music

# DEFINE welcome() to show greeting and menu

# INITIALIZE core objects:
#    - menu (Menu)
#    - money_machine (MoneyMachine)
#    - coffee_maker (CoffeeMaker)
#    - is_on = True

# WHILE is_on is True:
#    a. Show welcome message
#    b. Ask user for drink choice

#    c. IF input is 'off':
#        - Print shutdown message
#        - Set is_on to False to exit loop

#    d. ELSE IF input is 'report':
#        - Print coffee and money resource reports

#    e. ELSE IF invalid choice:
#        - Show error message

#    f. ELSE:
#        i. Get the drink from menu
#        ii. Check if resources are sufficient
#        iii. Ask for payment
#        iv. If both checks pass:
#            - Simulate coffee brewing with sleep
#            - Make coffee
#            - Show confirmation

# END PROGRAM
