# my_list = [1234,10,1200]
# for i in my_list:
#     if i > 100:
#      print(i)

# my_list = 60, 600, 1234,10,1200
# my_result = []
# for i in my_list:
#     if i > 100:
#         my_result.append(i)
# print(my_result)

# my_list = 60, 600, 1234,10,1200  ### тут вопросы
# if len(my_list) < 2:
#      result = my_list.append(0)
# elif len(my_list) >= 2:
#      sum_of_last = my_list[-1] + my_list[-2]
#       result = my_list.append(sum_of_last)
# print(result)

str ="0123456789"
# for num in str:
#     for num_2 in str:
#         print(int(num+num_2))


# for num in range(100):
#     print(num)
#
# num = 0
# while num <100:
#     print(num)
#     num += 1

ten_d = 0   ###didnt work
while ten_d < 10:
    one_d =0
    while one_d < 10:
        num_str = str[ten_d] + str[one_d]
        num_int = int(num_str)
        print(num_int)
        one_d +=1
        ten_d +=1