import sys


class Solution:

    def __init__(self):
        self.mystack = list()
        self.myqueue = list()
        return(None)

    def pushCharacter(self, char):
        self.mystack.append(char)
        #print self.mystack
    def popCharacter(self):
        return(self.mystack.pop(-1))
        #print self.mystack.pop(-1)
    def enqueueCharacter(self, char):
        self.myqueue.append(char)
        #print self.myqueue
    def dequeueCharacter(self):
        return(self.myqueue.pop(0))
        #print self.myqueue

# read the string s
s = raw_input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l / 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        print obj.popCharacter(),"and",obj.dequeueCharacter()
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write("The word, " + s + ", is a palindrome.")
else:
    sys.stdout.write("The word, " + s + ", is not a palindrome.")
