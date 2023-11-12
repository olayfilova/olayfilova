#тут два задания: Bla-bla;
#                 и внизу основное: min, max, average
#

#
# my_str ="bla Bla car"
# # my_list = []
# # for char in my_str.lower():
# #     if char not in my_list:
# #         my_list.append(char)
# # result = len(my_list)
# #
# # print(result)
#
# # my_str ="bla Bla car"
# # tmp_list = list(my_str.lower())
# # my_list = []
# # while len(tmp_list) !=0:
# #     symbol =tmp_list.pop()
# #     if symbol not in my_list:
# #         my_list.append(symbol)
# # print(len(my_list))
#
# # my_str ="bla Bla car"
# # tmp_list = list(my_str.lower())
# # my_list = []
# # while len(tmp_list) !=0:
# #     symbol =tmp_list.pop()
# #     if symbol not in my_list:
# #         my_list.append(symbol)
# # print(my_list)
#
# # my_str ="bla Bla car"
# # my_list = []
# #
# # letter = my_str[1::2]
# # for letter in my_str[::2]:
# #
# #     my_list.append(letter)
# # print(my_list)
#
# # my_str ="bla Bla car"
# # index_str = [0, 2, 4, 4, 8]
# # my_list = []
# #
# # for i in index_str:
# #     if i <= len(my_str) and i > 0:
# #         my_list.append(my_str[i])
# # print(my_list)
#
#
# # my_num =1213456
# #
# # print(len(str(my_num)))
#
#
# # my_num = str(12134568)
# # check_num = 9
# # while True:
# #     if str(check_num) in my_num:
# #         break
# #     check_num -= 1
# #
# # print(check_num)
#
# # my_num = 1213456
# # new_num = str(my_num)[::-1]
# # print(new_num)
#
# # my_num = 91213456
# # # sort ="".join(sorted(str(my_num)))
# # sort ="".join(sorted(str(my_num), reverse=True))
# # print(sort)
#
# # my_num = 1213456
# # maxim = max(str(my_num))
# # print(maxim)
#
# # my_list_1 = [1,2,3,5]
# # my_list_2 = [10,20,30,50]
# # my_res = []
# # for i in range(len(my_list_1)) and range(len(my_list_2)):
# #     my_res.append((my_list_1)[i])
# #     my_res.append((my_list_2)[i])
# # print(my_res)

# my_list_1 = [1,2,3,5]
# my_list_2 = [10,20,30,50,60]
# my_res = []
# for i in range(len(my_list_1)) and range(len(my_list_2)):
#     my_res.append((my_list_1)[i:])
#     my_res.append((my_list_2)[i:])
# print(my_res)
#
# my_list_1 = [1,2,3,5]
# my_list_2 = [10,20,30,50,60]
# my_res = []
# min_len = min(len(my_list_1), len(my_list_2))
# i =0
# while i< min_len:
#     my_res.append(my_list_1[i])
#     my_res.append(my_list_2[i])
#     i+=1
# my_res.extend(my_list_1[i:])
# my_res.extend(my_list_2[i:])
# print(my_res)
# # --------------------------------------------------------------------------------------------------

# #------------------------------------------------------------------------------------------------------
# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.
#
# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".
#
# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
#
# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# в) Порахувати середню вік усіх людей із початкового списку.
#
#
#
# i = "good"
# 1
# my_list = ["i'm not", "qwe", "ry", "to", "not"]
# new_list =[]
# for i in range(len(my_list)):
#     # print(i)
#     if i % 2 != 0:
#         # print(i)
#         res = my_list[i] [::-1]
#         # print(res)
#     else:
#         res = my_list[i]
#         # print(res)
#     # new_list =[]
#     new_list.append(res)
#
# # new_list =[]
# # new_list.append(res)
# print(new_list)


# 2
# my_list = ["even", 'thou', 'a', 'arranged', "attributes", "and"]
# new_list = []

#2.1
# for i in my_list:
#     if i.startswith("a"):
#         new_list.append(i)
# print(new_list)

#2.2
# new_list =[i for i in my_list if i.startswith("a")]
# print(new_list)

#2.3
# for i in my_list:
#     if i[0] == "a":
#         new_list.append(i)
# print(new_list)



# 3
# my_list = ["even", 'thou', 'a', "hallo", "that is", "easy", 'arranged', "attributes", "and"]
# new_list = []
#
# for i in my_list:
#     if "a" in i:
#         new_list.append(i)
# print(new_list)

# 4
# my_list= [{"name": "John", "age": 15},
#           {"name": "John", "age": 30},
#           {"name": "maria", "age": 45},
#           {"name": "maria", "age": 15},
#           {"name": "David", "age": 25},
#           {"name": "John", "age": 55},
#           ]
# new_list =[]
# age = []
# age_min = []
# name = []
# long_name = []
# mid_age =[]
# person, *tmp= my_list

#a

# for person in my_list:
#     age.append(person["age"])
# # print(age)
# a = min(age)
# # print(a)
# for person in my_list:
#     if str((person["age"])) == str(a):
#         age_min.append(person["age"])
# print(age_min)

#b

# for person in my_list:
#     name.append(person["name"])
# # print(name)
#
# a = len(max(name))
#
# for person in my_list:
#     if len(person["name"]) == a :
#         long_name.append(person["name"])
# print(long_name)


#c
# for person in my_list:
#     age.append(person["age"])
# a =sum(age)/ len(age)
#     # mid_age =sum(age.append(person["age"])) // len(my_list)
#
# print(a)

#5
dict_1 = {
    "name": "George",
    "family_name": "Habchi",
    "name": "George",
    "family_name": "Habchi"
          }
dict_2 ={
    "name": "Kevin",
    "email": "habchi_work@gmail.com",
    "address": "California",
         }

###a
# res = [key for key in dict_1 if key in dict_2]
# print(res)
###b
# res = [key for key in dict_1 if key not in dict_2]
# print(res)

###c смотрела разбор дз - сама не сообразила, откровенно :)

# dict_3 = {}
#
# for key in dict_1.keys():
#    if key not in dict_2:
#     dict_3[key] = dict_1[key]
# print(dict_3)


# dict_3={key: dict_1[key] for key in dict_1 if key not in dict_2}
# print(dict_3)

###d
# for key in dict_1:
#     if key not in dict_2:
#         dict_2[key] = dict_1[key]
# # print(dict_2)
#     elif key in dict_2:
#         dict_2[key] = [dict_1[key], dict_2[key]]
# print(dict_2)


















