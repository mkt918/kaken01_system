# Week 03: プログラムに「判断力」を与えよう ― 条件分岐 `if`

今週は、プログラムが「状況を判断して別の行動をする」ための命令、**if文（条件分岐）** を学びます。
ゲームで「HPが0になったらゲームオーバー」「鍵を持っていたら扉が開く」のも、すべてこの仕組みです。

---

## レッスン 1: True と False ― コンピュータの「判断結果」

Pythonでは、条件を判断した結果は **`True`（真・正しい）** か **`False`（偽・正しくない）** の2値になります。

### 比較演算子

| 演算子 | 意味 | 例 | 結果 |
|--------|------|-----|------|
| `==` | 等しい | `3 == 3` | `True` |
| `!=` | 等しくない | `3 != 5` | `True` |
| `>` | より大きい | `5 > 3` | `True` |
| `<` | より小さい | `5 < 3` | `False` |
| `>=` | 以上 | `5 >= 5` | `True` |
| `<=` | 以下 | `3 <= 2` | `False` |

```python
age = 20
print(age >= 18)    # True
print(age == 17)    # False
print(age != 20)    # False

score = 75
print(score > 60)   # True
print(score == 100) # False
```

### ハンズオン 1-A: 比較してみよう

```python
a = 10
b = 7

print(f"a > b  : {a > b}")
print(f"a < b  : {a < b}")
print(f"a == b : {a == b}")
print(f"a != b : {a != b}")
print(f"a >= 10: {a >= 10}")
```

---

## レッスン 2: 基本の `if` 文

条件が `True` のときだけ、特定の処理を実行するのが **`if`文** です。

### 書き方

```python
if 条件式:
    条件がTrueのときに実行する処理  # 必ず4スペースのインデント！
```

### 具体例

```python
score = int(input("点数を入力してください: "))

if score >= 60:
    print("合格です！おめでとうございます。")

print("採点終了")  # これはifの外なので必ず実行される
```

> **重要ルール（インデント）**
>
> `if` の下の処理は **半角スペース4つ**（Tabキー1回）でずらす必要があります。
> このずれを「インデント」といいます。インデントがないとエラーになります。

### インデントのエラー例

```python
if score >= 60:
print("合格")    # ← IndentationError！インデントが必要
```

---

## レッスン 3: 条件に当てはまらないとき ― `else`

条件が `False` のときに別の処理をするには **`else`** を使います。

```python
score = int(input("点数を入力: "))

if score >= 60:
    print("合格です！")
else:
    print("不合格です。次回頑張りましょう。")
```

### ハンズオン 3-A: 偶数・奇数の判定

```python
n = int(input("整数を入力してください: "))

if n % 2 == 0:
    print(f"{n} は偶数です")
else:
    print(f"{n} は奇数です")
```

> **ポイント**：`n % 2 == 0` は「nを2で割った余りが0」→ 偶数の条件です。

---

## レッスン 4: 3つ以上の分かれ道 ― `elif`

「AならX、BならY、それ以外ならZ」と3つ以上に分岐するときは **`elif`** を使います。

```python
score = int(input("点数を入力: "))

if score >= 90:
    print("評価：A（優秀）")
elif score >= 70:
    print("評価：B（良好）")
elif score >= 50:
    print("評価：C（合格）")
else:
    print("評価：D（不合格）")
```

> **重要**：`elif` は上から順番に判定され、**最初に True になった時点で残りはスキップ**されます。
> だから「大きい数から先に書く」のが鉄則です。

### 順番を間違えた失敗例

```python
# 間違い！score=95のとき「C（合格）」と表示されてしまう
if score >= 50:      # 95 >= 50 → True → ここで終了
    print("C（合格）")
elif score >= 70:
    print("B（良好）")
elif score >= 90:
    print("A（優秀）")
```

---

## レッスン 5: 文字列の条件分岐

条件は数値だけでなく、文字列にも使えます。

```python
color = input("好きな色は？（赤/青/黄）: ")

if color == "赤":
    print("情熱的ですね！")
elif color == "青":
    print("冷静な性格ですね！")
elif color == "黄":
    print("明るい性格ですね！")
else:
    print("その色も素敵ですね！")
```

