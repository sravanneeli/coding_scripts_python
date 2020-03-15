def pascal_triangle(A):
    output = []
    if A == 0:
        return output
    output.append([1])
    if A == 1:
        return output
    output.append([1, 1])
    if A == 2:
        return output
    for i in range(2, A):
        temp = [1]
        for j in range(1, len(output[-1])):
            temp.append(output[-1][j - 1] + output[-1][j])
        temp.append(1)
        output.append(temp)
    return output


def main():
    print(pascal_triangle(5))


if __name__ == "__main__":
    main()
