def main() -> None:
    # 整数の入力
    a = int(input())  # 500
    b = int(input())  # 100
    c = int(input())  # 50
    x = int(input())  # result

    cnt = 0

    for i in range(0, a + 1):
        for j in range(0, b + 1):
            for k in range(0, c + 1):
                if x == (500 * i + 100 * j + 50 * k):
                    cnt += 1

    # 出力
    print(f"{cnt}")


def main2() -> None:
    # 整数の入力
    a = int(input())  # 500
    b = int(input())  # 100
    c = int(input())  # 50
    x = int(input())  # result

    cnt = 0
    k_list = [i for i in range(0, c + 1)]

    for i in range(0, a + 1):
        for j in range(0, b + 1):
            cnt += len(
                tuple(filter(lambda k: x == (500 * i + 100 * j + 50 * k), k_list))
            )

    # 出力
    print(f"{cnt}")


if __name__ == "__main__":
    main2()
