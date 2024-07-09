#OS Modules
#OS Module is used to interact with the operating system
# Used for -> Get working directory, change directory,Fileexist, FileName, File size, env variable check

import os
print(os.name)
print(os.getcwd())
print(os.listdir()) #list the contents in the directory
size_of_file = os.path.getsize("testdata.txt")# checks the size of a file
print(size_of_file)

