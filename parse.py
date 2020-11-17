import os
import docx2txt
import csv

result = docx2txt.process("16__Chapter_16_Appraisal_ORIGKEY.docx")
content = []
for line in result.splitlines():
  #This will ignore empty/blank lines. 
  if line != '':
    #Append to list
    content.append(line)

csv_row = []
for i in range(0, len(content), 12):
    csv_row.append([content[i + 1], content[i + 3], content[i +5], content[i + 7],content[i + 9]])


with open('question.csv', mode='w') as question_file:
    writer = csv.writer(question_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_row:
        writer.writerow(row)
    
