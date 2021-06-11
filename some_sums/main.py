def main() -> None:
    # スペース区切りの整数の入力
    n, a, b = map(int, input().split())

    s = 0
    for k in range(0, n + 1):

        t = 0
        i = k
        while True:
            t += i % 10
            i //= 10
            if i < 10:
                t += i
                break

        if a <= t <= b:
            s += k
    print(s)


if __name__ == "__main__":
    main()
