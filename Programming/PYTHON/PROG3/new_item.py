class ArrayOperations:
    def __init__(self, elements):
        if not all(isinstance(i, int) for i in elements):
            raise ValueError("All elements must be integers.")
        self.arr = elements

    def append(self, new_item):
        if not isinstance(new_item, int):
            raise TypeError("Only integer values can be appended.")
        self.arr.append(new_item)
        return self.arr

try:
    array_op = ArrayOperations([10, 20, 30, 40])
    updated_array = array_op.append(50)
    print(f"Updated array: {updated_array}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")