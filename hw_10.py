##1
# file = "olgafilova/domains_TXT.py"
#
# def reading_file(file_data):
#     with open(file_data, "r") as input_file:
#         data = input_file.read().splitlines()
#     return data
#
#
# def list_domain(file_data):
#     open_data = reading_file(file_data)
#     dmn_list = [value.replace(".", "") for value in open_data]
#     return dmn_list
#
#
# lst_dmn = list_domain(file)
# print(lst_dmn)
#
#
# ##2

# file = "olgafilova/names_hw10.py"
#
# def get_family_names(file_name):
#     data_f_file = reading_file(file_name)
#     ln_lst =[ln.split("\t")[1] for ln in data_f_file if ln]
#     return ln_lst
#
# result = get_family_names(file)
# print(result)


##3

# file = "authors_.py"


# def get_dict(file_name):
#     data = reading_file(file_name)
#
#     new_d =[]
#     for i in data:
#         if i and "-" in i:
#             new_d.append({"date": i.split(" - ")[0]})
#     return new_d
#
# data_list = get_dict(file)
# print(data_list)