---

## ドリル 3-1: True/False の予測

次の式の結果（True / False）を答えましょう。

```
① 10 > 5
② 3 == 3.0
③ "abc" == "ABC"
④ 7 != 7
⑤ 100 >= 100
⑥ 0 == False
```

<details>
<summary>答えを見る</summary>

```
① True  （10は5より大きい）
② True  （整数と小数は値が同じなら等しい）
③ False （文字列は大文字・小文字を区別する）
④ False （7は7と等しいので、「等しくない」はFalse）
⑤ True  （100は100以上）
⑥ True  （0とFalseはPythonで等しい）
```

</details>

---

## ドリル 3-2: if-else を完成させよう

空欄を埋めてプログラムを完成させてください。

```python
temperature = float(input("今の気温は？: "))

if ___:                    # 30度以上なら
    print("熱中症に注意！水分補給を忘れずに。")
elif ___:                  # 10度未満なら
    print("防寒対策をしっかりしましょう。")
___:                       # それ以外
    print("過ごしやすい気候ですね。")
```

<details>
<summary>答えを見る</summary>

```python
temperature = float(input("今の気温は？: "))

if temperature >= 30:
    print("熱中症に注意！水分補給を忘れずに。")
elif temperature < 10:
    print("防寒対策をしっかりしましょう。")
else:
    print("過ごしやすい気候ですね。")
```

</details>

---

## ドリル 3-3: バグを直せ！

以下のプログラムには3か所バグがあります。すべて見つけて直してください。

```python
point = int(input("ポイントを入力: "))

if point = 100:
    print("満点！パーフェクト！")
elif point > 50
    print("合格ラインを超えています。")
else:
    print("もう少し頑張りましょう。")
    print("また挑戦してね！")
  print("採点終了")   # ← インデント注意
```

<details>
<summary>答えを見る</summary>

```
バグ1: point = 100  → point == 100  （比較は == を使う）
バグ2: elif point > 50  → elif point > 50:  （末尾のコロンが抜けている）
バグ3: print("採点終了") のインデントが2スペース → 0スペース（elseの外に出す）
```

修正後：

```python
point = int(input("ポイントを入力: "))

if point == 100:
    print("満点！パーフェクト！")
elif point > 50:
    print("合格ラインを超えています。")
else:
    print("もう少し頑張りましょう。")
    print("また挑戦してね！")
print("採点終了")
```

</details>

---

## ドリル 3-4: 順番パズル

以下のコードで「85点」を入力したとき、どの `print` が実行されますか？

```python
score = 85

if score > 60:
    print("A")
elif score > 75:
    print("B")
elif score > 90:
    print("C")
else:
    print("D")
```

<details>
<summary>答えを見る</summary>

**「A」が表示される**

`score > 60` が最初の条件。85 > 60 は True なので、ここで判定終了。
`elif score > 75` は絶対に評価されない（上で既にTrueになったから）。

正しい評価がしたければ、大きい値から書く必要があります：

```python
if score > 90:
    print("C（優秀）")
elif score > 75:
    print("B（良好）")
elif score > 60:
    print("A（合格）")
else:
    print("D（不合格）")
```

</details>

---

## ドリル 3-5: FizzBuzz チャレンジ

1から15までの数字について、以下のルールで出力するプログラムを作ってください。
（`for` 文の代わりに、数字を1つずつ `if` で判定してください）

- 3の倍数のとき → `"Fizz"`
- 5の倍数のとき → `"Buzz"`
- 3と5両方の倍数（15の倍数）のとき → `"FizzBuzz"`
- それ以外 → その数字をそのまま表示

ヒント：`n % 3 == 0` で3の倍数か確認できます。また15の倍数の条件を一番上に書くことがポイントです。

```python
n = int(input("数字を入力（1〜15）: "))

# ここに if-elif-else を書く
```

<details>
<summary>答えを見る</summary>

```python
n = int(input("数字を入力（1〜15）: "))

if n % 15 == 0:       # 15の倍数を最初に！
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
```

