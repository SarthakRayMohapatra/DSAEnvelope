# arr[] = [1 1 2 3 3 4 4]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

xor = 0

for i in range(n):
    xor = xor ^ arr[i]
print("Number that appears once =", xor)