# Data Structures: HashMap Implementations

## Overview
This repository contains an efficient implementation of HashMaps using two distinct methods: Open Addressing and Separate Chaining. These implementations are backed by fundamental data structures like Dynamic Arrays and Linked Lists, ensuring optimized performance and memory usage.

### Contents
- `data_structures.py`: Defines essential data structures like DynamicArray, LinkedList, and HashEntry.
- `hash_map_oa.py`: Implements HashMap using Open Addressing, with quadratic probing for collision resolution.
- `hash_map_sc.py`: Implements HashMap using Separate Chaining for managing collisions.

## Features
- **Dynamic Array**: A flexible array structure that grows dynamically.
- **Linked List**: A sequential collection of elements, allowing efficient insertion and deletion.
- **Hash Entry**: A specialized structure for storing key-value pairs in HashMap.
- **Open Addressing**: A collision resolution method using quadratic probing.
- **Separate Chaining**: A collision resolution strategy using linked lists.

## HashMap Implementations

### Open Addressing (`hash_map_oa.py`)
- **Quadratic Probing**: This file demonstrates an innovative approach to resolving hash collisions using quadratic probing.
- **Dynamic Resizing**: Ensures the HashMap remains efficient regardless of the number of elements.

### Separate Chaining (`hash_map_sc.py`)
- **Efficient Collision Handling**: Separate chaining allows multiple values to be stored at the same hash index, reducing collision occurrence.
- **Scalability**: Adapts well to a large number of entries, maintaining performance.

## Getting Started

To use these implementations in your project, simply clone this repository and import the required modules:

```python
from hash_map_oa import HashMap as HashMapOA
from hash_map_sc import HashMap as HashMapSC
```

## Usage

### Creating a HashMap
- Open Addressing: Use `HashMapOA` with a specified capacity.
- Separate Chaining: Use `HashMapSC` with a specified capacity.

### Basic Operations
#### **Insertion**: Add a key-value pair to the HashMap.
``` python
hash_map.put(key, value)
```
#### **Deletion**: Remove a key-value pair from the HashMap.
``` python
hash_map.remove(key)
```
#### **Check Existence**: Check if a key exists in the HashMap. Returns True if the key is present, otherwise False.
``` python
exists = hash_map.contains_key(key)
```
#### **Clearing the HashMap**: Remove all key-value pairs from the HashMap, effectively clearing it.
``` python
hash_map.clear()
```
#### **Retrieving Value Associated to a Key**: Returns the value associated with the given key.
``` python
hash_map.get(key)
```
#### **Retrieving All Key-Value Pairs**: Retrieve all key-value pairs as a DynamicArray, where each element is a tuple of (key, value).
``` python
key_value_pairs = hash_map.get_keys_and_values()
```
#### **Retrieving Size and Capacity of the Map**: Return size/capacity of the HashMap.
``` python
hash_map.get_size()
hash_map.get_capacity()
```
