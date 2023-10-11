class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary_Tree:
    def __init__(self):
        self.root=None
    
    def _add(self,node,data):
        if node.left==None:
            node.left=Node(data)
        else:
            self._add(node.left,data)
    def add(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._add(self.root,data)
    
    def _printtree(self,node):
        if node==None:
            return
        print(node.data)
        #self._printtree(node.left)
        self._printtree(node.right)
    def printtree(self):
        if self.root==None:
            return
        self._printtree(self.root)

bt=Binary_Tree()
bt.add(10)
bt.add(20)
bt.add(30)
bt.add(30)
bt.add(30)
bt.printtree()