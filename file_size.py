from os import walk
import os

my_path = input('What path do you want to check? \n')
largest_file = {}
for root, directories, files in os.walk(my_path):
    for file in files:
        full_path = os.path.join(root,file)   
        size = os.path.getsize(full_path)
        largest_file[file] = size
sorted_files = dict(sorted(largest_file.items(), key=lambda item: item[1], reverse=True))
shown = 0
for file in sorted_files:
    if shown < 5:
        print(file, sorted_files[file])
        shown+=1
    else:
        break
#/workspaces/SQLite3-with-python/