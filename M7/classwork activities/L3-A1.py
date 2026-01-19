# write in file using with() function
with open('Codingal.txt','w') as file:
 file.write("Hi! I am penguin and I am 1 yr old.\n")
 file.write("Hi! I am penguin.")


# split file into words
with open ('Codingal.txt','r') as file:
  data = file.readlines()
  print(data)
  print("Words in this file are....")
  for line in data:
    print(line)
    word = line.split()
    print(word)