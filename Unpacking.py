# the values in a tuple are called "packed". The reverse operation is called "unpacking".

# DOUBLE ASTERIKS 
# unpacks all iterable values that haven't been assigned to any variable.
start, *middle, end = [1, 2, 3, 4, 5]
print(start)   # 1
print(end)     # 5
print(middle)  # [2, 3, 4]

#In the example below, the middle variable ends up being an empty list. Example 1:
start, *middle, end = [1, 2]
print(start)   # 1
print(end)     # 2
print(middle)  # []

#Example 2:
nums = [1, 2, 3]
def multiply(num_1, num_2, num_3):
    return num_1 * num_2 * num_3
multiply(*nums)  # 6

#Example 3:
nums = [1, 2, 3]
more_nums = [4, 5, 6, 7]
all_nums = [*nums, *more_nums]
print(all_nums)  # [1, 2, 3, 4, 5, 6, 7]

#Example 4:  (prints only the keys)
my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
print(*my_dict)  # apple banana pear

# DOUBLE ASTERIKS
# prints the values of dictionaries
my_dict = {'apple': 1, 'banana': 2, 'pear': 3}

def fruit_sum(apple, banana, pear):
  return apple + banana + pear

print(fruit_sum(**my_dict)) # 6
# merge 2 dictionaries
dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'one': 'two', 'three': 'four'}

dict_3 = {**dict_1, **dict_2}  # {'a': 1, 'b': 2, 'c': 3, 'one': 'two', 'three': 'four'}

# create a copy of a dictionary and update its values at same time
my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
my_dict_copy = {**my_dict, 'apple': 100}
print(my_dict_copy) # {'apple': 100, ' banana': 2, 'pear': 3}