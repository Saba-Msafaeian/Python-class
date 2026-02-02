# import expert_function
import expert_function as exf

from expert_function import time_calculate as tc

# print(list(expert_function.even_numbers(12)))
print(list(exf.even_numbers(12)))

@tc
def some_thing(n):
    return n

