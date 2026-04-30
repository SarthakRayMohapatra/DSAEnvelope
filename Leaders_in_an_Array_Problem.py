# arr[] = [10 22 12 3 0 6]

def superiorElements(a):
    ans = []
    maxi = float('-inf')

    n = len(a)

    # Traverse from right
    for i in range(n - 1, -1, -1):
        if a[i] > maxi:
            ans.append(a[i])
        maxi = max(maxi, a[i])

    # Sort result
    ans.sort()

    return ans

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

result = superiorElements(a)

print("Superior elements:", result)