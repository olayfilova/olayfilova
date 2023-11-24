##### CLI command line interface #########
# print("world")


from argparse import ArgumentParser

args = ArgumentParser()
args.add_argument("main_command", type=str)  #"RATE", NEXT
args.add_argument("sub_main_command", type=str, default=0)

# args.add_argument("name", type=str)
# args.add_argument("age", type=str, default=0)
# args.add_argument("job", type=str, default="qa")
#
# args = vars(args.parse_args())
# print(args)
# print(args['name'])

#python3 trader.py BUY SELL

# config.json
#         "delta": 0.5
#
# >>>python trade.py NEXT
# >>>python trade.py RATE
# 26.19
# >>>python trade.py BUY 100
# >>>python trade.py AVAILABLE
# USD 100.0 UAH 10000


#####OOP
# наслидування
# инкапсулюция
# декораторы @property
# class Transport:
#
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return "the car"
#
#     def can_do(self):
#         return "Go!"
#
#
# class Radio:
#     pass
#
#
# class Car(Radio, Transport):
#     def __init__(self, model, color):
#         self.model = model
#         super().__init__(color)
#
#     def __repr__(self):
#         return "All night long" + f" {self.color}"
#
#     def __str__(self):
#         return super().__str__() + f", and car model {self.model} "
#
#
# BMW = Car("X5", "white")
# # print(BMW.model)
# # print(BMW.color)
# # print(BMW.can_do())
# print(BMW)
# print(BMW.__repr__())
####

##### incapsulation ####

class Transport:

    def __init__(self, color):
        self.color = color
        self.fuel = self.__get_fuel()   #####incaps


    def __str__(self):
        return "the car"

    def __get_fuel(self):   incaps
        return "Oil"

    def can_do(self):
        return "Go!"


class Radio:
    pass


class Car(Radio, Transport):
    def __init__(self, model, color):
        self.model = model
        super().__init__(color)

    def __repr__(self):
        return "All night long" + f" {self.color}"

    def __str__(self):
        return super().__str__() + f", and car model {self.model} "


BMW = Transport("white")

print(BMW.fuel)

BMW._get_fuel()

####### decorator
@property

class Transport:

    def __init__(self, color):
        self.color = color
        self.fuel = self.__get_fuel()   #####incaps


    def __str__(self):
        return "the car"

    @staticmethod
    def __get_fuel(self):
        return "Oil"

    def can_do(self):
        return "Go!"
@decorator


###############request
#####requests.readthedocs

import requests
responce = request.get("https://www.google.com/search?")
print(responce.status_code)
print(responce.content)

