# arr[] = [1 2 3 4 5]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

temp = arr[0]

for i in range(1, n):
    arr[i-1] = arr[i]
arr[n-1] = temp
print("Array after left rotation by one place:", arr)