def add_numbers(a, b):
    return a + b

def sum_list(lst):
    return reduce(add_numbers, lst, 0)

from functools import reduce

# Lista de números para somar
numbers = [1, 2, 3, 4, 5]

# Calculando a soma da lista
result = sum_list(numbers)

print(result)  # Saída: 15
