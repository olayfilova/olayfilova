import json
import random
from argparse import ArgumentParser
from json import JSONDecodeError


class Trader:
    config = "config.json"
    system = "system.json"

    def __init__(self):
        with open(self.config, "r") as f:
            try:
                config_data = json.load(f)
            except JSONDecodeError:
                config_data = {"delta": 0.5}
            self.delta = config_data.get("delta")

        with open(self.system, "r") as f:
            try:
                self.data = json.load(f)
            except JSONDecodeError:
                self.restart()

        last_act = self.data[-1]
        self.available_UAH = last_act.get("available_UAH")
        self.available_USD = last_act.get("available_USD")
        self.price = last_act.get("rate")

    def update_history(self, act):
        self.data.append({
            "available_USD": self.available_USD,
            "available_UAH": self.available_UAH,
            "rate": self.price,
            "action": act,
        })
        with open(self.system, "w") as f:
            json.dump(self.data, fp=f)

    def rate(self):
        self.update_history("rate")
        return self.price

    def next_price(self):
        self.price = round(random.uniform(self.price - self.delta, self.price + self.delta), 2)
        self.update_history("next")

    def get_available_USD(self):
        self.update_history("check USD")
        return self.available_USD

    def get_available_UAH(self):
        self.update_history("check UAH")
        return self.available_UAH

    def print_available(self):
        print(f"USD: {self.get_available_USD()}")
        print(f"UAH: {self.get_available_UAH()}")

    def print_state(self):
        print(f"price: {self.price}")
        print(f"USD: {self.available_USD}")
        print(f"UAH: {self.available_UAH}")

    def buy_USD(self, amount):
        actual_sum = round(amount * self.price, 2)
        print(actual_sum)
        if actual_sum > self.available_UAH:
            self.update_history("fail buy")
            print(f"Failed operation: Insufficient balance.\nRequired {actual_sum} UAH")
            return
        self.available_UAH -= actual_sum
        self.available_USD += amount
        self.update_history("buy")

    def sell_USD(self, amount):
        if amount > self.available_USD:
            self.update_history("Fail sell")
            print(f"Failed operation: Insufficient balance.\nRequired {amount} USD")
            return
        self.available_UAH += amount * self.price
        self.available_USD -= amount
        self.update_history("sell")

    def buy_all_USD(self):
        if not self.available_UAH:
            self.update_history("Fail buy")
            print("Failed operation: Insufficient balance.")
            return
        actual_sum = round(self.available_UAH / self.price, 2)
        self.available_UAH = 0
        self.available_USD += actual_sum
        self.update_history("Buy all")

    def sell_all_USD(self):
        if not self.available_USD:
            self.update_history("Fail sell")
            print("Failed operation: Insufficient balance.")
            return
        actual_sum = round(self.available_USD * self.price, 2)
        self.available_UAH += actual_sum
        self.available_USD = 0
        self.update_history("Sell all")

    def restart(self):
        self.data = [{"available_USD": 0.0,
                      "available_UAH": 10000.00,
                      "rate": 37.8,
                      "action": "initial",
                      }]
        with open(self.system, "w") as f:
            json.dump(self.data, f)

    def print_history(self):
        for action in self.data:
            print(f"Operation: {action.get('action')}\tRate:{action.get('rate')}\t",
                  f"USD:{action.get('available_USD')}\tUAH: {action.get('available_UAH')}")


args = ArgumentParser()
args.add_argument(dest="main_command", type=str,
                  choices=["NEXT", "RESTART", "HISTORY", "ALL", "BUY", "RATE", "AVAILABLE", "SELL"])
args.add_argument(dest="another_command", nargs="?", type=str, default=0)

args = vars(args.parse_args())

command_action = args["main_command"]
command_amount = args["another_command"]
trader = Trader()

if command_action == "RATE":
    trader.rate()
    trader.print_state()
elif command_action == "NEXT":
    trader.next_price()
    trader.print_state()
elif command_action == "AVAILABLE":
    print("BALANCE: ")
    trader.print_available()
elif command_action == "RESTART":
    print("RESTARTING")
    trader.restart()
    trader.print_state()
elif command_action == "BUY":
    if not command_amount:
        print("UNSUFFICIENT FOUND")
    trader.next_price()
    trader.print_state()
    if command_amount == "ALL":
        trader.buy_all_USD()
        trader.print_state()


    else:
        trader.buy_USD(float(command_amount))
        trader.print_state()
elif command_action == "SELL":

    if not command_amount:
        print("UNSUFFICIANT FOUND")
    if command_amount == "ALL":
        trader.sell_all_USD()
        trader.print_state()
    else:
        trader.sell_USD(float(command_amount))
        trader.print_state()
elif command_action == "HISTORY":
    trader.print_history()
