# arr[] = [-2 -3 4 -1 -2 1 5 -3]

def maxSubarraySum(arr, n):
    total = 0
    maxi = float('-inf')

    for i in range(n):
        total += arr[i]

        if total > maxi:
            maxi = total

        if total < 0:
            total = 0

    return maxi

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

result = maxSubarraySum(arr, n)

print("Maximum Subarray Sum =", result)