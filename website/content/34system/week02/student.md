# Week 02: 対話型アプリへの第一歩 ― 「入力」と「計算」

今週は、プログラムを使う人（ユーザー）から情報を聞き出す「**input()**」と、Pythonの計算力を組み合わせて、**対話型アプリ**を作っていきます。

---

## レッスン 1: ユーザーから情報をもらう ― `input()`

`input()` を使うと、プログラムが一時停止して、ユーザーがキーボードで入力するのを待ちます。

### 基本の使い方

```python
name = input("あなたの名前は？: ")
print(f"こんにちは、{name}さん！")
```

実行すると：

```
あなたの名前は？: 田中
こんにちは、田中さん！
```

### input() は「文字列」を返す

`input()` で受け取ったデータは、**必ず文字列（str）** になります。
数字として使いたいときは、**変換が必要**です。

```python
data = input("数字を入力: ")
print(type(data))       # <class 'str'>  ← 文字列！

number = int(data)      # int()で整数に変換
print(type(number))     # <class 'int'>  ← 整数になった
```

### ハンズオン 1-A: 名前と年齢を受け取る

```python
name = input("名前を入力してください: ")
age = int(input("年齢を入力してください: "))

print(f"こんにちは、{name}さん！")
print(f"来年は{age + 1}歳になりますね。")
```

---

## レッスン 2: 数値への変換 ― `int()` と `float()`

| 関数 | 変換先 | 使いどころ |
|------|--------|-----------|
| `int(x)` | 整数 | 個数・年齢・点数など小数が不要なとき |
| `float(x)` | 小数 | 身長・体重・金額など小数が必要なとき |
| `str(x)` | 文字列 | 数字を文字列として扱いたいとき |

```python
age = int(input("年齢: "))            # "17" → 17
height = float(input("身長(cm): "))   # "165.5" → 165.5
score = int(input("点数: "))          # "85" → 85
```

### 変換に失敗する例

```python
x = int("3.14")    # エラー！（floatの文字列はintに直接変換できない）
x = int(float("3.14"))  # OK：先にfloatにしてからintに変換
```

---

## レッスン 3: Pythonの演算子まとめ

| 演算子 | 意味 | 例 | 結果 |
|--------|------|-----|------|
| `+` | 足し算 | `3 + 4` | `7` |
| `-` | 引き算 | `10 - 3` | `7` |
| `*` | 掛け算 | `3 * 4` | `12` |
| `/` | 割り算（小数） | `7 / 2` | `3.5` |
| `//` | 割り算（整数・切り捨て） | `7 // 2` | `3` |
| `%` | 余り | `7 % 2` | `1` |
| `**` | べき乗 | `2 ** 8` | `256` |

### 複合代入演算子（省略形）

```python
score = 100
score += 20     # score = score + 20  と同じ → 120
score -= 10     # score = score - 10  と同じ → 110
score *= 2      # score = score * 2   と同じ → 220
score //= 3     # score = score // 3  と同じ → 73
```

### ハンズオン 3-A: 割り算の違いを確認

```python
a = 17
b = 5

print(f"{a} ÷ {b} = {a / b}")       # 3.4
print(f"{a} ÷ {b} = {a // b} 余り {a % b}")  # 3 余り 2
```

---

## レッスン 4: よく使う計算パターン

### 平均を計算する

```python
score1 = int(input("1教科目の点数: "))
score2 = int(input("2教科目の点数: "))
score3 = int(input("3教科目の点数: "))

average = (score1 + score2 + score3) / 3
print(f"平均点：{average:.1f}点")
```

### 税込価格を計算する

```python
price = int(input("商品の価格（円）: "))
tax_rate = 0.10

tax = int(price * tax_rate)
total = price + tax

print(f"本体価格：{price}円")
print(f"消費税  ：{tax}円")
print(f"税込合計：{total}円")
```

---

## ドリル 2-1: input() と型変換

次のプログラムを完成させてください。
半径（整数）を入力してもらい、円の面積を表示するプログラムです。

