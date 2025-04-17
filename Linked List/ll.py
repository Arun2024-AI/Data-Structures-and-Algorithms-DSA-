# Insert node at the beginning of the Linked List

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def insertAtHead(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode
    return head

# Insert node at the end of the Linked List

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def insertAtTail(head, value):
    newNode =Node(value)
    if head==None:
        head = newNode
        return head
    else:
        i = head
        while(i.next != None):
            i = i.next
        i.next =newNode
        return head

# Delete node at the beginning of the Linked List
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

def deleteAtHead(head):
    if head != None:
        head = head.next
    return head

# Delete node at the end of the Linked List
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def deleteAtTail(head):
    if head == None:
        return None
    if head.next == None:  #single node
        return None
    i = head 
    #Reach the second last node
    while (i.next.next!=None):
        i = i.next

    # i has Reached the second last node
    i.next =None

    return head

