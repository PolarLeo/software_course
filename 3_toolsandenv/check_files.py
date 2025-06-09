import filecmp
import os
list_of_files = os.listdir('a_few_files')
for file in list_of_files:
    for file2 in list_of_files[::-1]:
        if filecmp.cmp(f'a_few_files/{file}', f'a_few_files/{file2}'):
            print(f'{file} and {file2} are the same')
        else:
            print(f'{file} and {file2} are different')