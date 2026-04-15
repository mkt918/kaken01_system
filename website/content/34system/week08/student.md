# Week 08: 自分だけの命令を作る ― 関数（`def`）

これまで `print()`・`input()`・`len()` など、あらかじめ用意された命令を使ってきました。
今週は「**自分だけのオリジナル命令（関数）**」を作る方法を学びます。
同じ処理を何度も書かずに、名前をつけて使い回せるようになります。

---

## レッスン 1: 関数の定義と呼び出し ― `def`

### 書き方

```python
def 関数名():         # def で定義開始
    処理              # インデント必須（4スペース）

関数名()             # 呼び出し（これで初めて実行される）
```

### 基本例

```python
def say_hello():
    print("こんにちは！")
    print("今日も頑張りましょう！")

say_hello()    # 1回目の呼び出し
say_hello()    # 2回目の呼び出し
```

> **ポイント**：`def` は「定義するだけ」で、その場では実行されません。
> `say_hello()` と書いて初めて実行されます。

### ハンズオン 1-A: 挨拶関数を作ろう

```python
def greet():
    print("=" * 20)
    print("  ようこそ！")
    print("=" * 20)

greet()
greet()
greet()
```

---

## レッスン 2: 引数 ― 関数に「材料」を渡す

関数のカッコの中に変数名を書くと、呼び出し時にデータを渡せます。
これを **引数（ひきすう）** といいます。

```python
def greet(name):              # name が引数（受け取る箱）
    print(f"こんにちは、{name}さん！")

greet("田中")    # "田中" が name に入る
greet("鈴木")    # "鈴木" が name に入る
```

### 複数の引数

```python
def introduce(name, age):
    print(f"名前：{name}、年齢：{age}歳")

introduce("田中", 17)
introduce("鈴木", 16)
```

### デフォルト引数（省略可能な引数）

```python
def power(base, exp=2):       # exp のデフォルトは 2
    print(base ** exp)

power(3)        # 3² = 9（exp を省略）
power(2, 10)    # 2¹⁰ = 1024
```

---

## レッスン 3: 戻り値 ― 結果を「返す」`return`

`return` を使うと、関数の結果を呼び出し元に返せます。

```python
def add(a, b):
    return a + b          # 結果を返す

result = add(10, 5)       # 返ってきた値を変数に入れる
print(result)             # 15
print(add(100, 200))      # 直接 print もできる
```

### print と return の違い

```python
def show(x):
    print(x * 2)    # 画面に表示するだけ

def calc(x):
    return x * 2   # 値を返す（後で使える）

show(5)                  # 10（表示される）
a = show(5)              # aは None（returnがないと None が返る）

b = calc(5)              # bは 10（値として使える）
print(b + 3)             # 13（返ってきた値で計算できる）
```

### ハンズオン 3-A: BMI計算関数

```python
def calc_bmi(height_cm, weight):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

bmi = calc_bmi(170, 65)
print(f"BMI：{bmi:.1f}")
```

---

## ドリル 8-1: 関数の穴埋め

「2つの数字を受け取り、大きい方を返す」関数を完成させてください。

```python
def bigger(a, b):
    if a > b:
        ___
    ___:
        return b

print(bigger(10, 25))   # 25
print(bigger(7, 3))     # 7
```

<details>
<summary>答えを見る</summary>

```python
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(10, 25))   # 25
print(bigger(7, 3))     # 7
```

</details>

---

## ドリル 8-2: 実行結果の予測

次のコードを実行すると何が表示されますか？

```python
def double(n):
    return n * 2

def triple(n):
    return n * 3

x = 5
print(double(x))
print(triple(double(x)))
print(double(triple(x)) + 1)
```

<details>
<summary>答えを見る</summary>

```
10
30
31
```

解説：
- `double(5)` = 10
- `triple(double(5))` = `triple(10)` = 30
- `double(triple(5))` = `double(15)` = 30、+1 で 31

</details>

---

## ドリル 8-3: 関数を作れ！（段階的）

以下の3つの関数を順番に作ってください。

```
① greet_time(hour)
  hourが6以上12未満 → 「おはようございます」
  hourが12以上18未満 → 「こんにちは」
  それ以外 → 「こんばんは」

② is_even(n)
  n が偶数なら True を返す
  n が奇数なら False を返す

③ count_even(nums)
  リスト nums の中の偶数の個数を返す
```

<details>
<summary>解答例を見る</summary>

