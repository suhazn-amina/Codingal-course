# Program to merge two files into a third file
3# Reading data from file1
with open('Codingal.txt') as fp:
     data1 = fp.read()
# Reading data from file2
with open('Updatedfile.txt') as fp:
     data2 = fp.read()

     #merging 2 files
     # To add the data of file2
     #from next linr
     data1 = data1 + "\n"
     data3 = data1 + data2
     print("Merging two files....")
     with open ('mergedfile.txt','w') as fp:
          fp.write(data3)