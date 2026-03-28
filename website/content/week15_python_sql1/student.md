# Week 15: ついに合体！Pythonからデータベースを操る

これまでの2.5ヶ月間、皆さんは「1. Python（頭脳・計算）」と「2. SQL（記憶・倉庫）」を別々に学んできました。
今週からはいよいよ、この2つを合体させます！
Pythonのプログラムの力を使って、データベースに自動で大量のデータを書き込んだり、情報を引っ張り出したりする**「システム連携」**の第一歩です。

---

## 🕒 レッスン 1: 魔法の倉庫（DB）に接続する `sqlite3`

Pythonからデータベースを操るには、`sqlite3`（エスキューエルアイト・スリー）という連携ライブラリ（連絡用の電話）を使います。

### 💻 ハンズオン（やってみよう）
Pythonのコード（`app.py` など）に以下のコードをコピペして実行してみましょう。

```python
import sqlite3

# 1. データベースのファイルに接続する（無ければ新しく作られます！）
# "school.db" という名前の魔法の倉庫に電話をかけます
connection = sqlite3.connect("school.db")

# 2. データベースを操作するための「カーソル（マウスの矢印のようなもの）」を用意します
cursor = connection.cursor()

print("無事にデータベースに接続しました！")

# 3. 終わったら必ず電話を切る（閉じる）！
connection.close()
```

これを実行すると、プログラムが置いてあるフォルダに `school.db` という新しいファイルが自動的に生まれましたね？
これが本物のデータベースファイルです！

### ✍️ ドリル 1-1：RPGのセーブデータ庫
「`rpg_save.db`」という名前のデータベースファイルを作り、接続して「セーブデータ庫（DB）を作成しました！」とPrintしてから閉じるPythonプログラムを書いてください。

---

## 🕒 レッスン 2: Pythonからテーブル（箱）を作る

電話（connect）を繋いだら、いよいよSQLの呪文をPythonから唱えます！
呪文を唱える命令は `cursor.execute()`（エグゼキュート ＝ 実行する）です。

### 💻 ハンズオン（やってみよう）
```python
import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# クォーテーションを3つ繋げた """ """ で囲むと、複数行のSQLを綺麗に書けます！
sql_create = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT
);
"""

# SQLの呪文を唱える！
cursor.execute(sql_create)
print("students テーブルを作りました！")

connection.close()
```

> **💡 解説: `IF NOT EXISTS` って何？**
> 「もし、まだ無かったら（CREATE TABLE **IF NOT EXISTS**）」という意味のSQLの応用技です。
> プログラムを2回実行した時、「もうそのテーブルあるよ！」とPCが怒ってエラーで止まるのを防いでくれます。

---

## 🕒 レッスン 3: データを保存する絶対の掟 `commit()`

テーブルができたので `INSERT` でデータを入れてみましょう。
しかし、Pythonから書き込むときは**最後に必ず「セーブしろ！」と命令しないと、すべて消えてしまいます。**

### 💻 ハンズオン（やってみよう）
```python
import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# データをINSERTする呪文
sql_insert = "INSERT INTO students (id, name) VALUES (1, 'たかやま');"
cursor.execute(sql_insert)

# ⭐️【超重要】本当に書き込む（データを確定・セーブさせる）
connection.commit()
print("たかやまさんを登録しました！")

connection.close()
```

> **💡 解説: なぜ `commit()`（コミット）が必要なの？**
> もし銀行のプログラムで「Aさんの口座から1万円引いた」あと、「Bさんの口座に1万円足す」前にパソコンの電源が落ちたら？1万円が消滅して大事件になります。
> だからDBは、すべての処理が終わって「コミット（確約）してよし！」と言われるまで、本当の保存を「待ってくれる」安全機能があるのです。

---

## 🚀 今日の総仕上げ1：ミニプロジェクト「クラス名簿自動作成スクリプト」

Pythonファイルを実行するだけで、新しいDBファイルが生まれ、テーブルが作られ、自動的に最初の3人のデータがセットアップされる一連のプログラムを作ります。

### 📝 ミッション
- データベース `club.db` に接続します。
- `IF NOT EXISTS` を使って、`members` テーブル（`id` INTEGER, `name` TEXT, `club` TEXT）を作ります。
- 好きな友達3人のデータを `INSERT` するSQLを3回 `execute()` します。
- 最後に忘れずに `commit()` して閉じます！
 （一発でエラーなく実行できたら、完璧なエンジニアの素質があります！）

---

## 🚀 今日の総仕上げ2：ミニプロジェクト「スライム100匹・無限増殖ツール」

ここからがPythonとデータベースを合体させる**真骨頂**です。
Week 6で習った `for i in range()` と、`f文字列` を使って、一瞬で「スライム1号、スライム2号…」という100件のデータをデータベースにネジ込みます！手書きで100行打つ必要はありません。

### 📝 ミッション
1. `game.db` に接続し、`monsters` テーブル（`id` INTEGER, `name` TEXT, `hp` INTEGER）を作ります。
2. `for i in range(1, 101):` を使って1から100までのループを作ります。
3. ループの中で `f"INSERT INTO monsters (id, name, hp) VALUES ({i}, 'スライム{i}号', 10);"` というSQL文を作り、`execute()` します。
4. ループが終わった後に **1回だけ** `commit()` をして、100匹分のデータ保存を確定させましょう！
※「たった数行のforループ」で「100匹のモンスターが保存される」圧倒的パワーを体感してください！

---

## 📝 小テスト：実力チェック（全5問）

**Q1.** Pythonからデータベースを操作するために最初に `import` するライブラリ（連絡ツール）の名前はどれ？
- A. `sql_connect`
- B. `sqlite3`
- C. `database`

**Q2.** まず最初に、データベースのファイルにアクセス（電話をかける）するための命令文は？
- A. `sqlite3.open("db名")`
- B. `sqlite3.start("db名")`
- C. `sqlite3.connect("db名")`

**Q3.** SQLの呪文を呼び出すときに、「2度目以降の実行で『もうテーブルあるよ！』というエラー」を防ぐためにつける便利な言葉はどれ？
- A. `IF NOT EXISTS`
- B. `ONLY ONCE`
- C. `IGNORE ERROR`

**Q4.** Pythonで作ったSQLの呪文（CREATEやINSERT）を、実際にデータベースに向かって実行する（唱える）命令はどれ？
- A. `cursor.run()`
- B. `cursor.execute()`
- C. `cursor.play()`

**Q5.** `INSERT` や `UPDATE` でデータを変えた後、変更を本当に確定（完全にセーブ）するために絶対に忘れてはいけない命令はどれ？
- A. `save()`
- B. `commit()`
- C. `finish()`
