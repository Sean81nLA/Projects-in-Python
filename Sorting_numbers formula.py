#!/usr/bin/env python
# coding: utf-8

# In[ ]:


myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop
step=0
while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            step+=1
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            print('step:',step,end="")
            print(myList)
print(myList)

