from referential_array import build_array

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
        results = self.linear_probe(key)
        candidate_place = results[0]
        probeLength = results[1]
        if self.array[candidate_place] is None:
            self.count += 1
        self.array[candidate_place]=kv_pair(key,value)
        return probeLength

    def __getitem__(self, key):
        candidate_place = self.linear_probe(key)[0]
        if self.array[candidate_place] is None:
            raise KeyError(str(key)+" not found")
        return self.array[candidate_place]

    def __contains__(self,key):
        try:
            __getitem__(self,key)
            return True
        except KeyError as error:
            return False

    def __len__(self):
        return self.count

    def linear_probe(self,key,manualKey = None):
        if self.count == self.tableSize:
            raise IndexError("hash table is full!")
        if not manualKey is None:
            hashv = manualKey
        else:
            hashv = self.hash_value(key)  # first try
        pos = hashv
        probeLength = 0
        while not (self.array[pos] is None or self.array[pos].key == key):
            pos = (pos +1)%self.tableSize
            probeLength += 1
        return pos, probeLength

def giveMeStats(fileToOpen,myTableSize):
    myHashTable = Hash_table(myTableSize-100000)

    readFile = open(fileToOpen)
    
    probeLengthList = []
    for line in readFile:
        line = line.strip()
        probeLength = myHashTable.__setitem__(line,None)
        probeLengthList.append(probeLength)
        
    readFile.close()

    #get the average probe length
    averageProbeLength = 0
    for item in probeLengthList:
        averageProbeLength += item
    averageProbeLength = averageProbeLength/len(probeLengthList)

    #print the stats
    print("size: " + str(myTableSize-100000))
    print("file: " + str(fileToOpen))
    print("average probe length: " + str(averageProbeLength))
    print("load: " + str(myHashTable.__len__()/myHashTable.tableSize))
    print("\n")

tableSizes = [200000,200250,200500,200750,300000,300250,300500,300750,400000,400250]
primes = [2,31,73,127,179,233,283,353,419,467]
files = ["french3.txt"]

for openFile in files:
          for mySize in tableSizes:
              giveMeStats(openFile,mySize)
