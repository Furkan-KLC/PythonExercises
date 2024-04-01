import random as r 
from sympy import * 
import math
#-------QUESTION 1 ------------------:
'''
def points(w,d,l):
    point=(w*3) + (d*1) + (0*l)
    return point


def main():
    won=r.randint(15,25)
    draw=r.randint(3,6)
    lost=30-(won+draw)
    point_a=points(won,draw,lost)
    print("point A is:",point_a)
    won=r.randint(15,25)
    draw=r.randint(3,6)
    lost=30-(won+draw)
    point_b=points(won,draw,lost)
    print("point B is:",point_b)
    won=r.randint(15,25)
    draw=r.randint(3,6)
    lost=30-(won+draw)
    point_c=points(won,draw,lost)
    print("point C is:",point_c)
    if point_a>point_b and point_a>point_c:
        print("champion is team A")
    if point_b>point_a and point_b>point_c:
        print("champion is team B")
    if point_c>point_a and point_c>point_b:
        print("champion is Team C")

main()  
'''

#----------QUESTION 2 ------------------------------:
'''
def points(w,d,l):
    point=(w*3) + (d*1) + (0*l)
    return point

def generate():                                 #basicly we create another funciton for random win lost
    win=r.randint(15,25)                        #numbers and code in main function became shorter.
    draw=r.randint(3,6)
    lost=30-(win+draw)
    return win,draw,lost

def main():
    w,d,l=generate()
    point_a=points(w,d,l)
    print("point A is:",point_a)
    w,d,l=generate()
    point_b=points(w,d,l)
    print("point B is:",point_b)
    w,d,l=generate()
    point_c=points(w,d,l)
    print("point C is:",point_c)
    if point_a>point_b and point_a>point_c:
        print("champion is team A")
    if point_b>point_a and point_b>point_c:
        print("champion is team B")
    if point_c>point_a and point_c>point_b:
        print("champion is Team C")

main()
'''

#----------------------QUESTİON-3----------------------------:
'''
def division(n1,n2):
    quotient=n1//n2
    remainder=n1%n2
    return quotient,remainder

def main():
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    print("numbers are {} {}".format(num1,num2))
    result,remain=division(num1,num2)
    print("quotient is:{} remainder is:{}".format(result,remain))
    
main()
'''

#----------------------QUESTİON-4----------------:
'''
tolerance=1e-15

def root(a):
    x_n=a
    i=0
    while abs(x_n - a/x_n) > tolerance:    
        x_n=(a/x_n+x_n)/2.0
        i=i+1
    
    return x_n,i

def main():
    x=int(input("enter x"))
    sqr_root,iter_num=root(x)
    print("entered number is",x)
    print("square root of number is ",sqr_root)
    print("number of iteration is",iter_num)
    
main()
'''

#----------------QUESTION-5-------------------:
'''
tolerance=1e-15
def root(a):
    x_n=a
    i=0
    x=Symbol('x')
    f=x**2-11*x+28
    fPrime=f.diff()
    
    f_value = lambdify(x, f, 'numpy')
    fPrime_value = lambdify(x, fPrime, 'numpy')
    
    while abs(f_value(x_n)/fPrime_value(x_n)) > tolerance:    
        x_n=x_n-(f_value(x_n)/fPrime_value(x_n))
        i=i+1

    return x_n,i

def main():
    num=int(input("enter a number to find square rooot"))
    s_root,iter_num=root(num)
    print("number is:{} Square root is:{} iteration number is{}".format(num,s_root,iter_num))

main()
'''
'''
#------------------------ Question-6 -----------------------------------------------:
def primes(sayi):
    if sayi>1:
        for y in range(2,sayi):
            print("y is:",y)
            if (sayi % y ==0):
                print("number is not prime")
                return 0
        else:
            print("number is prime")
            return 1        
    else:
        print("can't decide")
        
def main():
    num=int(input("enter a number"))
    print("entered number is:",num)
    result=primes(num)
    print(result)
main()   

'''

#-------------------------------QUESTION-7----------------------------------:
'''
def prime_factor(n):
    factor = 2
    while factor*factor <= n:
        while n % factor == 0:
            # Cast out and write factor.
            n = n//factor
            print(factor, ' ')
        factor = factor+1

    print(n)

def main():
    x=int(input('Enter number'))
    prime_factor(x)
    
main()    
'''

#--------------------QUESTION -8 -------------------------------:

def main():                              
    number=int(input('Enter number '))   
    print(number)                        
    primes(number)                       
    
def primes(n):                          
    for i in range(1, n+1):
        print(i,"",end='')
    print()
    for i in range(1, n+1):             
        for j in range(1, n+1):         
            if math.gcd(i,j)==1:        
                print("* ",end='')      
            else:                       
                print("  ",end='')      
        print(i)                       
            
main()                              

        



        







































