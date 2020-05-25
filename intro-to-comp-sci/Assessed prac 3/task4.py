from referential_array import build_array
import timeit

class kv_pair:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return "("+str(self.key)+","+str(self.value)+")"

class Hash_table:
    def __init__(self,tableSize, probeLengthList = [], count = 0):
        self.array = build_array(tableSize)
        self.tableSize = tableSize
        self.probeLengthList = probeLengthList
        self.count = count

    def hash_value(self,key):
        prime_mult = 101
        result = 0
        #print(key)
        for character in key:
            result = (result * prime_mult + ord(character)) % self.tableSize
        return result

    def __str__(self):
        string = ""
        for index in range(self.tableSize):
            if self.array[index] is None:
                pass
            else:
                string += str((index,str(self.array[index])))
                string += ","
            string = string.strip(",")
        return string

    def __setitem__(self, key, value):
        hashValue = self.hash_value(key)
        if self.array[hashValue] == None:
            self.array[hashValue] = [kv_pair(key,value)]
        else:
            self.array[hashValue].append(kv_pair(key,value))
        self.count += 1

    def __contains__(self,key):
        try:
            __getitem__(self,key)
            return True
        except KeyError as error:
            return False

    def __len__(self):
        return self.count

def addItems(fileToOpen,myTableSize):
    start = timeit.timeit()
    print(str(start))
    myHashTable = Hash_table(myTableSize)

    readFile = open(fileToOpen)
    
    for line in readFile:
        line = line.strip()
        myHashTable.__setitem__(line,None)
        
    readFile.close()
    end = timeit.timeit()
    print(str(end))
    print("time taken: " + str(end-start))

    #print hash table
    for x in range(myHashTable.tableSize):
        print(str(x))
        if myHashTable.array[x] == None:
            print("\t" + str(None))
        else:
            for pair in myHashTable.array[x]:
                print("\t" + pair.__str__())

tableSizes = [200000,200250,200500,200750,300000,300250,300500,300750,400000,400250]
primes = [2,31,73,127,179,233,283,353,419,467]
files = ["english_small3.txt"]

addItems("english_small3.txt",20)


'''
for openFile in files:
          for mySize in tableSizes:
              giveMeStats(openFile,mySize)
'''
