# monster_gui.py - 🎨 モンスター図鑑を「アプリ」にしよう！ 🎨
import tkinter as tk
from tkinter import messagebox

# --- 【準備】データを入れる箱 ---
monsters = []

# --- 【関数】ボタンが押された時の動き ---
def add_monster():
    name = entry_name.get() # 入力欄から名前をゲット
    if name == "":
        messagebox.showwarning("入力エラー", "名前を入れてね！")
        return
    
    monsters.append(name)
    listbox.insert(tk.END, name) # リストに表示
    entry_name.delete(0, tk.END)  # 入力欄を空にする
    print(f"登録しました: {name}")

# --- 【画面を作る】 ---
root = tk.Tk()
root.title("⚔️ モンスター登録ツール ⚔️")
root.geometry("300x400")

# タイトルラベル
label_title = tk.Label(root, text="モンスター名を入力！", font=("MS Gothic", 12))
label_title.pack(pady=10)

# 入力欄
entry_name = tk.Entry(root, font=("MS Gothic", 12))
entry_name.pack(pady=5)

# 登録ボタン
button_add = tk.Button(root, text="図鑑に登録！", command=add_monster, bg="lightblue")
button_add.pack(pady=10)

# 表示用リストボックス
listbox = tk.Label(root, text="--- 図鑑リスト ---")
listbox.pack()
listbox = tk.Listbox(root, font=("MS Gothic", 10))
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# 実行！
print("プログラムが起動したよ。ウィンドウを閉じて終了してね。")
root.mainloop()
