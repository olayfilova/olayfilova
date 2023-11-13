##1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
###Якщо на парному – залишити без зміни.
import random


# def list_switch(my_list):
#     new_list = []
#
#
#     for index in range(len(my_list)):
#         if index % 2 == 0:
#             res = my_list[index] [::-1]
#         else:
#             res = my_list[index]
#         new_list.append(res)
#
#     return new_list
#
#
# my_list = ["asd", "asd", "hello", "try again"]
#
# result = list_switch(my_list)
#
# print(result)

###2. Написати функцію яка приймає один параметр – список рядків my_list.
# #Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".
#
# def starts_a(my_list):
#     new_list = []
#
#
#     for i in my_list:
#         if i.startswith("a") or i.startswith("A"):
#             new_list.append(i)
#
#
#     return new_list
#
#
# my_list = ["asd", "asd", "hello", "try again", "And done"]
# res = starts_a(my_list)
# print(res)



# #3. Написати функцію яка приймає один параметр – список рядків my_list.
# #Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

# def wordth_with_a(my_list):
#     new_list=[]
#
#     for i in my_list:
#         if "a" in i or "A" in i:
#             new_list.append(i)
#
#     return new_list
#
# my_list = ["asd", "asd", "hello", "try again", "And done", "even thAt"]
# res = wordth_with_a(my_list)
# print(res)

#
# #4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
# #Функція повертає новий список у якому містяться лише рядки з my_list.

# def return_str(my_list):
#     new_list=[]
#
#     for i in my_list:
#         if type(i)== str:
#             new_list.append(i)
#
#     return new_list
#
# my_list =[[1], "1", 1, "one"]
# res = return_str(my_list)
# print(res)


#
##5. Написати функцію яка приймає один параметр – рядок my_str.
# #Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.
#


# def return_unique_symb(my_str):
#     new_list = []
#
#     for i in my_str:
#         if my_str.count(i) ==1:
#             new_list.append(i)
#     return new_list
#
#
# my_str = "ahisiahhhh9, 911]"
# res = return_unique_symb(my_str)
# print(res)


##6. Написати функцію яка приймає один параметр - два рядки.
# #Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

#
# def unique_symb_in_2str(str_1, str_2):
#     new_list =[]
#
#
#     result = set(str_1.lower()).intersection(set(str_2.lower()))
#     new_list.append(result)
#     return new_list
#
# str_1 = "Yeah, if will storm"
# str_2 = "yeah^ storm in coming"
# res = unique_symb_in_2str(str_1, str_2)
# print(res)


#
# #7. Написати функцію яка приймає два параметри - два рядки.
## Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.
#
# def one_time_symb(str_1, str_2):
#     new_list=[]
#
#     for i in set(str_1).intersection(set(str_2)):
#         if str_1.count(i) == 1 and str_2.count(i) == 1:
#             new_list.append(i)
#     return new_list
#
# str_1 = "Yeah, if will storm, nah^"
# str_2 = "yeah^ storm is coming"
# res = one_time_symb(str_1, str_2)
# print(res)




# # 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
# #     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# # Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# # Рядок і число генерувати випадковим чином.
# #
# # Приклад використання функції:
# #
# # names = ["king", "miller", "kean"]
# # domains = ["net", "com", "ua"]
# # e_mail = create_email(domains, names)
# # print(e_mail)
#
#
# import random
# from string import ascii_lowercase
#
#
# def gen_email(list_name, list_domain):
#     emais=[]
#
#     name = random.choice(list_name)
#     domain =  random.choice(list_domain)
#     num = random.randint(100, 999)
#     str = "".join(random.choice(ascii_lowercase) for _ in range(random.randint(5, 7)))
#
#     # name = random.choice(list_name)
#     # num = random.randint(100, 999)
#     # str = "".join(random.choice(ascii_lowercase) for _ in range(random.randint(5, 7)))
#     # domain = random.choice(list_domain)
#
#     return f"{name}.{num}@{str}.{domain}"
#
#
# list_name = ["martina", "letitia", "nelly"]
# list_domain = ["com", "ie", "uk"]
# email = gen_email(list_name, list_domain)
# print(email)

