class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.head=None
    
    def recursion_add(self,node,data):
        if data<node.data:
            if node.left==None:
                node.left=Node(data)
            else:
                self.recursion_add(node.left,data)
        elif data> node.data:
            if node.right==None:
                node.right=Node(data)
            else:
                self.recursion_add(node.right,data)
        
        
    def add(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            self.recursion_add(self.head,data)
    
    def printbst(self):
        if self.head==None:
            return
        else:
            self._printbst(self.head)
    
    def _printbst(self,node):
        if node==None:
            return
        print(node.data)
        self._printbst(node.left)
        self._printbst(node.right)
    
    def _find(self,node,data):
        if node==None:
            return
        if node.data==data:
            return node
        left=self._find(node.left,data)
        right=self._find(node.right,data)
        if right:
            return right
        if left:
            return left
        
    def find(self,data):
        if self.head==None:
            return
        else:
            return self._find(self.head,data)

bst=BST()
bst.add(10)
bst.add(20)
bst.add(5)
bst.add(2)
bst.add(22)
print(bst.find(20))
#bst.printbst()