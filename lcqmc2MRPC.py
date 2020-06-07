# from tkitText import *
import  hashlib
import csv
def md5(string):
    # 对要加密的字符串进行指定编码
    string = string.encode(encoding ='UTF-8')
    # md5加密
    # print(hashlib.md5(string))
    # 将md5 加密结果转字符串显示
    string = hashlib.md5(string).hexdigest()
    # print(string)
    return string
def w2tsv(data,name):
    with open(name, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        # Quality	#1 ID	#2 ID	#1 String	#2 String
        tsv_writer.writerow(['Quality', '#1 ID','#2 ID','#1 String','#2 String'])
        for it in data:
            tsv_writer.writerow(it)
        # tsv_writer.writerow(['Shelah', 'Math'])
        # tsv_writer.writerow(['Aumann', 'Economic Sciences'])
        
file_list=["test.txt","dev.txt","train.txt"]

for file_neme in file_list:
    with open(file_neme, "r") as f:
        data=[]
        for it in  f.readlines():

            t=it.replace("\n", "").split("\t")
            # print(t)
            # one={
            #     "label":t[2],
            #     'sentence1':t[0],
            #     'sentence2':t[1],
            #     'sentence1id':md5(t[0]),
            #     'sentence2id':md5(t[1]),
            # }
            # print(one)
            one=[t[2],md5(t[0]),md5(t[1]),t[0],t[1]]
            data.append(one)
        name=file_neme.replace(".txt",'.tsv')
        w2tsv(data,name)
            


