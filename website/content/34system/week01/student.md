# Week 01: プログラミングの第一歩 ― 「変数」でデータを覚えさせよう

コンピュータは、ただ計算するだけでなく「情報を覚える」ことができます。
今週は、プログラムに情報を記憶させる仕組み「**変数**」と、画面に文字を表示する「**print()**」を徹底マスターします。

---

## レッスン 1: 画面への出力 ― `print()` を使いこなそう

プログラムの基本中の基本、「画面に文字や数字を表示する」方法を学びます。

### 基本の print()

```python
print("こんにちは！")
print("プログラミングの世界へようこそ。")
```

実行すると：

```
こんにちは！
プログラミングの世界へようこそ。
```

### 文字と数字を一緒に表示する

```python
print("私の年齢は", 17, "歳です。")
print("3 + 5 =", 3 + 5)
```

> **ポイント**：`print()` の中で `,`（カンマ）で区切ると、スペースを挟んで連続表示できます。

### ハンズオン 1-A: 自己紹介プログラム

以下をそのまま打って実行してみましょう。

```python
print("=== 自己紹介 ===")
print("名前：山田 太郎")
print("クラス：2年A組")
print("好きな教科：数学")
print("================")
```

---

## レッスン 2: 変数 ― コンピュータの「メモ帳」

**変数**とは、データを入れておく「名前付きの箱」です。一度入れたデータは何度でも使えます。

```python
name = "山田 太郎"      # 文字（文字列）を入れる箱
age = 17                 # 数字（整数）を入れる箱
height = 165.5           # 数字（小数）を入れる箱

print(name)              # 山田 太郎
print(age)               # 17
print(height)            # 165.5
```

### 変数名のルール

| OK の例 | NG の例 | 理由 |
|---------|---------|------|
| `score` | `1score` | 数字から始められない |
| `player_name` | `player name` | スペースは使えない |
| `total` | `if` | Pythonの予約語は使えない |
| `my_score2` | `my-score` | `-`（ハイフン）は使えない |

### 変数の値を更新する

```python
score = 50
print("最初のスコア:", score)

score = 80          # 値を上書き
print("更新後のスコア:", score)

score = score + 10  # 自分自身に10を足す
print("さらに更新:", score)
```

### ハンズオン 2-A: 変数で計算

```python
price = 1200       # 商品の値段
quantity = 3       # 個数
total = price * quantity

print("商品の値段:", price, "円")
print("個数:", quantity, "個")
print("合計金額:", total, "円")
```

---

## レッスン 3: データの種類（型）

Pythonのデータには「種類（型）」があります。種類が違うと演算の結果も変わります。

| 型 | 英語名 | 例 | 説明 |
|----|--------|-----|------|
| 整数 | int | `10`, `-3`, `0` | 小数点なしの数 |
| 小数 | float | `3.14`, `-0.5` | 小数点ありの数 |
| 文字列 | str | `"hello"`, `"ABC"` | `""`または`''`で囲む |
| 真偽値 | bool | `True`, `False` | 条件の正誤 |

### 型を確認する `type()`

```python
x = 42
y = 3.14
z = "こんにちは"

print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'str'>
```

### 文字列の「足し算」と「掛け算」

```python
a = "Hello"
b = " World"
print(a + b)        # Hello World （文字をつなぐ）
print(a * 3)        # HelloHelloHello （繰り返す）
```

> **注意**：数字の文字列と整数は足せません！
>
> ```python
> print("5" + 3)       # エラー！（TypeError）
> print(int("5") + 3)  # OK：int()で整数に変換してから足す
> ```

---

## レッスン 4: f-string ― スマートな文字の作り方

変数を文章の中に埋め込む最もスマートな方法が **f-string** です。

### 基本の書き方

```python
name = "田中"
age = 16
score = 87.5

print(f"名前：{name}")
print(f"年齢：{age}歳")
print(f"点数：{score}点")
```

### 式も書ける

```python
price = 1500
tax_rate = 0.10

print(f"税込価格：{price * (1 + tax_rate)}円")
print(f"消費税額：{price * tax_rate}円")
```

### 小数の桁数を指定する

```python
pi = 3.141592653589793
print(f"円周率は約 {pi:.2f} です")    # 小数第2位まで
print(f"円周率は約 {pi:.4f} です")    # 小数第4位まで
```

