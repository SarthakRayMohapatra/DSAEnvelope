# arr[] = [1 2 3 1 1 1 1 3 3]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

k = int(input("Enter value of k: "))

left = 0
right = 0
sum = arr[0]
max_length = 0
n = len(arr)

while right < n:
    while left <= right and sum > k:
        sum = sum - arr[left]
        left = left + 1

    if sum == k:
        max_length = max(max_length, right - left + 1)

    right = right + 1
    if right < n:
        sum = sum + arr[right]

print("Length of longest subarray with sum k =", max_length)