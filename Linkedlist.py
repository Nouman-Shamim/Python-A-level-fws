myLinkedList= [0 for index in range(0,12)]
myLinkedListPointers=[0 for index in range(0,12)]
startPointer=-1
heapStartPointer=0

for index in range(0,11):
    myLinkedListPointers[index]=index+1
myLinkedListPointers[11]=-1
print(myLinkedList)
print(myLinkedListPointers)
def insert(itemAdd):
    PreviousNodePtr=-2
    global startPointer,heapStartPointer
    if heapStartPointer == -1:
       print("Linked List full")
    else:
       newprt=heapStartPointer
       startPointer = heapStartPointer
       heapStartPointer = myLinkedListPointers[heapStartPointer]
       myLinkedList[newprt] = itemAdd
       ThisNodePtr=startPointer
       
       while ThisNodePtr!=-1 and myLinkedList[ThisNodePtr]<itemAdd:
           #II start at beginning of list
           PreviousNodePtr=ThisNodePtr #remember this node 
            # follow the pointer to the next node
           ThisNodePtr= myLinkedListPointers[ThisNodePtr]
       if PreviousNodePtr ==startPointer: 
         #insert new node at start of list 
           myLinkedListPointers[newprt]=StartPointer
           StartPointer=newprt
       else: # insert new node between previous node and this node
           myLinkedListPointers[newprt]= myLinkedListPointers[PreviousNodePtr]
           myLinkedListPointers[PreviousNodePtr]=newprt
insert(5)
insert(9)
insert(3)
print(myLinkedList)
print(myLinkedListPointers)
def find(itemSearch):
    found = False
    itemPointer = startPointer
    while itemPointer != -1 and not found:
         if myLinkedList[itemPointer] == itemSearch:
            found = True
         else:
            itemPointer = myLinkedListPointers[itemPointer]
    return itemPointer
#enter item to search for
item = int(input("Please enter item to be found "))
result = find(item)
if result != -1:
    print("Item found")
else:
    print("Item not found")
def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == -1:
        print("Linked List empty")
    else:
        index = startPointer
        while myLinkedList[index] != itemDelete and index != -1:
            oldindex = index
            index = myLinkedListPointers[index]
        if index == nullPointer:
            print("Item ", itemDelete, " not found")
        else:
            myLinkedList[index] = None
            tempPointer = myLinkedListPointers[index]
            myLinkedListPointers[index] = heapStartPointer
            heapStartPointer = index
            myLinkedListPointers[oldindex] = tempPointer



    

