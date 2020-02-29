import tests.graph_tests as tests
import math
if __name__ == "__main__":
    print("Hello, World!")
    tests.vertex_test()

def binary_search(A, key):
    i = int(len(A) / 2)
    while i > 0 and i < len(A):
        print("Searching")
        if A[i] == key:
            return key
        elif A[i] > key:
            i = int(i / 2)
        else:
            i = i + int(i / 2)
    print(i)
A = [1,2,3,4,5,6,7,8,9,10]
idx = binary_search(A,8)
print(idx)