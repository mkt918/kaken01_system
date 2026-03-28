# Week 21〜23: 卒業制作(3)〜(5) 集中開発＆エラーサバイバル辞典

ここからの3週間は、各々が自分の選んだ道（アプリ）をひたすら作り込む時間です。
プログラミングの世界では、**「開発の8割の時間はエラーとの戦い」**と言われています。
今週からの目標は「先生を呼ばずに、赤いエラーメッセージを自力で読み解いて解決する『自走力（プロの力）』を身につけること」です。

---

## 🛠️ 機能拡張レシピ集（作りたい機能をコピペして改造しよう）

プロトタイプ（入力と表示）ができたら、次は機能を追加してアプリをリッチにしましょう！

### レシピ1：「検索」ボタンを作りたい！
> 【ヒント】`WHERE` と `LIKE` を使います。

```python
def search_data():
    keyword = search_entry.get()
    
    conn = sqlite3.connect("あなたのDB.db")
    cursor = conn.cursor()
    # ▼ 名前に keyword が含まれている人だけを SELECT する！
    cursor.execute("SELECT * FROM テーブル名 WHERE name LIKE ?", (f'%{keyword}%',))
    rows = cursor.fetchall()
    conn.close()
    
    # 画面を一度カラにしてから、見つかった rows を入れ直す（Week 18参照！）
```

### レシピ2：リストにあるデータを「削除」したい！
> 【ヒント】`DELETE FROM` と、リストで「今選択されている行の文字」を取得する `curselection()` を使います。少しレベルが高いです！

```python
def delete_data():
    # 1. ユーザーがリストの中で「今クリックして青くなっている行」の番号を取る
    selected_index = listbox.curselection()

    if selected_index:  # もしちゃんと選ばれていたら
        # 2. その行に書かれている文字を取る
        target_text = listbox.get(selected_index)
        
        conn = sqlite3.connect("あなたのDB.db")
        cursor = conn.cursor()
        # ▼ その文字と一致するデータをDBから削除！
        cursor.execute("DELETE FROM テーブル名 WHERE name = ?", (target_text,))
        conn.commit()
        conn.close()
        
        # 3. リストを最新状態にする（再読み込み関数を呼ぶ）
        load_data()
```

---

## 🚨 エラーサバイバル辞典（赤い文字が出たらここを見ろ！）

画面の下（ターミナル）に真っ赤な文字でエラーが出たら、**絶対に逃げないでください。**
パソコンは意地悪でエラーを出しているのではなく、「ここが間違ってるよ！」と親切にヒントをくれているのです。

### エラー 1：`SyntaxError: invalid syntax`
- **【意味】**：文法（Syntax）が間違っています。英語のスペルミスです。
- **【解決法】**：エラーが出ている行の「カッコ `()` の閉じ忘れ」「コロン `:` の書き忘れ」「クォーテーション `""` の片方忘れ」がないか、虫メガネのように探してください。

### エラー 2：`NameError: name '〇〇' is not defined`
- **【意味】**：そんな名前の変数や関数は知りません（定義されていません）。
- **【解決法】**：大文字・小文字を間違えていませんか？（`Button` なのに `button` と書いている等）。または、作る前に使おうとしていませんか？

### エラー 3：`OperationalError: no such table: 〇〇`
- **【意味】**：データベースの中に、そんな名前のテーブルはありません。
- **【解決法】**：テーブル名（箱の名前）をタイプミスしていませんか？ または `CREATE TABLE` が成功する前に `INSERT` や `SELECT` をしようとしていませんか？

### エラー 4：`OperationalError: table 〇〇 already exists`
- **【意味】**：そのテーブルはもう存在しています（2回同じ名前で作ろうとしています）。
- **【解決法】**：`CREATE TABLE` の後ろに `IF NOT EXISTS` という「無ければ作る」のおまじないを書き忘れています！

### エラー 5：`TypeError: not all arguments converted during string formatting` などの引数エラー
- **【意味】**：`?` の数に対して、渡そうとしたデータの数が合っていません。
- **【解決法】**：`VALUES (?, ?)` とハテナが2つなら、`(変数1, 変数2)` のように渡すデータも2つでないとDBが混乱して怒ります。カンマの数も数えましょう。

### 🌟 最終奥義：Google先生（AI先生）に聞く
上の辞典に載っていないエラーが出たら、一番下のエラーの一文（`TypeError: ...` の部分）をマウスでコピーして、そのままWeb検索に入力してください。世界中のエンジニアの解決策がすぐに見つかります！
