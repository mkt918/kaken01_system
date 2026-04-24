# Week 01-2: 文字の出力 ― f-string 完全ガイド

> 📊 **スライド資料を先に見ましょう！**：[W1-2 - インタラクティブスライド](./slides.html) で、f-stringの全機能を視覚的に理解できます。

f-string（フォーマット済み文字列リテラル）は、Pythonで変数を文字に埋め込む最も強力で柔軟な方法です。
このセクションでは、基本から応用的なフォーマット方法まで、詳しく解説します。

---

## レッスン 1: f-string の基本

### f-string とは？

f-string は、文字列の先頭に `f` をつけることで、`{}` の中に変数や式を直接埋め込める仕組みです。

```python
name = "田中"
age = 16

print(f"名前：{name}")      # 名前：田中
print(f"年齢：{age}歳")    # 年齢：16歳
```

### f-string を使わない方法との比較

#### 方法1: カンマ区切り（昔ながらの方法）

```python
name = "田中"
age = 16
print("名前：", name, "年齢：", age)
# → 名前： 田中 年齢： 16
```

問題：スペースが余分に挿入される

#### 方法2: `+` で文字を連結（NG の例）

```python
name = "田中"
age = 16
# print("名前：" + name + "年齢：" + age)  # ❌ エラー！整数は足せない
print("名前：" + name + "年齢：" + str(age))  # str() で変換が必要
# → 名前：田中年齢：16
```

問題：型の変換が手間

#### 方法3: `%` フォーマット（古い方法）

```python
name = "田中"
age = 16
print("名前：%s 年齢：%d" % (name, age))
# → 名前：田中 年齢：16
```

問題：書き方が複雑で読みにくい

#### 方法4: `.format()` メソッド

```python
name = "田中"
age = 16
print("名前：{} 年齢：{}".format(name, age))
# → 名前：田中 年齢：16
```

問題：対応させるのが面倒

#### 方法5: **f-string（推奨） ★**

```python
name = "田中"
age = 16
print(f"名前：{name} 年齢：{age}歳")
# → 名前：田中 年齢：16歳
```

✅ **最も読みやすく、シンプル！**

---

## レッスン 2: f-string の仕組み

### 波括弧 `{}` の中には何が入る？

f-string の `{}` の中には、以下のものを入れられます。

#### ① 変数

```python
score = 85
print(f"点数：{score}")  # 点数：85
```

#### ② 式（計算）

```python
x = 10
y = 20
print(f"合計：{x + y}")  # 合計：30
```

#### ③ メソッド呼び出し

```python
text = "python"
print(f"大文字：{text.upper()}")  # 大文字：PYTHON
```

#### ④ if 式（三項演算子）

```python
age = 17
print(f"ステータス：{'成人' if age >= 18 else '未成年'}")
# → ステータス：未成年
```

> **大事な点**：`{}` の中は「Pythonコード」として評価されます。だから計算も式も使えます！

---

## レッスン 3: フォーマット指定子（書式設定）

f-string は、`{}` の中に `:` の後に**フォーマット指定子**を書くことで、表示方法を細かく制御できます。

### 基本の書き方

```python
値 = 100
print(f"{値:5}")    # フォーマット指定子：「5」
```

### 3.1: 右寄せ・左寄せ・中央寄せ

#### 右寄せ（`>`）

数字や名前を右側に寄せたい場合：

```python
name1 = "太郎"
name2 = "花子"
price1 = 1500
price2 = 250

print(f"{name1:>8} {price1:>6}円")
print(f"{name2:>8} {price2:>6}円")

# 出力：
#      太郎   1500円
#      花子    250円
```

> **右寄せのコツ**：金額や数字の列をそろえたいときに使う。金額表示では金額を右寄せすると見やすい。

#### 左寄せ（`<`）

```python
item1 = "りんご"
item2 = "バナナ"

print(f"{item1:<8} 150円")
print(f"{item2:<8} 120円")

# 出力：
# りんご       150円
# バナナ       120円
```

#### 中央寄せ（`^`）

```python
title = "メニュー"
print(f"{title:^15}")

# 出力：
#     メニュー    
```

---

### 3.2: ゼロ埋め（`0` 埋め）

数字の前にゼロを詰めたい場合（例：学籍番号、日時）：

```python
student_id = 7
print(f"学籍番号：{student_id:03d}")      # 007
print(f"学籍番号：{student_id:05d}")      # 00007

year = 2026
month = 4
day = 21
print(f"日付：{year}-{month:02d}-{day:02d}")  # 2026-04-21
```

> **`03d` の意味**：`0` で埋め、最低3桁。`d` は「整数」を意味します。

---

### 3.3: 桁区切り（カンマ区切り）

大きな数字を見やすくするために、千の位にカンマを入れる：

```python
price = 1500000
print(f"価格：{price:,}円")            # 価格：1,500,000円

population = 125000000
print(f"人口：{population:,}人")       # 人口：125,000,000人
```

> **`,` の役割**：自動的に3桁ごとにカンマが挿入されます。

---

### 3.4: 小数点以下の桁数を指定

```python
pi = 3.141592653589793

print(f"π = {pi}")          # π = 3.141592653589793（全部表示）
print(f"π = {pi:.2f}")      # π = 3.14（小数第2位）
print(f"π = {pi:.4f}")      # π = 3.1416（小数第4位）

average = 85.333333
print(f"平均：{average:.1f}点")  # 平均：85.3点
```

> **`.2f` の意味**：`.` は小数を意味し、`2` は小数第2位、`f` は浮動小数点数（小数）を意味します。

---

### 3.5: パーセント表記

```python
score = 85
max_score = 100
percentage = score / max_score

print(f"得点率：{percentage:.1%}")      # 得点率：85.0%
print(f"正答率：{0.8765:.2%}")          # 正答率：87.65%

# 別の書き方：
print(f"得点率：{percentage*100:.1f}%")  # 得点率：85.0%
```

> **`.1%` の意味**：自動的に100倍されてパーセント記号がつきます。

---

## レッスン 4: 実践例 ― レシート・報告書

### 例 1: 店舗の売上レシート

```python
item = "ノート"
quantity = 3
unit_price = 150
discount_rate = 0.1

subtotal = quantity * unit_price
discount = subtotal * discount_rate
total = subtotal - discount

print("=" * 35)
print(f"{'商品':<12} {'数量':>4} {'単価':>6} {'金額':>8}")
print("-" * 35)
print(f"{item:<12} {quantity:>4}個 {unit_price:>6}円 {subtotal:>8}円")
print("-" * 35)
print(f"{'小計':>24} {subtotal:>8}円")
print(f"{'割引(10%)':>24} {discount:>8.0f}円")
print(f"{'合計':>24} {total:>8.0f}円")
print("=" * 35)
```

**出力：**

```
===================================
商品         数量  単価    金額
-----------------------------------
ノート         3個    150円      450円
-----------------------------------
                    小計      450円
                割引(10%)       45円
                    合計      405円
===================================
```

### 例 2: 成績報告書

```python
student_name = "田中 太郎"
japanese = 78
math = 92
science = 85
english = 88

average = (japanese + math + science + english) / 4

print("=" * 50)
print(f"{'学生氏名':<15}: {student_name}")
print("=" * 50)
print(f"{'国語':<15}: {japanese:>3}点")
print(f"{'数学':<15}: {math:>3}点")
print(f"{'理科':<15}: {science:>3}点")
print(f"{'英語':<15}: {english:>3}点")
print("-" * 50)
print(f"{'平均':<15}: {average:>6.1f}点")
print("=" * 50)
```

**出力：**

```
==================================================
学生氏名       : 田中 太郎
==================================================
国語           :  78点
数学           :  92点
理科           :  85点
英語           :  88点
--------------------------------------------------
平均           :  85.8点
==================================================
```

### 例 3: 商品カタログ

```python
products = [
    ("イヤホン", 5000, 4.5),
    ("ヘッドホン", 15000, 4.8),
    ("スピーカー", 8000, 4.2),
]

print(f"{'商品名':<15} {'価格':>8} {'評価':>6}")
print("-" * 35)

for name, price, rating in products:
    print(f"{name:<15} {price:>8,}円 {rating:>6.1f}★")
```

**出力：**

```
商品名              価格     評価
-----------------------------------
イヤホン            5,000円    4.5★
ヘッドホン         15,000円    4.8★
スピーカー          8,000円    4.2★
```

---

## ドリル 1-1: f-string の基本

次のプログラムの出力結果を答えましょう。

```python
name = "山田"
age = 16
height = 165.7

print(f"名前：{name}")
print(f"年齢：{age}歳")
print(f"身長：{height}cm")
```

<details>
<summary>答えを見る</summary>

```
名前：山田
年齢：16歳
身長：165.7cm
```

</details>

---

## ドリル 1-2: 式を使った f-string

次のプログラムの出力結果を答えましょう。

```python
x = 10
y = 20
z = 5

print(f"x + y = {x + y}")
print(f"x * z = {x * z}")
print(f"y / z = {y / z}")
```

<details>
<summary>答えを見る</summary>

```
x + y = 30
x * z = 50
y / z = 4.0
```

</details>

---

## ドリル 1-3: 右寄せ・左寄せ

次の出力になるコードを完成させてください。

```
りんご        150円
バナナ        120円
ぶどう        200円
```

