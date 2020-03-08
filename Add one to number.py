def plusOne(A):
    A = A[::-1]
    carry = 1
    for i in range(len(A)):
        digit = A[i] + carry
        if digit >= 10:
            A[i] = digit % 10
            carry = digit // 10
        else:
            A[i] = A[i] + carry
            carry = 0
            break
    if carry == 0:
        A = A[::-1]
        i = 0
        while A[i] == 0:
            if A[i] == 0:
                A.pop(i)
        return A
    else:
        A.append(carry)
        A = A[::-1]
        i = 0
        while A[i] == 0:
            if A[i] == 0:
                A.pop(i)
        return A


def main():
    print(plusOne([1, 9, 9, 9, 9]))


if __name__ == "__main__":
    main()
