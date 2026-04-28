# arr[] = [7 1 5 3 6 4]

def maximumProfit(prices):
    mini = prices[0]
    maxProfit = 0

    n = len(prices)

    for i in range(1, n):
        cost = prices[i] - mini
        maxProfit = max(maxProfit, cost)
        mini = min(mini, prices[i])

    return maxProfit

n = int(input("Enter number of elements: "))
prices = list(map(int, input("Enter elements: ").split()))

result = maximumProfit(prices)

print("Maximum Profit =", result)