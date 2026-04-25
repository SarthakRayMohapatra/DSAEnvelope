# arr[] = [7 7 5 7 5 1 5 7 5 5 7 7 5 5 5 5]

def majorityElement(v):
    cnt = 0
    el = 0

    for i in range(len(v)):
        if cnt == 0:
            cnt = 1
            el = v[i]
        elif v[i] == el:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0

    for i in range(len(v)):
        if v[i] == el:
            cnt1 += 1

    if cnt1 > (len(v) // 2):
        return el

    return -1

n = int(input("Enter number of elements: "))
v = list(map(int, input("Enter elements: ").split()))

result = majorityElement(v)

print("Majority Element =", result)