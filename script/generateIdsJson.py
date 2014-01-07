import sys, os

file_from_name = '../data/tweetIds.txt'
file_to_name = '../json/tweetIds.json'
if os.path.exists(file_to_name):
    os.remove(file_to_name)

file_from = open(file_from_name, 'r')
file_to = open(file_to_name, 'a')

file_to.write('{"ids":[')
lines = file_from.readlines()
ids = []
for line in lines:
    line = line.strip()
    if len(line) != 0:
        ids.append(line)
for i in range(len(ids) - 1):
    file_to.write('{"id": "' + ids[i] + '"},')
file_to.write('{"id": "' + ids[len(ids) - 1] + '"}')
file_to.write(']}')

file_from.close()
file_to.close()