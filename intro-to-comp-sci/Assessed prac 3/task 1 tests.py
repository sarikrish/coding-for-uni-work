from task1 import kv_pair


def test1(): # testing __str__(self) from kv_pair
    myPair = kv_pair("Daniel",6) #pass a standard key and pair
    case = myPair.__str__()
    if case == "(Daniel,6)":
        print("passed")
    else:
        print("failed")

    myPair = kv_pair(None,None) #pass two None variables
    case = myPair.__str__()
    if case == "(None,None)":
        print("passed")
    else:
        print("failed")
    
    

test1()
