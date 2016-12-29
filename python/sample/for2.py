a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for x in a:
    if (x%2==0):
        print x


for x in a:
    if (a[x]%2==0):
        print a[x]

# ================================================
# Write your function below!
def fizz_count(x):
    count = 0
#    print x
    for n in x:
#        print n
        if n=='fizz':
            count = count + 1
    print count
    return count
        

fizz_count(["fizz","cat","fizz"])