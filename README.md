# my-hash-table-struct
## Demonstration of a custom hash table data structure

This project is given as an assignment of a course in The Open University.
The assignment was to implement a hash based data structure that is capable of storing strings as fast as possible, while trying to avoid inaccuracy (while speed is at max priority over accuracy).
Hence, given 3 parameters (N = amount of items stored, m = size of bitarray, K = amount of different hash functions), there is a certain possibility that a given string that was not inserted into the structure will actually be found as inserted.

The project allows you to examine the effect of those 3 parameters (N, m, K) on the possibility that the search function will fail and announce a string as "inserted".

#### Hashing
I used [Universal hashing](https://en.wikipedia.org/wiki/Universal_hashing) in order to generate K random hashing functions.

#### String-to-key
I converted each string to an integer key as a 128 base number using ascii code of each character (e.g: given the string "hi", using ascii code "h"=104, "i"=105, the key will be 104 x 128^0 + 105 x 128^1=13544)

#### Examples using different parameters
You can find the used text files in the repository.

![](https://user-images.githubusercontent.com/74790003/102716825-f5484e80-42e6-11eb-9006-4c00947016f4.png)
![](https://user-images.githubusercontent.com/74790003/102716853-21fc6600-42e7-11eb-9c6e-ec65d67053b7.png)
![](https://user-images.githubusercontent.com/74790003/102716861-258fed00-42e7-11eb-8d31-555853d5ada3.png)
