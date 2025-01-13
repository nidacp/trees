from collections import deque

def POL_helper():
    print("File Imported")

class BTNode:
    def __init__(self, data:int|float):
        self.left:BTNode|None = None
        self.right = None
        self.data:int|float = data

def append(arr:list, val:int|float) -> list:
    ''' Resizes and adds a node to the end of an array, returning the new array.
    :param arr: (list) the array that has to be resized.
    :param val: (str) the node that should be added to the end of the array
    :return : (list) the new list, containing all the same elements of arr with the addition of val at the end.
    
    >>> append({}, "a")
    {"a"}
    >> append({"a"}, "b")
    {"a", "b"}
    '''
    new_arr:list[str|None] = [None] * (len(arr) + 1)
    for i in range(len(arr)):
        new_arr[i] = arr[i]
    new_arr[len(arr)] = val
    return new_arr

def inOrderWalk(root:BTNode) -> list:
    ''' Creates an in-order list representation of a binary tree.
    :param root: (BTNode) the root/start of the tree to be turned into a list.
    :returns : (list) the list representation of a binary tree.
    
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    >>>inorderWalk(root)
    [45, 34, 50, 10, 89]
    '''
    if root == None:
        return []
    return recWalk(root, [])

def recWalk(root:BTNode, ret:list) -> list:
    ''' uses recursion to add nodes in LVR (left, visited, right) order until every node in a tree has been visited.
    :param root: (BTNode) the start node of the tree to be traversed and added to the list.
    :param ret: (list) the list that is an inorder representation of a binary tree.
    :returns : (list) the list representation of a binary tree.
    
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    >>>inorderWalk(root)
    [45, 34, 50, 10, 89]
    '''
    if root.left is not None:
        ret = recWalk(root.left, ret)
    ret = append(ret, root.data)
    if root.right is not None:
        ret = recWalk(root.right, ret)
    return ret

def listToTree(tree_as_list:list) -> BTNode:
    ''' Turns a sorted array into a balanced Binary Search Tree.
    :param tree_as_list: (list) array to turn into a binary search tree
    :return : (BTNode) root/start node of the binary search tree
    
    >>> listToTree([1,3,4])
    BTNode root (data=3, root.left=1, root.right=4)
    '''

    #Find 'middle' point and make it the child of the previous middle. Divide and conquer
        #If it's a list of one, no recursive call
    if tree_as_list==None or len(tree_as_list)==0:
        return None
    if len(tree_as_list)==1:
        node = BTNode(list[0])
        return node
    
    
    return recToTree(tree_as_list, 0, len(tree_as_list)-1)

def recToTree(tree_as_list:list, start:int, end:int) -> BTNode:
    ''' Turns a sorted array into a balanced Binary Search Tree through recursion.
    :param tree_as_list: (list) array to turn into a binary search tree
    :return : (BTNode) root/start node of the binary search tree
    
    >>> listToTree([1,3,4])
    BTNode root (data=3, root.left=1, root.right=4)
    '''
    
    if start>end:
        return None
    
    middle = start + (end-start) // 2
    
    root = BTNode(tree_as_list[middle])
    
    root.left = recToTree(tree_as_list, start, middle-1)
    root.right = recToTree(tree_as_list, middle+1, end)
    
    return root

def fixTree(root:BTNode) -> BTNode:
    ''' Takes an unsorted binary tree and creates a balanced & sorted binary search tree with the same nodes.
    :param root: (BTNode) the root/start node of the unsorted binary tree
    :return : (BTNode) the root/start node of the sorted binary search tree
    
    root = BTNode(3)
    root.left = BTNode(2)
    root.right = BTNode(1)
    >>>fixTree(root)
    BTNode root2 (data = 2, root2.left=1, root2.right=3)    
    '''
    
    
    #if the tree is of length 1 or 0, there is nothing to fix
    if root==None:
        return None
    if root.left==None and root.right==None:
        return root
    
    temp_list = inOrderWalk(root)
    sorting(temp_list, 0, len(temp_list)-1)
    new_root=listToTree(temp_list)
    
    return new_root 

def sorting(arr:list, left:int, right:int) -> None:
    ''' merge sort!
    :param arr: (list) the array to be sorted
    :param left: (int) the start index of the sorting
    :param right: (int) the end index of the sorting
    '''
    if left<right:
        middle = (left+right)//2
        
        sorting(arr, left, middle)
        sorting(arr, middle+1, right)
        merge(arr, left, middle, right)
    
