#!/bin/python
'''
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array. 
The respective fractions of positive numbers, negative numbers and zeroes are ,  and , respectively.

'''
import sys


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
po = 0
ne = 0
zo = 0
for i in range(n):
    if arr[i] > 0:
        po += 1
    elif arr[i] < 0:
        ne += 1
    else:
        zo += 1
print '%.6f' % (float(po) / n)
print '%.6f' % (float(ne) / n)
print '%.6f' % (float(zo) / n)
