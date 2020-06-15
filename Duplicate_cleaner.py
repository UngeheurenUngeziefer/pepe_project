import hashlib
from hashlib import md5
from scipy import *
import matplotlib.pyplot as plt
import time
import numpy as np
import os

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()

os.chdir(r'C:\Users\sewer\MyPython\Pepe_project\downloads')
# print(os.getcwd())

files_list = os.listdir()
# print(len(files_list))

duplicates = []
hash_keys = dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash] = index
        else:
            duplicates.append((index, hash_keys[filehash]))

# print(duplicates)
# 405 and 4

for file_indexes in duplicates[:30]:
    plt.subplot(121), plt.imshow(imread(files_list[file_indexes[1]]))
    plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(imread(files_list[file_indexes[0]]))
    plt.title(str(file_indexes[0]) + ' duplicate', plt.xticks([]), plt.yticks([]))
    plt.show()

