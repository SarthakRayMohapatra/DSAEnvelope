# arr1[] = [1 2 2 3 3 4 5 6]
# arr2[] = [2 3 3 5 6 6 7]

# Intersection: [2 3 3 5 6]

def sortedArray(a, b):
    n1 = len(a)
    n2 = len(b)

    i = 0
    j = 0

    intersectionArr = []

    while i < n1 and j < n2:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:   # FIXED here
            j += 1
        else:
            intersectionArr.append(a[i])
            i += 1
            j += 1

    return intersectionArr

n1 = int(input("Enter number of elements in first array: "))
a = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter number of elements in second array: "))
b = list(map(int, input("Enter elements of second array: ").split()))

result = sortedArray(a, b)

print("Intersection of two sorted arrays:", result)