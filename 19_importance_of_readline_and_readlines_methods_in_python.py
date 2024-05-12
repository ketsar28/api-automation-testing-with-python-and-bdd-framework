file = open('bahan\\text.txt')

# ! read all the contents of file
# print(file.read())

# ! read n number of characters by passing parameter
# print(file.read(12))

# ! read one single line at the time readLine()
# print(file.readline())
# print(file.readline())
# print(file.readline())

# ! print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# ! print all the lines using readlines method
# * ['ahmad','bonpi','damon','ewok']
for line in file.readlines():
    print(line)

file.close()
