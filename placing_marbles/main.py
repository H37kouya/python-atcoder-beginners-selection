
def main() -> None:
    # 文字列の入力
    s = input()

    s1 = s[0]
    s2 = s[1]
    s3 = s[2]

    c = 0
    if s1 == "1":
        c += 1
    if s2 == "1":
        c += 1
    if s3 == "1":
        c += 1

    # 出力
    print(f"{c}")


if __name__ == "__main__":
    main()
