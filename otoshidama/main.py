def main() -> None:
    # スペース区切りの整数の入力
    n, y = map(int, input().split())

    for ten_yen in range(0, n + 1):
        for five_yen in range(0, n + 1 - ten_yen):
            one_yen = n - ten_yen - five_yen
            if y == (ten_yen * 10000 + five_yen * 5000 + one_yen * 1000):
                print(ten_yen, five_yen, one_yen)
                return

    print(-1, -1, -1)


if __name__ == "__main__":
    main()
