n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
    result=[]
    for i in lists:
        for n in i:
            result.append(n)
    return result


print flatten(n)