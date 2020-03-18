# Good resource: https://www.youtube.com/watch?v=Pl4Hp8qwwes

# Exercise 1

import os
import json
import pickle

# Part A

def read_json(in_file_path):
    with open(in_file_path) as f:
        json_input = json.load(f)
    return json_input

path1 = "/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json"

a = read_json(path1)
print(a)

"""
In Part A, we are using the OS Module to open and read a JSON file and then 
return a Python dictionary. Meaning, the string contents of a JSON file are
being deserialized into a usable Python data structure, a dictionary. 
"""

# Part B

def read_all_json_files(path):
    for direpath, direnames, filenames in os.walk(path):
        result = []
        for f in filenames:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(path,f))
                result.append(json_content)
    return result

path2 = "/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/"

b = read_all_json_files(path2)
print(b)

"""
In Part B, we want to apply the function from Part A to all files in a particular
directory. 

We begin by declaring 3 arguments required for the os.walk() method: root, _, and files.

In the official documentation, they are called: direpath, direnames, filenames. 
https://docs.python.org/3/library/os.html 
Note how the direnames was renamed _ since it is not relevant here. 

dirpath (root) is a string, the path to the directory. 
dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..'). 
filenames is a list of the names of the non-directory files in dirpath. 
Note that the names in the lists contain no path components. To get a full path 
(which begins with top) to a file or directory in dirpath, do os.path.join(dirpath, name).

os.walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up. 
For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

Then, we create an empty list and add files to the list if the file_path + f ends with .json,
meaning that it's a JSON file. 

"""

# Part C

# out_file_path should have a .pkl extension like '/.../out_file_path.pkl
def write_pickle(out_file_path, data):
    with open(out_file_path, 'wb') as f:
        pickle.dump(data, f)


# Part D

def load_pickle(out_file_path):
    with open(out_file_path, 'rb') as f:
        data = pickle.load(f)
    return data

"""
Pickle reads (Part C) / writes (Part D) the python object as binary. It preserves the object as it was in memory.
"""


# Exercise 2

path3 = "/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/marvel/"

content = read_all_json_files(path3)
# This creates a list of Python dictionaries. 
print(content)

write_pickle(path3+'marvel_pickle.pkl', content)
# This serializes the data in content and saves it into a file
with open(path3+'marvel_pickle.pkl', 'rb') as f:
    for line in f:
        print(line)

marvel_content = load_pickle(path3+'marvel_pickle.pkl')
#This unserializes the data stored in marvel_pickle.pkl
print(marvel_content)
