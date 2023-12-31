# Implementation of a HashMap using Separate Chaining

from data_structures import (DynamicArray, LinkedList,
                        hash_function)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def put(self, key: str, value: object) -> None:
        """Updates the key/value pair in the hash map, and calls resize when needed

        Args:
            key (str): The key
            value (object): The value
        """
        #Check if resize is needed
        if self.table_load() >= 1:
            self.resize_table(2 * self._capacity)

        #Find the list we will put our value in
        list = self._buckets[self._hash_function(key) % self._capacity]
        
        #if key already exists, update value and exit
        for node in list:
            if node.key == key:
                node.value = value
                return
        
        #Else, insert, increment size
        list.insert(key, value)
        self._size += 1

    def empty_buckets(self) -> int:
        """Returns the number of empty buckets in the hash table

        Returns:
            int: Number of empty buckets in the hash table
        """
        empty_count = 0
        
        for list in range(self._capacity):
            if self._buckets[list].length() == 0:
                empty_count += 1
        return empty_count

    def table_load(self, new_capacity=None) -> float:
        """
        Returns the current hash table load factor
        """
        if new_capacity == None:
            new_capacity = self._capacity
        return self._size / new_capacity

    def clear(self) -> None:
        """
        Clears the contents of the hash map
        """
        for index in range(self._capacity):
            self._buckets[index] = (LinkedList())
        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table
        All existing key/value pairs remain in the new hash map, and all hash table links are rehashed
        
        Args:
            new_capacity (int): The new capacity
        """
        #Checks for new_capacity
        if new_capacity < 1:
            return
        if self._is_prime(new_capacity) == False:
            new_capacity = self._next_prime(new_capacity)
        
        #Loop until you get the capacity with an acceptable load factor
        while True:
            if self.table_load(new_capacity) <= 1:
                break
            else:
                new_capacity = self._next_prime(new_capacity * 2)

        #Fill up the array of empty lists
        new_lists = DynamicArray()
        for _ in range(new_capacity):
            new_lists.append(LinkedList())
        
        #Loop through existing lists, and fill up new "buckets"
        for index in range(self._capacity):
            list = self._buckets[index]
            for node in list:
                new_lists[self._hash_function(node.key) % new_capacity].insert(node.key, node.value)

        #Update current HashMap
        self._buckets = new_lists
        self._capacity = new_capacity
        
    def get(self, key: str):
        """Returns the value associated with the given key

        Args:
            key (str): Key associated with the value

        Returns:
            _type_: Value if there, othersise, None
        """
        list = self._buckets[self._hash_function(key) % self._capacity]
        
        for node in list:
            if node.key == key:
                return node.value
        return None

    def contains_key(self, key: str) -> bool:
        """
        Finds if the passed key is in the HashMap or not

        Args:
            key (str): They key to look for

        Returns:
            bool: True if the given key is in the hash map, otherwise it returns False
        """
        list = self._buckets[self._hash_function(key) % self._capacity]
        
        for node in list:
            if node.key == key:
                return True
        return False

    def remove(self, key: str) -> None:
        """Removes the given key and its associated value from the hash map

        Args:
            key (str): Key associated to the value
        """
        list = self._buckets[self._hash_function(key) % self._capacity]
        
        for node in list:
            if node.key == key:
                list.remove(node.key)
                self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """Returns all key/value pairs

        Returns:
            DynamicArray: A dynamic array where each index contains a tuple of a key/value pair
        """
        keys_and_values = DynamicArray()
        
        for list in range(self._capacity):
            for node in self._buckets[list]:
                tuple = (node.key, node.value)
                keys_and_values.append(tuple)
        
        return keys_and_values
      
