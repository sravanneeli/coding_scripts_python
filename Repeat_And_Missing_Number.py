def repeatedNumber(A):
    counter = {}
    a = 0
    b = 0
    for i in range(len(A)):
        counter[i + 1] = 0
    for i in range(len(A)):
        counter[A[i]] += 1
    for key, value in counter.items():
        if value == 0:
            b = key
        if value == 2:
            a = key
    return [a, b]


def main():
    A, B = repeatedNumber([1, 2, 3, 5, 3])
    print("Repeat number is {} and missing number is {}".format(A, B))


if __name__ == "__main__":
    main()
