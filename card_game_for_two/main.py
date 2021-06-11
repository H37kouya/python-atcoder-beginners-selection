def main() -> None:
    # 整数の入力
    n = int(input())
    # スペース区切りの整数の入力
    l = map(int, input().split())

    ret = 0
    for idx, num in enumerate(sorted(l, reverse=True)):
        if idx % 2 == 0:
            ret += num
        else:
            ret -= num

    print(ret)


if __name__ == "__main__":
    main()
