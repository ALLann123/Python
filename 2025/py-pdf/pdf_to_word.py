#!/usr/bin/python3
from pdf2docx import Converter

print("*****************"*4)
print("      Converting PDF to DOCX   ")
print("*****************"*4)

#name of the pdf file
pdf_file="output.pdf"

#the desired name of the word document
docx_file="output.docx"

#pass the pdf to be converted
cv=Converter(pdf_file)
print("Converting PDF")

#the new word document from pdf
cv.convert(docx_file)

#close to release any resources
cv.close()





"""
 python .\pdf_to_word.py
********************************************************************
      Converting PDF to DOCX
********************************************************************
Converting PDF
[INFO] Start to convert output.pdf
[INFO] [1/4] Opening document...  
[INFO] [2/4] Analyzing document...
[INFO] [3/4] Parsing pages...
[INFO] (1/2) Page 1
[INFO] (2/2) Page 2
[INFO] [4/4] Creating pages...
[INFO] (1/2) Page 1
[INFO] (2/2) Page 2
[INFO] Terminated in 3.21s.
"""

