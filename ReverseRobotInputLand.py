import sys
import math

# Lets find where the robot lands!

c = input().split()  # The sentence containing all the commands
l = []
x = 0
for i in c:
    if i == "Rise": #could have used dictionary, probably wouldve been better/more efficien, but idk i kinda like this. its basic
        x += 2
    elif i == "Fall":
        x -=2
    elif i == "Leap":
        x+= 1
    elif i == "Sink":
        x -= 1
    else:
        x = 0
print(x)

#The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
#1 Test 1 Input Rise Rise
#Expected output 4

#Fall Fall Fall Rise Rise Rise Leap
#1

#Rise Rise Rise Rise Rise Reset Rise
#2


#Rise Leap Leap Rise Fall Leap Rise Rise Reset Leap Fall Rise Leap Rise Fall Sink Sink Leap Sink Leap Reset Fall Leap Sink Rise
# 0

#Sink Fall Sink Fall Reset Sink
#-1

