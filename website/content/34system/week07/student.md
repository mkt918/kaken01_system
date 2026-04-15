# Week 07: データを一網打尽！ ― リスト（配列）

今まで1つの変数には「1つのデータ」しか入れられませんでした。
クラス全員の点数や、勇者の所持品を1つずつ変数にすると100個になってしまいます。
今週は「**複数のデータを一列に並べてまとめる**」仕組み、**リスト** を学びます。

---

## レッスン 1: リストの作り方と取り出し方

### リストを作る

```python
fruits = ["りんご", "バナナ", "ぶどう"]   # 文字列のリスト
scores = [85, 72, 91, 60]              # 数値のリスト
mixed = ["田中", 17, True, 3.14]       # 混在もOK
```

### インデックスで取り出す（0から数える！）

```python
fruits = ["りんご", "バナナ", "ぶどう"]

print(fruits[0])    # りんご（0番目）
print(fruits[1])    # バナナ（1番目）
print(fruits[2])    # ぶどう（2番目）
print(fruits[-1])   # ぶどう（後ろから1番目）
print(fruits[-2])   # バナナ（後ろから2番目）
```

### ハンズオン 1-A: インデックスの確認

```python
items = ["ひのきのぼう", "やくそう", "布の服", "金の盾"]

print(items[0])    # ひのきのぼう
print(items[-1])   # 金の盾
print(len(items))  # 4（要素数）
```

---

## レッスン 2: リストの変更 ― 追加・書き換え・削除

### 値の書き換え

```python
items = ["ひのきのぼう", "やくそう", "布の服"]
items[0] = "はがねの剣"    # 0番目を上書き
print(items)              # ['はがねの剣', 'やくそう', '布の服']
```

### 末尾に追加 `append()`

```python
members = []                  # 空のリスト
members.append("田中")
members.append("鈴木")
members.append("佐藤")
print(members)               # ['田中', '鈴木', '佐藤']
print(len(members))          # 3
```

### 削除 `remove()` と `pop()`

```python
fruits = ["りんご", "バナナ", "ぶどう"]

fruits.remove("バナナ")       # 値を指定して削除
print(fruits)                # ['りんご', 'ぶどう']

last = fruits.pop()          # 末尾を取り出して削除
print(last)                  # ぶどう
print(fruits)                # ['りんご']
```

---

## レッスン 3: リストと for ループの組み合わせ

リストと `for` を組み合わせると、全要素を処理できます。

```python
scores = [85, 72, 91, 60, 78]
total = 0

for score in scores:
    total += score

print(f"合計：{total}点")
print(f"平均：{total / len(scores):.1f}点")
```

### スライス ― 部分リストを取り出す

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:3])    # [20, 30]（1番目から3番目の手前まで）
print(nums[:3])     # [10, 20, 30]（先頭から3番目の手前まで）
print(nums[2:])     # [30, 40, 50]（2番目から末尾まで）
```

---

## ドリル 7-1: インデックスの選択

```python
weapons = ["剣", "槍", "弓", "杖", "斧"]
```

このリストから以下を取り出すコードを書いてください。

```
① 「槍」を取り出す
② 「斧」を後ろから指定して取り出す
③ 「弓」と「杖」を スライス で取り出す（結果：['弓', '杖']）
```

<details>
<summary>答えを見る</summary>

```python
weapons = ["剣", "槍", "弓", "杖", "斧"]

print(weapons[1])     # 槍
print(weapons[-1])    # 斧
print(weapons[2:4])   # ['弓', '杖']
```

</details>

---

## ドリル 7-2: append() でリストを作る

3回入力させて、入力した値をリストに溜め、最後に一覧表示するプログラムを作ってください。

```
例：
好きな食べ物: ラーメン
好きな食べ物: 寿司
好きな食べ物: ピザ
あなたの好きな食べ物：['ラーメン', '寿司', 'ピザ']
```

<details>
<summary>解答例を見る</summary>

```python
foods = []

for i in range(3):
    food = input("好きな食べ物: ")
    foods.append(food)

print(f"あなたの好きな食べ物：{foods}")
```

</details>

---

## ドリル 7-3: 実行結果の予測

次のコードを実行すると何が表示されますか？

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = []

for n in nums:
    if n > 4:
        result.append(n)

print(result)
print(len(result))
```

<details>
<summary>答えを見る</summary>

```
[5, 9, 6]
3
```

解説：4より大きい値は 5, 9, 6 の3つ。

</details>

---

## ドリル 7-4: リストの合計と平均

5人分のテスト点数が入ったリストについて、合計・平均・最高点・最低点を表示するプログラムを作ってください。

```python
scores = [78, 92, 65, 88, 71]
# max() や min() は使わずに for ループで求めよう
```

<details>
<summary>解答例を見る</summary>

```python
scores = [78, 92, 65, 88, 71]
total = 0
maximum = scores[0]
minimum = scores[0]

for s in scores:
    total += s
    if s > maximum:
        maximum = s
    if s < minimum:
        minimum = s

average = total / len(scores)
print(f"合計：{total}点")
print(f"平均：{average:.1f}点")
print(f"最高点：{maximum}点")
print(f"最低点：{minimum}点")
```

</details>

---

