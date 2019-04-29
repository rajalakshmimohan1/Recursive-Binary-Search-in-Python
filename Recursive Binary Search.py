
# coding: utf-8

# In[4]:


def binarysearch(arr,first,last,item):
    while(first<=last):
        middle=int((first+last)/2)
        if item==arr[middle]:
            return  middle
        else:
            if item>arr[middle]:
                return binarysearch(arr,middle+1,last,item)
            else:
                 return binarysearch(arr,first,middle-1,item)
    return -1

arr=[20,40,60,90,100]
x=int(input("enter item to be searched for"))
pos=binarysearch(arr,0,(len(arr)-1),x)
if(pos==-1):
    print("not found")
else:
    print("found at pos: ",pos)
    

