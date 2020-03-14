import pyperclip
import re

phone_regex = re.compile(r'''
    \s*(ext|x|ext.)\s*\d{2,5}
    ''', re.VERBOSE)


text = '400-120-3532 ext 2024 \n 420-180-3542 ext. 1024'
matches = []
for groups in phone_regex.findall(text):
    print(groups)
