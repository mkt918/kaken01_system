# Week 04: 複雑な判断をこなす ― 複数条件と `elif` の完全マスター

先週は「もし〜なら（`if`）」を学びました。現実世界の判断は「Aならこう、Bならこう、それ以外ならこう」と複雑です。
今週は、3つ以上の分かれ道と「かつ（`and`）」「または（`or`）」という複数条件を組み合わせる高度な技を身につけます。

---

## レッスン 1: `else` と `elif` ― 複数の分かれ道

`if` に続けて `elif`（else if の略）を使うと、条件を何段階にも増やせます。

### 映画館の料金システム

```python
age = int(input("年齢を入力してください: "))

if age < 6:
    print("未就学児：無料")
elif age < 12:
    print("こども料金：1,000円")
elif age < 18:
    print("中高生料金：1,500円")
elif age >= 65:
    print("シニア料金：1,200円")
else:
    print("一般料金：1,800円")
```

> **ルール**
> 1. 最初は必ず `if` から始める
> 2. 中間の条件は `elif` をいくつでも追加できる
> 3. 最後の「それ以外すべて」は `else:` で終わる（条件式は書かない）
> 4. 上から順番に判定され、最初に True になった時点で終了

### ハンズオン 1-A: テストの成績表

点数（score）を入力させ、以下の基準で評価を表示してみましょう。

```python
score = int(input("テストの点数は？: "))

if score >= 90:
    print("S評価：すばらしい！")
elif score >= 70:
    print("A評価：よくできました！")
elif score >= 50:
    print("B評価：合格ライン！")
else:
    print("C評価：次はもっとがんばろう！")
```

---

## レッスン 2: `and` と `or` ― 複数条件の「接着剤」

「身長が120cm以上」**かつ**「年齢が10歳以上」のように、複数の条件を組み合わせる方法です。

| 演算子 | 意味 | True になる条件 |
|--------|------|----------------|
| `and` | かつ（両方） | 両方の条件がTrueのとき |
| `or` | または（どちらか） | どちらか一方でもTrueのとき |
| `not` | ではない（否定） | 条件がFalseのとき |

### 真理値表

```
# and（両方Trueのみ True）
True  and True  → True
True  and False → False
False and True  → False
False and False → False

# or（どちらかがTrue なら True）
True  or True  → True
True  or False → True
False or True  → True
False or False → False
```

### ハンズオン 2-A: and でローラーコースター

```python
height = int(input("身長(cm)を入力: "))
age = int(input("年齢を入力: "))

if height >= 130 and age >= 10:
    print("絶叫ローラーコースターに乗れます！")
else:
    print("ごめんなさい、安全のため乗れません。")
```

### ハンズオン 2-B: or で割引判定

```python
print("※カードあり=1、なし=0")
has_card = int(input("会員カードは？: "))
age = int(input("年齢は？: "))

if has_card == 1 or age >= 60:
    print("10%割引になります！")
else:
    print("通常料金です。")
```

> **よくあるミス**：`or` の右側も省略できません
>
> ```python
> # 間違い：パソコンは「何と比べるか」を毎回書く必要がある
> if has_card == 1 or 60:    # ← 60は常にTrueとして扱われる！
>
> # 正しい
> if has_card == 1 or age >= 60:
> ```

### ハンズオン 2-C: not で否定

```python
is_raining = True

if not is_raining:
    print("お出かけ日和ですね！")
else:
    print("傘を持っていきましょう。")
```

---

## レッスン 3: 条件の順番が命 ― 「論理崩壊バグ」

`if-elif` は**上から順番**に判定され、一度 True になったら下の条件は無視されます。
これを理解していないと、正しく動かないバグが生まれます。

### バグの体験

```python
score = int(input("点数は？: "))

# 間違い！100点を入れると「もう少し」と表示される
if score > 0:           # 100 > 0 → True → ここで終了！
    print("もう少しがんばりましょう。")
elif score > 50:
    print("よくできました！")
elif score > 80:
    print("たいへんよくできました！")
```

### 正しい順番（厳しい条件＝大きい数から書く）

```python
score = int(input("点数は？: "))

if score > 80:          # 一番厳しい条件を先に
    print("たいへんよくできました！")
elif score > 50:
    print("よくできました！")
elif score > 0:
    print("もう少しがんばりましょう。")
else:
    print("0点ですね。")
```

---

## レッスン 4: 条件の組み合わせパターン

### パターン1: and + elif（段階的かつ複合）

```python
# 成人男性のみ特定サービスを利用可
gender = input("性別(男/女): ")
age = int(input("年齢: "))

if gender == "男" and age >= 20:
    print("サービスAが利用可能です")
elif gender == "女" and age >= 18:
    print("サービスBが利用可能です")
else:
    print("利用条件を満たしていません")
```

### パターン2: 条件を変数に入れる（可読性UP）

