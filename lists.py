# Give the length of a list.
# Don't use `len`!
# You can check if a list has NO items by comparing it using == to an empty list, i.e., [].
# This is your base case!

print("\n### length")
def length(arr):
  pass;

result1 = length([3, 4, 6, 8, 13])
print(f"length([3, 4, 6, 8, 13]) should be 5 and is, in fact: {result1}")

result2 = length([1, 3, 5, -8, 4, 0, -100, 0.5])
print(f"length([1, 3, 5, -8, 4, 0, -100, 0.5]) should be 8 and is, in fact: {result2}")

print("\n### sum_list")
# Finish the sum_list function, which takes in a list of numbers and returns the sum of all its numbers.
# What's your base case?
# What is the value you want to pass to the next level?
def sum_list(nums):
  pass;

result1 = sum_list([])
print(f"sum_list([]) should be 0 and is, in fact: {result1}")

result2 = sum_list([3])
print(f"sum_list([3]) should be 3 and is, in fact: {result2}")

result3 = sum_list([3, 4, 5])
print(f"sum_list([3, 4, 5]) should be 12 and is, in fact: {result3}")

print("\n### product_of_list")
# Finish the product_of_list function, which takes in a list of numbers and returns the product of all its numbers. (All numbers multiplied together.)
def product_of_list(nums):
  pass;

result1 = product_of_list([3])
print(f"product_of_list([3]) should be 3 and is, in fact: {result1}")

result2 = product_of_list([3, 4, 5])
print(f"product_of_list([3, 4, 5]) should be 60 and is, in fact: {result2}")

print("\n### sum_of_a_nested_list")
# Give the sum of a list with lists inside it (and possibly lists inside those, forever and ever, amen).
def sum_of_a_nested_list (nums):
  pass;

result1 = sum_of_a_nested_list([])
print(f"sum_of_a_nested_list([]) should be 0 and is, in fact: {result1}")

result2 = sum_of_a_nested_list([3])
print(f"sum_of_a_nested_list([3]) should be 3 and is, in fact: {result2}")

result3 = sum_of_a_nested_list([[3], 4, 5])
print(f"sum_of_a_nested_list([3, 4, 5]) should be 12 and is, in fact: {result3}")

result4 = sum_of_a_nested_list([[3], [6, [4, 5]]])
print(f"sum_of_a_nested_list([[3], [6, [4, 5]]]) should be 18 and is, in fact: {result4}")

