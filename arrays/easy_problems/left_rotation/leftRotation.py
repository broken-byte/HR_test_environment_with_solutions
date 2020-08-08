L = [1, 2, 3, 4, 5]

def leftRotate(A):
    rotA = [None for x in range(len(A))]
    for i in range(len(A)):
        rotA[i-1] = A[i]
    return rotA


print(L)
print(leftRotate(L))


def leftRotation(A, d):
    # None list of size len(A)
    rotA = [None for x in range(len(A))]
    # Iterate through A to get elements
    for i in range(len(A)):
        # Copy elements from A into their correct elements in rotA
        rotA[i - d] = A[i]
    return rotA

print(leftRotation(L, 2))