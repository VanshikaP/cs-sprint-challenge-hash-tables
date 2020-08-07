1. Hashing functions
A: Hashing functions map the given key to a unique deterministic value. They should operate such that the result value follows following rules - 
    * Same key should always result in same index value
    * No two input keys should result in same index value
    * The return values must be within a specific range

2. Collision resolution
A: Sometimes when we don't know the size of our input, hash table might be too small. Because of this our hash function may generate same index value for 2 different keys and then the collisions occur. We have to design the ways in our hash functions to resolve these collisions when they occur. Some methods include chaining of values and automatic resizing.

3. Performance of basic hash table operations
A: The performance for basic hash table operations like insertion, deletion and lookup is constant time. 

4. Load factor
A: Load Factor gives us the information about how full the hash table is. It is calculated as number_of_entries / number_of_slots

5. Automatic resizing
When we resize the hash table based on the load factor during the insertion and deletion phases, without calling for resizing separately, collision is significantly minimized. 

6. Various use cases for hash tables
* Counting things
* Memoization
* Remove duplicates
* Network Cache
* Indexing
* Fast lookups for big arrays