```python
PI = 3.14159
radius = ___（半径を整数で受け取る）___

area = PI * radius ** 2
print(f"半径 {radius}cm の円の面積は {area:.2f} cm² です")
```

<details>
<summary>答えを見る</summary>

```python
PI = 3.14159
radius = int(input("半径(cm)を入力してください: "))

area = PI * radius ** 2
print(f"半径 {radius}cm の円の面積は {area:.2f} cm² です")
```

実行例：

```
半径(cm)を入力してください: 5
半径 5cm の円の面積は 78.54 cm² です
```

</details>

---

## ドリル 2-2: 演算子の選択

次の問題に最も適した演算子を答えましょう。

```
① 1時間を分に換算したい（時間 × ___）
② 商品の在庫が5で1人3個ずつ買えるとき、何人買えるか（在庫 ___ 個数）
③ 同じく何個余るか（在庫 ___ 個数）
④ 2の10乗を計算したい（2 ___ 10）
⑤ 商品の金額に8%の税を上乗せしたい（price + price ___ 0.08）
```

<details>
<summary>答えを見る</summary>

```
① * （掛け算）60分
② // （整数割り算）→ 5 // 3 = 1人
③ %  （余り）→ 5 % 3 = 2個
④ ** （べき乗）→ 2 ** 10 = 1024
⑤ *  （掛け算）→ price + price * 0.08
```

</details>

---

## ドリル 2-3: プログラムの出力を予測せよ

次のコードを実行すると何が表示されますか（入力値は `"25"` とします）。

```python
data = input("数字を入れて: ")
a = int(data)
b = a // 7
c = a % 7

print(f"{a}を7で割ると{b}余り{c}")
print(f"float変換：{float(data)}")
print(f"2倍：{a * 2}")
```

<details>
<summary>答えを見る</summary>

```
25を7で割ると3余り4
float変換：25.0
2倍：50
```

解説：
- `25 // 7 = 3`（7×3=21）
- `25 % 7 = 4`（25-21=4）

</details>

---

## ドリル 2-4: バグを直せ！

以下のプログラムには2か所バグがあります。直してください。

```python
price = input("値段を入力: ")
count = input("個数を入力: ")

total = price * count
tax = total * 0.1

print(f"合計（税抜）: {total}円")
print(f"消費税: {tax}円")
```

<details>
<summary>答えを見る</summary>

```
バグ1: price = input(...)   → price = int(input(...))
バグ2: count = input(...)   → count = int(input(...))
```

`input()` は文字列を返すため、数値計算の前に `int()` で変換が必要。

修正後：

```python
price = int(input("値段を入力: "))
count = int(input("個数を入力: "))

total = price * count
tax = total * 0.1

print(f"合計（税抜）: {total}円")
print(f"消費税: {tax}円")
```

</details>

---

## ドリル 2-5: 3教科の成績を処理しよう

国語・数学・英語の点数を入力し、以下を出力するプログラムを作ってください。

- 3教科の合計点
- 3教科の平均点（小数第1位まで）
- 最高点の教科名（ヒント：今の知識で作るには点数を直接比べる）

```
国語の点数: 75
数学の点数: 90
英語の点数: 82
-----
合計：247点
平均：82.3点
```

<details>
<summary>解答例を見る</summary>

```python
kokugo = int(input("国語の点数: "))
math = int(input("数学の点数: "))
eigo = int(input("英語の点数: "))

total = kokugo + math + eigo
average = total / 3

print("-----")
print(f"合計：{total}点")
print(f"平均：{average:.1f}点")
```

</details>

---

## ミニプロジェクト: BMI計算機を作ろう

身長と体重を入力してもらい、BMIを計算して判定するプログラムを作ります。

### BMIの計算式

```
BMI = 体重(kg) ÷ 身長(m) ÷ 身長(m)
```

### 判定基準

