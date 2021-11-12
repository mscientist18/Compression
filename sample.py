import os 
from compression import compress, decompress

degree = 2
directory1 = 'mri_mini'
directory2 = directory1 + '_compressed'
directory3 = directory1 + '_decompressed'

for file in os.listdir(directory1):
    compress(directory1, file, degree, directory2)

for file in os.listdir(directory2):
    decompress(directory2, file, directory3)

for file in os.listdir(directory1):
    f1 = open(directory1 + '/' + file,'rb')
    f2 = open(directory3 + '/' + file,'rb')
    f1 = f1.read()
    f2 = f2.read()

    if len(f1) != len(f2):
        print(False)
        print(file, 'len')
    
    for i in range(0, len(f1)):
        if f1[i] != f2[i]:
            print(False)
            print(file, 'val', i)
            break

