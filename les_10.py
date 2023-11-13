#
# def square_area(val_str, debug_mode=False):
#     pwr= val_str  **2
#
#     if debug_mode:
#         print(("!!!!", pwr))
#
#     return pwr


# value_str = 10
# print(square_area(value_str, debug_mode=True))

#####*args **kwargs
# def test_def(*args):
#     # print(args)
#     for arg in args:
#         print(arg)
# test_def( 1,2,3)


# def test_def(*args,  **kwargs):
    # print(args)
    # for arg in args:
    #     print(arg)

    # print(kwargs)

    # for kwarg in kwargs:
    #     print(kwarg)

    #     for kwarg in kwargs.items():
    #         print(kwarg)

#     for kwarg in kwargs:
#         print(kwarg, kwargs[kwarg])
#
#
# test_def(1, 2, 3, key=1, val=2)


# def square_area(val_str: float, debug_mode: bool = False):
#     pwr= val_str  **2
#
#     if debug_mode:
#         print(("!!!!", pwr))
#
#     return pwr
#
#
# print(square_area(10, True))

############
### files

# file_name = "lesson_4/lesson_4.py"
# my_file = open(file_name, "r")   #"r"- read, "w" write
# data = my_file.read()
# my_file.close()
#
# print(data)


### context manager

# file_name = "lesson_4/lesson_4.py"
# with open(file_name, "r") as my_file:
#     data = my_file.read()
#
# print(data)

######## with(context manager) work
# try:
#     my_file = open(file_name, "r")   #"r"- read, "w" write
#     data = my_file.read()
# except:
#     print("error")
# finally:
#     my_file.close()

#########

#########

# file_name = "lesson_4/lesson_4.py"
# with open(file_name, "r") as my_file:
#     data = my_file.readline()
#     data_1 = my_file.readline()
#     data_2= my_file.readline()

# print(data, data_1, data_2)

#####
# file_name = "lesson_4/lesson_4.py"
# with open(file_name, "r") as my_file:
#     for i in range(10):
#         print(my_file.readline())



#  ##########
# file_name = "lesson_4/lesson_4.py"  ####### list with\n-row is new object
# with open(file_name, "r") as my_file:
#     data =my_file.readlines()
#
# print(data)



##### write
####


# file_name = "lesson_4/lesson_4.py"
# with open(file_name, "r") as my_file:
#     data = my_file.read()
#
# data += "tIEeeeest"
#
# with open(file_name + "_test", "w") as my_file:
#     my_file.write(data)
#
#
# print(data)

#######
# file_name = "lesson_4/lesson_4.py"
# with open(file_name, "r") as my_file:
#     data = my_file.readlines()
#
# data.append("tIEeeeest")
#
# with open(file_name + "_test", "w") as my_file:
#     my_file.writelines(data)
# print(data)

file_name = "../lesson_4/lesson_4.py"
# with open(file_name, "r") as my_file:
#     data = my_file.readlines()
#
# data.append("\n\ttIEeeeest")
#
# with open(file_name + "_test", "w") as my_file:
#     my_file.writelines(data)
# print(data)




def reading_readlines(file: str) -> list:
    with open(file, "r") as f:
        data = f.readlines()
    return data


def writinging_writelines(file: str, data: list) -> bool:
    with open(file, "w") as my_file:
        my_file.writelines(data)

    return True


data = reading_readlines(file_name)
print(data)



