# my_str = "0123456789"

# for i in my_str:
#     for y in my_str:
#         res = int(i + y)
#     print(res)

#
# for i in range(100):
#
#     # for y in range(len(my_str)):
#     #     res = int(i + y)
#     #
#     # if i <= int(my_str) and y <= int(my_str):
#     print(i)
# ten_d = 0
#
# while ten_d < 10:
#     one_d = 0
#     while one_d < 10:
#         num_str = str[ten_d] + str[one_d]
#         res = int(num_str)
#         print(res)
#         ten_d += 1
#         one_d += 1


# list--------------------------------
# list=["1", "2", "3","4"]
# new_list = list*4
# # print(new_list)
#
# list[0] =10
# # print(list)
# print(f"{new_list} {list}")

# list=["1", "2", "3","4"]
# new_list = [list] *4
# list[0] =[20]
# print(f"{list}{new_list}")

# base_list = ["1", "2", '3', "deep"]
# base_list.append("norm")
# print(base_list)
# base_list.pop()
# print(base_list)
# base_list.pop((2))# index(01234567)
# print(base_list)
# pop_val = base_list.pop(0)# only pop gives the value
# print(pop_val)


# web_s = ["www.org1",
#          "www.org2",
#          "www.org3",
#          "www.org4",
#          "www.org5",
#          ]
# # while len(web_s)!= 0:
# #         deleted_val = web_s.pop()
# #         print(deleted_val)
#
# while len(web_s) :
#         deleted_val = web_s.pop()
#         print(deleted_val)


# val= "www.fhjfg/org"
# new_val = val.rsplit("/", 1)
# print(new_val)
# new_val[0] = "cross_fingers"
# print(new_val)
# final_res_val_join = ".".join(new_val)
# print(final_res_val_join)


# val= "www.fhjfg/kshv/dububx/fafr/olya/org"
# new_val = val.split("/")
# print(new_val)
#
# final_res_val_join = "!".join(new_val)
# print(final_res_val_join)


# list = [-5, -7, 10, 1, 13, 7, 21, 37, 11]
# # list.sort()### list changed
# # print(list)
# # list.sort(reverse=True)
# # print(list)
# print(sorted(list))### list did not change ^ the original    ,key=len)   ,key=
# print(sorted(list, reverse=True))

### ASCII

# print(ord("1"), ord("a"), ord("A"), ord("4"))
#
# print(chr(49), chr(97), chr(65), chr(52))
