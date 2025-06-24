from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep
import pygame

pygame.mixer.init()
pygame.mixer.music.load("classical_music.mp3")
pygame.mixer.music.play(-1) 

def welcome():
    print('''\033[33m
             )))
            (((
          +------+
          | .☘︎ ݁˖ |] - WELCOME TO THE MEII COFFEE MACHINE!
          `------' 
    
          ------ MENU ------ 
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------
    
          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    welcome()
    options = menu.get_items()
    user_choice = str(input(f'What would you like?\nOptions ({options}): ')).strip().lower()
    if user_choice == 'off':
        print('\033[31m<<THE END>>\033[m')
        is_on = False

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
