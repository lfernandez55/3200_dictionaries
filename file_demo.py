print("+++++++++++Reading from romeo.txt and printing contents+++++++++++++++++++++++++++++++++++++++++++++++++++")
with open('romeo.txt', 'r') as f:
    data = f.read()
print(data)

print("+++++++++++Writing to romeo.txt and then reading and printing contents again+++++++++++++++++++++++++++++")
with open('romeo.txt', 'w') as f:
    data = f.write('foo bar')

with open('romeo.txt', 'r') as f:
    data = f.read()
print(data)