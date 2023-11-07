with open('pre.txt', 'r') as original_file, open('done.txt', 'w') as new_file:
    for line in original_file:
        new_file.write(line.replace(' ', '').strip())
