from math import floor
from math import log2
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'Data.txt')

def readFile(txtFile,dataType):
    with open(txtFile, mode='r') as f:
        data_content = f.read()
        data_content=data_content.split()
        f.close()
        if dataType=='movieId':
            return data_content[3::3]
        if dataType=='movieRating':
            return data_content[4::3]
        if dataType=='movieVoting':
            return data_content[5::3]

movieIds=readFile(my_file,'movieId')
movieRatings=readFile(my_file,'movieRating')
movieVotings=readFile(my_file,'movieVoting')
print(movieVotings[0],movieIds[0],movieRatings[0])
print(len(movieRatings),len(movieVotings),len(movieIds))
for i in range(99):
    print(movieIds[i],movieRatings[i],movieVotings[i])
def Movie_Data(rating):
    singlemovieData=[]
    len_Of_data=len(movieRatings)



class Node:
    def __init__(self, mids,mrating,mvoting):
        self.data = data
        # self.node = None
        self.left = None
        self.right = None
        self.height = 1

    def printData(self):
        print(self.data)


class AVLTree:
    def __init__(self):
        self.root = None

    def Max(self, a, b):
        if a > b:
            return a
        return b

    def getHeight(self, root):
        if root == None:
            return 0
        return root.height

    def getBalanceFactor(self, root):
        if root == None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def lowestValue(self, root):
        if root is None or root.left is None:
            return root
        return self.lowestValue(root.left)

    def insert(self, root, value):
        if root == None:
            return Node(value)
        elif value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        # return root
        # Update Height
        root.height = 1 + self.Max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalanceFactor(root)

        # left left violaion:
        if balanceFactor > 1 and root.left.data > value:
            return self.rightRotate(root)

        # right right violation:
        if balanceFactor < -1 and root.right.data < value:
            return self.leftRotate(root)

        # left right violation:
        if balanceFactor > 1 and root.left.data < value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # right left violation:
        if balanceFactor < -1 and root.right.data > value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def rightRotate(self, node):
        leftOfRoot = node.left
        rightOfLeft = leftOfRoot.right
        leftOfRoot.right = node
        node.left = rightOfLeft
        node.height = 1 + self.Max(self.getHeight(node.left), self.getHeight(node.right))
        leftOfRoot.height = 1 + self.Max(self.getHeight(leftOfRoot.left), self.getHeight(leftOfRoot.right))
        return leftOfRoot

    def leftRotate(self, node):
        rightOfRoot = node.right
        leftOfRight = rightOfRoot.left
        rightOfRoot.left = node
        node.right = leftOfRight
        node.height = 1 + self.Max(self.getHeight(node.left), self.getHeight(node.right))
        rightOfRoot.height = 1 + self.Max(self.getHeight(rightOfRoot.left), self.getHeight(rightOfRoot.right))
        return rightOfRoot

    def Delete(self, root, value):

        if root == None:
            return root

        elif value < root.data:
            root.left = self.Delete(root.left, value)

        elif value > root.data:
            root.right = self.Delete(root.right, value)

        else:
            if root.left == None:
                reservedData = root.right
                root = None
                return reservedData

            elif root.right is None:
                reservedData = root.left
                root = None
                return reservedData

            reservedData = self.getLowestValue(root.right)
            root.data = reservedData.data
            root.right = self.Delete(root.right, reservedData.data)

        if root == None:
            return root

        root.height = 1 + self.Max(self.getHeight(root.left), self.getHeight(root.right))
        BalanceFactor = self.getBalanceFactor(root)

        if BalanceFactor > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rightRotate(root)

        if BalanceFactor < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.leftRotate(root)

        if BalanceFactor > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if BalanceFactor < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inOrderTraversal(self, root):
        # left -> root -> right
        if not root:
            return
        self.inOrderTraversal(root.left)
        root.printData()
        self.inOrderTraversal(root.right)

    def preOrderTraversal(self, root):
        # root -> left -> right
        if not root:
            return
        root.printData()
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        # left -> right -> root
        if not root:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        root.printData()

    def Search(self, root, element, Treevalue):
        if Treevalue == True:
            return True
        if root.left != None:
            Treevalue = self.Search(root.left, element, Treevalue)
        if root.data == element:
            print('The Data Exists In The Tree: ')
            print(root.data)
            return True
        if root.right != None:
            Treevalue = self.Search(root.right, element, Treevalue)
        return Treevalue

    def CountNodes(self, root):
        if root == None:
            return 0
        return (1 + self.CountNodes(root.left) + self.CountNodes(root.right))

    def Height(self):
        return floor(log2(self.CountNodes(self.root)))


# Function For Menu
def AVLoperationMenu():
    print('Menu to Perform Operations on AVL Tree')
    print('a. Insert (add a value in the AVL Tree')
    print('b. search (search an element from the AVL Tree')
    print('c. Delete (to delete a value from AVL')
    print('d. Height (print Height of AVL Tree')
    print('e. Preorder Traversal (print elements of AVL Tree in pre-order fashion')
    print('f. In-order Traversal (print elements of AVL Tree in In-order fashion')
    print('g. Post Traversal (print elements of AVL Tree in Post-order fashion')
    print('h. Exist the program')
    AVL = AVLTree()
    while True:
        UserInput = input('Enter any above alphabet to perfoem operations: ')
        if UserInput == 'a':
            print('"INSERT": Here The Data Add To The AVL Tree')
            UserData = input('Enter Value To Add In The AVL Tree: ')
            AVL.root = AVL.insert(AVL.root, UserData)
            print('Data Added Successfully')

        if UserInput == 'b':
            print('Search The Data In The AVL Tree')
            UserData = input('Enter Element To Search: ')
            if AVL.Search(AVL.root, UserData, '') != True:
                print('Value Not Found In The AVL Tree')

        if UserInput == 'c':
            UserData = input('Enter Element To Delete: ')
            if AVL.Search(AVL.root, UserData, '') == True:
                AVL.root = AVL.Delete(AVL.root, UserData)
                print('Successfully Deleted')
            else:
                print('value is not found in the AVL Tree')
        if UserInput == 'd':
            print('Number Of Nods Are: ', AVL.CountNodes(AVL.root))
            print('Height of the Tree is: ')
            print(AVL.Height())

        if UserInput == 'e':
            print('Pre-OrderTraversal Of Tree Is: ')
            AVL.preOrderTraversal(AVL.root)
        if UserInput == 'f':
            print('In-OrderTraversal of Tree Is: ')
            AVL.inOrderTraversal(AVL.root)
        if UserInput == 'g':
            print('Post-OrderTraversal Of Tree Is: ')
            AVL.postOrderTraversal(AVL.root)
        if UserInput == 'h':
            print('Program Exit Successfully')
            return quit()


AVLtree1 = AVLoperationMenu()