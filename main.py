yellow = "\033[33m"
red = "\033[31m"
default = "\033[0m"
list = [ ]
def printList( ):
    print()
    for item in list:
     print(item)
     print( )
while True:
    print("{}TO-DO LIST MANAGER{}".format(yellow,default))
    user = input("Do you wish to add, view,remove,edit or delete the list?:")
    if user == "add":
        item = input("What do you wish to add?:")
        if item in list:
            print ("This item is already in the list")
        else:
            list.append(item)
        print(item)
    elif user == "view": 
        printList()
    elif user == "remove":
        item = input("What do you wish to remove?:")
        if item in list:
            list.remove(item)
    elif user == "edit":
        item = input("What do you wish to edit?:")
        new = input("What do you wish to change it to?:")
        for i in range(0,len(list)):
            if list[i]== item:
                list[i]= new
    elif user == "delete":
        list=[ ]
    else:
        print("{}It is not in the to-do list{}".format(red,default))