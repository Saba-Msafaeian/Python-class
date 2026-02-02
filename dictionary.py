car = {
    'brand': 'Ford',
    'name': 'Mustang',
    'year': [1969, 1970]
}

# print(car['year'])

# car['name'] = 'GT50'
# print(car)

# car['color'] = 'blue'
# print(car)

# car.pop('year')
# print(car)

# car.popitem()
# print(car)

# for i in car:
#     print(i , car[i])

# print(car.keys())
# print(car.values())
# print(car.items())

for i, j in car.items():
    pass
    # print(i, j)


lst = [2,3,4,5,6,7,8,9]

for idx, item in enumerate(lst):
    pass
    # print(idx, item)


library = {}



family = {
    "dad" : {
        "name": "bob",
        "age" : 40
    },
    "mom": {
        "name": "sara",
        "age": 40
    },
    "child": {
        "name": "rose",
        "age": 10
    }
}

# print(family['dad']['name'])


employees = [
    {
        "name": "alex",
        "xp": 10,
        "job" : "backend developer"
    },
    {
        "name" : "anne",
        "xp": 7,
        "job": "AI"
    }
]

# print(employee[0])

for employee in employees:
    if employee['job'] == "AI":
        print(employee['name'])