def add(x, y, *args, **kwargs):
    return x + y

def calc(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return add, sub, mul, div

x, y, z, w = calc(y = 12,x = 4)



# print(x)

def even_numbers(n=10):
    # lst = []
    for i in range(n):
        if not i % 2:
            yield i
            # lst.append(i)
    # return lst
    

def odd_numbers():
    n = 1
    while True:
        if n % 2:
            yield n
        n += 1

g = odd_numbers()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for _ in range(10):
    pass
    # print(next(g))

# def comp_add(lst):
#     x = 0
#     for i in range(len(lst)):
#         x = lst[i] + x
#     return x

# test_list = [1,1,1]

# print(comp_add(test_list))

def comp_add(*args):
    res = 0
    for i in args:
        res += i
    return res

# print(comp_add(2,3,4,5,6,7,1,0))

# def welcome(dict):
#     print(f"welcome {dict['name']}")

def welcome(**kwargs):
    print(f"welcome {kwargs['name']}")

# welcome(name='mhdi', xp=12, desc='welcome to user')

# print(add(12,3,5))


temp = add
temp(12, 3)

def low(txt):
    return txt.lower()

def up(txt):
    return txt.upper()

def greet(txt, func):
    print(func(txt))

# greet('Hello', low)

# def radical2(n):
#     return n ** (1/2)

# def radical3(n):
#     return n ** (1/3)


def radical(unit):
    def calc(n):
        return n ** (1/unit)
    return calc

def old_radical(n, unit):
    return n ** (1/unit)

radical2 = radical(2)
radical3 = radical(3)
radical4 = radical(4)

# print(old_radical(unit = 2, n = 4))
# print(radical2(4))

def hello_deco(func):
    def _inner():
        print('hello')
        func()
        print("bye...")
    
    return _inner

@hello_deco
def into_deco():
    print("i am in third party function")

# into_deco()
# res = hello_deco(into_deco)
# res()



import time
# print(time.strftime("%a %d %b %u %Y %H:%M:%S"))

# print("Hello")
# time.sleep(2)
# print("world")

# print(time.time()) # 1 1 1970 0:0:0

# begin = time.time()
# is_prime(69)
# end = time.time()

# end - begin

def time_calculate(func):
    def _inner(*args, **kwargs):
        begin = time.time()
        temp = func(*args, **kwargs)
        end = time.time()

        print(f"runtime of function is {end - begin}")
        print(f"answer of function is {temp}")
    
    return _inner

@time_calculate
def is_prime(n):
    time.sleep(2)
    for i in range(2, n):
        if not n % i:
            return False
    return True

# for i in range(2, 200, 2):
#     is_prime(i)

@time_calculate
def my_add(x,y):
    return x + y

# my_add(12,4)

if __name__ == "__main__":
    print(x, y, z , w)
    print(list(even_numbers()))
