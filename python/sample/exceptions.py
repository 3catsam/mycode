
class Calculator(object):

    #def __init__(self):
       # pass

    def power(self, n, p):
        self.n = n
        self.p = p
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p


myCalculator = Calculator()
T = int(raw_input())
for i in range(T):
    n, p = map(int, raw_input().split())
    try:
        ans = myCalculator.power(n, p)
        print ans
    except Exception, e:
        print e