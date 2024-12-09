import copy

x = frozenset([1, 2, 3, 4, 5])
y = frozenset([5, 6, 7, 8, 9])

a = copy.copy(x) 
z = copy.deepcopy(x) 

print(id(x))
print(id(z)) 
print(id(a)) 