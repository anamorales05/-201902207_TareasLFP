import csv

with open('tarea python/tarea2.csv', newline='') as File:
    reader = csv.reader(File)
    for document in reader:
        print(document)