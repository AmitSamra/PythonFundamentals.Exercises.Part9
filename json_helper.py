# Exercise 1

# Part A

import os
import json

path = "/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json" 

def read_json(path):
    file_name = path
    with open(file_name, 'r') as f:
        data = json.load(f)
    print(data)
    return data
    
read_json(path)

# or

path = "/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json" 

def read_json(path):
    file_name = path
    with open(file_name, 'r') as f:
        data = json.load(f)
    print(data)
    return data
    
read_json(path)


# Part B

def read_all_json_files():
    json_list = []
    for file in os.listdir(path):
        full_file_name = os.path.join(path, file)
        with open(full_file_name, 'r') as f2:
            data2 = json.load(f2)
            json_list.append(data2)
    print(json_list)
    return json_list


# Part C

path = "/Users/asamra/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json"
data = "super_smash_characters.pickle"

def write_pickle(path_input, data):
    f = open(b"super_smash_characters.pickle", "wb")
    pickle.dump(path_input, f)
    f.close()

write_pickle(path,data)


# Part D