### ハンズオン 4-A: f-stringで名刺を作ろう

```python
name = "佐藤 花子"
school = "〇〇高校"
grade = 2
club = "プログラミング部"

print("=" * 30)
print(f"  氏 名：{name}")
print(f"  学 校：{school}")
print(f"  学 年：{grade}年生")
print(f"  部 活：{club}")
print("=" * 30)
```

---

## ドリル 1-1: 変数の基本

次のプログラムの空欄を埋めてください。

```python
# 変数に値を代入する
fruit = ___          # りんご という文字列を入れる
count = ___          # 5 という整数を入れる
price = ___          # 198.0 という小数を入れる

print(f"{count}個の{fruit}、合計{count * price}円")
```

<details>
<summary>答えを見る</summary>

```python
fruit = "りんご"
count = 5
price = 198.0

print(f"{count}個の{fruit}、合計{count * price}円")
# → 5個のりんご、合計990.0円
```

</details>

---

## ドリル 1-2: 型の選択

以下のデータに適切な型（int / float / str / bool）を答えましょう。

```
① 生徒の出席番号（1, 2, 3...）          → ___
② 商品の重さ（0.5kg, 1.2kg...）         → ___
③ ユーザーの名前（"田中", "鈴木"...）    → ___
④ ログインに成功したか（成功/失敗）       → ___
⑤ 摂氏温度（-5.0, 36.5, 100.0...）      → ___
```

<details>
<summary>答えを見る</summary>

```
① int   （番号は整数）
② float （重さは小数が必要）
③ str   （名前は文字列）
④ bool  （True/False で表現）
⑤ float （温度は小数が必要）
```

</details>

---

## ドリル 1-3: f-string を完成させよう

次のコードを実行すると何が表示されますか？

```python
item = "ノート"
price = 150
count = 4
discount = 0.1

total = price * count
after_discount = total * (1 - discount)

print(f"{item}を{count}冊買いました。")
print(f"定価合計：{total}円")
print(f"10%割引後：{after_discount}円")
```

<details>
<summary>答えを見る</summary>

```
ノートを4冊買いました。
定価合計：600円
10%割引後：540.0円
```

</details>

---

## ドリル 1-4: バグを直せ！

以下のプログラムには3か所バグがあります。すべて見つけて直してください。

```python
name = 山田太郎
age = "17"
height = 170

print(f"名前：{name}")
print(f"来年は{age + 1}歳になります。")
print(f"身長：{Height}cm")
```

<details>
<summary>答えを見る</summary>

```
バグ1: name = 山田太郎  → name = "山田太郎"  （文字列はクォートが必要）
バグ2: age + 1          → int(age) + 1       （文字列は整数に変換してから足す）
バグ3: {Height}         → {height}           （変数名は大文字・小文字を区別する）
```

修正後：

```python
name = "山田太郎"
age = "17"
height = 170

print(f"名前：{name}")
print(f"来年は{int(age) + 1}歳になります。")
print(f"身長：{height}cm")
```

</details>

---

## ドリル 1-5: プログラムを読んで答えよう

以下のプログラムを実行したとき、最終的に `total` の値はいくつになりますか？

```python
a = 10
b = 3
total = a + b
total = total * 2
a = 5
total = total + a
print(total)
```

<details>
<summary>答えを見る</summary>

```
ステップ1: total = 10 + 3 = 13
ステップ2: total = 13 * 2 = 26
ステップ3: a = 5（aを上書き）
ステップ4: total = 26 + 5 = 31

答え：31
```

</details>

---

## ドリル 1-6: 演算子の優先順位

以下の式を計算した結果を答えましょう（Pythonのルールに従う）。

```python
# 次の結果を求めよ
a = 2 + 3 * 4
b = (2 + 3) * 4
c = 10 / 4
d = 10 // 4
e = 10 % 3
```

<details>
<summary>答えを見る</summary>

```
a = 2 + 3 * 4 = 2 + 12 = 14  （×が先）
b = (2 + 3) * 4 = 5 * 4 = 20  （()が先）
c = 10 / 4 = 2.5              （/は小数の割り算）
d = 10 // 4 = 2               （//は整数の割り算・切り捨て）
e = 10 % 3 = 1                （%は割った余り：10 = 3×3 + 1）
```

</details>

---

## ミニプロジェクト: お買い物レシートを作ろう

