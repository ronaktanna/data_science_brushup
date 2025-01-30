"""
@author: ronaktanna
"""

import numpy as np

def operate_a():
    # Making a NumPy array and initializing it with the numbers in the range [0-15) with step size of 1
    a = np.arange(0, 15, 1)
    print("****** EXAMPLE 1 ******\n")
    print("The Numpy Array is ")
    print(a)
    print("\n")

    # apply the different attributes
    applying_attributes(a)
    print("\n")

def applying_attributes(a):
    print("ndarray.ndim output is : {}".format(a.ndim))
    print("ndarray.shape output is : {}".format(a.shape))
    print("ndarray.size output is : {}".format(a.size))
    print("ndarray.dtype output is : {}".format(a.dtype))
    print("ndarray.itemsize output is : {} bytes".format(a.itemsize))
    print("ndarray.amin output is : {}".format(np.amin(a)))
    print("ndarray.amax output is : {}".format(np.amax(a)))
    print("ndarray.sum output is : {}".format(np.sum(a)))
    print("ndarray.cumsum output is : {} \n".format(np.cumsum(a)))
    print("After reshaping the array using np.reshape(a,(5,3)) : \n\n {}".format(np.reshape(a, (5,3))))

def operate_b():
    b = np.array([[0, 1, 2, 3],
                  [4, 5, 6, 7],

                  [8, 9, 10, 11],
                  [12, 13, 14, 15],

                  [16, 17, 18, 19],
                  [20, 21, 22, 23]])

    print("****** EXAMPLE 2 ******\n")
    print("The Numpy Array is ")
    print(b)
    print("\n")

    applying_attributes_multiple_dimensions(b)

def applying_attributes_multiple_dimensions(a):
    print("ndarray.ndim output is : {}".format(a.ndim))
    print("ndarray.shape output is : {}".format(a.shape))
    print("ndarray.size output is : {}".format(a.size))
    print("ndarray.dtype output is : {}".format(a.dtype))
    print("ndarray.itemsize output is : {} bytes".format(a.itemsize))
    print("\n")


    print("Sum of all the values in the array is : {}".format(np.sum(a)))
    print("Sum of values along the column is {}".format(np.sum(a, axis=0)))
    print("Sum of values along the row is {}".format(np.sum(a, axis=1)))
    print("\n")

    print("Minimum value in the array is : {}".format(np.amin(a)))
    print("Minimum element in each column is {}".format(np.amin(a, axis=0)))
    print("Minimum element in each row is {}".format(np.amin(a, axis=1)))
    print("\n")

    print("Maximum value in the array is : {}".format(np.amax(a)))
    print("Maximum element in each column is {}".format(np.amax(a, axis=0)))
    print("Maximum element in each row is {}".format(np.amax(a, axis=1)))
    print("\n")

    print("Cumulative Sum along the columns is : \n\n {}".format(np.cumsum(a, axis=0)))
    print("\n")
    print("Cumulative Sum along the rows is : \n\n {}".format(np.cumsum(a, axis=1)))
    print("\n")

    print("After flattening the array using np.ravel() : \n\n {}".format(np.ravel(a)))
    print("\n")

    print("Before changing the data type : {}".format(a.dtype))
    print("After changing the data type using a.astype(np.float32) : {}".format(a.astype(np.float32).dtype))

def demo_np_creation():
    print("****** np.empty Usage ******\n")
    a = np.empty(shape=[2, 2], dtype=int)
    print(a)
    print("\n")

    print("****** np.eye Usage ******\n")

    # N = row count
    # M = col count

    b = np.eye(N=2, M=2, k=0, dtype=int)
    print("For k=0\n")
    print(b)
    print("\n")

    c = np.eye(N=2, M=2, k=1)
    print("For k=1\n")
    print(c)
    print("\n")

    print("****** np.identity Usage ******\n")

    # n is the dimension of square numpy array

    d = np.identity(n=2, dtype=float)

    print(d)
    print("\n")

    print("****** np.linspace Usage ******\n")
    # endpoint=True is default -> (stop-start)/(num-1)
    # endpoint=False -> (stop-start)/num

    e = np.linspace(start=1.0, stop=5.0, num=5) # 5 numbers including stop value 5.0
    print("Including the stop element\n")
    print(e)
    print("\n")

    f = np.linspace(start=1.0, stop=5.0, num=5, endpoint=False) # 5 numbers excluding 5.0, spaced by (5-1)/5 = 0.8
    print("Excluding the stop element\n")
    print(f)
    print("\n")

    print("****** np.ones Usage ******\n")
    g = np.ones(shape=(5,), dtype=int)
    print(g)
    print("\n")

    print("****** np.zeros Usage ******\n")

    h = np.zeros(shape=(5, 5), dtype=int)
    print(h)
    print("\n")

if __name__ == "__main__":
    operate_a()
    operate_b()
    demo_np_creation()