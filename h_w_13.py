## 1 повертає імя файлів (без папок)

import os

# class NameFile:
#     def __init__(self, directory):
#         self.directory = directory
#
#     def names_of_files(self):
#         if not os.path.exists(self.directory) or not os.path.isdir(self.directory):
#             return {"file_names": []}
#
#         items = os.listdir(self.directory)
#         file_names = [i for i in items if os.path.isfile(os.path.join(self.directory, i))]
#
#         return {"file_names": file_names}
#
#
# directory = '../lesson_5/home_wok_5.py'
# result = NameFile(directory)
# res = result.names_of_files()
# print(res)


## 2 списку рядків (назви повертати без крапки)

# class DomainList:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.domain_list = self.load_surnames()
#
#     def load_surnames(self):
#         domain_list = []
#         try:
#             with open(self.file_name, 'r') as my_file:
#                 for i in my_file:
#                     domain = i.strip()
#                     domain = domain.strip('.')
#                     domain_list.append(domain)
#
#         except FileNotFoundError:
#             print(f"File '{self.file_name}' not found.")
#
#         return domain_list
#
#     def print_domains(self):
#         if self.domain_list:
#             print(self.domain_list)
#         else:
#             print("No data.")
#
#
# file_n = '../olgafilova/domains_TXT.py'
# domain_instance = DomainList(file_n)
# domain_instance.print_domains()


# # 2 2 Розділювач - символ табуляції "t"

# class FamilyName:
#     def __init__(self, file):
#         self.file = file
#         self.last_names = self.read_last_names()
#
#     def read_last_names(self):
#         with open(self.file, 'r') as file:
#             return [line.strip().split('\t')[1] for line in file if len(line.strip().split('\t')) > 1]
#
#     def print_last_names(self):
#         if self.last_names:
#             print(self.last_names)
#         else:
#             print("Empty folder.")
#
#
# if __name__ == '__main__':
#     result = FamilyName("../olgafilova/names_hw10.py")
#     result.print_last_names()

import re

# class MyFileReader:
#     def __init__(self, filename):
#         self.filename = filename


## 3 {"date": date}

import re

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def get_dates(self):
        date_list = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.search(r'\b(\d{1,2}(st|nd|rd|th) \w+ \d{4})\b', line)
                if match:
                    date = match.group(1)
                    date_dict = {"date": date}
                    date_list.append(date_dict)
        return date_list


file_reader = FileReader("../olgafilova/authors_.py")
date_list = file_reader.get_dates()

print("Dates:", date_list)

## with open(self.filename, 'r') as file:
##     for i in file:
##        if i and "-" in i:
##            date_list.append({"date": i.split(" - ")[0]})
##        return date_list
