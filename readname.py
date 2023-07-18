
import os
path = "D:/abc"
datanames = os.listdir(path)
for i in datanames:
    names = os.listdir(path+"/"+i)
    for name in names:
        suffixname = os.path.splitext(name)[-1]
        oldName = os.path.splitext(name)[0]
        newName = oldName+"-"+ i + suffixname
        # os.rename(fi, fi+" "+ i)
        print(oldName)
        print(newName)
