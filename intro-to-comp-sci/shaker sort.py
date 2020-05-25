def bubbleSort(myList):
    n = len(myList)
    for mark in range(n-1,0,-1):
        swapped = False
        for i in range(mark):
            if myList[i] > myList[i+1]:
                swap(myList, i, i+1)
                swapped = True
        if not swapped:
            break

def shakeLeft(myList,start,stop):
    swapped = False
    for i in range(start,stop):
        if myList[i] > myList[i+1]:
            swap(myList, i, i+1)
            swapped = True
    return myList, swapped
    
def shakeRight(myList,start,stop):
    swapped = False
    for i in range(stop,start,-1):
        if myList[i] < myList[i-1]:
            swap(myList, i, i-1)
            swapped = True
    return myList, swapped

def shakerSort(myList):
    n = len(myList)
    turn = 3
    start = 0
    stop = n-1
    while start < stop:
        if turn == 4:
            #print("shaking right")
            myList, swapped = shakeRight(myList,start,stop)
            if not swapped:
                break
            start += 1
            turn = 3
        elif turn == 3:
            #print("shaking left")
            myList, swapped = shakeLeft(myList,start,stop)
            if not swapped:
                break
            stop -= 1
            turn = 4
    return myList

def swap(aList,positionOne,positionTwo):
    tmp = aList[positionOne]
    aList[positionOne] = aList[positionTwo]
    aList[positionTwo] = tmp

amountOfNumbers = int(input("How many elements would you like to sort? "))
toSort = []
for x in range(amountOfNumbers):
    toSort.append(int(input("Enter element " + str(x) + ": ")))

print(shakerSort(toSort))