```python
# ①
def greet_time(hour):
    if 6 <= hour < 12:
        return "おはようございます"
    elif 12 <= hour < 18:
        return "こんにちは"
    else:
        return "こんばんは"

# ②
def is_even(n):
    return n % 2 == 0    # True/False を直接 return

# ③
def count_even(nums):
    count = 0
    for n in nums:
        if is_even(n):   # ②で作った関数を活用
            count += 1
    return count

# テスト
print(greet_time(9))          # おはようございます
print(is_even(4))             # True
print(count_even([1,2,3,4,5,6]))  # 3
```

</details>

---

## ドリル 8-4: バグを直せ！

以下のプログラムには3か所バグがあります。すべて見つけて直してください。

```python
def calc_tax(price, rate = 0.10):
    tax = price * rate
    total = price + tax
    print(total)          # ← バグ1

result = calc_tax(1000)
print(result + 100)       # ← バグ2

def repeat_print(text, times):
    for i in range(times):
        print(text)

repeat_print("Hello")     # ← バグ3
```

<details>
<summary>答えを見る</summary>

```
バグ1: print(total)  →  return total
  （値を返さないと呼び出し元で使えない）

バグ2: print(result + 100) は result が None のため TypeError
  →  バグ1を直せば result = 1100.0 になり、print(result + 100) = 1200.0

バグ3: repeat_print("Hello") → repeat_print("Hello", 3) など
  （times に引数が渡されていない。デフォルト値を設定するか引数を渡す）
```

修正後：

```python
def calc_tax(price, rate=0.10):
    tax = price * rate
    total = price + tax
    return total          # return に修正

result = calc_tax(1000)
print(result + 100)       # 1200.0

def repeat_print(text, times=3):   # デフォルト値を追加
    for i in range(times):
        print(text)

repeat_print("Hello")     # 3回表示
```

</details>

---

## ドリル 8-5: 関数の設計（中級）

「成績評価システム」の関数を作ってください。

```python
def get_grade(score):
    """
    点数を受け取り、評価文字（S/A/B/C/D）を返す関数
    S: 95点以上
    A: 80点以上
    B: 65点以上
    C: 50点以上
    D: 50点未満
    """
    pass  # ここを実装する

def print_report(name, score):
    """
    名前と点数を受け取り、評価レポートを表示する関数
    get_grade() を内部で呼び出すこと
    """
    pass  # ここを実装する

# テスト
print_report("田中", 97)
print_report("鈴木", 73)
print_report("佐藤", 44)
```

期待する出力：

```
田中さん：97点 → S評価
鈴木さん：73点 → B評価
佐藤さん：44点 → D評価
```

<details>
<summary>解答例を見る</summary>

```python
def get_grade(score):
    if score >= 95:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

def print_report(name, score):
    grade = get_grade(score)
    print(f"{name}さん：{score}点 → {grade}評価")

print_report("田中", 97)
print_report("鈴木", 73)
print_report("佐藤", 44)
```

</details>

---

## ドリル 8-6: 関数 + リスト + ループ（総合問題）

以下の関数を実装し、複数の名前と点数を処理するシステムを作ってください。

```python
def average(scores):
    """リストの平均を返す"""
    pass

def above_average(names, scores):
    """平均以上の点数の人の名前リストを返す"""
    pass

names = ["田中", "鈴木", "佐藤", "山田", "高橋"]
scores = [78, 92, 55, 83, 67]

avg = average(scores)
print(f"平均点：{avg:.1f}点")
print(f"平均以上：{above_average(names, scores)}")
```

<details>
<summary>解答例を見る</summary>

```python
def average(scores):
    return sum(scores) / len(scores)

def above_average(names, scores):
    avg = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] >= avg:
            result.append(names[i])
    return result

names = ["田中", "鈴木", "佐藤", "山田", "高橋"]
scores = [78, 92, 55, 83, 67]

avg = average(scores)
print(f"平均点：{avg:.1f}点")           # 75.0点
print(f"平均以上：{above_average(names, scores)}")  # ['鈴木', '山田']
```

</details>

---

## ミニプロジェクト: 多言語あいさつロボ

名前と言語番号を入力してもらい、言語に応じた挨拶をする関数を作りましょう。

### 要件

- `multi_greet(name, lang)` 関数を定義する
- `lang = "1"` → 日本語、`"2"` → 英語、`"3"` → 関西弁、それ以外 → エラーメッセージ
- メインのコードで `input()` を使って名前と言語を受け取り、関数を呼び出す

### 完成イメージ

```
名前を入力: 田中
言語（1=日本語 / 2=英語 / 3=関西弁）: 2
Hello, 田中！Nice to meet you!
```

