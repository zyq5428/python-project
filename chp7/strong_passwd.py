import re

print('Please input your password:')
pwd = str(input())
len_cond = False
upper_cond = False
lower_cond = False
digital_cond = False

lower_regex = re.compile(r'[a-z]')
upper_regex = re.compile(r'[A-Z]')
digital_regex = re.compile(r'\d')

if len(pwd) >= 8:
    len_cond = True
if lower_regex.search(pwd) != None:
    lower_cond = True
if upper_regex.search(pwd) != None:
    upper_cond = True
if digital_regex.search(pwd) != None:
    digital_cond = True

if len_cond and upper_cond and lower_cond and digital_cond:
    print('Password set successfully!')
else:
    print('Please include uppercase and lowercase letters and numbers!')