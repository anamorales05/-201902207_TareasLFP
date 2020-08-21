import json
def tarea():
    file = open('tarea python/tarea2.json')
    data = json.load(file)
    file.close()
    return data

document = tarea()
for element in document:
    print(element)
