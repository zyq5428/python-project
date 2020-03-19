import sys, os, re
from openpyxl import Workbook
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='myProgramLog.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def dir_tree(path):
    for folderName, subfolders, filenames in os.walk(path):
        cwd_abs = os.path.abspath(folderName)
        logging.debug('The current folder is : %s' % (cwd_abs))

        if len(subfolders) == 0:
            logging.debug('No subfolder')
        else:
            logging.debug('SUBFOLDER OF %s : ' % (folderName))
            for subfolder in subfolders:
                logging.debug('%s ' % (subfolder))
                #print(subfolder, end=' ')
            #print('\n')

        logging.debug('FILE INSIDE %s : ' % (folderName))
        for filename in filenames:
            logging.debug('%s ' % (filename))
            #print(filename, end=' ')
        #print('\n')

        return(filenames)

DIR_PATH = './'
col_boot = 1
col_of_cell = col_boot
#List all files in the specified directory.
DIR_PATH_ABS = os.path.abspath(DIR_PATH)
file_all = dir_tree(DIR_PATH)
#print(file_all)

#Create a Excel
wb = Workbook()
ws = wb.active

#Matches a specific format file
txt_regex = re.compile(r'.*txt')

for n in range(len(file_all)):
    if txt_regex.search(file_all[n]) != None:
        files_abs = os.path.join(DIR_PATH_ABS, file_all[n])
        txt_file = open(files_abs)
        lines = txt_file.readlines()
        logging.debug('lines is  %s : ' % (lines))
        row_of_cell = 1
        for line in lines:
            ws.cell(row=row_of_cell, column=col_of_cell).value = line
            ws.row_dimensions[row_of_cell].height = 30
            logging.debug('row height is  %s : ' % (ws.row_dimensions[row_of_cell].height))
            row_of_cell += 1
        col_of_cell += 1

#Save Excel
wb.save("text_to_excel.xlsx")