#!/usr/bin/env python
# coding: utf-8

# # LAB 1

# 1. Write a program to denonstrate different numbers of data types in python..

# In[2]:


# we can tell about the data-type/class of a particular variable by using the type() function...

# 1. int 
a = 5
print(a, "is of type", type(a))

# 2. float
b = 2.0
print(b, "is of type", type(b))

# 3. complex
c = 1+2j
print(c, "is of type", type(c))

# 4. boolean
d= True
print(d, "is of type", type(d))

# 5. string
e="Python"
print(e, "is of type", type(e))

# 6. lists
f=[2,3,4,5,6]
print(f, "is of type", type(f))

# 7. tuples
g=(1,2,3,4,5)
print(g, "is of type", type(g))

# 8. sets
h={1,3,5,7,7,5}
print(h, "is of type", type(h))

# 9. dictionaries
i={"key":1,"value":2}
print(i, "is of type", type(i))


# In[ ]:





# In[ ]:





# 2. Write a program to perform different arithmetic operations on numbers in python..

# In[6]:


# here consider any two numbers , such as a=20, b=10
a=25
b=12

  # different arithmetic operations are as follows   


# 1. addition- adds values on either side of operator..
print("the addition of the numbers is",a+b)

# 2. subtraction- Subtracts right hand operand from left hand operand..
print("the subtraction of the numbers is",a-b)

# 3. multiplication- Multiplies values on either side of the operator..
print("the multiplication of the numbers is",a*b)

# 4. division- Divides left hand operand by right hand operand..
print("the division of the numbers is",a/b)

# 5. modulus- Divides left hand operand by right hand operand and returns remainder..
print("the modulus of the numbers is",a%b)

# 6. exponents- Performs exponential (power) calculation on operators
print("the exponential calculation of the numbers is",a**b)

# 7. floor division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
# But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −
print("the floor division of the numbers is",a//b)


# In[ ]:





# In[ ]:





# 3. Write a function that draws a grid like this:
* - - - - * - - - - *
|         |         |
|         |         |
|         |         |
|         |         |
* - - - - * - - - - *
|         |         |
|         |         |
|         |         |
|         |         |
* - - - - * - - - - *

# In[40]:


def line1():
    print('*','-','-','-','-',end=' ')
    print('*','-','-','-','- ', end="*")
    print()

def line2():
    print('|',end='         ')
    print('|',end='         |')
    print()
  

#1. using for loop
# for i in range(1,12):
#     if(i==1 or i==6 or i==11):
#         line1()
#     else:
#         line2()

        
# 2. simply calling the functions linewise..
line1()
line2()
line2()
line2()
line2()
line1()
line2()
line2()
line2()
line2()
line1()

        


# In[ ]:




