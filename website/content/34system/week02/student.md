# Week 02: 対話型アプリへの第一歩 ― 「入力」と「計算」

今週は、プログラムを使う人（ユーザー）から情報を聞き出す「**input()**」と、Pythonの計算力を組み合わせて、**対話型アプリ**を作っていきます。

## 📊 インタラクティブスライド資料

まずこちらのスライドを見て、input()と演算子を視覚的に理解しましょう。左右の矢印キーまたはボタンでスライドを進めます。

<div style="width: 100%; max-width: 100%; margin: 30px 0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
<iframe src="./slides.html" style="width: 100%; height: 600px; border: none;"></iframe>
</div>

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

## 【重要】データ型と計算結果の違い

**同じ数値でも、int か float かで計算結果が大きく変わります！**

### Case 1: 税金計算のトラップ

```python
price = 1000
tax_rate = 0.10

# ❌ パターンA：整数で計算
tax_int = int(price * tax_rate)      # 100.0 → 100に切り捨て
total_int = price + tax_int           # 1100
print(f"合計（int）：{total_int}円")    # 1100円 ✓正確

# ✓ パターンB：小数で計算
tax_float = price * tax_rate          # 100.0（そのまま）
total_float = price + tax_float       # 1100.0
print(f"合計（float）：{total_float}円") # 1100.0円 ✓正確

# ⚠ 注意：微妙な違いが出る例
price = 999
tax_int = int(price * 0.10)           # 99.9 → 99に切り捨て ⚠
total_int = price + tax_int           # 1098円（本来は1098.9円）
```

> **学習ポイント**：`int()` で変換すると **小数点以下が切り捨てられます**。金額計算では注意が必要です！

### Case 2: 演算の順序も重要

```python
# 同じ計算でも、型が違うと出力形式が変わる
value = 10

# パターンA：intで計算
result_int = value // 3               # 10 // 3 = 3（余りは切り捨て）
print(result_int)                     # 3 ← 整数として表示

# パターンB：floatで計算
result_float = value / 3              # 10 / 3 = 3.3333...
print(result_float)                   # 3.3333333333333335 ← 小数として表示

# パターンC：計算後に型変換
result_convert = int(value / 3)       # int(3.333...) = 3
print(result_convert)                 # 3
```

### データ型を選ぶチェックリスト

| 状況 | 選択 | 理由 |
|------|------|------|
| 個数・人数・枚数 | `int` | 小数は発生しない |
| 金額（価格計算） | `float` or `int` | 端数処理まで考える必要あり |
| 身長・体重・温度 | `float` | 小数が自然に発生 |
| 年齢・点数 | `int` | 通常は整数で十分 |
| 計算の中途結果 | `float` | 精度を保つため |
| 最終表示値 | 用途で決定 | 「何を表示するか」で決める |

---

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
print(f"平均点：{average:.1f}点")  # 小数第1位まで表示
```

### 税込価格を計算する ★型の選択が重要！

```python
price = int(input("商品の価格（円）: "))
tax_rate = 0.10

tax = int(price * tax_rate)  # ⚠ ここで int() を使う理由：「端数は円単位で切り捨て」
total = price + tax

print(f"本体価格：{price}円")
print(f"消費税  ：{tax}円")    # 税金は整数の円で表示するため
print(f"税込合計：{total}円")
```

#### この計算で何が起きるか

```
例：商品価格 999円の場合
①  price * tax_rate = 999 * 0.10 = 99.9
②  int(99.9) = 99  ← 小数点以下が切り捨てられる！
③  total = 999 + 99 = 1098円

⚠ 注意：int()を使わないと...
  tax = 99.9（小数）→ 表示が「99.9円」になって不自然
```

#### 代替案：小数で計算しておく

```python
price = int(input("商品の価格（円）: "))
tax_rate = 0.10

tax = price * tax_rate         # 小数のまま計算
total = price + tax

print(f"本体価格：{price}円")
print(f"消費税  ：{tax:.0f}円")  # 小数第0位で表示（整数のように見える）
print(f"税込合計：{total:.0f}円")
```

> **どちらを選ぶ？**
> - **int()版**：税金は必ず整数円（シンプル、実務的）
> - **float版**：計算過程で精度を保つ（数学的に正確）
> 
> 実務では **int()版** がよく使われます。

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

## ドリル 2-4: バグを直せ！ ★重要：型変換を理解しよう

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

#### なぜバグが生じるのか？

もしバグのままだと...

```python
price = input("値段を入力: ")     # price = "150" （文字列）
count = input("個数を入力: ")     # count = "3"   （文字列）

total = price * count             # "150" * "3" = "150150150" ⚠ 掛け算ではなく繰り返し！
tax = total * 0.1                 # TypeError！（文字列に 0.1 は掛けられない）
```

#### 正しい修正方法

修正後：

```python
price = int(input("値段を入力: "))    # price = 150 （整数）
count = int(input("個数を入力: "))    # count = 3   （整数）

total = price * count                 # 150 * 3 = 450 ✓ 正しい計算
tax = int(total * 0.1)                # 45 （消費税は整数で）

print(f"合計（税抜）: {total}円")
print(f"消費税: {tax}円")
```

実行結果：

```
値段を入力: 150
個数を入力: 3
合計（税抜）: 450円
消費税: 45円
```

> **重要ポイント**：
> - `input()` は **常に文字列** を返す
> - 数値計算する前に、必ず `int()` または `float()` で変換する
> - 型変換を忘れると、予期しない結果や**エラー**が発生する

</details>

---

## ドリル 2-5: 3教科の成績を処理しよう ★型の使い分け

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
kokugo = int(input("国語の点数: "))     # 点数は整数で受け取る
math = int(input("数学の点数: "))
eigo = int(input("英語の点数: "))

total = kokugo + math + eigo             # int + int + int = int（合計は整数）
average = total / 3                      # int / 3 = float（平均は小数になる）

print("-----")
print(f"合計：{total}点")                 # 整数として表示
print(f"平均：{average:.1f}点")           # 小数第1位まで表示
```

#### 型が変わる様子

```
kokugo = 75 (int)
math = 90 (int)
eigo = 82 (int)

total = 75 + 90 + 82 = 247 (int のまま)
average = 247 / 3 = 82.33333... (float に変わる！)

出力時に {average:.1f} で小数第1位までに調整
→ 82.3 と表示される
```

> **注意**：計算の途中で型が変わることがあります。
> - `int / int` = `float`（割り算の結果は小数）
> - `int // int` = `int`（整数割りは整数）
> - `int * int` = `int`（掛け算は整数のまま）

</details>

---

## ミニプロジェクト: BMI計算機を作ろう ★float が必須な理由

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
height_cm = float(input("身長(cm)を入力: "))  # ⚠ float が必須！小数を受け取る
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

#### なぜ float を使う？

もし `int()` を使ったら...

```python
# ❌ 間違った方法：int を使う
height_cm = int(input("身長(cm)を入力: "))  # 170.5 → 170 に切り捨て ⚠
weight = int(input("体重(kg)を入力: "))     # 65.5 → 65 に切り捨て ⚠

# 計算結果が大きく変わってしまう！
bmi = weight / height_m / height_m  # 値が不正確

# ✓ 正しい方法：float を使う
height_cm = float(input("身長(cm)を入力: "))  # 170.5 → 170.5 （正確）
weight = float(input("体重(kg)を入力: "))     # 65.5 → 65.5 （正確）
```

> **重要**：小数が自然に発生する値（身長・体重・温度など）は、**必ず `float()` で受け取る**！

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
