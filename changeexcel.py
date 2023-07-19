import openpyxl
import handleCNY
from shutil import copyfile
import os
import random
path = "D:/abc"
# datanames = os.listdir(path)
# for i in datanames:
#     names = os.listdir(path+"/"+i)
#     for name in names:
#         suffixname = os.path.splitext(name)[-1]
#         oldName = os.path.splitext(name)[0]
#         newName = oldName+"-"+ i + suffixname
#         # os.rename(fi, fi+" "+ i)
#         print(oldName)
#         print(newName)
source_file1 = "D:/test/报价单1.xlsx"
source_file2 = "D:/test/报价单2.xlsx"
name1 = "姓名1"
name2 = "姓名2"
company1 = "c1"
company2 = "c2"
email1 = "e1"
email2 = "e2"
phono2 = "p2"
address1 = "address1"
address2 = "address2"
company_name = ""
def recursive_listdir(path):
    change = handleCNY.ChangeCNY()
    files = os.listdir(path)
    if(len(files)!=0):
        for file in files:
            file_path = os.path.join(path, file)

            if os.path.isfile(file_path):
                print(file)

            elif os.path.isdir(file_path):
                global company_name
                company_name= file_path
                recursive_listdir(file_path)
    else:
        projectname = company_name.split(' ')[1]
        value = round(random.random()*100000,2)
        destination_file1 = "报价单1-"+projectname+".xlsx"
        destination_file2 = "报价单2-"+projectname+".xlsx"
        copyfile(source_file1, path+"/"+destination_file1)
        copyfile(source_file2, path+"/"+destination_file2)
        book = openpyxl.load_workbook(path+"/"+destination_file1)
        sheet = book['Sheet1']
        sheet['B2'] = projectname+"报价单"
        sheet['B3'] = company1
        sheet['C4'] = name1
        sheet['E4'] = email1
        sheet['H4'] = address1
        sheet['D7'] = str(value)+'（'+change.small_to_big(str(value))+'）'
        book.save(path+"/"+destination_file1)
        
        book = openpyxl.load_workbook(path+"/"+destination_file2)
        sheet = book['Sheet1']
        sheet['A1'] = projectname+"报价单"
        sheet['A2'] = "报价单位："+company2
        sheet['A3'] = "联系电话："+phono2
        sheet['E2'] = "地址："+address2
        sheet['E3'] = "邮箱："+email2
        value2 = round(random.random()*100000,2)
        sheet['A11'] = "合计金额（大写）："+change.small_to_big(str(value2))
        sheet['E11'] = "合计金额（小写）：" + str(value2)
        sheet['A12'] = "报价人：" + name2
        book.save(path+"/"+destination_file2)


if __name__ == '__main__':
    recursive_listdir('D:/test')
    
    
# # 创建一个Excel workbook 对象
