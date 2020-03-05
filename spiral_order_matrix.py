def spiral_print(mat):
    m, n = len(mat), len(mat[0])
    k, l, pos = 0, 0, 0
    spiral_order = [0] * (m * n)
    while k < m and l < n:
        for i in range(l, n):
            spiral_order[pos] = mat[k][i]
            pos += 1
        k += 1
        for i in range(k, m):
            spiral_order[pos] = mat[i][n - 1]
            pos += 1
        n -= 1
        if k < m:
            for i in range(n - 1, (l - 1), -1):
                spiral_order[pos] = mat[k - 1][i]
                pos += 1
            m -= 1
        if l < n:
            for i in range(m - 1, k - 1, -1):
                spiral_order[pos] = mat[i][l]
                pos += 1
            l += 1
    return spiral_order


matrix = [[1, 2, 3, 5], [4, 5, 6, 9], [7, 8, 9, 123]]
print(spiral_print(matrix))
