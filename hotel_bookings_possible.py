def hotel_bookings(arrive, depart, k):
    n = len(arrive)
    ans = []
    for i in range(n):
        ans.append((arrive[i], 1))
        ans.append((depart[i], 0))
    ans.sort()
    curr_active, max_active = 0, 0
    for i in range(n + n):
        if ans[i][1] == 1:
            curr_active += 1
            max_active = max(curr_active, max_active)
        else:
            curr_active -= 1
    return max_active >= k


def main():
    print(hotel_bookings([1, 2, 3, 4, 5], [8, 12, 11, 23, 11], k=4)) # The two arrays should be always of same length


if __name__ == '__main__':
    main()
