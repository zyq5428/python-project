import sys, os
import logging
import PyPDF2

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='myProgramLog.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


pdf1_file = open('meetingminutes.pdf', 'rb')
pdf2_file = open('meetingminutes2.pdf', 'rb')

pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)

pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf1_reader.numPages):
    page_obj = pdf1_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

for page_num in range(pdf2_reader.numPages):
    page_obj = pdf2_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

pdf_out_file  = open('combinedminutes.pdf', 'wb')
pdf_writer.write(pdf_out_file)
pdf_out_file.close()
pdf1_file.close()
pdf2_file.close()