**なぜ15の倍数を最初に書くのか？**
15は3の倍数でもあるため、`n % 3 == 0` を先に書くと15も「Fizz」と判定されてしまいます。
厳しい条件（より特殊な条件）を先に書くのが if-elif の鉄則です。

</details>

---

## ミニプロジェクト: 自動販売機シミュレーター

お金を入れて飲み物を選ぶ、自動販売機プログラムを作りましょう。

### 要件

- 飲み物の種類と価格：コーラ 150円、お茶 120円、水 100円
- 投入金額を入力してもらう
- 選んだ飲み物を入力してもらう
- 金額が足りていれば「購入完了」とお釣りを表示
- 金額が足りなければ「金額が足りません」と返金額を表示
- 存在しない飲み物は「その商品はありません」と表示

### 完成イメージ

```
=== 自動販売機 ===
コーラ：150円 / お茶：120円 / 水：100円
投入金額: 200
商品を選んでください: コーラ
コーラを購入しました！お釣りは 50 円です。
```

<details>
<summary>解答例を見る</summary>

```python
print("=== 自動販売機 ===")
print("コーラ：150円 / お茶：120円 / 水：100円")

money = int(input("投入金額: "))
item = input("商品を選んでください: ")

if item == "コーラ":
    price = 150
elif item == "お茶":
    price = 120
elif item == "水":
    price = 100
else:
    print("その商品はありません。")
    price = -1  # 商品なしフラグ

if price >= 0:
    if money >= price:
        change = money - price
        print(f"{item}を購入しました！お釣りは {change} 円です。")
    else:
        shortage = price - money
        print(f"金額が足りません。あと {shortage} 円必要です。{money}円を返金します。")
```

</details>

---

## 発展チャレンジ: 数当てゲーム（1回挑戦版）

```python
secret = 42  # 正解の数字

print("=== 数当てゲーム ===")
print("1〜100の整数を当ててください！")
guess = int(input("あなたの答え: "))

if guess == secret:
    print("正解！すごい！")
elif guess > secret:
    print(f"惜しい！正解は {secret} より小さいです。")
else:
    print(f"惜しい！正解は {secret} より大きいです。")
```

**チャレンジ**：正解の数字を `import random` と `random.randint(1, 100)` でランダムにしてみましょう。

```python
import random
secret = random.randint(1, 100)
```

---

## 小テスト（全5問）

**Q1.** `if` ブロックの中の処理はどのように書きますか？

- A. 行の先頭に `#` をつける
- B. 行の先頭を半角スペース4つでインデントする
- C. 処理を `{}` で囲む

<details>
<summary>答えを見る</summary>

**B. 行の先頭を半角スペース4つでインデントする**
Pythonではインデントでブロックを表します。`{}` はJavaScriptやC言語のスタイルです。

</details>

---

**Q2.** `10 % 3` の結果は？

- A. `3`
- B. `1`
- C. `0`

<details>
<summary>答えを見る</summary>

**B. `1`**
10 ÷ 3 = 3 余り 1。`%` は余りを返します。

</details>

---

**Q3.** 次のコードで `score = 55` のとき、表示されるのは？

```python
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
```

- A. `A`
- B. `B`
- C. `C`

<details>
<summary>答えを見る</summary>

**C. `C`**
55は90未満、60未満なので `else` に到達します。

</details>

---

**Q4.** `else` の書き方として正しいものは？

- A. `else(score < 60):`
- B. `else:`
- C. `else score < 60:`

<details>
<summary>答えを見る</summary>

**B. `else:`**
`else` には条件式を書きません。「それ以外すべて」を受け取る受け皿です。

</details>

---

**Q5.** 以下のコードで `n = 9` のとき、出力は？

```python
if n % 2 == 0:
    print("偶数")
elif n % 3 == 0:
    print("3の倍数")
else:
    print("その他")
```

- A. `偶数`
- B. `3の倍数`
- C. `その他`

<details>
<summary>答えを見る</summary>

**B. `3の倍数`**
`9 % 2 = 1`（偶数ではない）→ `9 % 3 = 0`（3の倍数！）→ 「3の倍数」を表示。

</details>
