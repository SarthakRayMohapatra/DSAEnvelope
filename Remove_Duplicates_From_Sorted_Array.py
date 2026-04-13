# arr[] = [1 1 2 2 2 3 3]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

i = 0

for j in range(1, n):
    if arr[i] != arr[j]:
        arr[i+1] = arr[j]
        i += 1
print("Array after removing duplicates:", arr[:i+1])