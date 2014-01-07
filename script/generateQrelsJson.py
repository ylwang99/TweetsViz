import sys, os

file_from_name = '../data/qrels.txt'
file_to_name = '../json/qrels.json'
if os.path.exists(file_to_name):
    os.remove(file_to_name)

file_from = open(file_from_name, 'r')
file_to = open(file_to_name, 'a')

file_to.write('{"qrels":[')
lines = file_from.readlines()
ids = []
rels = []
for line in lines:
    line = line.strip().split()
    if len(line) != 0:
        ids.append(line[2])
        rels.append(line[3])
for i in range(len(ids) - 1):
    file_to.write('{"id": "' + ids[i] + '", "rel": "' + rels[i] + '"},')
file_to.write('{"id": "' + ids[len(ids) - 1] + '", "rel": "' + rels[len(ids) - 1] + '"}')
file_to.write(']}')

file_from.close()
file_to.close()