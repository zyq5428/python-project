import os
import zipfile

os.chdir('/home/hero/git/python-project/chp9')
example_zip = zipfile.ZipFile('example.zip')

print(example_zip.namelist())

spam_info = example_zip.getinfo('example/spam.txt')
print(spam_info.file_size)
print(spam_info.compress_size)
print('Compressed file is %sx smaller!' % (round(spam_info.file_size / spam_info.compress_size, 2)))
example_zip.close()