```python
height = int(input("身長(cm): "))
age = int(input("年齢: "))

tall_enough = height >= 130
old_enough = age >= 10
vip = True  # VIP会員かどうか

if (tall_enough and old_enough) or vip:
    print("優先乗車をご利用いただけます")
else:
    print("通常の乗車をご利用ください")
```

---

## ドリル 4-1: True / False の予測

次の式の結果（True / False）を答えましょう。

```
x = 15
y = 8

① x > 10 and y > 10
② x > 10 or y > 10
③ not (x > 10)
④ x > 10 and y < 10
⑤ x == 15 or y == 15
⑥ not (x == 15 and y == 8)
```

<details>
<summary>答えを見る</summary>

```
① False （15>10はTrue、8>10はFalse → True and False → False）
② True  （15>10はTrue → True or ... → True）
③ False （15>10はTrue → not True → False）
④ True  （15>10はTrue、8<10はTrue → True and True → True）
⑤ True  （15==15はTrue → True or ... → True）
⑥ False （15==15かつ8==8はTrue → not True → False）
```

</details>

---

## ドリル 4-2: elif の完成

空欄を埋めてプログラムを完成させてください。

```python
# 電気料金の段階制料金
usage = int(input("今月の電力使用量(kWh): "))

if ___:          # 120kWh以下
    rate = 19.88
elif ___:        # 120kWhを超え300kWh以下
    rate = 26.48
___:             # 300kWhを超える場合
    rate = 30.57

charge = usage * rate
print(f"使用量：{usage}kWh")
print(f"電気料金：{charge:.0f}円")
```

<details>
<summary>答えを見る</summary>

```python
usage = int(input("今月の電力使用量(kWh): "))

if usage <= 120:
    rate = 19.88
elif usage <= 300:
    rate = 26.48
else:
    rate = 30.57

charge = usage * rate
print(f"使用量：{usage}kWh")
print(f"電気料金：{charge:.0f}円")
```

</details>

---

## ドリル 4-3: and / or の選択

以下の文章を `and` か `or` を使った条件式に書き換えましょう。

```
① 気温が35度以上 かつ 湿度が80%以上 → 熱中症警戒アラート
② 在庫が0 または 販売終了フラグがTrue → 売り切れ表示
③ ログイン済み かつ 管理者権限あり → 管理画面を表示
④ テスト1が60点以上 または テスト2が60点以上 → 仮進級
```

変数は：`temp`, `humidity`, `stock`, `end_flag`, `is_login`, `is_admin`, `test1`, `test2`

<details>
<summary>答えを見る</summary>

```python
# ①
if temp >= 35 and humidity >= 80:
    print("熱中症警戒アラート")

# ②
if stock == 0 or end_flag == True:
    print("売り切れ")

# ③
if is_login and is_admin:
    print("管理画面を表示")

# ④
if test1 >= 60 or test2 >= 60:
    print("仮進級")
```

</details>

---

## ドリル 4-4: 順番パズル ― バグを直せ！

以下のコードは「100点を入力すると間違った評価が出る」バグがあります。
**条件の順番を正しく並べ替えて**修正してください。

```python
score = int(input("点数は？: "))

if score >= 60:
    print("C：合格")
elif score >= 80:
    print("B：良好")
elif score >= 90:
    print("A：優秀")
elif score == 100:
    print("S：満点！")
else:
    print("D：不合格")
```

<details>
<summary>答えを見る</summary>

厳しい条件（数字が大きいもの）から順に書きます：

```python
score = int(input("点数は？: "))

if score == 100:
    print("S：満点！")
elif score >= 90:
    print("A：優秀")
elif score >= 80:
    print("B：良好")
elif score >= 60:
    print("C：合格")
else:
    print("D：不合格")
```

</details>

---

## ドリル 4-5: プログラムを読んで答えよう

以下のコードで `age=15`, `height=125` を入力したとき、表示される文字は？

```python
age = int(input("年齢: "))
height = int(input("身長: "))

if age >= 18 or height >= 160:
    print("A")
elif age >= 12 and height >= 120:
    print("B")
elif age >= 6 or height >= 100:
    print("C")
else:
    print("D")
```

<details>
<summary>答えを見る</summary>

**「B」が表示される**

- `age >= 18 or height >= 160`：15>=18はFalse、125>=160はFalse → `False or False` → **False**
- `age >= 12 and height >= 120`：15>=12はTrue、125>=120はTrue → `True and True` → **True** → ここで決定！

</details>

---

## ドリル 4-6: FizzBuzz 拡張版

1〜20の範囲で数字を入力し、以下のルールで出力するプログラムを作ってください。

- 15の倍数 → `"FizzBuzz"`
- 3の倍数 → `"Fizz"`
- 5の倍数 → `"Buzz"`
- 7の倍数 → `"Lucky"`
- それ以外 → その数字をそのまま表示

