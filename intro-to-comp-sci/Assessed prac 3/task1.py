from referential_array import build_array


class kv_pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        """
        This function implements 
        :param : a key-value pair
        :return: a string format of the pair
        :complexity: best case O(1), worst case O(1)
        """
        return str("("+str(self.key)+","+str(self.value)+")")


class Hash_table:
    def __init__(self, tableSize):
        self.array = build_array(tableSize)
        self.tableSize = tableSize
        self.count = 0

    def hash_value(self, key):
        """
        This function implements the hashing of a key
        :param : a key
        :return: the hash value of the key
        :complexity: n being the number of characters in best case O(1) (key is empty string), worst case O(n) (key is not empty string)
        """
        prime_mult = 101
        result = 0
        for character in key:
            result = (result * prime_mult + ord(character)) % self.tableSize
        return result

    def __str__(self):
        """
        This function implements converting a table to string form
        :param : hashing of a key
        :return: the hash value of the key
        :complexity: n being the number of characters in best case O(1), worst case O(1)
        """
        string = ""
        for index in range(self.tableSize):
            if self.array[index] is None:
                pass
            else:
                string += str((index, str(self.array[index])))
                string += ","
            string = string.strip(",")
        return string

    def __setitem__(self, key, value):
        """
        This function implements setting a key-value pair into the hashtable
        :param : the key and its hash value
        :complexity: best case O(1), worst case O(1)
        """
        candidate_place = self.linear_probe(key)
        if self.array[candidate_place] is None:
            self.count += 1
        self.array[candidate_place] = kv_pair(key, value)

    def __getitem__(self, key):
        """
        This function implements finding the location of a key 
        :param : a key
        :return: (if the key is present) the index of the key in the hashtable
        :raises: KeyError if the key is not contined in the hash table
        :complexity: n being count, in best case O(1) (no probing is required), worst case O(n) (table almost full and key hashes the the first full spot)
        """
        candidate_place = self.linear_probe(key)
        if self.array[candidate_place] is None:
            raise KeyError(str(key)+" not found")
        return self.array[candidate_place]

    def __contains__(self, key):
        """
        This function implements detemining if a key is in the hashtable
        :param : a key
        :return: (if the key is present) True, else False
        :complexity: n being count, in best case O(1) (no probing is required), worst case O(n) (table almost full and key hashes the the first full spot)
        """
        try:
            __getitem__(self, key)
            return True
        except KeyError as error:
            return False

    def __len__(self):
        """
        This function implements returning the amount of items in the hashtable
        :return: the amount of items in the hashtable
        :complexity: best case O(1) worst case O(n)
        """
        return self.count

    def linear_probe(self, key, manualKey=None):
        """
        This function implements finding the intended location of a key for insertion through linear probing
        :param : a key
        :return: the index where the key should be inserted in the hashtable
        :raises: IndexError if hash table is full
        :complexity: n being count, in best case O(1) (no probing is required), worst case O(n) (table almost full and key hashes the the first full spot)
        """
        if self.count == self.tableSize:
            raise IndexError("hash table is full!")
        if not manualKey is None:  # feed in manualKey if defined
            hashv = manualKey
        else:
            hashv = self.hash_value(key)  # first try
        pos = hashv
        while not (self.array[pos] is None or self.array[pos].key == key):
            pos = (pos + 1) % self.tableSize
        return pos


Names = ["Eva", "Amy", "Tim", "Ron", "Jan", "Kim", "Dot", "Ann", "Jim", "Jon"]
myHashTable = Hash_table(20)

for item in Names:
    myHashTable.__setitem__(item, None)
    print("Inserted " + item)
    print("Current table: ")
    for x in range(myHashTable.tableSize):
        print(str(x) + "\t" + str(myHashTable.array[x]))
    print("\n")
