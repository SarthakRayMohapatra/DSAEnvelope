# arr[] = [1 2 4 7 7 5]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

largest = arr[0]
second_largest = float('-inf')

for i in range(n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] < largest and arr[i] > second_largest:
        second_largest = arr[i]

print("Second largest element =", second_largest)