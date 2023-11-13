# 1
# num = 100
# find_symbol = "0"
# num_str = str(num)
# result = num_str.count(find_symbol)
# print(result)

# num = 105000000
# symb = "0"
# new_l =[]
# result = 0
#
# for i in str(num)[::-1]:
#     if i == symb:
#         result += 1
#         new_l.append(i)
#     else:
#         break
# print(result)

# new_num = str(num)
# result = len(new_num) - len(new_num.rstrip("0"))
# print(result)

# list_1 = ["mamba", "q", "1", "roar"]
# list_2 = ["king", "taxi", "programming is hard", ":-)"]
# result = list_1[::2] + list_2[::2]
# print(result)

# list_1 = ["hot", "pot","cold", "not"]
# list_2 = ["success", "tmr run", "and"]
# new_list = list_1  + list_2
# print(new_list)

# list_1 = ["hot", "pot","cold", "not"]
# new_list = list_1[1::] + list_1[0:1]
# print(new_list)

# list = [ 1, 2, 3, 4]
# list.append(list.pop(0))
# print(list)

# text = "43 більше ніж 34, але менше ніж 56"
# lst = []
# # for word in text:
# #     if not word.isdigit():
# #         text = text.replace(word," ")
# # num_list = text.split()
# # for word in num_list:
# #     text = str(num_list)
# #
# # print(text)
#
#
#
#
# # for i in text.split():
# #     if i.isdigit():
# #         lst.append(int(i))
# #     else:
# #         dgt = ""
# #         for smbl in i:
# #             if smbl.isdigit():
# #               dgt += smbl
# #             else:
# #                 if dgt:
# #                  lst.append(str(dgt))
# #                  dgt = ""
# #
# # result = sum(lst)
# # print(result)
#


# list_1= [2, 4, 1, 5, 3, 9, 0, 7]
# result = 0
# for i in range(1, len(list_1) - 1):
#     if list_1[i] > list_1[i - 1] + list_1[i + 1]:
#         result += 1
# print(result)


# txt = [1, 2, 3, "11", "22", 33]
# new_list = []
# for val in txt:
#     if type(val) == str:
#         new_list.append(val)
# print(new_list)

# my_str ="dshaudfuguuhdmmmm"
# new_str = []
#
# for symb in my_str:
#     if my_str.count(symb) == 1:
#         new_str.append(symb)
# print(new_str)

# my_str = "dgsgkjcius"
# my_str_2 = "jdfuctdgcm"
# the_set = set(my_str).intersection(my_str_2)
# result = list(the_set)
# print(result)

# txt_1 = "aaaasdf1"
# txt_2 = "asdfff2"
# txt_res = []
#
# for symbol in set(txt_1).intersection(set(txt_2)):
#     if txt_1.count(symbol) ==1 and txt_2.count(symbol) ==1:
#         txt_res.append(symbol)
# print(txt_res)








