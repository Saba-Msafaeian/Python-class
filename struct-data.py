x = 12
y = "python"

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

# print(my_list[0])

# print(len(my_list))

# print(my_list[::2])
# print(my_list[::-1])

# print(my_list[-5:-1]+[my_list[-1]])

# print(my_list)

my_list[0] = 101
# print(my_list)

# my_list[1:3] = [1002, 1003, 1004, 1005]
my_list[1:3] = [1002,1003]
# my_list[1:3] = []
# print(my_list)

my_list.insert(4, 'python')
# print(my_list)

my_list.append(True)
# print(my_list)

# new_list = [17,18,19,20]
# res_list = new_list + my_list
# print(res_list)

my_list.remove('python')
# print(my_list)

my_list.pop()
# print(my_list)

my_list.pop(0)
# print(my_list)

my_list.clear()
# print(my_list)

del my_list
# print(my_list)

my_tuple = ('python', 'javascript', 'C++')
# print(my_tuple[0:3:2])

# my_tuple[0] = 2

temp = list(my_tuple)
temp[1] = 'haskell'

temp.append('lua')
temp.append('javascript')

my_tuple = tuple(temp)
del temp

print(my_tuple)

*one, = my_tuple
print(one)
# print(two)
# print(three)

my_set = {2,3,4,5,6,7,8,8,9,1,2}
print(my_set)

new_set = {18,19,20}
new_list = [18,19,20]

my_set.add(13)
my_set.update(new_list)

my_set.remove(4)
my_set.discard(19)

scores = [2,3,4,5,17,18]
# 0 - len(scores) - 1

for i in range(len(scores)):
    pass
    # print(scores[i])

for i in scores:
    pass
    # print(i)

my_tuple = (12,13,14,15)

for i in range(len(my_tuple)):
    pass

for i in my_tuple:
    pass

new_set = {2,3,4,5,6,7,8,9}

for i in new_set:
    print(i)