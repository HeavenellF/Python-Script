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

if not os.path.exists(dir_path):
    print(f"{dir_path} doesnt exist")
    sys.exit(1)

print("Script Complete!")