# Week 05: パソコンの最強特技 ― 「繰り返し」`while`

今週から、コンピュータが人間より圧倒的に優れている「文句を言わずに何万回でも同じ作業を繰り返す」技を学びます。
ゲームの「HPが0になるまでバトルが続く」「メイン画面がずっと表示され続ける」も、すべて繰り返し（ループ）の仕組みです。

---

## レッスン 1: 繰り返しの基本 ― `while` 文

「もし〜なら」は `if` でしたが、「〜の間はずっと繰り返す」は **`while`（ホワイル）** を使います。

### 書き方

```python
while 条件式:
    繰り返す処理  # インデント必須
```

### 基本例

```python
count = 1

while count <= 3:         # count が 3 以下の間、繰り返す
    print(f"{count}回目！")
    count = count + 1     # 毎回1ずつ増やす（これがないと無限ループ！）

print("終了")
```

> **重要**：`count = count + 1` は「今の count に1を足して、同じ箱に上書き保存」という意味。
> `count += 1` とも書けます（同じ意味）。

### ハンズオン 1-A: カウントダウン

```python
time = 5

while time > 0:
    print(f"発射まであと {time} 秒...")
    time -= 1   # time = time - 1 と同じ

print("発射！")
```

---

## レッスン 2: 無限ループと `break`

`while True:` と書くと意図的に永遠に繰り返します。`break` で抜け出せます。

```python
while True:                           # 永遠に繰り返す
    word = input("何か入力（'終了'で止まる）: ")

    if word == "終了":
        print("プログラムを終了します。")
        break                         # ループを抜ける

    print(f"入力: {word}")
```

> **Ctrl+C** で強制終了できます（無限ループに入ったときの緊急脱出）。

### ハンズオン 2-A: 無限ループ体験

以下を実行し、すぐに **Ctrl+C** で止めてみましょう。

```python
hp = 10

while hp > 0:
    print(f"HPは{hp}だ！")
    # hp を減らすのを忘れると永遠に続く！
```

---

## レッスン 3: `continue` ― 今回だけスキップ

`break` がループ全体を終了するのに対し、**`continue`** は「今回の繰り返しだけスキップして次へ」です。

```python
for i in range(5):
    if i == 2:
        continue      # i=2 のときだけスキップ
    print(i)

# 出力: 0  1  3  4  （2だけ飛ばされる）
```

---

## ドリル 5-1: while 文の穴埋め

1から5まで順番に表示するプログラムの空欄を埋めてください。

```python
n = ___

while n ___ 5:
    print(n)
    n ___

print("完了")
```

<details>
<summary>答えを見る</summary>

```python
n = 1

while n <= 5:
    print(n)
    n += 1

print("完了")
```

</details>

---

## ドリル 5-2: 実行結果の予測

次のコードを実行すると何が表示されますか？

```python
x = 10

while x > 0:
    print(x)
    x -= 3

print("終わり")
```

<details>
<summary>答えを見る</summary>

```
10
7
4
1
終わり
```

解説：10 → 7 → 4 → 1 → 次は -2 になり `x > 0` が False になるので終了。

</details>

---

## ドリル 5-3: 合い言葉で開く扉

「開けゴマ」と入力されるまで「合い言葉が違います！」と繰り返し、正解なら「扉が開いた！」と表示して終了するプログラムを作ってください。

```python
# while True + break を使って作ろう
```

<details>
<summary>解答例を見る</summary>

```python
while True:
    answer = input("合い言葉は？: ")
    if answer == "開けゴマ":
        print("扉が開いた！")
        break
    else:
        print("合い言葉が違います！")
```

</details>

---

## ドリル 5-4: 合計を求めるループ

ユーザーが「0」を入力するまで数字を入力させ続け、その合計を表示するプログラムを作ってください。

```
例：
3 → 7 → 2 → 0
合計：12
```

<details>
<summary>解答例を見る</summary>

```python
total = 0

while True:
    n = int(input("数字を入力（0で終了）: "))
    if n == 0:
        break
    total += n

print(f"合計：{total}")
```

</details>

---

## ドリル 5-5: バグを直せ！（応用）

以下のプログラムは「1から指定した数まで足し算する」つもりですが、正しく動きません。
バグを見つけて修正してください。

```python
limit = int(input("いくつまで足す？: "))
total = 0
i = 1

while i <= limit:
    total = i
    i += 1

print(f"合計：{total}")
```

<details>
<summary>答えを見る</summary>

```
バグ：total = i  →  total += i

「total = i」は「totalをiで上書き」してしまっている。
「total += i」（total = total + i）と書くことで、足し算になる。
```

修正後：