（ヒント：複数の条件に当てはまる場合、一番上に書いた条件が優先されます）

<details>
<summary>解答例を見る</summary>

```python
n = int(input("数字を入力（1〜20）: "))

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
elif n % 7 == 0:
    print("Lucky")
else:
    print(n)
```

注意：21は3の倍数でも7の倍数でもあります。どちらを優先するかは仕様次第です。

</details>

---

## ミニプロジェクト: 遊園地のアトラクション案内所

年齢と身長を入力させ、乗れるアトラクションを案内するプログラムを作ります。

### アトラクション条件

| アトラクション | 条件 |
|--------------|------|
| 絶叫ドラゴンコースター | 身長130cm以上 かつ 年齢12歳以上 |
| ゆったり急流すべり | 身長100cm以上 |
| メリーゴーランド | 制限なし（上記以外） |

### 完成イメージ

```
=== 案内ロボット ===
年齢を入力: 13
身長(cm)を入力: 140
→ 絶叫ドラゴンコースターがおすすめです！
```

<details>
<summary>解答例を見る</summary>

```python
print("=== 案内ロボット ===")
age = int(input("年齢を入力: "))
height = int(input("身長(cm)を入力: "))

if height >= 130 and age >= 12:
    print("→ 絶叫ドラゴンコースターがおすすめです！")
elif height >= 100:
    print("→ ゆったり急流すべりがおすすめです！")
else:
    print("→ 保護者と一緒にメリーゴーランドへどうぞ！")
```

</details>

---

## 発展チャレンジ: RPGのダンジョン「2つの扉」

目の前に「金の扉」と「銀の扉」があります。それぞれ開く条件が違います。

### 条件

- **金の扉**：レベル10以上 かつ 魔法の鍵（1）を持っている
- **銀の扉**：レベル5以上

### 完成イメージ

```
=== ⚔️ ダンジョン地下1階 ⚔️ ===
勇者のレベルは？: 12
魔法の鍵を持ってる？(1=yes/0=no): 1
どの扉を開ける？(金/銀): 金
ガチャッ！金の扉が開いた！宝箱から10,000ゴールドを手に入れた！
```

<details>
<summary>解答例を見る</summary>

```python
print("=== ⚔️ ダンジョン地下1階 ⚔️ ===")
level = int(input("勇者のレベルは？: "))
has_key = int(input("魔法の鍵を持ってる？(1=yes/0=no): "))
door = input("どの扉を開ける？(金/銀): ")

if door == "金":
    if level >= 10 and has_key == 1:
        print("ガチャッ！金の扉が開いた！宝箱から10,000ゴールドを手に入れた！")
    else:
        print("ガチン！金の扉は開かない。レベルか鍵が足りないようだ...")
elif door == "銀":
    if level >= 5:
        print("キィ...銀の扉が開いた！500ゴールドを発見！")
    else:
        print("銀の扉も開かない。まだ力が足りないようだ。")
else:
    print("その扉は存在しない。")
```

**チャレンジ**：罠の扉（ランダム）や「両方の鍵を持っていれば隠し部屋に入れる」などを追加してみましょう。

</details>

---

## 小テスト（全5問）

**Q1.** `if` の次に書く、「追加の条件」を表すキーワードは？

- A. `else if`
- B. `and if`
- C. `elif`

<details>
<summary>答えを見る</summary>

**C. `elif`**
Pythonでは `else if` を1つの単語 `elif` と書きます。

</details>

---

**Q2.** すべての条件に当てはまらなかった「最後の受け皿」に使うキーワードは？

- A. `other:`
- B. `else:`
- C. `final:`

<details>
<summary>答えを見る</summary>

**B. `else:`**
`else` には条件式を書かず、コロン（`:`）のみです。

</details>

---

**Q3.** `True and False` の結果は？

- A. `True`
- B. `False`
- C. エラー

<details>
<summary>答えを見る</summary>

**B. `False`**
`and` は両方が True のときのみ True。片方でも False なら False になります。

</details>

---

**Q4.** Pythonの `if-elif-else` は、どのような順番で判定されますか？

- A. 上から順番に判定し、1つでも当てはまったらそこで終わる
- B. 下から順番に判定する
- C. すべての条件を同時に判定する

<details>
<summary>答えを見る</summary>

**A. 上から順番に判定し、1つでも当てはまったらそこで終わる**
これが「厳しい条件（大きい数）を先に書く」理由です。

</details>

---

**Q5.** 変数 `age` が「10より大きい」または「5より小さい」ことを調べる正しい書き方は？

- A. `age > 10 and age < 5`
- B. `age > 10 or age < 5`
- C. `age > 10 else age < 5`

<details>
<summary>答えを見る</summary>

**B. `age > 10 or age < 5`**
「または（どちらか）」は `or` を使います。`and` だと「10より大きく かつ 5より小さい」という矛盾した条件になります。

</details>
