def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %.2f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %.2f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


# Define your spam function starting on line 5. You
# can leave the code on line 11 alone for now--we'll
# explain it soon!
def spam():
    """print word 'Eggs!'"""
    print "Eggs!"

# Define the spam function above this line.
spam()


def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.

square(10)


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(5,4)  # Add your arguments here!


def one_good_turn(n):
    return n + 1
def deserves_another(n):
    return one_good_turn(n) + 2
print one_good_turn(5)
print deserves_another(5)



def cube(number):
    number *=number**2
    return number
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print by_three(6)