変数と f-string を駆使して、本物らしいレシートを出力するプログラムを作りましょう。

### 要件

- 商品3点を変数で定義する
- 各商品の値段と数量を変数で管理する
- 小計・消費税（10%）・合計を計算して表示する
- `"=" * 30` などで見た目を整える

### 完成イメージ

```
==============================
    スーパーマーケット ABC
==============================
りんご         3個  × 150円
牛乳           2本  × 200円
パン           1個  × 120円
------------------------------
小計                   970円
消費税(10%)             97円
------------------------------
合計                  1067円
==============================
ありがとうございました！
```

<details>
<summary>解答例を見る</summary>

```python
# 商品の定義
item1_name = "りんご"
item1_count = 3
item1_price = 150

item2_name = "牛乳"
item2_count = 2
item2_price = 200

item3_name = "パン"
item3_count = 1
item3_price = 120

# 計算
subtotal = (item1_price * item1_count +
            item2_price * item2_count +
            item3_price * item3_count)
tax = int(subtotal * 0.10)
total = subtotal + tax
# （計算検証：150×3 + 200×2 + 120×1 = 450 + 400 + 120 = 970）

# 表示
print("=" * 30)
print("    スーパーマーケット ABC")
print("=" * 30)
print(f"{item1_name:<8}{item1_count}個  × {item1_price}円")
print(f"{item2_name:<8}{item2_count}本  × {item2_price}円")
print(f"{item3_name:<8}{item3_count}個  × {item3_price}円")
print("-" * 30)
print(f"小計{subtotal:>24}円")
print(f"消費税(10%){tax:>18}円")
print("-" * 30)
print(f"合計{total:>24}円")
print("=" * 30)
print("ありがとうございました！")
```

</details>

---

## 発展チャレンジ: RPGステータス画面

ゲームのキャラクターのステータス画面を作ってみましょう。

### 要件

- キャラクター名・職業・レベル・HP・MP・攻撃力・防御力を変数で定義
- HP・MPは「現在値 / 最大値」の形式で表示（例：`80/100`）
- 攻撃力と防御力の合計「戦闘力」を計算して表示

### 完成イメージ

```
╔══════════════════════════╗
║  ⚔ キャラクターシート ⚔  ║
╠══════════════════════════╣
║ 名前   : 勇者アルス       ║
║ 職業   : 戦士             ║
║ レベル : 15               ║
║ HP     : 80 / 100        ║
║ MP     : 40 / 60         ║
║ 攻撃力 : 85               ║
║ 防御力 : 70               ║
╠══════════════════════════╣
║ 戦闘力 : 155              ║
╚══════════════════════════╝
```

---

## 小テスト（全5問）

**Q1.** Pythonで変数 `score` に整数 `85` を代入する正しい書き方は？

- A. `score == 85`
- B. `score = 85`
- C. `int score = 85`

<details>
<summary>答えを見る</summary>

**B. `score = 85`**
`==` は「等しいか確認する」演算子。代入は `=` を使います。

</details>

---

**Q2.** 以下のコードの出力結果は？

```python
x = "10"
y = 5
print(x * y)
```

- A. `50`
- B. `1010101010`
- C. エラーになる

<details>
<summary>答えを見る</summary>

**B. `1010101010`**
文字列 `"10"` に整数 `5` を掛けると、文字列が5回繰り返されます。

</details>

---

**Q3.** f-string の正しい書き方はどれ？

- A. `f"名前：name"`
- B. `f"名前：{name}"`
- C. `"名前：{name}"`

<details>
<summary>答えを見る</summary>

**B. `f"名前：{name}"`**
f-string は先頭に `f` をつけ、変数は `{}` で囲みます。

</details>

---

**Q4.** 変数名として使えないものはどれ？

- A. `total_score`
- B. `2nd_player`
- C. `myScore`

<details>
<summary>答えを見る</summary>

**B. `2nd_player`**
変数名は数字から始められません。`player2` や `second_player` に変える必要があります。

</details>

---

**Q5.** 以下のコードを実行すると `result` の値は？

```python
a = 4
b = 3
result = a ** b
print(result)
```

- A. `7`
- B. `12`
- C. `64`

<details>
<summary>答えを見る</summary>

**C. `64`**
`**` はべき乗演算子です。`4 ** 3 = 4 × 4 × 4 = 64`

</details>
