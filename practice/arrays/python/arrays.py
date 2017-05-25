
import array
import numpy as np

# Experiments using Python arrays and vectors


def arrays_basic():

    # initializing array with array values
    # initializing array with signed integers
    arr = array.array("i", [3, 5, 6, 7])

    val1 = 4
    val2 = 5
    val3 = 3
    ind1 = 2
    ind2 = 3

    print("\n" * 2)

    # add the value at the end of the array
    arr.append(val1)
    print("The appended array is: ", arr)
    # output: [3, 5, 6, 7, 4]


    # add the value at specified index
    # array.insert(index, value)
    arr.insert(ind1, val2)
    print("The array after insertion value {} at index {}: {}".format(val2, ind1, arr))
    # output: [3, 5, 5, 6, 7, 4]


    # return an element at index
    # array.pop(index)
    popped = arr.pop(ind2)
    print("The popped value at index {} is {}, {}".format(ind2, popped, arr))
    # out: 6, array: [3, 5, 5, 7, 4]


    # remove the first occurrence of the value
    # array.remove(index)
    arr.remove(val3)
    print("The array after removing element {}, {}".format(val3, arr))
    # out: [3, 5, 6, 4]


    # index of the first occurrence of value
    # array.index(value)
    ind = arr.index(val1)
    print("The index of value {} is {}, {}".format(val1, ind, arr))
    # out: [3, 5, 6, 4]


    # reverse the array
    arr.reverse()
    print("Reverse the array: {}".format(arr))
    # out: [4, 6, 5, 3]

    # return the data type by wich array is initialized
    arr.typecode
    print("The data type of the initialized array is {}".format(arr.typecode))
    # out: i

    # return size in bytes of a single array element
    arr.itemsize
    print("The item size of the array is {}".format(arr.itemsize))
    # out: 4

    # return a tuple with an address in which array is stored and n of elements
    arr.buffer_info()
    print("The address and number of elements of the array: ", arr.buffer_info())


    # number of occurrences of an element in the array
    count = arr.count(val2)
    print("Number {} occurs {} times in the array {}".format(val2, count, arr))
    # out: 2


    # merge two arrays
    # extend(array)
    arr2 = array.array("i", [2, 2, 3, 3])
    arr.extend(arr2)
    print("Initial array merged with {} : {}".format(arr2, arr))
    # out: [4, 7, 5, 5, 2, 2, 3, 3]

    # append a list to the end of the array
    # fromlist(list)
    li = [1, 1]
    arr4 = arr.fromlist(li)
    print("Array after list {} is appended: {}".format(li, arr))
    # out: [4, 7, 5, 5, 2, 2, ,3, 3, 1, 1]

def arrays_numpy():

    # initialize numpy array
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    print("\n")

    # type of array
    print("Array type is {}".format(type(arr)))

    # array dimensions
    print("№ of dimensions in {}".format(arr.ndim, arr))

    # shape of array
    print("Shape of the array is {}".format(arr.shape))

    # array size
    print("Array size is {}".format(arr.size))

    # type of elements in the array
    print("Array stores elements of type {}".format(arr.dtype))

    # create array 3X5 with all zeros
    arrA = np.zeros((3,5))
    print("Array created with all zeros \n {} \n".format(arrA))

    # create complex array with specified placeholder
    arrB = np.full((3, 4), 5, dtype = 'complex')
    print("A Complex 3X4 array with all 5 \n {} \n".format(arrB))

    # create an array with random values
    arrC = np.random.random((2, 2))
    print("A Random 2X2 array \n {} \n".format(arrC))

    # create a sequence of 10 values in range 0 to 5
    arrD = np.linspace(0, 5, 10)
    print("A sequential array with steps of 5 \n {} \n".format(arrD))

def arrays():
    arrays_basic()
    arrays_numpy()

def main():
    arrays()

main()