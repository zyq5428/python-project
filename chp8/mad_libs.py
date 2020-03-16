import os
import re

key_word = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

libs_file = open('libs.txt', 'r')
content = libs_file.read()
libs_file.close()

print(content)

completed = False

while completed == False:
    bool_v = [False] * len(key_word)
    completed = True
    for n in range(len(key_word)):
        change_regex = re.compile(key_word[n])
        if change_regex.search(content) != None:
            bool_v[n] = False
            print('Enter a ' + key_word[n].lower() + ':')
            replace_word = str(input())
            content = change_regex.sub(replace_word, content, 1)
            print(content)
        else:
            bool_v[n] = True
        completed = bool_v[n] and completed

print(content)

new_libs_file = open('new_libs.txt', 'w')
new_libs_file.write(content)
new_libs_file.close()
