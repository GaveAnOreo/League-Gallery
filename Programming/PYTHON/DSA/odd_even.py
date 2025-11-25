def split_even_odd(arr):
    if not all(isinstance(i, int) for i in arr):
        raise ValueError("All elements in the array must be integers.")
    
    
    even_numbers = list(filter(lambda x: x % 2 == 0, arr))
    odd_numbers = list(filter(lambda x: x % 2 != 0, arr))

    return {'even': even_numbers, 'odd': odd_numbers}
\
try:
    input_array = [11, 22, 33, 44, 55, 66, 77, 88]
    result = split_even_odd(input_array)
    print(f"Even numbers: {result['even']}")
    print(f"Odd numbers: {result['odd']}")
except ValueError as e:
    print(f"Error: {e}") 
