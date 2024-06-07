# Python List Methods with Examples



# 1. append()

# Adds a single element to the end of the list.



my_list = [1, 2, 3]

my_list.append(4)

print(my_list) # Output: [1, 2, 3, 4]



# 2. extend()

# Adds all elements of an iterable (like another list) to the end of the list.



my_list = [1, 2, 3]

my_list.extend([4, 5])

print(my_list) # Output: [1, 2, 3, 4, 5]



# 3. insert()

# Inserts an element at a specified position.



my_list = [1, 2, 3]

my_list.insert(1, 'a')

print(my_list) # Output: [1, 'a', 2, 3]



# 4. remove()

# Removes the first occurrence of a specified value.



my_list = [1, 2, 3, 2]

my_list.remove(2)

print(my_list) # Output: [1, 3, 2]



# 5. pop()

# Removes and returns the element at the specified position. If no index is specified, it removes and returns the last item.



my_list = [1, 2, 3]

item = my_list.pop(1)

print(item) # Output: 2

print(my_list) # Output: [1, 3]



# 6. clear()

# Removes all elements from the list.



my_list = [1, 2, 3]

my_list.clear()

print(my_list) # Output: []



# 7. index()

# Returns the index of the first occurrence of a specified value.



my_list = [1, 2, 3, 2]

index = my_list.index(2)

print(index) # Output: 1



# 8. count()

# Returns the number of occurrences of a specified value.



my_list = [1, 2, 3, 2]

count = my_list.count(2)

print(count) # Output: 2



# 9. sort()

# Sorts the list in ascending order by default. You can specify the reverse parameter to sort in descending order.



my_list = [3, 1, 2]

my_list.sort()

print(my_list) # Output: [1, 2, 3]



my_list.sort(reverse=True)

print(my_list) # Output: [3, 2, 1]



# 10. reverse()

# Reverses the elements of the list in place.



my_list = [1, 2, 3]

my_list.reverse()

print(my_list) # Output: [3, 2, 1]



# 11. copy()

# Returns a shallow copy of the list.



my_list = [1, 2, 3]

new_list = my_list.copy()

print(new_list) # Output: [1, 2, 3]



# 12. len()

# Although not a method, len() is a built-in function that returns the number of items in a list.



my_list = [1, 2, 3]

length = len(my_list)

print(length) # Output: 3