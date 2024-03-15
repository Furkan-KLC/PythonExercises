#week 2-lab experiment codes
import math
#qestion1-------------------
'''
a1=int(input("enter a value for A1"))
b1=int(input("enter a value for B1"))
angle=int(input("enter a value for angle"))

A1=math.sqrt(a1**2+b1**2)
angle=-math.atan2(b1/a1)
g1=A1*math.cos(math.pi/4+angle)

#question2-------------------
#𝑦 = 𝑓(𝑥1 ∗ 𝑤1 + 𝑥2 ∗ 𝑤2 + 𝑏)

x1=int(input("enter value of x1"))
x2=int(input("enter value of x2"))
w1=int(input("enter value of w1"))
w2=int(input("enter value of w2"))
b=int(input("enter value of b"))

y_value=(x1 * w1 + x2 * w2 + b)

sigmoid_func=1 / (1+e**-y)

print("result of output:",sigmoid_func)

'''
#---------------------------------------
'''
sopen=float(input("enter value for sopen"))
sclose=float(input("enter value for sclose"))
ssemiopen=float(input("enter value for semiopen"))

popen=math.exp(sopen)/(math.exp(sopen)+math.exp(sclose)+math.exp(ssemiopen))
pclose=math.exp(sclose)/(math.exp(sopen)+math.exp(sclose)+math.exp(ssemiopen))
psemiopen=math.exp(ssemiopen)/(math.exp(sopen)+math.exp(sclose)+math.exp(ssemiopen))
output=""

if popen>pclose:
    if popen>psemiopen:
        output="open door"
    elif popen<psemiopen:
        if pclose< psemiopen:
            output="semi open door"

if popen<pclose:
    if pclose>psemiopen:
        output="close door"


print("output is:",output)
'''
#--------question8----------------------------------------------------

goal=float(input("enter value of goal"))
dist=float(input("enter value for distance"))
message=""

if goal==1 and  dist >= 16.5:
    message="he scores,absolutely brilliant !"
elif goal==1 and dist <=16.5:
    if dist>= 5.5:
        message="A fantastic move and a good finish !"
    else:
        message="he finds the net with ease !"
else:
    message="he should have scored"

print(message)
















