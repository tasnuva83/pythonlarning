with open ("to read in python.txt", 'r') as in_file, open ("output_new.txt", 'w') as out_file:
    for line in in_file:
        out_file.write(line)