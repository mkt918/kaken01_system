# Week 06: 回数を正確に制御する ― `for` ループ

先週の `while` は「条件を満たす間ずっと繰り返す」でした。
今週は「**ちょうど10回繰り返す**」「リストの全要素を1つずつ処理する」など、**回数・範囲が決まっている**繰り返しに最適な **`for`** を学びます。

---

## レッスン 1: `for` と `range()` ― 回数を指定する

### 基本の書き方

```python
for i in range(5):      # 5回繰り返す
    print(f"{i}回目")   # iは 0, 1, 2, 3, 4 と変化する
```

> **重要**：Pythonは「0から数える」ので `range(5)` は 0, 1, 2, 3, 4 の5回です。

### range() の3つの使い方

| 書き方 | 生成される数列 |
|--------|--------------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8（2ずつ増加）|
| `range(5, 0, -1)` | 5, 4, 3, 2, 1（逆順）|

### ハンズオン 1-A: range() の動きを確認

```python
print("--- range(5) ---")
for i in range(5):
    print(i)

print("--- range(1, 6) ---")
for i in range(1, 6):
    print(i)

print("--- range(0, 10, 3) ---")
for i in range(0, 10, 3):
    print(i)
```

---

## レッスン 2: リストを for でループする

`for` はリストの全要素を順番に処理するのが得意です。

```python
fruits = ["りんご", "バナナ", "ぶどう"]

for fruit in fruits:          # 1つずつ取り出す
    print(f"{fruit} は美味しい！")
```

### enumerate() ― 番号付きで取り出す

```python
fruits = ["りんご", "バナナ", "ぶどう"]

for i, fruit in enumerate(fruits):
    print(f"{i + 1}番目：{fruit}")
```

出力：

```
1番目：りんご
2番目：バナナ
3番目：ぶどう
```

---

## レッスン 3: ループ内での集計

`for` ループは「どんどん足し合わせる」集計が得意です。

```python
total = 0                    # 合計を入れる変数（最初は0）

for i in range(1, 11):       # 1〜10
    total += i               # total = total + i

print(f"1〜10の合計：{total}")   # 55
```

### ハンズオン 3-A: 得点の集計

```python
scores = [85, 72, 91, 60, 78]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"合計：{total}点")
print(f"平均：{average:.1f}点")
```

---

## ドリル 6-1: range() の穴埋め

以下の出力になる `range()` の引数を答えましょう。

```
① 1, 2, 3, 4, 5       → range(___, ___)
② 0, 2, 4, 6, 8       → range(___, ___, ___)
③ 10, 9, 8, 7, 6, 5   → range(___, ___, ___)
④ 3, 6, 9, 12         → range(___, ___, ___)
```

<details>
<summary>答えを見る</summary>

```
① range(1, 6)
② range(0, 10, 2)
③ range(10, 4, -1)
④ range(3, 13, 3)
```

</details>

---

## ドリル 6-2: 実行結果の予測

次のコードを実行すると何が表示されますか？

```python
total = 0

for i in range(1, 6):
    if i % 2 == 0:
        total += i

print(total)
```

<details>
<summary>答えを見る</summary>

```
6
```

解説：1〜5のうち偶数は 2, 4。`total = 2 + 4 = 6`

</details>

---

## ドリル 6-3: 星の階段を作ろう

`for` ループと文字の掛け算を使い、以下のような5段の階段を表示してください。

```
★
★★
★★★
★★★★
★★★★★
```

<details>
<summary>解答例を見る</summary>

```python
for i in range(1, 6):
    print("★" * i)
```

`range(1, 6)` で i は 1, 2, 3, 4, 5 と変化し、`"★" * i` で段が増えます。

</details>

---

## ドリル 6-4: リストの最大値を求めよ

以下のリストから `max()` 関数を使わずに最大値を求めるプログラムを作ってください。

```python
nums = [34, 12, 78, 45, 91, 23]
# for ループを使って最大値を見つけよう
```

ヒント：`maximum = nums[0]` でスタートし、ループで比較します。

<details>
<summary>解答例を見る</summary>

```python
nums = [34, 12, 78, 45, 91, 23]
maximum = nums[0]       # 最初の値を仮の最大値にする

for n in nums:
    if n > maximum:
        maximum = n     # より大きい値が出たら更新

print(f"最大値：{maximum}")   # 91
```

