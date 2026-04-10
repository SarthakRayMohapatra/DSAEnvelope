# arr[] = [3, 2, 1, 5, 2]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

largest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element =", largest)