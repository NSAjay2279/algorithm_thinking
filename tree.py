class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.value = value
        
def printTabs(numtabs):
    for i in range(numtabs):
        print("\t", end="")

def printTreeRec(root, level):
    if root == None:
        printTabs(level)
        print("---<empty>--")
        return
    printTabs(level)
    print("value = ", root.value)
    printTabs(level)
    print("left")
    
    printTreeRec(root.left, level+1)
    printTabs(level)
    print("right")
    
    printTreeRec(root.right, level+1)
    
    printTabs(level)
    print("done")
    
def printTree(root):
    printTreeRec(root, 0)
    
n1 = TreeNode(10)
n2 = TreeNode(11)
n3 = TreeNode(12)
n4 = TreeNode(13)
n5 = TreeNode(14)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

printTree(n1) 

