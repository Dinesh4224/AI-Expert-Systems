# Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Length
length = len(nested_list)
print("Length:", length)

# Concatenation
concatenation = nested_list + [[10, 11, 12]]
print("Concatenation:", concatenation)

# Membership
print("Membership:", 3 in [1, 2, 3])

# Iteration
print("Iterations")
for sublist in nested_list:
    for element in sublist:
        print(element,"\t")

# Indexing
index = nested_list[1][2]
print("Indexing:", index)

# Slicing
slice = nested_list[1:]
print("Slicing:", slice)
