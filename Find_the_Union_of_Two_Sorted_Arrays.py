# arr1[] = [1 1 2 3 4 5]
# arr2[] = [2 3 4 4 5]

# Union: [1 2 3 4 5]

def sortedArray(a, b):
    n1 = len(a)
    n2 = len(b)

    i = 0
    j = 0

    unionArr = []

    while i < n1 and j < n2:
        if a[i] <= b[j]:
            if len(unionArr) == 0 or unionArr[-1] != a[i]:
                unionArr.append(a[i])
            i += 1
        else:
            if len(unionArr) == 0 or unionArr[-1] != b[j]:
                unionArr.append(b[j])
            j += 1

    while j < n2:
        if len(unionArr) == 0 or unionArr[-1] != b[j]:
            unionArr.append(b[j])
        j += 1

    while i < n1:
        if len(unionArr) == 0 or unionArr[-1] != a[i]:
            unionArr.append(a[i])
        i += 1

    return unionArr

n1 = int(input("Enter number of elements in first array: "))
a = list(map(int, input("Enter elements of first array: ").split()))

n2 = int(input("Enter number of elements in second array: "))
b = list(map(int, input("Enter elements of second array: ").split()))

result = sortedArray(a, b)

print("Union of two sorted arrays:", result)