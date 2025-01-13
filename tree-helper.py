from tree import *

def getSmallTree() -> BTNode:
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    return root

def anotherSmallTree() -> BTNode:
    root = BTNode(10)
    root.left = BTNode(34)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    return root

def main():
    POL_helper()  
    small_tree = getSmallTree()
    smaller_tree = anotherSmallTree()
    
    print("TESTING ISBALANCED.")
    print("Should return True. Returns ", isBalanced(small_tree))
    print("Should return False. Returns ", isBalanced(smaller_tree))
    print("TESTING FIXTREE.")
    print("List starts as ", inOrderWalk(small_tree))
    print("List should now be [10, 34, 45, 50, 89]")
    print("List is ", inOrderWalk(fixTree(small_tree)))
    print("TESTING ADD NODE.")
    addNodeBST(smaller_tree, 89)
    print("List should be [45, 34, 50, 10, 89]. List is ", inOrderWalk(smaller_tree))
    print("TESTING REMOVE NODE.")
    removeNodeBST(smaller_tree, 89)
    print("List should be [45, 34, 50, 10]. List is ", inOrderWalk(smaller_tree))


if __name__ == "__main__":
    main()