<details>
<summary>解答例を見る</summary>

```python
def multi_greet(name, lang):
    if lang == "1":
        print(f"こんにちは、{name}さん！よろしくお願いします！")
    elif lang == "2":
        print(f"Hello, {name}! Nice to meet you!")
    elif lang == "3":
        print(f"なんや{name}やんか！よろしゅうな！")
    else:
        print("その言語番号は存在しません。")

name = input("名前を入力: ")
lang = input("言語（1=日本語 / 2=英語 / 3=関西弁）: ")
multi_greet(name, lang)
```

</details>

---

## 発展チャレンジ: Step1 総決算 ― コマンド選択式RPGバトル

W1〜W8で学んだすべての知識を使って、本格的なバトルゲームを作りましょう。

### 使う知識

- 変数・f-string → HPの管理・表示
- while True → 戦闘ループ
- if/elif/else → コマンド分岐
- リスト → アイテム管理
- 関数 → 攻撃・回復処理をまとめる
- import random → 敵のランダムダメージ

### 完成イメージ

```
=== ターン1 ===
勇者HP: 30 | ボスHP: 50
コマンド（1=攻撃 / 2=回復 / 3=アイテム）: 1
勇者の攻撃！ボスに10ダメージ！
ボスの反撃！勇者は8ダメージを受けた！
```

<details>
<summary>解答例を見る</summary>

```python
import random

def player_attack(boss_hp, damage=10):
    boss_hp -= damage
    print(f"勇者の攻撃！ボスに{damage}ダメージ！")
    return boss_hp

def player_heal(player_hp, heal=15):
    player_hp += heal
    print(f"回復魔法！HPが{heal}回復した！")
    return player_hp

def boss_attack(player_hp):
    damage = random.randint(5, 15)
    player_hp -= damage
    print(f"ボスの反撃！勇者は{damage}ダメージを受けた！")
    return player_hp

player_hp = 30
boss_hp = 50
items = ["やくそう", "やくそう", "どくけし"]
turn = 1

while player_hp > 0 and boss_hp > 0:
    print(f"\n=== ターン{turn} ===")
    print(f"勇者HP: {player_hp} | ボスHP: {boss_hp}")
    print(f"アイテム: {items}")
    cmd = input("コマンド（1=攻撃 / 2=回復 / 3=アイテム）: ")

    if cmd == "1":
        boss_hp = player_attack(boss_hp)
    elif cmd == "2":
        player_hp = player_heal(player_hp)
    elif cmd == "3":
        if len(items) > 0:
            used = items.pop(0)
            player_hp += 20
            print(f"{used}を使った！HPが20回復！")
        else:
            print("アイテムがない！")
    else:
        print("そのコマンドは存在しない。")
        continue

    if boss_hp > 0:
        player_hp = boss_attack(player_hp)

    turn += 1

if player_hp <= 0:
    print("\nゲームオーバー...")
else:
    print("\n世界を救った！おめでとう！")
```

</details>

---

## 小テスト（全5問）

**Q1.** 新しい関数を定義するキーワードは？

- A. `fun`
- B. `def`
- C. `make`

<details>
<summary>答えを見る</summary>

**B. `def`**

</details>

---

**Q2.** 関数を呼び出すときに渡すデータを何と呼ぶ？

- A. 引数（ひきすう）
- B. 変数（へんすう）
- C. 関数（かんすう）

<details>
<summary>答えを見る</summary>

**A. 引数（ひきすう）**

</details>

---

**Q3.** 次のコードで `result` の値は？

```python
def calc(a, b):
    return a * b + 1

result = calc(3, 4)
print(result)
```

- A. `12`
- B. `13`
- C. `None`

<details>
<summary>答えを見る</summary>

**B. `13`**
`3 * 4 = 12`、`12 + 1 = 13`

</details>

---

**Q4.** `return` のない関数を変数に代入すると、変数の値はどうなる？

- A. `0`
- B. `False`
- C. `None`

<details>
<summary>答えを見る</summary>

**C. `None`**
`return` がない関数は暗黙的に `None` を返します。

</details>

---

**Q5.** 以下のコードで何が表示されますか？

```python
def mystery(nums):
    result = 0
    for n in nums:
        if n % 2 == 0:
            result += n
    return result

print(mystery([1, 2, 3, 4, 5, 6]))
```

- A. `6`
- B. `12`
- C. `21`

<details>
<summary>答えを見る</summary>

**B. `12`**
偶数は 2, 4, 6。合計 = 2 + 4 + 6 = **12**

</details>
