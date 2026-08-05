#-----------------------------------------LINNKED LISTT------------------------------------

class  Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linnkedlist:
    def  __init__(self):
        self.head=None

    def ins_at_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def ins_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def anypos(self,data):
        newnode=Node(data)
        pos=int(input("enter the position:"))
        if self.head==None:
                    print("list is empty so inserting it in first position:")
                    self.head=newnode
                    return
        if pos==0: 
             newnode=Node(data)
             newnode.next=self.head
             self.head=newnode
        temp=self.head
        count=0
        while temp is not None and count<pos-1:
             temp=temp.next 
             count+=1
        if temp is None:
             print("invalid position:")
             return
        newnode.next=temp.next
        temp.next=newnode

    def display(self):
        temp=self.head
        while temp:
             print(temp.data ,end=" ->")
             temp=temp.next
        print(None)
l=linnkedlist()
l.ins_at_beg(20)
l.ins_at_beg(10)
l.ins_at_end(30)
l.ins_at_end(40)
l.anypos(5)
l.display() 


#wap to move the last node to the begining
#wap to dived an ll into 2 equal half's
#wap to sum of all node values in a ll 
#wap to delete alter nodes from linked
          


        
        

    