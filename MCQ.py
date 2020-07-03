import PyPDF2
import re
with open("The_Living_World.pdf",'rb') as file:
    pdf_reader=PyPDF2.PdfFileReader(file)
    entire_pdf=''
    for i in range(pdf_reader.numPages):
        entire_pdf=entire_pdf+pdf_reader.getPage(i).extractText()
#print(entire_pdf)
regx=r'([0-9]+\.[a-zA-Z\s\.\?\-\/,\(\)______‘’\[\]&\[AIPMT (Prelims)-2007\]\[NEET (Phase 2)-2016\]NEET 2013:]+)\(1\)([a-zA-Z\s\-–,’\'\";\(\)—“”0-9×&]+)\(2\)([a-zA-Z\s\-–,’\'\";\(\)—“”0-9×&]+)\(3\)([a-zA-Z\s\-–,’\'\";\(\)—“”0-9×&]+)\(4\)([a-zA-Z\s\-–,’\'\";\(\)—“”0-9×&]+)Sol\.Answer \(([0-4])\)'
ans=re.findall(regx,entire_pdf)

result=[]
for i in range(len(ans)):
    temp=[]
    for j in range(6):
        temp.append(ans[i][j].replace('\n',''))
    result.append(temp)

for i in result:
    for j in i:
        print(j)
