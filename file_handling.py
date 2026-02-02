# import sys
# import os
import json

# f = open('docs.txt', 'r')
# print(f.read())
# f.close

# with open('docs.txt', 'r') as file:
#     print(file.read())

# with open('demo.txt', 'w') as file:
#     file.write('write text from python code\n')

# with open('demo.txt', 'a') as file:
#     file.write('append some text into my file')


# with open('temp.txt', 'w') as file:
#     file.write('this is new file')

# os.mkdir('data')
# os.rmdir('data')


with open('data.json', 'r') as file:
    data = json.load(file)

print(data[0]["name"])

var = {
    "Car": {
        "brand": "ford",
        "model": "GT50"
    }
}

jvar = """
{
    "Computer" : {
        "name": "ryzen",
        "Cpu" : "i9",
        "Ram" : "32G"
    }
}
"""

var = json.loads(jvar)
with open("data_temp.json", 'w') as file:
    json.dump(var, file)