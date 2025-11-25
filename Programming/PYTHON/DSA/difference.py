def difference_from_average(arr):
    if not arr:
        raise ValueError("Input array cannot be empty.")
    
    average = sum(arr) / len(arr)
    differences = list(map(lambda x: round(x - average, 2), arr))

    return {'average': average, 'differences': differences}

try:
    input_array = [5, 15, 25, 35, 45]
    result = difference_from_average(input_array)
    print(f"Average: {result['average']}")
    print(f"Differences from average: {result['differences']}")
except ValueError as e:
    print(f"Error: {e}")
