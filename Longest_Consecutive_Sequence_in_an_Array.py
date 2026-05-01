# arr[] = [102 4 100 1 101 3 2 1 1]

def superiorElements(a):
    ans = []
    maxi = float('-inf')

    n = len(a)

    for i in range(n - 1, -1, -1):
        if a[i] > maxi:
            ans.append(a[i])
        maxi = max(maxi, a[i])

    ans.sort()

    return ans

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

result = superiorElements(a)

print("Superior elements:", result)