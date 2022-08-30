import shutil


def Dcm2jpg(file_path):
    for i in range(1, 200):
        new_file = "./data/Images/data" + str(i) + ".nii.gz"
        shutil.copyfile(file_path, new_file)


Dcm2jpg("../data/Images/data0.nii.gz")
