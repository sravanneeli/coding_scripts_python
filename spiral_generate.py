def generate(A):
    output = [[0] * A for l in range(A)]
    i, j, pos = 0, 0, 0
    m, n = A, A
    index = 1
    while i < m and j < n:
        for k in range(j, n):
            output[i][k] = index
            index += 1
        i += 1
        for k in range(i, m):
            output[k][n - 1] = index
            index += 1
        n -= 1
        if i < m:
            for k in range(n - 1, j - 1, -1):
                output[m - 1][k] = index
                index += 1
            m -= 1
        if j < n:
            for k in range(m - 1, i - 1, -1):
                output[k][j] = index
                index += 1
            j += 1
    return output


def main():
    print(generate(5))


if __name__ == "__main__":
    main()
