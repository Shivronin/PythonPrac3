from file import my_file
import os

leng = len(my_file.name)
STR_FILE = list(my_file.name[0:leng-4].split('/'))
vowel='аеёиоуыэюяoaeuiu'
for i in STR_FILE[1]:
    if i not in vowel:
        i = i.capitalize()
    my_file.write(i + ' ' + '\n')
my_file.close()