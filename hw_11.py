import os


def create_fld_discrb(folder = ""):
    if not folder:
        folder_obj = os.listdir()
    else:
        fld_obj =os.listdir(folder)
    file_name = []
    sub_fld =[]
    for obj in fld_obj:

        obj_path = os.path.join(folder, obj)
        if os.path.isdir(obj_path):
            sub_fld.append(obj)
        else:
            file_name.append(obj)

    return {"file_name": file_name, "dirname": sub_fld}


def sort_fldr_obj(folder_obj, without_reverse =True):
    for i in folder_obj:
        folder_obj[i].sort(reverse = not without_reverse)
        return folder_obj

def update_fld_obj(folder_obj, obj_name: str):
    key = "dirname"
    if "." in obj_name:
        key ="file_name"

    self.folder_obj[key].append(obj_name)
    return self.folder_obj


def compare_obj(folder_obj, dirname: str):
    folder_obj_real = create_fld_discrb(dirname)

    for file_name in set(folder_obj["file_name"]).difference(set(folder_obj_real["file_name"])):
        with open(os.path.join(dirname, file_name), "w") as file:
            file.write("")

    for fld in set(folder_obj["dirname"]).difference(set(folder_obj_real["dirname"])):
        os.makedirs(os.path.join(dirname, fld))

fld = create_fld_discrb("../")
print(fld)



class File:
    def __init__(self, folder_obj):
        self.folder_obj = folder_obj


    def sort_fld_obj(self, witout_reverse =True):
        for i in self.folder_obj:
            self.folder_obj[i].sort(reverse=not witout_reverse)
        return self.folder_obj


    def update_fld_obj(self, obj_name:str):
        key = "dirname"
        if "." in obj_name:
            key= "file_name"
        else:
            key = "dirname"


        self.fld_obj[key].append(obj_name)
        return self.folder_obj


    def compare_obj(self, dirname: str):
        folder_obj_real = create_fld_discrb(dirname)

        for file_name in set(folder_obj["file_name"]).difference(set(folder_obj_real["file_name"])):
            with open(os.path.join(dirname, file_name), "w") as file:
                file.write("")

        for fld in set(folder_obj["dirname"]).difference(set(folder_obj_real["dirname"])):
            os.makedirs(os.path.join(dirname, fld))




