#3. week is about loops we will solve some questions 
#-1^n+1 . x^n/n! sum only positive items test it with x=2
import math


'''
x=int(input("enter a value for x please"))

result=0
for n in range(1,8):
    add=((-1)**(n+1)) * (x**n)/math.factorial(n)
    if add>=0:
        print("result:",result)
        result=result+add
    else:
        continue
'''    
    
#QUESTION3 ---------Write a Python program to convert a binary number to a decimal number. Test your program
#i)        x=110.    ii) x= 1010       iii) x= 11101

'''   
elem_num=int(input("enter number of input"))
binary_list=[]
while int(elem_num)>0:
    binary_list.append(input("enter element of binary number digit by digit"))
    elem_num-=1
    
print(binary_list)    

binary_list[::-1]=binary_list
print(binary_list)

add=0
result=0
a=0


for i in range(0,len(binary_list)):
    add=(2 ** a)* int((binary_list[i]))
    a+=1
    result+=add
    print("added:",add)
print("sum of binary is :",result)   
'''
#--------------------QUESTION 4------------------
#What is the greatest common divisor of 54 and 24?
#basicly write common greates divisor finder 

'''
number_list=[]
num1=int(input("enter number one"))
num2=int(input("enter number two"))
number_list.append(num1)
number_list.append(num2)
dividing_one=[]
dividing_two=[]

i=1
a=0

'''

'''main idea is taking all the dividings of both number in one list and find repeated biggest  number
    because it is the answer "
'''
'''
for i in range(1,num1+1):       
    if num1 % i==0:
        dividing_one.append(i)

i=1      
for i in range(1,num2+1):
    if num2 % i==0:
        dividing_one.append(i)     #taking dividing of both numbers one list 

print(dividing_one)        
for x in dividing_one:
    result=dividing_one.count(x)  #finding repeated numbers in the list and put them another list 
    if result != 1:
        dividing_two.append(x)
        dividing_two.sort(reverse=True)  #sorting list from biggest to smallest 
print("greatest common number is:",dividing_two[0]) 

'''

#-----------------QUESTION4-------------------------:
'''
th=0.01
x=1.5708
num1=2
sign=-1
res=1
lastTerm=1

while math.fabs(lastTerm)>th:
    lastTerm=sign*(x**num1)/math.factorial(num1)
    res=res+lastTerm
    num1=num1+2
    sign=sign*(-1)
    
'''

#---------------QUESTION-5-------------------------:
'''
num=int(input("enter your number"))
num_sqr=num ** 2
value=0
i=0
x=1
digit_num=len(str(num))

while x <= (digit_num):
    sayi=str(num_sqr)[-x]
    value+=int(sayi)* (10**i)
    print("value is:",value)
    i+=1
    x+=1
   
if num==value:
    print("number is automorphic")    
'''    
#---------QUESTİON-6---------------------------------:
'''
acc_num=int(input("enter a account number to check"))
summation=0
i=0
x=1

while x <= len(str(acc_num)):
    digit=str(acc_num)[i]
    if x%2!=0:
        summation+=int(digit)
    else:
        summation+=(2*int(digit))
    digit=int(digit)
    digit+=1
    i+=1
    x+=1
    print(summation)

if summation %10 == 0:
    print("account number is valid")
    
'''
#------------------question-7----------------------:
'''
number=int(input("enter a number"))
power=len(str(number))
sum=0
i=0

for  i in range(0, len(str(number))):
    base=str(number)[i]
    sum+=int(base)**power
    i+=1
    
if sum==number:
    print(f"number:{number} is narcissistic number")


'''

#------------------QUESTİON-8-------------------:
'''
num=int(input("enter a number"))
n=0
copy_num=num

while num!=0:
    num=num/10
    n+=1
    print("n is:",n)
if n%2==1:
    i=0
    left_sum=0
    right_sum=0
    num=copy_num
else:
    print("x not number")
    while i<n:
        rem=num%10
        Num=num/10
        if i<(n/2):
            right_sum=right_sum+rem
        elif i>(n/2):
            left_sum=left_sum+rem
            
        i+=1
    if(left_sum==right_sum):
        print("X number")
    else:
        print("x not number")
'''
#--------------------QUESTİON 9 ----------------------:

a=int(input("enter a value for lowe interval"))
b=int(input("enter a value for upper interval "))
tol=0.00001
print("a:",a,"b:",b)
print("tolerance value is:",tol)

f_a=(a**3)-(5*a)-9
f_b=(b**3)-(5*b)-9
print("f(a):",f_a,"\n","f(b):",f_b)    

c=b-f_b*((b-a)/(f_b-f_a)) 
f_c=(c**3)-(5*c)-9   
print("c value is:{} and F(c):{}".format(c,f_c))

while math.fabs(f_c)>tol:
    f_a=(a**3)-(5*a)-9
    f_b=(b**3)-(5*b)-9
    c=b-f_b*((b-a)/(f_b-f_a))
    f_c=(c**3)-(5*c)-9
    if(f_a*f_c)<0:
        
        b=c
    else:
        a=c
    print("new interval is {} to {}".format(a,b))
print("root of function is:{}".format(f_c))    



















        