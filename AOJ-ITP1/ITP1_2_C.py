# 入力を空白区切りで読み込み、整数に変換
a, b, c = map(int, input().split())

# 小さい順に並べるための比較と交換
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

# 結果を出力
print(a, b, c)

"""
# 入力を空白区切りで読み込み、整数に変換
a, b, c = map(int, input().split())

# 3つの数をリストに格納し、並べ替え
numbers = [a, b, c]
numbers.sort()

# 並べ替えた結果を出力（スペース区切りで）
print(*numbers)

"""