import os

bacon_file = open('bacon.txt', 'w')
bacon_file.write('Hello world!\n')
bacon_file.close()

bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable\n')
bacon_file.close()

bacon_file = open('bacon.txt', 'r')
content = bacon_file.read()
bacon_file.close()

print(content)