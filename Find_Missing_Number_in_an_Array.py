# arr[] = [1 2 4 5], N = 5

# Missing Number: 3

N = int(input("Enter value of N: "))
arr = list(map(int, input("Enter elements: ").split()))

xor1 = 0
xor2 = 0

n = N - 1

for i in range(n):
    xor2 = xor2 ^ arr[i]
    xor1 = xor1 ^ (i + 1)

xor1 = xor1 ^ N

missingNumber = xor1 ^ xor2
print("Missing number =", missingNumber)