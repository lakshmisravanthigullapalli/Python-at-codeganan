a=10
b=20
print(a is b)
a=10
b=a
print(a is b)
x = 10
y = 10
print(x is y)
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (values same)
print(a is b)   # False (memory different)  
 
