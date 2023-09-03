import os
import shutil
import sys

if len(sys.argv) != 2 :
    print("need 1 Argument")
    print("Usage : python FileTypeSorter.py <dir_path>")
    sys.exit(1)

dir_path = sys.argv[1]
subDir_Doc = 'Documents'
subDir_Img = 'Images'
subDir_Txt = 'Texts'
imgFormat = ['.jpg', '.png', '.jpeg']
txtFormat = ['.txt']
docFormat = ['.wordx', '.pdf']
if not os.path.exists(dir_path):
    print(f"{dir_path} doesnt exist")
    sys.exit(1)

for subDir in [subDir_Doc, subDir_Img, subDir_Txt]:
    subDir_name = os.path.join(dir_path, subDir)
    if not os.path.exists(subDir_name):
        os.makedirs(subDir_name)
        print(f"create {subDir} in {dir_path}")
    else :
        print(f"{subDir} in {dir_path} already exists")


for item in os.listdir(dir_path):
    file = os.path.join(dir_path, item)
    if os.path.isfile(file):
        file_extension = os.path.splitext(item)[1].lower()
        if file_extension in imgFormat:
            dir_destination = os.path.join(dir_path, subDir_Img)

        elif file_extension in txtFormat:
            dir_destination = os.path.join(dir_path, subDir_Txt)

        elif file_extension in docFormat:
            dir_destination = os.path.join(dir_path, subDir_Doc)

        else:
            dir_destination = None
        
        if dir_destination :
            shutil.move(file, dir_destination)

