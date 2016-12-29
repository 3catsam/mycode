def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!

print range(6) # => [0,1,2,3,4,5]
print range(1,6) # => [1,2,3,4,5]
print range(1,6,3)