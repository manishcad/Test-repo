

class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def solve(self,n1,l1):
        carry=0

        while n1 or l1 or carry:
            v1= n1.val if n1  else 0
            v2=l1.val if l1 else 0

            value=int(v1)+int(v2)+carry
            carry=value//10
            val=value%10
            print(val)
            #print(carry)
            if n1:
                n1=n1.next
            if l1:
                l1=l1.next

#1234
#5678
n1=Node(1)
n2=n1.next=Node(2)
n3=n2.next=Node(3)
n3.next=Node(4)

l1=Node(5)
l2=l1.next=Node(6)
l3=l2.next=Node(7)
l4=l3.next=Node(8)

s=Solution()
s.solve(n1,l1)