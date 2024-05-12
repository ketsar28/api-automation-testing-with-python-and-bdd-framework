# read the file and store all the lines in list
with open('./bahan/text.txt', 'r') as reader:
    contents = reader.readlines()
# revese the list
    reverse_contents = reversed(contents)
# write the list back to the file
    with open('./bahan/text.txt','w') as writer:
        for content in reverse_contents:
            writer.write(content)

 