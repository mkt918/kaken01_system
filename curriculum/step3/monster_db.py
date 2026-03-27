# monster_db.py - 📦 「消えない」最強の図鑑を完成させよう！ 📦
import sqlite3

# --- 【準備】データベースに接続する ---
# dbファイルを作るよ。存在しなければ自動で作ってくれる！
conn = sqlite3.connect('monster_data.db')
cursor = conn.cursor()

# テーブル（表）を作る命令
cursor.execute('''
    CREATE TABLE IF NOT EXISTS monsters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
conn.commit()

print("==============================")
print("   📦 データベース図鑑システム 📦   ")
print("==============================")

while True:
    # データベースからこれまでに登録したものを全部読み込む
    cursor.execute("SELECT name FROM monsters")
    rows = cursor.fetchall()
    
    print("\n--- 現在の図鑑データ ---")
    if not rows:
        print("(まだ誰もいないよ)")
    for r in rows:
        print(f"・{r[0]}")

    name = input("\n新しいモンスターを登録！ (qで終了): ")
    if name == 'q':
        break
    
    # データベースに保存（INSERT）する命令
    cursor.execute("INSERT INTO monsters (name) VALUES (?)", (name,))
    conn.commit() # 「これで確定！」という意味
    print(f">>> データベースに保存したよ: {name}")

# 最後は接続を閉じる
conn.close()
print("\nプログラムを終了したよ。")
print("今度はプログラムを閉じても、データは次に開いた時も残っているよ！✨")
