class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

#     METHOD __init__():
#         SET profit to 0
#         SET money_received to 0

#     METHOD report():
#         PRINT current profit with currency symbol

#     METHOD process_coins():
#         PRINT accepted coin types
#         FOR each coin type in COIN_VALUES:
#             ASK user how many of that coin
#             ADD total value of coins to money_received
#         PRINT total money provided
#         RETURN money_received

#     METHOD make_payment(cost):
#         CALL process_coins()
#         IF money_received >= cost:
#             CALCULATE change
#             PRINT change returned
#             ADD cost to profit
#             RESET money_received to 0
#             RETURN True
#         ELSE:
#             PRINT refund message
#             RESET money_received to 0
#             RETURN False