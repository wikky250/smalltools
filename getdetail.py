import os
import openpyxl
import operator
import numpy as np
import pandas as pd 

headers = ['项目','明细','单价']
detail1 = []
detail2 = []


def get_detail(path):
    print(path)
    book = openpyxl.load_workbook(path)
    sheet = book.active
    if operator.contains(path,"报价单1"):
        for i in range(0,10):
            if not operator.contains(str(sheet['B'+str(6+i)].value),"合计") :
                print(sheet['D'+str(6+i)].value)
                print(sheet['F'+str(6+i)].value)
                print(sheet['G'+str(6+i)].value)
                detail1.append([path.split(' ')[1],sheet['D'+str(6+i)].value,sheet['G'+str(6+i)].value])
                # if len(detail)==0:
                # else:
                #     detail = np.r_[detail,[path.split(' ')[1],sheet['D'+str(6+i)].value,sheet['G'+str(6+i)].value]]
                # print(detail)
            else:
                break
    if operator.contains(path,"报价单2"):
        for i in range(0,10):
            if not operator.contains(str(sheet['A'+str(5+i)].value),"备注") :
                print(sheet['B'+str(5+i)].value)
                print(sheet['F'+str(5+i)].value)
                print(sheet['G'+str(5+i)].value)
                value=0
                if sheet['G'+str(5+i)].value is None:
                    value =  sheet['F'+str(5+i)].value
                else:
                    value = sheet['G'+str(5+i)].value
                detail2.append([path.split(' ')[1],sheet['B'+str(5+i)].value,value])
                # if len(detail)==0:
                # else:
                #     detail = np.r_[detail,[path.split(' ')[1],sheet['D'+str(6+i)].value,sheet['G'+str(6+i)].value]]
                # print(detail2)
            else:
                break
                
    pd.DataFrame(detail1).to_csv('d:/detail1.csv')
    pd.DataFrame(detail2).to_csv('d:/detail2.csv')
    
    print(path)

def recursive_listdir(path):
    lastfile = ""
    projectname = ""
    files = os.listdir(path)
    if(len(files)!=0):
        for file in files:
            file_path = os.path.join(path, file)

            if os.path.isdir(file_path):
                if 2==recursive_listdir(file_path):                
                    lastfile= file_path
                    projectname = lastfile.split(' ')[1]
                    print("last file:"+lastfile)
                    
            if os.path.isfile(file_path):
                get_detail(file_path)

    return len(files)
                
                
                
if __name__ == '__main__':
    recursive_listdir('D:/报价单')
    
    