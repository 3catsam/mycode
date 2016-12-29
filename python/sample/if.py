def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Make sure that the_flying_circus() returns True
def the_flying_circus(a):
    if a>1 and a<5:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return 0
    elif a>6 or a<1:
        # Keep going here.
        # You'll want to add the else statement, too!
        return 1
    else:
        print "no true"
print "the_flying_circus(4) ",the_flying_circus(4)


# Make sure that the_flying_circus() returns True
def the_flying_circus2():
    if 1==1 and 2==2:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return True
    elif 1==1 or 1<1:
        # Keep going here.
        # You'll want to add the else statement, too!
        return True
    else:
        print "no true"
print "the_flying_circus2 ",the_flying_circus2()