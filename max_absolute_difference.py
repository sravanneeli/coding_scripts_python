import sys


def maxArr(A):
    max1 = - sys.maxsize
    min1 = sys.maxsize
    max2 = - sys.maxsize
    min2 = sys.maxsize
    for i in range(len(A)):
        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)

    return max(max1 - min1, max2 - min2)


def main():
    print("Maximum Absolute Difference is", maxArr([1, 4, -5, 2, 11, 53, 2]))


if __name__ == "__main__":
    main()
