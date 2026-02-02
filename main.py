# name = input("please enter your name : ")
# age = int(input("please enter your age : "))

# hello my name is mhdi and i am 20 years old

# print("hello my name is " + name + " and i am " + str(age) + " years old")
# print("hello my name is {} and i am {} years old".format(name, age))
# print(f"hello my name is {name} and i am {age} years old")
# print("hello my name is %s and i am %d years old"%(name, age))


# number = int(input("Please write a number: "))

# is_prime = True # flag
# for i in range (2, number):
#     if number % i == 0:
#         is_prime = False
#         break
    
# if is_prime :
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")

#

# print(add(12, 4) + 16)

# 0 1 1 2 3 5 8 13 21 ...

# def fibonnaci (s1 , s2): 
#     s3 = 0
#     for i in range (10):
#         s3 = s1 + s2
#         print(s3)
#         s1 = s2
#         s2 =  s3
            
    
# fibonnaci(0 , 1)

def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        a,b = 0,1
        c = 0
        i = 2
        while(i < n):
            c = a + b
            a = b
            b = c
            i += 1
        return c

# 0 1 1 2 3 5
print(fibonacci(6))


# 2456
def number_counter(n):
    count = 0

    if n == 0:
        count = 1
    else:
        while n > 0:
            n //= 10
            count += 1

    return count
   
i = 0
n = 4
# digits = 5

while (i < 8):
    if (is_prime(fibonacci(n))):
        if (number_counter(fibonacci(n)) == 5):
            print(fibonacci(n))
        i += 1
    n += 1

# print(number_counter(-123))