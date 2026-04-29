# arr[] = [3 1 2]

def nextGreaterPermutation(A):
    ind = -1
    n = len(A)

    for i in range(n - 2, -1, -1):
        if A[i] < A[i + 1]:
            ind = i
            break

    if ind == -1:
        A.reverse()
        return A

    for i in range(n - 1, ind, -1):
        if A[i] > A[ind]:
            A[i], A[ind] = A[ind], A[i]
            break

    A[ind + 1:] = reversed(A[ind + 1:])

    return A

n = int(input("Enter number of elements: "))
A = list(map(int, input("Enter elements: ").split()))

result = nextGreaterPermutation(A)

print("Next Greater Permutation:", result)