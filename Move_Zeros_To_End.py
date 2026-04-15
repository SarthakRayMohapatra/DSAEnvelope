# arr[] = [1 0 2 3 2 0 0 4 5 1]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

j = -1

for i in range(n):
    if arr[i] == 0:
        j = i
        break

if j == -1:
    print("No zeros in the array.")
else:
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[j] = arr[i]
            arr[i] = 0
            j += 1

    print("Array after moving zeros to the end:", arr)