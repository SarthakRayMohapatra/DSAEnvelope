# arr[] = [6 7 8 4 1], key = 4

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

key = int(input("Enter the key to search: "))

for i in range(n):
    if arr[i] == key:
        print("Element found at index:", i)
        break