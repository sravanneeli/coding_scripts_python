def getRow(A):
    output = [[1]]
    if A == 0:
        return output[0]
    output[0] = [1, 1]
    if A == 1:
        return output[0]
    for i in range(1, A):
        temp = [1]
        for j in range(1,len(output[0])):
            temp.append(output[0][j-1]+output[0][j])
        temp.append(1)
        output[0] = temp
    return output[0]


def main():
    print(getRow(10))


if __name__ == "__main__":
    main()
