def main() -> None:
    # 整数の入力
    n = int(input())
    # スペース区切りの整数の入力
    l = map(int, input().split())

    k = 0
    tmp_list = list(l)
    while True:
        is_even = False

        # 全て偶数かチェック
        for tmp in tmp_list:
            # 奇数のとき
            if tmp % 2 != 0:
                is_even = True
                break

        # 奇数のとき
        if is_even:
            break

        for i in range(len(tuple(tmp_list))):
            tmp_list[i] = tmp_list[i] / 2
        k += 1

    print(k)


# こっちの方が早い
def main2() -> None:
    # 整数の入力
    n = int(input())
    # スペース区切りの整数の入力
    l = map(int, input().split())

    k = 0
    tmp_list = list(l)
    while True:
        # 偶数のみ取得
        filter_odd = tuple(filter(lambda x: x % 2 == 0, tmp_list))

        # 奇数のとき
        if len(filter_odd) != len(tmp_list):
            break

        tmp_list = list(map(lambda x: x / 2, tmp_list))

        k += 1

    print(k)


if __name__ == "__main__":
    main2()
