from tkitFile import *

file_list=["test.txt"]

for file_neme in file_list:
    with open(file_neme, "r") as f:
        for it in  f.readlines():

            t=it.replace("\n", "").split("\t")
            print(t)
            one={
                "label":t[2],
                'sentence':t[0],
                'sentence':t[1]
            }
            
