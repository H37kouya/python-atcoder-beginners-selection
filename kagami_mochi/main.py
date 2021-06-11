def main() -> None:
    # 整数の入力
    n = int(input())

    d_list = []
    for _ in range(0, n):
        d_list.append(int(input()))

    # d_list = [int(input()) for _ in range(0, n)]

    print(len(set(d_list)))


if __name__ == "__main__":
    main()