def merge(arr:list, left:int, mid:int, right:int) -> None:
    ''' "merges" 2 sections of a list in sorted order
    :param arr: (list) the array to be sorted
    :param left: (int) the start index of the left side of the array
    :param right: (int) the end index of the right side of the array
    :param mid: (int) the dividing index of the array
    '''
    #TODO: docstring
    size1 = mid-left+1
    size2 = right-mid
    
    left_arr = [0] * size1
    right_arr = [0] * size2
    
    for i in range(size1):
        left_arr[i] = arr[left + i]
    for j in range(size2):
        right_arr[j] = arr[mid + j + 1]

    i=0
    j=0
    k=left
    
    while i<size1 and j<size2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1
        
    while i<size1:
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j<size2:
        arr[k] = right_arr[j]
        j+=1
        k+=1

def addNodeBST(root:BTNode, data:int) -> bool:
    ''' Adds a node into a sorted binary search tree.
    :param root: (BTNode) the root, or starting node, of the binary search tree the node will be added to
    :param data: (int) the data contained in the added node
    :return : (bool) True if the node has been added, false if it has not (i.e. if there is no tree to add it to).
    
    root = BTNode(10)
    >>> addNodeBST(root, 5)
    True
    >>> addNodeBST(None, 5)
    False
    '''
    if root==None:
        return False
    
    temp:BTNode = root
    
    # exits if there's a spot to the left or to the right that the node can go
    while (temp.left != None and data<=temp.data) or (temp.right != None and data>temp.data):
        # if it's larger, it should traverse down the right. else, it should traverse down the left
        if temp.right != None and data>temp.data:
            temp=temp.right
        else:
            temp = temp.left
    
    # if it's larger, then it should be placed to the left. If it's smaller, it should be placed to the right
    if data>temp.data:
        temp.right = BTNode(data)
    else:
        temp.left = BTNode(data)
    
    if not isBalanced(root):
        fixTree(root)
    return True

def removeNodeBST(root:BTNode|None, data) -> bool:
    """
    Removes a node with the given data from the binary search tree.
    :param root: The root node of the binary search tree.
    :param data: The value to remove.
    :return: True if the removal was successful, false if it was not.
    """
    if root is None:
        return False
    recRemove(root,data)
    return True
    
def recRemove(root:BTNode|None, data) -> BTNode:
    """
    Removes a node with the given data from the binary search tree.
    :param root: The root node of the binary search tree.
    :param data: The value to remove.
    :return: The new root of the binary search tree after removal.
    """
    if root is None:
        return None
    # Traverse the tree
    if data < root.data:
        root.left = recRemove(root.left, data)
    elif data > root.data:
        root.right = recRemove(root.right, data)
    else:
        # Node to be deleted found
        # Case 1: No children
        if root.left is None and root.right is None:
            return None
        # Case 2: One child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Case 3: Two children
        else:
            # Find the in-order successor (smallest in the right subtree)
            successor = getSuccessor(root)
            root.data = successor.data
            root.right = recRemove(root.right, successor.data)

    return root

def getSuccessor(node:BTNode) -> BTNode:
    """
    Finds the in-order successor of the given node.
    The in-order successor is the smallest node in the right subtree.
    :param node: The node whose successor is to be found.
    :return: The in-order successor node.
    """
    current = node.right
    while current is not None and current.left is not None:
        current = current.left
    return current

def isBalanced(root:BTNode) -> bool:
    ''' Finds whether a tree is balanced. A balanced tree is defined as the maximum and minimum depths having a difference of, at most, one.
    :param root: (BTNode) the root/start of the tree that will be checked.
    :return : (bool) True if the max/min has a difference of 0 or 1, False if there is a difference greater than 1
    
    root1 = BTNode(5)
    root1.left = BTNode(3)
    >>> isBalanced(root1)
    True
    
    root2 = BTNode(10)
    root2.left=root1
    >>> isBalanced(root2)
    False
    '''
    # modified binary search that tracks max and min
    return (maxDepth(root) - minDepth(root)) <= 1

def maxDepth(node:BTNode|None) -> int:
    ''' finds the maximum distance between a root/start and a leaf in a tree.
    :param node: (BTNode) the start node of distance 0 that all of its leaves will be compared to.
    :return : (int) the number of nodes between the inputted node and its furthest leaf.
    
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    >>> maxDepth(root)
    3
    '''
    if node==None:
        return 0
    
    left = maxDepth(node.left)
    right = maxDepth(node.right)
    
    return max(left, right)+1

def minDepth(node:BTNode|None) -> int:
    ''' finds the minimum distance between a root/start and a leaf in a tree.
    :param node: (BTNode) the start node of distance 0 that all of its leaves will be compared to.
    :return : (int) the number of nodes between the inputted node and its closest leaf.
    
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    >>> minDepth(root)
    3
    '''
    if node==None:
        return 0
    
    left = maxDepth(node.left)
    right = maxDepth(node.right)
    
    return min(left, right)+1

