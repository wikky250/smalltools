from docx import Document
import re
doc = Document(r"D:\02.docx")
restr = '([一-龥])（(\s+)\)'

redst = '\1\(\2\)'

pattern = re.compile("([一-龥])（(.+)）",re.U) 


for p in doc.paragraphs:
    matchRet = pattern.findall(p.text)
    for r in matchRet:
        p.text = p.text.replace(restr, redst)
doc.save(r'D:\论文_修正.docx')