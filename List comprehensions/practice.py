# Filter even numbers and square them:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [i ** 2 for i in numbers if i % 2 == 0]
print(result)


# Convert a list of strings to uppercase:
# words = ['hello', 'world', 'python']
# Expected Output: ['HELLO', 'WORLD', 'PYTHON']
words = ['hello', 'world', 'python']
result = [str(x).upper() for x in words]
print(result)

# Extract the first letter of each word:
# words = ['hello', 'world', 'python']
# # Expected Output: ['h', 'w', 'p']
words = ['hello', 'world', 'python']

result = [ str(x)[0] for x in words]
print(result)

# Generate a list of tuples (number, square):
# numbers = [1, 2, 3, 4, 5]
# Expected Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
numbers = [1, 2, 3, 4, 5]

result = [(x, x **2) for x in numbers]
print(result)

# Flatten a nested list:
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

result = [x for sublist in nested_list for x in sublist]
print(result)

