# Week 18: 画面とデータベースを合体させよう！（フルスタック開発）

今週は、**「Pythonプログラミング」＋「SQLデータベース」＋「GUI（画面）」** という、これまでに習った3つの魔法をすべて同時に合体させます。
あなたが普段使っているスマホアプリの「画面から入力して保存する」「データ一覧を画面で見る」という仕組みを自力で作り上げる、究極のレッスンです！

---

## 🕒 レッスン 1: 画面の入力欄からDBに「保存（INSERT）」する

GUIの入力ボックス（`Entry`）に書かれた文字を受け取り、安全なプレースホルダ（`?`）を使ってデータベースに `INSERT` します。

### 💻 ハンズオン（やってみよう）
```python
import tkinter as tk
import sqlite3

# --- データベースの準備（テーブルがなければ作る） ---
conn = sqlite3.connect("contacts.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS friends (name TEXT)")
conn.commit()
conn.close()

# --- ボタンを押した時の関数 ---
def save_data():
    # 1. 画面から文字を取り出す
    friend_name = entry.get()
    
    # 2. DBを開いてINSERTする！
    conn = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO friends (name) VALUES (?)", (friend_name,))
    conn.commit()
    conn.close()
    
    # 3. 保存したよ！と画面に出す
    status_label.config(text=f"{friend_name} を保存しました！")

# --- 画面づくり ---
root = tk.Tk()
root.geometry("400x200")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="DBに保存する", command=save_data)
button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
```

---

## 🕒 レッスン 2: DBのデータを画面に「表示（SELECT）」する

今度は、データベースの中に入っている情報を引っ張り出し、画面のリストとして表示させます。
Tkinterの **`Listbox`（リストボックス）** という便利なパーツを使います。

### 💻 ハンズオン（やってみよう）
```python
import tkinter as tk
import sqlite3

def load_data():
    # 1. DBからデータを全件 SELECT する
    conn = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM friends")
    rows = cursor.fetchall()  # 全部取ってくる！
    conn.close()
    
    # 2. 画面のリストを一度カラにする
    listbox.delete(0, tk.END)
    
    # 3. ループを使って、1つずつ画面のリストに追加（insert）する
    for row in rows:
        # row[0]はフレンドの名前
        listbox.insert(tk.END, row[0])

# --- 画面づくり ---
root = tk.Tk()
root.geometry("400x300")

load_button = tk.Button(root, text="DBから読み込む", command=load_data)
load_button.pack()

# データを一覧表示するための大きな箱
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack()

root.mainloop()
```

**【結果の確認】**
ボタンを押すと、さっき「レッスン1」で保存した友達の名前がリストにズラッと並びましたか？
**おめでとうございます！あなたは今、「フルスタック（全部入り）アプリ」の仕組みを完成させました！**

---

## 🚀 今日の総仕上げ1：ミニプロジェクト「ウィンドウ版パスワード金庫」

前回は黒い画面で作ったパスワード金庫を、本格的なウィンドウアプリに進化させます。

### 📝 ミッション
- `vault.db`（金庫DB）に接続し、`passwords`（`site` TEXT, `pwd` TEXT）テーブルを準備します。
- **入力画面エリア**：サイト名（`site_entry`）とパスワード（`pwd_entry`）を書く2つの入力欄を用意します。
- **保存ボタン**：押すと2つの入力欄の文字を `INSERT` します。
- **読み込みボタン**：押すとDBから `SELECT` して `Listbox` に「サイト名：パスワード」の形で全て表示（ロード）します。

---

## 🚀 今日の総仕上げ2：ミニプロジェクト「本格ToDoリスト（やることリスト）アプリ」

これは、プロのエンジニアが一番最初に練習で必ず作る「ToDoリスト」アプリです。
来週からの「卒業制作」の最高のお手本になります。

### 📝 ミッション
1. `todo.db` を作り、`tasks`（`task_name` TEXT）テーブルを作ります。
2. 画面の上半分は「タスク入力欄」と「追加ボタン」です。
3. 画面の下半分には「大きなリストボックス（Listbox）」を置きます。
4. **【超重要】**：「追加ボタン」を押した時（`add_task`関数の中身）の動きを以下のようにします。
   - `INSERT` して保存する。
   - すぐに「入力欄の中身をカラッポ（`entry.delete(0, tk.END)`）」にする。
   - すぐに「読み込み関数（`load_data()`）」を呼び出して、下のリストボックスを最新状態に更新する！
     （※こうすることで、追加ボタンを押した瞬間に、下のリストにフッ！とタスクが現れる魔法のような動きになります！）

---

## 📝 小テスト：実力チェック（全5問）

**Q1.** 複数のデータを一覧でズラッと縦に並べて表示するための、Tkinterの画面パーツはどれ？
- A. `tk.Entry`
- B. `tk.Listbox`
- C. `tk.Button`

**Q2.** GUIでボタンを押した時に実行される関数の中で、DBにデータを保存したら絶対に忘れてはいけない命令はどれ？
- A. `conn.commit()`
- B. `conn.connect()`
- C. `conn.close_all()`

**Q3.** Listboxの中身を **一度すべてカラにする（消す）** ために使う命令はどれ？
- A. `listbox.clear()`
- B. `listbox.empty()`
- C. `listbox.delete(0, tk.END)`

**Q4.** Listboxの一番下（末尾）に、新しい文字を「追加」していくために使う呪文の指定の仕方はどれ？
- A. `listbox.add("文字")`
- B. `listbox.insert(tk.END, "文字")`
- C. `listbox.push("文字")`

**Q5.** ToDoリストアプリで、「追加ボタン」を押した瞬間に追加したタスクが下のリストにすぐ表示されるようにするには、関数の最後で何をすればいい？
- A. もう一度ウインドウを作り直す
- B. データをセーブした直後に、SELECTして画面に入れ直す `load_data()` 関数を呼び出す
- C. パソコンを再起動する
