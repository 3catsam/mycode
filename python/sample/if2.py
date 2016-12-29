def distance_from_zero(num):
    if type(num)==int or type(num)==float:
        return abs(num)
    else:
        return "Nope"
print distance_from_zero(-20)
print distance_from_zero("-20")
