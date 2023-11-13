# ######strip - rstrip
# # name = "   Amanda   "
# # print(name.strip())
# #
# num = 105000
# find_symb ="0"
#
# def count_symb(obj, symb):
#     num_str = str(obj)
#     res = len(num_str) - len(num_str.rstrip(symb))
#
#     return res
#
# # res = count_symb(num, find_symb)
# # print(res)
#
#
# res = count_symb(105000, "0")
# print(res)



# find_symb ="0"
# new_list = []
# res =0
#
# num_str = str(num)
# res = len(num_str) - len(num_str.rstrip(find_symb))
# print(res)







# import random
# ###############module#######
#
# # import string
# #
# # alphabeth = string.ascii_uppercase
# # print(alphbeth)
# #
# # alphabeth = list(string.ascii_uppercase)
# # print(alphabeth)
#
# from string import ascii_lowercase, ascii_uppercase
# from string import ascii_letters as alphabeth
#
#
# #######functions######
#
# # def new function():
# #
# #
# #
# #
# # return
# ############ ind-y
# # dot_1 ={
# #     "x": random.randint(1,100),
# #     "y": random.randint(1,100),
# #     "z": random.randint(1,100),
# # }
# #
# # dot_2 ={
# #     "x": random.randint(1,100),
# #     "y": random.randint(1,100),
# #     "z": random.randint(1,100),
# # }
# # dot_3 ={
# #     "x": random.randint(1,100),
# #     "y": random.randint(1,100),
# #     "z": random.randint(1,100),
# # }
# #
# # triangle = [dot_1, dot_2, dot_3]
# # print(triangle)
# #######################################function+ return
#
# def create_dot():
#     dot = {
#         "x": random.randint(1, 100),
#         "y": random.randint(1, 100),
#         "z": random.randint(1, 100),
#     }
#     return dot
#
# ########
# def create_dot():
#     return {
#         "x": random.randint(1, 100),
#         "y": random.randint(1, 100),
#         "z": random.randint(1, 100),
#     }
#
# triangle = [create_dot(), create_dot(),  create_dot()]
# print(triangle)
#
# ##########
# def create_dot(x_coord, y_coord, z_coord, ):
#     return {
#         "x": x_coord,
#         "y": y_coord,
#         "z": z_coord,
#     }
#
# triangle = [create_dot(
#     random.randint(1, 100),
#     random.randint(1, 100),
#     random.randint(1, 100),
#
#
# ),
#     create_dot(random.randint(1, 100),
#                random.randint(1, 100),
#                random.randint(1, 100),
#                ),
#     create_dot(
#         random.randint(1, 100),
#         random.randint(1, 100),
#         random.randint(1, 100),
#     )]
# print(triangle)
#
# #######
#
# triangle = [create_dot(2, 9, 18),
#             create_dot(14, 54, 82),
#             create_dot(27, 93, 128),
# ]
#
# print(triangle)
#
#
# def printing_obj (obj_type, obj_coord):
#     result = f"this is type{obj_type}, and coordints are{obj_coord}"
#
#     return result
#
#
# #######
# def printing_obj (obj_type, obj_coord):
#     result = f"this is type{obj_type}, and coordints are{obj_coord}"
#
#     return result
# triangle = [create_dot(2, 9, 18),
#             create_dot(14, 54, 82),
#             create_dot(27, 93, 128),
# ]
# printing_obj(triangle, "triangle")


# def adding(first_num, second_num):
#
#     result = first_num + second_num
#
#     return result
#
# print(adding(1, 12))
