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
    
#Write a Python program to convert a binary number to a decimal number. Test your program
#i)        x=110.    ii) x= 1010       iii) x= 11101
   
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
b=0


for i in range(0,3):
    add=int((2 ** a) * binary_list[b])
    a+=1
    b+=1
    result+=add
    print(result)
print(result)   



   

