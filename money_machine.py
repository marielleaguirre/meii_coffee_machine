class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print('''\033[33m
        We accept the following coins:
        Quarters ($0.25), dimes ($0.10)
        nickles ($0.05), pennies ($0.01)\033[m
        ''')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}? Please: ")) * self.COIN_VALUES[coin]
        print(f'You have provided: {self.CURRENCY}{self.money_received}')
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
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