#ilk hafta aritmetik operatörler ve koşullu ifadelere kadar geldik.
'''
print("sayimiz 1256.2164864864 ")
print("format (sayi.virgüllü kisim \".2f \" ile sayiyi formatlayabiliyoruz\n ",format(1256.2164864864,".2f")) 
'''
"""
print("Python Programming course will be funny.")
print("Python Programming \
    course will be funny.")
print("one","two","three",sep="----")

"""

#3 sayı al azalan ve artan ise sırasıyla sonucu doğru değilse false bunu boolean bir veri tutucu ile sakla
#ve boolean veri tutucuyu printle
"""
x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
result=""

if (x<y and y<z):
    result=True
elif (z<y and y<x):
    result=True
else:
    result=False 
      
print(result)  
"""

#q3:

"""
y0 =y - (14 - m) / 12
x = y0 + y0/4 - y0/100 + y0/400
m0 = m + 12 * ((14 - m) / 12) - 2
d0 = (d + x + (31*m0)/ 12) mod 7


"""

"""

d=int(input("enter a number"))
m=int(input("enter a number"))
y=int(input("enter a number"))

y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31*m0)//12) % 7

if d0==0:
    print("sunday")
elif d0==1:
    print("monday")
elif d0==2:
    print("tuesday")    
elif d0==3:
    print("wednesday")
elif d0==4:
    print("thirsday") 
elif d0==5:
    print("friday") 
elif d0==6:
    print("saturday") 
"""
"""    
#q4
r=int(input("enter a number"))
g=int(input("enter a number"))
b=int(input("enter a number"))

w = max(r/255, g/255, b/255) 
c = (w - r/255) / w
m = (w - g/255) / w
y = (w - b/255) / w
k = 1 - w    
print("c y m k is:",c,y,m,k)

"""


"""
#q5  If a<b+c and b<a+c and c<b+a, the result must be True
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
result=""

if a<b+c and b<a+c and c<b+a:
    result=True
else:
    result=False
    
print(result)    
"""
#q6

x=int(input("enter a value please"))

if x<-3:
    result=(x**3 +4)/x**2

elif x>=-3 and x<0:
    result=x**2 + 3*x -10
    if result<0:
        result=result*-1
elif x>=0 and x<4:
    result=x**2 - 4*x 
    
print(result)           
















