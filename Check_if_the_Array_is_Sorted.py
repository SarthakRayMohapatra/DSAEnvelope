# arr[] = [1 2 2 3 3 4]
# arr[] = [1 2 1 3 4]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

is_sorted = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")