```python
limit = int(input("いくつまで足す？: "))
total = 0
i = 1

while i <= limit:
    total += i
    i += 1

print(f"合計：{total}")
```

</details>

---

## ドリル 5-6: 条件を自分で設計する（総合問題）

「100点になるまで点数を足し続けるゲーム」を作ってください。

### 仕様

- `score = 0` からスタート
- ループの中で「何点加える？（1〜20）」と入力させる
- 入力値が1〜20の範囲外なら「1〜20の間で入力してください」と表示してやり直し
- `score` が100以上になったらループを終了し、「ゴール！〇〇ターンかかりました！」と表示

<details>
<summary>解答例を見る</summary>

```python
score = 0
turns = 0

while score < 100:
    n = int(input("何点加える？（1〜20）: "))
    if n < 1 or n > 20:
        print("1〜20の間で入力してください")
        continue
    score += n
    turns += 1
    print(f"現在のスコア：{score}点")

print(f"ゴール！{turns}ターンかかりました！")
```

</details>

---

## ミニプロジェクト: 数当てゲーム（ヒント付き・リベンジ版）

正解の数字（1〜20）を当てるまで何度でも挑戦できるゲームを作りましょう。

### 要件

- 正解は変数 `secret = 13` で固定（後でランダムにしてもOK）
- 間違えるたびに「もっと大きい」か「もっと小さい」のヒントを表示
- 正解したら「正解！〇〇回かかりました！」と表示

### 完成イメージ

```
=== 数当てゲーム（1〜20）===
予想: 10
もっと大きい！
予想: 16
もっと小さい！
予想: 13
正解！3回かかりました！
```

<details>
<summary>解答例を見る</summary>

```python
secret = 13
tries = 0

print("=== 数当てゲーム（1〜20）===")

while True:
    guess = int(input("予想: "))
    tries += 1

    if guess == secret:
        print(f"正解！{tries}回かかりました！")
        break
    elif guess < secret:
        print("もっと大きい！")
    else:
        print("もっと小さい！")
```

**発展**：`import random` と `random.randint(1, 20)` を使って正解をランダムにしてみましょう。

</details>

---

## 発展チャレンジ: RPGの戦闘シーン

```python
slime_hp = 30
player_hp = 50

print("=== 戦闘開始！ ===")

while slime_hp > 0 and player_hp > 0:
    print(f"あなたHP:{player_hp} / スライムHP:{slime_hp}")
    action = input("行動？（1=攻撃 / 0=逃げる）: ")

    if action == "1":
        damage = 10
        slime_hp -= damage
        print(f"スライムに{damage}ダメージ！（残りHP:{max(0, slime_hp)}）")
    elif action == "0":
        print("逃げ出した！")
        break
    else:
        print("その行動は存在しない。")
        continue

    # スライムの反撃
    if slime_hp > 0:
        slime_dmg = 8
        player_hp -= slime_dmg
        print(f"スライムの反撃！{slime_dmg}ダメージ受けた。")

if slime_hp <= 0:
    print("スライムを倒した！")
elif player_hp <= 0:
    print("やられてしまった...")
```

---

## 小テスト（全5問）

**Q1.** 「〜の間ずっと繰り返す」に使うキーワードは？

- A. `loop`
- B. `repeat`
- C. `while`

<details>
<summary>答えを見る</summary>

**C. `while`**

</details>

---

**Q2.** `count += 1` は何と同じ意味ですか？

- A. `count = 1`
- B. `count = count + 1`
- C. `count + 1`

<details>
<summary>答えを見る</summary>

**B. `count = count + 1`**
`+=` は「自分自身に足して代入」する複合代入演算子です。

</details>

---

**Q3.** 次のコードは何回「こんにちは」と表示しますか？

```python
n = 0
while n < 4:
    print("こんにちは")
    n += 1
```

- A. 3回
- B. 4回
- C. 5回

<details>
<summary>答えを見る</summary>

**B. 4回**
`n = 0, 1, 2, 3` の4回 True になります（4になると `4 < 4` が False）。

</details>

---

**Q4.** ループを途中で強制終了するキーワードは？

- A. `stop`
- B. `exit`
- C. `break`

<details>
<summary>答えを見る</summary>

**C. `break`**

</details>

---

**Q5.** 以下のコードで無限ループが起きる原因は何ですか？

```python
hp = 10
while hp > 0:
    print(f"HPは{hp}")
```

- A. `print` の使い方が間違っている
- B. `hp` を変化させる処理がないので、条件が永遠に True のまま
- C. `while` の後にコロンがない

<details>
<summary>答えを見る</summary>

**B. `hp` を変化させる処理がないので、条件が永遠に True のまま**
`hp -= 1` など、条件に関わる変数を変化させる処理が必要です。

</details>
