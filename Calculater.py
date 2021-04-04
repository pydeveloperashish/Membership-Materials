#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=int(input("Enter the value of X: "))
y=int(input("Enter the value of y: "))

function=int(input("press 1 for add, press 2 for sub, press 3 for mult, press 4 for div: "))

choices=[1,2,3,4]

def add(x,y):
    return print(x+y)

def sub(x,y):
    return print(x-y)

def mult(x,y):
    return print(x*y)

def div(x,y):
    return print(x/y)
    
if function not in choices:
    for i in range(1,4):
        if function not in choices:
            print("invalid number")
            function=int(input("press 1 for add, press 2 for sub, press 3 for mult, press 4 for div: "))
            if i==3 and function not in choices:
                print("You have reached limit of invalid numbers")
        else:
            break
    
if function==1:
    add(x,y)
    
elif function==2:
    sub(x,y)
    
elif function==3:
    mult(x,y)
    
elif function==4:
    div(x,y)
    

    


# In[ ]:




