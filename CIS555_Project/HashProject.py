import hashlib
import os
def ComputeHash(filename):
    FileHash = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            FileHash.update(data)
    return FileHash.hexdigest()
def merkle(file_list):
    Hash_list = [ComputeHash(i) for i in file_list]
    while len(Hash_list) > 1:
        Hash_list = [hashlib.md5(Hash_list[i].encode('utf-8') + Hash_list[i+1].encode('utf-8')).hexdigest() for i in range(0, len(Hash_list), 2)]
    return Hash_list[0]

#Compute top hash with 4 files.
file_list = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
top_hash = merkle(file_list)
print('Top hash with original files:', top_hash)

#Compute top hash with a new file indicating change in one of base file resulting hash
file_list = ['file1.txt', 'file2.txt', 'file3.txt', 'file5.txt']
top_hash = merkle(file_list)
print('Top hash with a new file:', top_hash)

#Compute top hash with one of 2 files being duplicates indicating change to resultig hash of one of the source files.
file_list = ['file1.txt', 'file1.txt', 'file3.txt', 'file4.txt']
top_hash = merkle(file_list)
print('Top hash with 2 duplicate files:', top_hash)

