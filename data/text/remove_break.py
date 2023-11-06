# Open the original file in read mode and the new file in write mode
with open('data/2011.txt', 'r') as original_file, open('data/2011_2.txt', 'w') as new_file:
    for line in original_file:
        # Remove the line break and spaces from each line and write it to the new file
        new_file.write(line.replace(' ', '').strip())
