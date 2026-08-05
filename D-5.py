#------------------------------------------------LINKED LIST---------------------------------------------------------
#1.find all pairs who sum is equal to the given number
#2.sort the array without using bulit in sort fun
#3.union of 2 arrayys
#4.find the 1st non repeating ele in array
#5.re-arrange the array so that +ve & -ve num alternate 


#-----------------1.answer-------------
# li=[10,8,6,5,2,33,4,3]
# n=len(li)
# gn=int(input("enter the number:"))
# sum=0
# p=[]
# for i in range(n):
#     for j in range(i+1,n):
#         if gn==li[i]+li[j]:
#             p.append((li[i],li[j]))
# print(p)

#----------------2.answer---------------

# arr=[10,8,6,5,2,33,4,3]
# n=len(arr)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr)

#---------------3.answer------------------

# li=[10,8,6,5,2,33,4,3]
# l2=[10,33,6,8,18,7,9,3]
# s=set()
# # for i in li:
# #     s.add(i)
# # for j in l2:
# #     s.add(j)
# # print(s)
# s1=set(li)
# s2=set(l2)
# u=s1.union(s2)
# print(u)

#-------------4.answer---------------

# arr=list(map(int,input("enter the ele").split()))
# arr.sort()
# print(arr)
# n=len(arr)
# d=[]
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i]!=arr[j]:
#             d.append(arr[i])
# print(d)

#-----------------------------------------TWO POINTERS METHOD------------------------------------

# li=[50,40,30,20,10]
# n=len(li)-1
# left=0
# right=n
# while left<right:
#     li[left],li[right]=li[right],li[left]
#     left+=1
#     right-=1
# print(li)

#---------------------------1.plaindrom-----------------------------


# li=input()
# l1=list(li)
# n=len(li)-1
# left=0
# right=n
# while left<right:
#      l1[left],l1[right]=l1[right],l1[left]
#      left+=1
#      right-=1
# rev="".join(l1)
# if li==rev:  
#     print("palindrom")
# else:
#      print("not a plaindrom")

#------------------------------------------------------
#1.remove duplicate from sorted arr
#2.merge to sorted arr
#3.sqr of 2 sorted arrays

#-----------1.answer---------
# li=list(map(int,input("enter the array:").split()))
# left=0
# right=1
# while left < right:
#       if li[left]>li[right]:
#             li[left],li[right]=li[right],li[left]
#       if li[left]==li[right]:
#             li.remove()
#       left+=1
#       right-=1
# print(li)

#------------------------------------------LINKED LIST--------------------------------------    



#linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def insertAtBeg(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def  innsertataypos(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head==newnode
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
            

    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
       
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="")
            print("->",end="")
            temp=temp.next
l=linked_list()
l.insertAtBeg(10)
l.innsertataypos(40)
l.insertAtEnd(20)
l.insertAtEnd(30)
l.insertAtBeg(10)
l.display()


        








        
