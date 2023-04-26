
# 1

def power(a: int, b: int) -> int:
    # BASE CASE: : if either a or b is less than or equal to 0, return -1
    if a <= 0 or b <= 0:              #accepts two integers >0 otherwise returns -1
        return -1

    # BASE CASE: if b is equal to 1, return a
    elif b == 1:
        return a

    # RECURSION
    else:
        return a * power(a, b-1)       #calculates a to the power of b

result = power(2, 10)
print(result)

# 2

def binary_search(numbers, num):
    # BASE CASE: if the list is empty, the element is not in the list
    if not numbers:
        return -1

    # find the midpoint index and value
    mid = len(numbers) // 2
    mid_val = numbers[mid]

    if mid_val == num:
        # the element is found
        return mid

    elif num < mid_val:
        # if the element is less than the midpoint value, search the left half
        return binary_search(numbers[:mid], num)    # Recursion on the left half

    else:
        # if the element is greater than the midpoint value, search the right half
        result = binary_search(numbers[mid+1:], num)    # Recursion on the right half
        # adjust the returned index to be relative to the full list, not just the right half
        return mid + 1 + result if result != -1 else -1

# Usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 5
index = binary_search(numbers, num)
print(index)

num = 20
index = binary_search(numbers, num)
print(index)