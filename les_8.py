# val_list = [1, 2, "hello and and", "extra", "and", "more"]

# # val_1, val_2, val_3 = val_list
# #
# # print(val_1, val_2, val_3)
#
# # val_1, val_2, val_3 = val_list[:3]
# #
# # print(val_1, val_2, val_3)
#
# val_1, val_2, val_3, *tmp = val_list ####tmp, *tmp
#
# print(val_1, val_2, val_3)
#
# val_1, val_2, val_3, *tmp = val_list
#
# print(val_1, val_2, val_3, tmp)
#
# print(val_list) ### with temples
# print(*val_list)### as list


# val_list = [1, 2, "hello and and", "extra", "and", "more"]
# request_list = ["", "", ""]
# if len(request_list) >3:
#     val_1, val_2, val_3, *tmp = request_list
#     ## add a honeypot - error to user, tryed to hack
# else:
#     val_1, val_2, val_3 = request_list

###dict
# val_dict = {}

# val_dict = {"key": "val",
#             "key1": "val",
#             "key2": "val",
#             1:3,
#
#
#             # (1, 2):3 ## very rare
#             # 1.2 :3
#             # True :3
#             # None:3
#             }
address ={
    "country":"USA",
     "city":"New York",
}
person ={
    "first name":"Maria",
    "second_name":"Antouan",
    "date of birth":"12.12.1900",
    "pass":"11111111",
    "email": "",
    "address":address,
}
# print(person["first name"])
# print(person["date of birth"])
# print(person)

# print(person, ["address"])
# print(person, ["address"], ["city"])

person_3={
    "first name":"Maria",
    "second_name":"Antouan",
    "date of birth":"12.12.1900",
    "pass":"11111111",
    "email": "",
    "address":address,
}
person_1 ={
    "first name":"gMadre",
    "second_name":"Antouan",
    "date of birth":"12.12.1900",
    "pass":"11111111",
    "email": "",
    "address":address,
}

person_2 ={
    "first name":"pAdre",
    "second_name":"Antouan",
    "date of birth":"12.12.1900",
    "pass":"11111111",
    "email": "",
    "address":address,
}

group_person = [person, person_1, person_2, person_3] ### list- easy to add to list data,
#group_person =()# tulple^ when constante data^ example keys, date of birth, address

# val = "12345"
# for i in enumerate(val):
#     print(i)

# print([group_person])


# for_ in range(10):#### _ignoring var
# print("hello")

# for i in person_2:
#     print(i)

# the same
# for key in person_2:
#     print(key)
#
# for key in person_2:
#     print(key, person_2[key])
#
# for key in person_2:
#     print(key, person_2[i])

# for key in person_2.items():
#     print(key[0], key[1])

# for key, value in person_2.items():
#     print(key, value)

# print(person_2.keys())
# print(list(person_2.keys()))#.append)

# print(person_2.values())

# person_4 =dict() ##### like that!!!! dict
# person_4["first_name"]= "Dasha"
# person_4["last_ name"]= "Dante"
# person_4["email"]= "quata_costa@"
# print(person_4)

# email_4 = person_4.get("email", False ) ## if data is notin the base!! CHECKing if data is availbl
# print(email_4)


# if "email" in person_4:
#     email_4 = person_4["email"]
#     print(email_4)


# email_4 = person_4.get("email", False ) ## if data is notin the base!! CHECKing if data is availbl
# print(email_4)



# if "email" not in person_4:   #### iF email area is not field^ to user setn msg"...."
#     print("email is a necessary")

####res = 4


# from random import randint
# res = randint(1, 6)
#
# dice_dict ={
#     1: "This is 1",
#     2: "This is 2",
#     3: "This is 3",
#     4: "This is 4",
#     5: "This is 5",
#     6: "This is 6",
# }
#
# print(dice_dict[res])


####### ASCII

# print(ord("a"))
#
# print(chr(97))

# alphabeth_dict ={
#
# }
# #
# for key in range(ord("a"), ord("z")+1):
# #     # print(key)#
#   alphabeth_dict[key] = chr(key)
# print(alphabeth_dict)
#
#
# new_alphabeth_dict = {
#
# }
# for key in alphabeth_dict:
#     new_alphabeth_dict[alphabeth_dict[key]] = key
# print(new_alphabeth_dict)


# val_1 = 1
# val_2 = 2
# val_1, val_2 = val_2, val_1
# print(val_1)

# for key, val in alphabeth_dict.items():
#     new_alphabeth_dict[val] = key
# print(new_alphabeth_dict)

# val_list= [i for i in range(10)]
# print(list)

# val_dict ={i: f"This is number:{i}" for i in  range(10)
#            }
# print(val_dict)

# val_dict ={i: f"This is number:{i}" for i in  range(1, 7)
#            }
# print(val_dict)


# val_dict ={i: i**2 for i in  range(1, 6)
#            }
# print(val_dict)
#
# val_dict ={
#     i: i**2 for i in  range(1, 6) if i % 2
#            }
# print(val_dict)
#
# val_dict ={
#     i: i**2 for i in  range(1, 6) if not i % 2
#            }
# print(val_dict)


### update()

# val_dict_1 ={
#     1: "1111",
#     2: "2222",
# }
#
# val_dict_2 ={
#     3: "3333",
#     4: "4444",
# }
#
# val_dict_1.update(val_dict_2)
# print(val_dict_1)


#
# val_dict_1 ={
#     1: "1111",
#     2: "2222",
# }
#
# val_dict_1.pop(1)#### only with key!
# print(val_dict_1)