ヒント：`print(f"{item:<8} {price:>4}円")` の形式を使いましょう。

<details>
<summary>答えを見る</summary>

```python
items = [("りんご", 150), ("バナナ", 120), ("ぶどう", 200)]

for item, price in items:
    print(f"{item:<8} {price:>4}円")
```

</details>

---

## ドリル 1-4: ゼロ埋めと小数点の桁数

次のプログラムの出力結果を答えましょう。

```python
month = 4
day = 7
price = 1500.5

print(f"日付：2026-{month:02d}-{day:02d}")
print(f"価格：{price:.1f}円")
print(f"学籍番号：{3:05d}")
```

<details>
<summary>答えを見る</summary>

```
日付：2026-04-07
価格：1500.5円
学籍番号：00003
```

</details>

---

## ドリル 1-5: バグを直せ！

以下のプログラムにはバグがあります。直してください。

```python
price = 1200
discount = 0.2
result = price * (1 - discount)

print(f"定価：{price}円")
print(f"割引後：{result}円")  # ❌ 小数が表示されて見にくい
```

<details>
<summary>答えを見る</summary>

小数点以下が無駄に表示されています。整数として表示するか、小数第1位で統一しましょう。

**修正方法1：小数第1位に統一**

```python
price = 1200
discount = 0.2
result = price * (1 - discount)

print(f"定価：{price}円")
print(f"割引後：{result:.0f}円")  # .0f で小数を表示しない
```

**修正方法2：int() で整数に変換**

```python
price = 1200
discount = 0.2
result = int(price * (1 - discount))

print(f"定価：{price}円")
print(f"割引後：{result}円")
```

</details>

---

## ドリル 1-6: 総合問題 ― 給料明細を作ろう

以下の条件で、給料明細を表示するプログラムを作ってください。

**条件：**
- 基本給：250,000円
- 残業手当：30,000円
- 所得税（10%）を自動計算
- 最終支給額を表示
- 右寄せ・桁区切りを使って見栄え良く

**完成イメージ：**

```
=============================
       給料明細書
=============================
基本給         250,000円
残業手当        30,000円
-----------------------------
総支給額        280,000円
所得税(10%)     28,000円
-----------------------------
最終支給額      252,000円
=============================
```

<details>
<summary>解答例を見る</summary>

```python
base_salary = 250000
overtime = 30000
gross = base_salary + overtime
tax = int(gross * 0.1)
net = gross - tax

print("=" * 29)
print(f"{'給料明細書':^29}")
print("=" * 29)
print(f"基本給{base_salary:>20,}円")
print(f"残業手当{overtime:>18,}円")
print("-" * 29)
print(f"総支給額{gross:>20,}円")
print(f"所得税(10%){tax:>16,}円")
print("-" * 29)
print(f"最終支給額{net:>18,}円")
print("=" * 29)
```

</details>

---

## 小テスト（全5問）

**Q1.** f-string を使って変数 `name` を埋め込む正しい書き方は？

- A. `print("名前：name")`
- B. `print(f"名前：{name}")`
- C. `print("名前：" + name)`

<details>
<summary>答えを見る</summary>

**B. `print(f"名前：{name}")`**

f-string は先頭に `f` をつけ、変数は `{}` で囲みます。

</details>

---

**Q2.** 次のコードの出力結果は？

```python
x = 5
y = 3
print(f"結果：{x * y}")
```

- A. `結果：5 * 3`
- B. `結果：53`
- C. `結果：15`

<details>
<summary>答えを見る</summary>

**C. `結果：15`**

f-string の `{}` の中は式として評価されるので、`5 * 3 = 15` が計算されます。

</details>

---

**Q3.** `{price:>8}` の意味は？

- A. 変数 `price` を右寄せ、最低8文字幅
- B. 変数 `price` に8を足す
- C. 変数 `price` を文字列に変換

<details>
<summary>答えを見る</summary>

**A. 変数 `price` を右寄せ、最低8文字幅**

`>` は右寄せ、`8` は最小幅を指定します。

</details>

---

**Q4.** `{value:.2f}` の意味は？

- A. 変数 `value` を小数第2位まで表示
- B. 変数 `value` を2倍にする
- C. 変数 `value` の最初の2文字を取る

<details>
<summary>答えを見る</summary>

**A. 変数 `value` を小数第2位まで表示**

`.2f` は「小数第2位までの浮動小数点数」を意味します。

</details>

---

**Q5.** 1,500,000 をカンマ区切りで表示するコードは？

- A. `print(f"{price:,}")`
- B. `print(f"{price:.0f}")`
- C. `print(f"{price:>10}")`

<details>
<summary>答えを見る</summary>

**A. `print(f"{price:,}")`**

`,` を使うことで、自動的に千の位にカンマが挿入されます。

</details>

---