## ドリル 7-5: バグを直せ！

以下のプログラムには2か所バグがあります。直してください。

```python
scores = [85, 72, 91]

# 各点数に10点ボーナスを加えて表示
for i in range(len(scores)):
    scores[i] = scores[i] + 10

# 合計を計算
total = 0
for score in scores:
    total = score     # ← バグ

print(f"ボーナス後の点数：{scores}")
print(f"合計：{total}")
```

<details>
<summary>答えを見る</summary>

```
バグ: total = score  →  total += score
```

`total = score` は「scoreで上書き」してしまうため、最後のスコアしか残りません。
`total += score` で「足し合わせる」必要があります。

修正後：

```python
scores = [85, 72, 91]

for i in range(len(scores)):
    scores[i] = scores[i] + 10

total = 0
for score in scores:
    total += score

print(f"ボーナス後の点数：{scores}")
print(f"合計：{total}")
```

</details>

---

## ドリル 7-6: 条件で絞り込んで別リストに（総合問題）

点数リストから「70点以上」の点数だけを取り出し、新しいリストに入れて表示してください。さらに「70点未満だった人数」も表示してください。

```python
all_scores = [88, 54, 72, 45, 91, 63, 77, 39, 85, 60]
```

<details>
<summary>解答例を見る</summary>

```python
all_scores = [88, 54, 72, 45, 91, 63, 77, 39, 85, 60]
passed = []
failed_count = 0

for s in all_scores:
    if s >= 70:
        passed.append(s)
    else:
        failed_count += 1

print(f"70点以上の点数：{passed}")
print(f"合格者数：{len(passed)}人")
print(f"70点未満の人数：{failed_count}人")
```

</details>

---

## ミニプロジェクト: クラス成績集計システム

クラス人数を入力してもらい、全員の点数を入力して、成績レポートを出力するプログラムを作りましょう。

### 要件

- 人数を入力 → その回数分点数を入力してリストに追加
- 合計・平均・最高点・最低点を表示
- 合格（60点以上）と不合格の人数を表示

### 完成イメージ

```
何人分の点数を入力しますか？: 4
1人目の点数: 85
2人目の点数: 42
3人目の点数: 77
4人目の点数: 61
---
点数一覧：[85, 42, 77, 61]
合計：265点 / 平均：66.3点
最高点：85点 / 最低点：42点
合格（60点以上）：3人 / 不合格：1人
```

<details>
<summary>解答例を見る</summary>

```python
n = int(input("何人分の点数を入力しますか？: "))
scores = []

for i in range(1, n + 1):
    s = int(input(f"{i}人目の点数: "))
    scores.append(s)

total = 0
maximum = scores[0]
minimum = scores[0]
passed = 0

for s in scores:
    total += s
    if s > maximum:
        maximum = s
    if s < minimum:
        minimum = s
    if s >= 60:
        passed += 1

print("---")
print(f"点数一覧：{scores}")
print(f"合計：{total}点 / 平均：{total / n:.1f}点")
print(f"最高点：{maximum}点 / 最低点：{minimum}点")
print(f"合格（60点以上）：{passed}人 / 不合格：{n - passed}人")
```

</details>

---

## 発展チャレンジ: 単語帳アプリ

`while True` ループで「終了」が入力されるまで単語を追加し続け、最後にまとめて表示するアプリを作りましょう。

```
=== 単語帳アプリ ===
単語を入力（「終了」でストップ）: apple
単語を入力（「終了」でストップ）: orange
単語を入力（「終了」でストップ）: banana
単語を入力（「終了」でストップ）: 終了
---
3個の単語を登録しました：
1: apple
2: orange
3: banana
```

---

## 小テスト（全5問）

**Q1.** リストを作るのに使うカッコはどれ？

- A. `{ }`
- B. `( )`
- C. `[ ]`

<details>
<summary>答えを見る</summary>

**C. `[ ]`**

</details>

---

**Q2.** `items = ["剣", "槍", "弓"]` で「槍」を取り出すのは？

- A. `items[0]`
- B. `items[1]`
- C. `items[2]`

<details>
<summary>答えを見る</summary>

**B. `items[1]`**
インデックスは0から始まります。

</details>

---

**Q3.** リストの末尾に新しいデータを追加する命令は？

- A. `add()`
- B. `insert()`
- C. `append()`

<details>
<summary>答えを見る</summary>

**C. `append()`**

</details>

---

**Q4.** `nums = [10, 20, 30, 40, 50]` のとき `nums[1:3]` の結果は？

- A. `[10, 20, 30]`
- B. `[20, 30]`
- C. `[20, 30, 40]`

<details>
<summary>答えを見る</summary>

**B. `[20, 30]`**
スライスは「1番目から3番目の手前まで」なので、インデックス1と2の要素です。

</details>

---

**Q5.** 以下のコードで `result` の値は？

```python
nums = [1, 2, 3, 4, 5]
result = 0

for n in nums:
    if n % 2 != 0:
        result += n

print(result)
```

- A. `6`
- B. `9`
- C. `15`

<details>
<summary>答えを見る</summary>

**B. `9`**
奇数（余りが0でない）は 1, 3, 5。合計 = 1 + 3 + 5 = **9**

</details>
