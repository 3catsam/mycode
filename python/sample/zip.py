'''zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

zip can handle three or more lists as well!'''




list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

com=[]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a>b:
        print a
    else:
        print b