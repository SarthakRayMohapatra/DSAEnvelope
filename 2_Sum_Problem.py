# arr[] = [2 6 5 8 11], Target = 14

def read(n, book, target):
    left = 0
    right = n - 1

    book.sort()

    while left < right:
        sum_val = book[left] + book[right]

        if sum_val == target:
            return "YES"
        elif sum_val < target:
            left += 1
        else:
            right -= 1

    return "NO"

n = int(input("Enter number of books: "))
book = list(map(int, input("Enter book values: ").split()))

target = int(input("Enter target sum: "))

result = read(n, book, target)

print(result)