import os

def rename_file():
    file_list = os.listdir("C:\pydoc\prank")
    print file_list
    path=os.getcwd()
    os.chdir("C:\pydoc\prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
        print "\nfile_name =", file_name
    os.chdir(path)

rename_file()

