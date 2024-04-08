#----------------QUESTION-1-------------:
import random
import numpy as np
"""
correct_ans=["A","C","A","A","D","B","C","A","C","B","B","A","D","C","A","D","C","B","B","D","A"]
wrong_question_numbers=[]
std_ans=[]
options=["A","B","C","D"]
for i in range(0,20):
    j = random.choice(options)
    std_ans.append(j)
print("Answers of student are:",std_ans)

result=0
for i in range(0,20):
    if(std_ans[i]==correct_ans[i]):
        result+=1
    else:
        wrong_question_numbers.append(i+1)    
       
if result>=15:
    print("Student passed exam,number of correct answered question is:{}".format(result))

else:
    print("Student failed the exam, number of correct answered questions are:{}".format(result))
    
print("Numbers of incorrectly answered questions are:",wrong_question_numbers)    
"""
#-------------------QUESTION-2---------------------:    
"""
def grid():
    magic_square=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            a=random.randint(1,9)
            magic_square[i][j]=a
            
    
    print(magic_square)
    return magic_square


def magic_square_checker(two_dim_list):
    row_sum=[]
    sum_row=0
    sum_col=0
    col_sum=[]
    for i in range(0,3):
        for j in range(0,3):
           sum_row+=two_dim_list[i][j]
        row_sum.append(sum_row)
        sum_row=0
    a=0
    while a<3:
        
        sum_col+=two_dim_list[0][a]
        sum_col+=two_dim_list[1][a]
        sum_col+=two_dim_list[2][a]
        a+=1
        col_sum.append(sum_col)
        sum_col=0
        
    print("sum of each row is:",row_sum)
    print("sum of each columns is:",col_sum)
    
    if(row_sum[0]==row_sum[1]==row_sum[2]) and (col_sum[0]==col_sum[1]==col_sum[2]):
        print("The given 3x3 matrix  is a Magic Square.")
    else:
        print("The given 3x3 matrix is not magic square")
#diagonals are not checked.   
magic_square_checker(grid())
"""
#----------------------QUESTION-3--------------------------:
"""
letter_to_number = {"A": 2, "B": 2,"C": 2,"D": 3, "E": 3,"F": 3,"G": 4,"H": 4,"I": 4,"J": 5,"K": 5,"L": 5,"M": 6,"N": 6,"O": 6,"P": 7,
    "Q": 7,
    "R": 7,
    "S": 7,
    "T": 8,
    "U": 8,
    "V": 8,
    "W": 9,
    "X": 9,
    "Y": 9,
    "Z": 9,
}

user_message=str(input("enter your seven letter message WITHOUT SPACE"))
numbers=[]
for i in range(0,len(user_message)):
    numbers.append(letter_to_number[user_message[i]])

print("555-",end="")
print(*numbers[:3],sep='', end = '')
print('-',end=" ")
print(*numbers[3:7], sep='')


"""
#---------------------QUESTION-4---------------------------:
"""
num_list=[]
for i in range(0,100):
    num_list.append(random.randint(1,10))

my_dict={}
for  i in range(0,10):
    key=i+1
    value=num_list.count(i+1)
    my_dict[key]=value
print(my_dict)
"""

#--------------------QUESTION-5------------------------------:
"""
image=np.random.randint(0,255,size=(32,32))
image_flatten=image.flatten()

W1 = np.random.uniform(0,1, size=(32*32,48))
b1 = np.random.uniform(0,1, size=48)
h1 = np.add(np.matmul(image_flatten, W1), b1)
h1 = np.maximum(0,h1)

W2 = np.random.uniform(0,1, size=(48,3))
b2 = np.random.uniform(0,1, size=3)
o = np.add(np.matmul(h1,W2), b2) #np.matmul is matrix  multiplication

pred = np.argmax(o)

if(pred == 0):
    print("Prediction : Cat")
elif(pred == 1):
    print("Prediction : Dog")
elif(pred == 2):
    print("Prediction : Bird")
"""
#------------QUESTION-6-------------------------------------:
class_array=np.concatenate((np.zeros(40),np.ones(50),2*np.ones(10)))
result_array=np.random.randint(1,3,size=100)

accuracy=np.mean(result_array==class_array)
for i in range(0,3):
    tp=np.sum(np.logical_and(result_array==i,class_array==i))
    fp=np.sum(np.logical_and(result_array==i,class_array!=i))
    fn=np.sum(np.logical_and(result_array!=i,class_array==i))

precision=tp/(tp+fp)
recall=tp/(tp+fn)
f1score=2*(precision*recall)/(precision+recall)

print("Accuracy of the classifier : ", accuracy)
print("Precision for each class : ")
print(precision)
print("\nRecall for each class : ")
print(recall)
print("\nF1 Score for each class : ")
print(f1score)

       