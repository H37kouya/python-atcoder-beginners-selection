EVEN = 'Even'
ODD = 'Odd'


def main() -> None:
    # スペース区切りの整数の入力
    a, b = map(int, input().split())

    if a * b % 2 == 0:
        # 出力
        print(f"{EVEN}")
    else:
        print(f"{ODD}")


if __name__ == "__main__":
    main()
