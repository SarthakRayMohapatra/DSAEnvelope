# arr[] = [1 1 0 1 1 1 0 1 1]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

maximum = 0
counter = 0

for i in range(n):
    if(arr[i] == 1):
        counter += 1
        maximum = max(maximum, counter)
    else:
        counter = 0
print("Maximum consecutive ones =", maximum)