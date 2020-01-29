fname = "romeo.txt"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# count the words in the file
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# find one of the words with the highest counts
highest_value=0
highest_key = ''
for key, value in counts.items():
    print(key, ":",  value)
    if highest_value < value:
        highest_value = value
        highest_key = key

print("highest key: ", highest_key, "highest value: ", highest_value)

# sort the words by frequency by printing out a list of tuples
list_of_tuples = sorted(counts.items(), key=lambda item: item[1])

for x in list_of_tuples:
    print(x)