| BMI | 判定 |
|-----|------|
| 18.5未満 | 低体重 |
| 18.5以上25未満 | 標準 |
| 25以上30未満 | 過体重 |
| 30以上 | 肥満 |

### 完成イメージ

```
=== BMI 計算機 ===
身長(cm)を入力: 170
体重(kg)を入力: 65
-----------------
身長: 170.0 cm
体重: 65.0 kg
BMI : 22.49
判定: 標準
```

<details>
<summary>解答例を見る</summary>

```python
print("=== BMI 計算機 ===")
height_cm = float(input("身長(cm)を入力: "))
weight = float(input("体重(kg)を入力: "))

height_m = height_cm / 100
bmi = weight / height_m / height_m

print("-----------------")
print(f"身長: {height_cm} cm")
print(f"体重: {weight} kg")
print(f"BMI : {bmi:.2f}")

# 判定（if文は次週学ぶので今はコメントのみ）
# if bmi < 18.5:  判定 = 低体重
# elif bmi < 25:  判定 = 標準
# elif bmi < 30:  判定 = 過体重
# else:           判定 = 肥満
```

</details>

---

## 発展チャレンジ: お釣り計算機

商品の価格と受け取ったお金を入力し、お釣りの枚数を最小枚数で表示するプログラムを作りましょう。

### 要件

- 硬貨・紙幣：500円、100円、50円、10円、5円、1円
- 各金種の枚数を `//` と `%` を使って計算する

### 完成イメージ

```
商品の値段: 378
受け取ったお金: 1000
お釣りは 622 円です
-----
500円: 1枚
100円: 1枚
 50円: 0枚
 10円: 2枚
  5円: 0枚
  1円: 2枚
```

<details>
<summary>解答例を見る</summary>

```python
price = int(input("商品の値段: "))
paid = int(input("受け取ったお金: "))

change = paid - price
print(f"お釣りは {change} 円です")
print("-----")

coins = [500, 100, 50, 10, 5, 1]
remaining = change

for coin in coins:
    count = remaining // coin
    remaining = remaining % coin
    print(f"{coin:>4}円: {count}枚")
```

（注：`for` 文は今後のWeekで学びます。今は `//` と `%` の部分だけ意識しましょう）

</details>

---

## 小テスト（全5問）

**Q1.** `input()` で受け取ったデータの型は？

- A. int（整数）
- B. str（文字列）
- C. float（小数）

<details>
<summary>答えを見る</summary>

**B. str（文字列）**
`input()` は常に文字列を返します。数値として使うには `int()` や `float()` で変換が必要です。

</details>

---

**Q2.** `17 % 5` の結果は？

- A. `3`
- B. `2`
- C. `3.4`

<details>
<summary>答えを見る</summary>

**B. `2`**
`17 ÷ 5 = 3 余り 2`。`%` は余りを返します。

</details>

---

**Q3.** 次のコードでエラーが起きる理由は？

```python
age = input("年齢: ")
print(age + 1)
```

- A. `print()` の使い方が間違っている
- B. `input()` は文字列を返すので、整数と足せない
- C. `age` という変数名が使えない

<details>
<summary>答えを見る</summary>

**B. `input()` は文字列を返すので、整数と足せない**
`age = int(input("年齢: "))` と書けば解決します。

</details>

---

**Q4.** `int(float("3.9"))` の結果は？

- A. `4`（四捨五入）
- B. `3`（切り捨て）
- C. エラー

<details>
<summary>答えを見る</summary>

**B. `3`（切り捨て）**
`float("3.9")` → `3.9`、`int(3.9)` → `3`（切り捨て）。四捨五入ではない点に注意。

</details>

---

**Q5.** 以下のコードの出力は？

```python
a = 10
a += 3
a *= 2
a -= 1
print(a)
```

- A. `25`
- B. `26`
- C. `23`

<details>
<summary>答えを見る</summary>

**A. `25`**
`a = 10` → `a = 13`（+3）→ `a = 26`（×2）→ `a = 25`（-1）

</details>
