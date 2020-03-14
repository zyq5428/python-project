import re

phone_regex = re.compile(r'(\(\d\d\d\)-)?\d\d\d-\d\d\d\d')

mo = phone_regex.search('My number is (415)-555-4242.')
mo2 = phone_regex.search('My number is 555-4242.')

print('Phone numbere found: ' + mo.group())
print('Phone numbere found: ' + mo2.group())
#print('Phone numbere found: ' + mo.groups())