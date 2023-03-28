#Reverse mode
#The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
#Test 1
#Input (())
#Expected output 0

#Test 2
#Input )())())
#expected output -3

#Test 3
#Input ()(((()))(()()()((((()(((())(()(()((((((()(()(((())))((()(((()))((())(()((()()()()(((())(((((((())))()()(()(()(())(((((()()()((())(((((()()))))()(())(((())(())((((((())())))(()())))()))))()())()())((()()((()()()()(()((((((((()()())((()()(((((()(((())((())(()))()((((()((((((
#Expected output 66

#Though confusing at first, the given problem wants us to take the amount of right parenthesis subtracts by left parenthesis.

import sys #auto gen by codingame
import math

log = input()
right = log.count('(')
left = log.count(')')

print(right-left)

