# Implementation of a HashMap using Open Addressing

from data_structures import (DynamicArray, HashEntry,
                        hash_function)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out
        
    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number to find the closest prime number
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
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        """
        return self._capacity

    def put(self, key: str, value: object) -> None:
        """Updates the key/value pair in the hash map, and calls resize when needed

        Args:
            key (str): The key
            value (object): The value
        """
        #Check if resize is needed
        if self.table_load() >= 0.5:
            self.resize_table(2 * self._capacity)
        
        index = self._hash_function(key) % self._capacity
        for i in range(self._capacity):
            next_index = (index + i**2) % self._capacity
            #If the index is empty
            if self._buckets[next_index] is None or self._buckets[next_index].is_tombstone == True:
                self._buckets[next_index] = HashEntry(key, value)
                self._size += 1
                return
            
            #If the index is full, but has same key
            if self._buckets[next_index].key == key:
                self._buckets[next_index].value = value
                return
    
    def table_load(self, new_capacity=None) -> float:
        """
        Returns the current hash table load factor
        """
        return self._size / self._capacity

    def empty_buckets(self) -> int:
        """Returns the number of empty buckets in the hash table

        Returns:
            int: Number of empty buckets in the hash table
        """
        empty_count = 0
        
        for index in range(self._capacity):
            if self._buckets[index] == None or self._buckets[index].is_tombstone == True:
                empty_count += 1
        return empty_count

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table
        All existing key/value pairs remain in the new hash map, and all hash table links are rehashed
        
        Args:
            new_capacity (int): The new capacity
        """
        #Checks for new_capacity
        if new_capacity < self._size:
            return
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)
        
        old_bucket = self._buckets
        old_capacity = self._capacity
        self._buckets = DynamicArray()
        self._capacity = new_capacity
        self._size = 0
        
        #Fill up the array of empty lists
        for _ in range(new_capacity):
            self._buckets.append(None)
        
        #Loop through existing pairs, and fill up new array
        for index in range(old_capacity):
            pair = old_bucket[index]
            if pair != None and pair.is_tombstone == False:
                self.put(pair.key, pair.value)    

    def get(self, key: str) -> object:
        """Returns the value associated with the given key

        Args:
            key (str): Key associated with the value

        Returns:
            _type_: Value if there, othersise, None
        """
        index = self._hash_function(key) % self._capacity
        
        for i in range(self._capacity):
            next_index = (index + i**2) % self._capacity
            if self._buckets[next_index] == None:
                return None
            if self._buckets[next_index].key == key and self._buckets[next_index].is_tombstone == False:
                return self._buckets[next_index].value
            
    def contains_key(self, key: str) -> bool:
        """
        Finds if the passed key is in the HashMap or not

        Args:
            key (str): They key to look for

        Returns:
            bool: True if the given key is in the hash map, otherwise it returns False
        """
        index = self._hash_function(key) % self._capacity
        
        for i in range(self._capacity):
            next_index = (index + i**2) % self._capacity
            if self._buckets[next_index] == None:
                return False
            
            if self._buckets[next_index].key == key and self._buckets[next_index].is_tombstone == False:
                    return True
    
    def remove(self, key: str) -> None:
        """Removes the given key and its associated value from the hash map

        Args:
            key (str): Key associated to the value
        """
        index = self._hash_function(key) % self._capacity
        
        for i in range(self._capacity):
            next_index = (index + i**2) % self._capacity
            
            #If key does not exist, or already removed, return
            if self._buckets[next_index] == None:
                return
            
            #If we found it, update .is_tombstone and decrement ._size
            if self._buckets[next_index].key == key and self._buckets[next_index].is_tombstone == False:
                self._buckets[next_index].is_tombstone = True
                self._size -=1
                return

    def clear(self) -> None:
        """
        Clears the contents of the hash map
        """
        for index in range(self._capacity):
            self._buckets[index] = None
        self._size = 0

    def get_keys_and_values(self) -> DynamicArray:
        """Returns all key/value pairs

        Returns:
            DynamicArray: A dynamic array where each index contains a tuple of a key/value pair
        """
        keys_and_values = DynamicArray()
        
        for index in range(self._capacity):
            if self._buckets[index] is None or self._buckets[index].is_tombstone == True:
                pass
            else:
                tuple = (self._buckets[index].key, self._buckets[index].value)
                keys_and_values.append(tuple)
        
        return keys_and_values

    def __iter__(self):
        """
        Create iterator for loop
        """
        self._index = 0        
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        """
        while self._index < self._capacity:
            self._index += 1
            if self._buckets[self._index-1] is not None:
                return self._buckets[self._index-1]
        raise StopIteration()