</details>

---

## ドリル 6-5: バグを直せ！

「1から入力した数まで全部掛け算する（階乗）」プログラムにバグがあります。直してください。

```python
n = int(input("何の階乗を計算する？: "))
result = 0           # ← バグ1

for i in range(n):   # ← バグ2
    result *= i

print(f"{n}! = {result}")
```

<details>
<summary>答えを見る</summary>

```
バグ1: result = 0 → result = 1（掛け算の初期値は0ではなく1）
バグ2: range(n) → range(1, n + 1)（0が含まれると全部0になる。1〜nが必要）
```

修正後：

```python
n = int(input("何の階乗を計算する？: "))
result = 1

for i in range(1, n + 1):
    result *= i

print(f"{n}! = {result}")
```

例：5! = 5×4×3×2×1 = 120

</details>

---

## ドリル 6-6: 九九表を出力しよう（総合問題）

`for` ループを2つ重ねて（入れ子ループ）、以下の形式で九九表を表示してください。

```
1×1= 1  1×2= 2  1×3= 3  ...  1×9= 9
2×1= 2  2×2= 4  ...
...
9×1= 9  ...  9×9=81
```

ヒント：外側のループで段（1〜9）、内側のループで列（1〜9）を制御します。
`print(..., end="  ")` で改行しないで横に並べられます。

<details>
<summary>解答例を見る</summary>

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()  # 1行分終わったら改行
```

</details>

---

## ミニプロジェクト: お小遣い貯金シミュレーター

毎月のお小遣いを半年間（6ヶ月）貯金したら毎月いくらになるかシミュレーションします。

### 要件

- 毎月のお小遣い額を入力
- 毎月「〇ヶ月目：〇〇円貯まりました！」と表示
- 最後に合計を表示

### 完成イメージ

```
毎月のお小遣い: 3000
1ヶ月目：3000円貯まりました！
2ヶ月目：6000円貯まりました！
...
6ヶ月目：18000円貯まりました！
半年で合計 18000 円貯まりました！
```

<details>
<summary>解答例を見る</summary>

```python
monthly = int(input("毎月のお小遣い: "))
total = 0

for i in range(1, 7):
    total += monthly
    print(f"{i}ヶ月目：{total}円貯まりました！")

print(f"半年で合計 {total} 円貯まりました！")
```

</details>

---

## 発展チャレンジ: 魔法の三角形ビルダー

ユーザーが入力した段数で「山形の三角形」を作るプログラムを作りましょう。

```
段数: 5
    ★
   ★★★
  ★★★★★
 ★★★★★★★
★★★★★★★★★
```

ヒント：`" " * (n - i)` でスペース、`"★" * (2 * i - 1)` で星を制御します（`i` は 1から）。

---

## 小テスト（全5問）

**Q1.** 繰り返す「回数」が決まっているとき便利なループは？

- A. `if`
- B. `while`
- C. `for`

<details>
<summary>答えを見る</summary>

**C. `for`**

</details>

---

**Q2.** `range(3)` で生成される数列は？

- A. `1, 2, 3`
- B. `0, 1, 2`
- C. `0, 1, 2, 3`

<details>
<summary>答えを見る</summary>

**B. `0, 1, 2`**
Pythonは0から数え始めます。3は含まれません。

</details>

---

**Q3.** `range(2, 10, 3)` で生成される数列は？

- A. `2, 5, 8`
- B. `2, 4, 6, 8`
- C. `2, 3, 4, 5, 6, 7, 8, 9`

<details>
<summary>答えを見る</summary>

**A. `2, 5, 8`**
2から始まり、3ずつ増加。10に達する前（10は含まない）で終了。

</details>

---

**Q4.** `"★" * 4` の出力は？

- A. `★ * 4`
- B. `★★★★`
- C. `4★`

<details>
<summary>答えを見る</summary>

**B. `★★★★`**

</details>

---

**Q5.** 以下のコードの出力は？

```python
total = 0
for i in range(1, 5):
    total += i * 2
print(total)
```

- A. `10`
- B. `20`
- C. `24`

<details>
<summary>答えを見る</summary>

**B. `20`**
i=1: 2、i=2: 4、i=3: 6、i=4: 8。合計 = 2+4+6+8 = **20**

</details>
