def diagonal(A):
    output = []
    N = len(A)
    for i in range(N):
        temp = []
        bound = i
        row = 0
        while bound > -1 and row < N:
            temp.append(A[row][bound])
            bound -= 1
            row += 1
        output.append(temp)
    for i in range(1, N):
        temp = []
        bound = i
        col = N - 1
        while bound < N and col > -1:
            temp.append(A[bound][col])
            bound += 1
            col -= 1
        output.append(temp)
    return output


def main():
    print(diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Enter only square matrix


if __name__ == "__main__":
    main()
