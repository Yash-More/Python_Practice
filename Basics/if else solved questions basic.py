#!/usr/bin/env python
# coding: utf-8

# In[4]:


name = ("Python")
if 'a' in name:
    print("Yes")
else :
    print("Not")


# In[9]:


a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))
c = int(input("Enter the Number:"))
if a > b:
    print(a," is greater")
elif b>c:
    print(b," is greater")
else :
    print(c," is greater")


# In[30]:


a = int(input("Enter the year"))
if (a%4==0 and (a%400==0 or a%100!=0)):
    print("Its Leap year:")
else:
    print("Not leap year")


# In[34]:


wd = int(input("Enter the working days:"))
pd = int(input("Enter the persent days:"))
percentage =(pd/wd)*100
print(percentage)
if percentage > 75:
    print("Student will able to sit in exam")
else :
    print("Student will not able to sit in exam")
    


# In[37]:


a = input("Enter the vowel:")
if 'a' in 'aeiousAEIOUS':
    print("Vowel")
else:
    print("Not vowels")


# In[38]:


num = int(input("Enter the Number:"))
if num ==1:
    print("Sunday")
elif num ==2:
    print("Monday")
elif num ==3:
    print("Tuesday")
elif num ==4:
    print("Wednesday")
elif num ==5:
    print("Thursday")
elif num ==6:
    print("Friday")
elif num == 7:
    print("Saturday")    
else:
    print("Invaild input:")


# In[41]:


city = input("Enter the City:")
if city == 'delhi':
    print("Redfort")
elif city == 'Agra':
    print("Taj Mahal")
elif city == 'jaipur':
    print("Jal Mahal")
else :
    print("Enter wrong city:")


# In[43]:


Age = int(input("Enter the age:"))
if Age >= 18:
    print("Eligible for voting")
else :
    print("not Eligible for voting")


# In[47]:


print("basic Calculator")
n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
print("Which expression you want to perform:")
print("1. + (Addition)")
print("2. - (Subtraction)")
print("3. * (Multiplication)")
print("4. / (Division)")
print("5. ** (Exponentiation)")
print("6. // (Floor division)")
print("7. % (Modulus)")
num = int(input("Enter the Experssion Number:"))
if num == 1:
    print("Additon",n1+n2)
elif num == 2:
    print("Substraction",n1-n2)
elif num == 3:
    print("Multiplication",n1*n2)
elif num == 4:
    print("Division",n1/n2)
elif num == 5:
    print("Exponentiation",n1**n2)
elif num == 6:
    print("Floor Division",n1//n2)
elif num == 7:
    print("Modules",n1%n2)
else:
    print("Enter The Wrong Input:")


# In[50]:


a = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
if a == b :
    print("Its Square")
else:
    print("not Square")


# In[ ]:




