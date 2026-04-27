# arr[] = [-1 2 3 4 -3 1]

# pos[] = [2 3 4 1]
# neg[] = [-1 -3]

def alternateNumbers(a):
    pos = []
    neg = []

    n = len(a)

    for i in range(n):
        if a[i] > 0:
            pos.append(a[i])
        else:
            neg.append(a[i])

    if len(pos) > len(neg):
        for i in range(len(neg)):
            a[2 * i] = pos[i]
            a[2 * i + 1] = neg[i]

        index = len(neg) * 2

        for i in range(len(neg), len(pos)):
            a[index] = pos[i]
            index += 1

    else:
        for i in range(len(pos)):
            a[2 * i] = pos[i]
            a[2 * i + 1] = neg[i]

        index = len(pos) * 2

        for i in range(len(pos), len(neg)):
            a[index] = neg[i]
            index += 1

    return a

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

result = alternateNumbers(a)

print("Array after alternate arrangement:", result)