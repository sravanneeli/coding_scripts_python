def coverPoints(A, B):
    steps = 0
    for i in range(1, len(A)):
        steps += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))
    return steps


def main():
    steps = coverPoints([1, 2, 3, 4], [3, 5, 7, 1])
    print("Minimum no of steps taken to cover the points in 2d grid", steps)


if __name__ == "__main__":
    main()
