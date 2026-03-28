# 指導案: Week 14 「別々のデータをくっつける（JOINとStep2総決算）」

## 🎯 今週のねらいと授業のゴール
Step 2（SQL基礎）の最終週です。中学生には高度なトピックになりがちな「テーブル結合（JOIN）」を、座学を削って「パズルのように合体させる」感覚で体験させます（外部キーなどの難しいDB設計用語は最小限にします）。
後半の1時間は「SQL大脱出ゲーム」と題し、ここまでの6週間で学んだSELECT・WHERE・ORDER BY・LIMIT・集計関数の全てをノーヒントで使わせる総合演習を行います。

---

## 🛠️ 事前準備（※授業の最初に必ずRunさせる）
以下のSQLを生徒に配り、オンラインSQLエディタで一番最初に実行（Run）させてデータを揃えてください。

```sql
CREATE TABLE customers (id INTEGER, name TEXT);
INSERT INTO customers VALUES (1, 'たかやま'), (2, 'すずき'), (3, 'さとう');

CREATE TABLE orders (id INTEGER, customer_id INTEGER, item_name TEXT, price INTEGER);
INSERT INTO orders VALUES (101, 1, 'パソコン', 100000), (102, 1, 'マウス', 5000), (103, 2, 'キーボード', 10000), (104, 3, 'モニター', 30000), (105, 3, 'ケーブル', 2000);

CREATE TABLE weapons (id INTEGER, weapon_name TEXT);
INSERT INTO weapons VALUES (1, 'ひのきの棒'), (2, 'はがねの剣'), (3, '炎の杖');

CREATE TABLE heroes (id INTEGER, name TEXT, weapon_id INTEGER);
INSERT INTO heroes VALUES (1, 'アーサー', 2), (2, 'マーリン', 3), (3, '村人A', 1);

CREATE TABLE escape_data (id INTEGER, name TEXT, age INTEGER, weight INTEGER, blood_type TEXT, status TEXT);
INSERT INTO escape_data VALUES (1, 'たかし', 20, 60, 'A', 'DANGER'), (2, 'エミ', 25, 50, 'B', 'SAFE'), (3, 'ジョン', 40, 90, 'O', 'SAFE'), (4, 'エリカ', 30, 55, 'A', 'DANGER'), (5, 'ケン', 22, 70, 'AB', 'SAFE'), (6, 'マイ', 18, 48, 'B', 'SAFE');
```

---

## ⏱️ タイムテーブル (180分)

### 1️⃣ なぜテーブルを分けるのか？ (0分〜30分)
- **【解説】**: 「Excelみたいに1枚のシートに全部書けばいいじゃん！」という生徒の素朴な疑問に対し、「武器の攻撃力変更」などの例を挙げて「更新漏れ（データ不整合）を防ぐため」だと論理的に説明します。
- **【演習】**: 事前準備（Run）を済ませさせます。

### 2️⃣ くっつける魔法（JOINとON） (30分〜70分)
- **【解説】**: `customers.name` のように「テーブル名.カラム名」の表記が初登場します。「名字と名前の関係だよ。佐藤くんの太郎、みたいな」と説明します。
- **【演習】**: 「レッスン2」と「ドリル2-1」を実行させます。
- **【トラブルシューティング】**: 
  - `ON` 条件の `=` を忘れたり、そもそも `ON` を書き忘れたりするミスが多発します。「くっつける時の糊（のり）がONだよ！」としつこく教えます。

### 3️⃣ ミニプロジェクト 1：お店の売上分析（VIPを探せ） (70分〜110分) ※その後休憩10分
- **【総合演習 1】**: 「SQLで最も書く回数が多い」と言っても過言ではない、JOINとGROUP BYとSUMの合体クエリです。
- **【解答例】**: 
  ```sql
  SELECT customers.name, SUM(orders.price) 
  FROM orders 
  JOIN customers ON orders.customer_id = customers.id 
  GROUP BY customers.name 
  ORDER BY SUM(orders.price) DESC;
  ```
  この長文を自力で書けた生徒は天才です。全力で褒めてください。「将来データサイエンティストになれるよ！」という声かけが効果的です。

### 4️⃣ Step 2 総決算：SQL大脱出ゲーム (120分〜170分)
- **【総合演習 2】**: 怒涛の全復習クイズです。ヒントなしで挑ませ、どうしても苦戦しているグループにだけ板書の過去の文法を指差してあげます。
- **【解答と正解】**:
  - 第1の扉：`SELECT COUNT(*) FROM escape_data WHERE status = 'SAFE';`（正解：4人）
  - 第2の扉：`SELECT name FROM escape_data ORDER BY weight DESC LIMIT 1;`（正解：ジョン）
  - 第3の扉：`SELECT AVG(age) FROM escape_data WHERE name LIKE '%エ%';`（エミ25、エリカ30 なので 正解：27.5）
  - 最後の扉：`SELECT blood_type, COUNT(*) FROM escape_data GROUP BY blood_type ORDER BY COUNT(*) DESC;`（正解：A型とB型が2人で同率1位 ※どちらを答えてもOKとする）

### 5️⃣ 小テストと総括式 (170分〜180分)
- 小テストを行い、これにて「Step 2：SQL基礎（データベース）」が見事クリアされたことを宣言します。
- 「次回からはいよいよ、PythonとSQLを合体させたシステム作り（Step 3）に入るぞ！」と予告し、モチベーションを高めて終わります。

---

## 📝 小テストの解答と解説（Step 2 最終確認テスト）

**Q1.** データを入れるための「枠組み」であるテーブルを新しく作成するSQLは？
- **正解:** **B. `CREATE TABLE`**

**Q2.** テーブルから、いらなくなったデータ（行）を削除するSQLは？
- **正解:** **A. `DELETE FROM`**

**Q3.** 「大きい順（降順）」に並べ替えたいときに `ORDER BY` のあとに書く指定は？
- **正解:** **C. `DESC`**

**Q4.** 文字列の一部が一致するものを探す「曖昧検索」で使うワイルドカード記号はどれ？
- **正解:** **B. `%`** （パーセント）

**Q5.** 別々に分かれた2つのテーブルを、「共通のID」などを鍵にして1つにくっつける（合体させる）SQLは？
- **正解:** **C. `JOIN`**
- **解説:** アプリやゲームの裏側では、10個以上のテーブルをJOINして膨大なデータから一瞬で答えを弾き出していることを伝えましょう。
