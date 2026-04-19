# Week 11: プロの検索テクニック「SELECT応用」

先週の `WHERE` では「完全に一致するもの（`=`）」だけを探しました。
しかし、Google検索やYouTubeの検索のように**「はっきり覚えてないけど、名前に『ドラゴン』がつくやつ！」**と探したいときの方が多いですよね。
今週はそういった「職人的な検索テクニック」を学びます！

---

## 🛠️ 事前準備（※授業の最初に必ずRunさせる）

先生が配る以下のSQLを、オンラインSQLエディタに貼り付けて一番最初に Run（実行）してください。

```sql
CREATE TABLE enemies (id INTEGER, name TEXT, type TEXT, hp INTEGER);
INSERT INTO enemies VALUES (1, 'レッドスライム', '炎', 20), (2, 'ブルースライム', '水', 20), (3, 'レッドドラゴン', '炎', 300), (4, 'メタルスライム', '鋼', 5), (5, 'ドクログール', '闇', 80), (6, 'キングレッドドラゴン', '炎', 999);

CREATE TABLE players (id INTEGER, name TEXT, team TEXT, score INTEGER);
INSERT INTO players VALUES (1, 'メッシ', 'A', 35), (2, 'ロナウド', 'B', 30), (3, 'ネイマール', 'A', 28), (4, 'エムバペ', 'C', 33), (5, 'ハーランド', 'B', 34), (6, 'ケイン', 'C', 25);

CREATE TABLE messages (id INTEGER, user_name TEXT, content TEXT);
INSERT INTO messages VALUES (1, 'たか', 'こんにちは！'), (2, '匿名', 'お前まじでばかだな'), (3, 'ゆう', '今日の給食おいしかった'), (4, '荒らし', 'あほくさ。帰るわ'), (5, '先生', '宿題忘れないように！');
```

---

## 🕒 レッスン 1: 曖昧（あいまい）な検索 `LIKE` の魔法

Googleで「プログラ」と入力すると「プログラミング」「プログラマー」など、**一部だけが一致する結果**を見せてくれます。
SQLでこの「曖昧（あいまい）検索」をするには、`=` の代わりに **`LIKE`** と **`%`（ワイルドカード）** を使います。

### 📚 LIKE と % の考え方

`%` は「ここに『何か』の文字が入るよ」という意味です。数学の「x」のような存在ですね。

```
LIKE 'ド%'
     ↓
「ド」で始まる、その後ろに何かがある
例：「ドラゴン」「ドラキー」「ドクログール」

LIKE '%ドラゴン%'
     ↑        ↑
「ドラゴン」という文字が入っていれば、前後どちらに何があってもOK
例：「レッドドラゴン」「キングレッドドラゴン」
```

### 💻 ハンズオン（LIKEで曖昧検索）

先生が用意した事前準備コードをRunして、大量の敵データ（`enemies` テーブル）を準備してください。

```sql
/* 「ド」から始まる名前の敵を全て探す */
SELECT * FROM enemies
WHERE name LIKE 'ド%';

/* どこかに「ドラゴン」を含む敵を全て探す（前後どちらに文字があってもOK） */
SELECT * FROM enemies
WHERE name LIKE '%ドラゴン%';
```

### 📖 LIKE の3つのパターン

| パターン | 名前 | 意味 | 例 |
|---------|------|------|-----|
| `LIKE 'ド%'` | 前方一致 | 「ド」で**始まる** | ドラゴン、ドクロ... |
| `LIKE '%ス'` | 後方一致 | 「ス」で**終わる** | スライム、ゴブリン... |
| `LIKE '%ドラゴン%'` | 部分一致 | 「ドラゴン」が**どこかに含まれる** | レッドドラゴン、ドラゴン... |

### ⚠️ よくあるミス（BEST 3）

```sql
❌ ミス1：% をシングルクォーテーションの外に書く
WHERE name LIKE %レッド%;
                ↑ ここがダメ

✓ 正しい：% は ' の中に
WHERE name LIKE '%レッド%';

❌ ミス2：= と LIKE を混ぜる
WHERE name = '%スライム%';
      ↑ これは曖昧検索にならない

✓ 正しい：曖昧検索は LIKE を使う
WHERE name LIKE '%スライム%';

❌ ミス3：テーブル名を忘れる
LIKE '%ド%';  ← WHERE がないとエラー
```

### ✍️ ドリル 1-1：レッドを探せ

名前に `'レッド'` という言葉を含む敵の全データを抽出してください。

```sql
SELECT * FROM enemies
WHERE name LIKE '%レッド%';
```

> **確認チェック：**
> - [ ] レッドスライム、レッドドラゴン、キングレッドドラゴンの3匹が表示された？
> - [ ] 前後の `%` を忘れなかった？

### ✍️ ドリル 1-2：スライム族を探せ

名前に `'スライム'` が含まれている敵を名前と属性（type）だけで表示してください。

```sql
SELECT name, type FROM enemies
WHERE name LIKE '%スライム%';
```

> **期待結果：** レッドスライム（炎）、ブルースライム（水）、メタルスライム（鋼）

### ✍️ ドリル 1-3：メタルで始まる敵

名前が `'メタル'` で**始まる**敵を探してください。

```sql
SELECT name, hp FROM enemies
WHERE name LIKE 'メタル%';
```

> **期待結果：** メタルスライム だけが表示される

---

## 🕒 レッスン 2: トップだけを取り出す `LIMIT`

100万人のゲームプレイヤーがいるとき、ランキングを見るために全員のデータを表示していたら、スマートフォンの画面がいっぱいになってしまいます。
「上位5人だけを見せて！」「最新の投稿10件だけ表示して！」という便利魔法が **`LIMIT`（リミット）** です。

### 📚 LIMIT の考え方

データベースから取り出すデータの「個数」を制限します。

```
【全員を見た場合】
1位：キングレッドドラゴン（HP 999）
2位：レッドドラゴン（HP 300）
3位：ドクログール（HP 80）
4位：ブルースライム（HP 20）
5位：レッドスライム（HP 20）
6位：メタルスライム（HP 5）

【LIMIT 3 で上位3匹だけ】
1位：キングレッドドラゴン（HP 999）
2位：レッドドラゴン（HP 300）
3位：ドクログール（HP 80）
```

### 💻 ハンズオン（ORDER BY + LIMIT で最強ランキング）

先週習った `ORDER BY`（並べ替え）と組み合わせるのが最強のテクニックです。

```sql
/* HPが高い順（DESC）に並べ替えて、上位「3件だけ」を表示する */
SELECT name, hp
FROM enemies
ORDER BY hp DESC
LIMIT 3;

/* 逆に、HPが低い順（ASC）に並べて、弱い敵トップ2を表示 */
SELECT name, hp
FROM enemies
ORDER BY hp ASC
LIMIT 2;
```

### 📖 LIMIT の構文

```
SELECT 列名 FROM テーブル名 ORDER BY 並べ替え列 DESC LIMIT 件数;
```

**重要な順番：`SELECT` → `FROM` → `WHERE` → `ORDER BY` → `LIMIT`**

### ⚠️ よくあるミス（BEST 3）

```sql
❌ ミス1：LIMIT が WHERE と ORDER BY の間に来る
SELECT name FROM enemies LIMIT 3 WHERE hp > 100;
                         ↑ 順番違い

✓ 正しい：LIMIT は一番最後
SELECT name FROM enemies WHERE hp > 100 ORDER BY hp DESC LIMIT 3;

❌ ミス2：ORDER BY なしで LIMIT を使う
SELECT * FROM enemies LIMIT 3;  ← 結果が「何順」かわからない

✓ 正しい：ランキングは ORDER BY と組み合わせる
SELECT name, hp FROM enemies ORDER BY hp DESC LIMIT 3;

❌ ミス3：OFFSET（スキップ）を忘れる
LIMIT 3 OFFSET 2  ← 3件目から2件飛ばして表示... これは応用
```

### ✍️ ドリル 2-1：最強モンスター TOP 3

HPが一番**高い**モンスター 3匹の「名前」と「HP」を表示してください。

```sql
SELECT name, hp
FROM enemies
ORDER BY hp DESC
LIMIT 3;
```

> **期待結果：** キングレッドドラゴン、レッドドラゴン、ドクログール

### ✍️ ドリル 2-2：最弱モンスター決定戦

HPが一番**低い**モンスターの「名前」と「HP」を**1匹だけ**表示してください。

```sql
SELECT name, hp
FROM enemies
ORDER BY hp ASC
LIMIT 1;
```

> **期待結果：** メタルスライム（HP: 5）だけ

### ✍️ ドリル 2-3：得点トップ 2 選手

`players` テーブルから、得点が高い順に上位2人の「名前」と「得点」を表示してください。

```sql
SELECT name, score
FROM players
ORDER BY score DESC
LIMIT 2;
```

> **期待結果：** メッシ（35点）、ハーランド（34点）

### ✍️ ドリル 2-4：得点が最も少ない選手

`players` テーブルから、得点が最も少ない選手の「名前」と「得点」を表示してください。

```sql
SELECT name, score
FROM players
ORDER BY score ASC
LIMIT 1;
```

> **期待結果：** ケイン（25点）

---

## 🕒 レッスン 3: カブリを消し去る `DISTINCT`

たくさんデータがあるとき、「全部で何種類の『属性（type）』があるんだろう？」と知りたいことがあります。
同じものをギュッと1つにまとめて（重複を排除して）表示する魔法が **`DISTINCT`（ディスティンクト）** です。

### 📚 DISTINCT の考え方

データに「重複」がある場合が多いですが、DISTINCT はそれを削除してくれます。

```
【普通に SELECT type FROM enemies】
炎（レッドスライム）
水（ブルースライム）
炎（レッドドラゴン）
鋼（メタルスライム）
闇（ドクログール）
炎（キングレッドドラゴン）
6件表示される（同じ「炎」が3回出現）

【DISTINCT を使ったら】
炎
水
鋼
闇
4種類だけが表示される（重複した「炎」が1つにまとまった）
```

### 💻 ハンズオン（DISTINCTで重複排除）

```sql
/* 普通に属性を出すと、炎、炎、水、水、炎... と大量に出てしまう */
SELECT type FROM enemies;

/* DISTINCT を使うと、かぶりを消して「炎、水、鋼、闇」など種類だけを教えてくれる！ */
SELECT DISTINCT type FROM enemies;
```

### 📖 DISTINCT の構文

```
SELECT DISTINCT 列名 FROM テーブル名;
```

**重要：`SELECT` の直後に `DISTINCT` を付ける**

### ⚠️ よくあるミス（BEST 2）

```sql
❌ ミス1：DISTINCT の位置が違う
SELECT type DISTINCT FROM enemies;
              ↑ この位置はNG

✓ 正しい：DISTINCT は SELECT の直後
SELECT DISTINCT type FROM enemies;

❌ ミス2：複数列でも DISTINCT 使える（応用）
SELECT DISTINCT type, name FROM enemies;
↑ この場合、「type と name の組み合わせ」で重複排除
```

### ✍️ ドリル 3-1：何種類の属性がある？

`enemies` テーブルから、全部で何種類の属性（`type`）があるか調べてください。
DISTINCT を使って、重複なしで属性を表示してください。

```sql
SELECT DISTINCT type FROM enemies;
```

> **期待結果：** 炎、水、鋼、闇 の4種類

### ✍️ ドリル 3-2：何種類のチームがある？

`players` テーブルから、全部で何種類のチーム（`team`）があるか調べてください。

```sql
SELECT DISTINCT team FROM players;
```

> **期待結果：** A、B、C の3チーム

### ✍️ ドリル 3-3：ユーザー情報を調べる

`messages` テーブルから、実際に投稿した人の名前（`user_name`）を、重複なしで表示してください。

```sql
SELECT DISTINCT user_name FROM messages;
```

> **期待結果：** たか、匿名、ゆう、荒らし、先生 の5人

---

## 🚀 今日の総仕上げ：ミニプロジェクト「スポーツ得点王ランキング」

事前準備で用意された `players` テーブル（選手データ）を使います。
カラムは `id`, `name`, `team`（チーム名）, `score`（得点）です。

### 📝 ミッション：新聞の1面に載せる「得点ランキング」を作成

あなたはスポーツ新聞の記者です。翌日の1面に載せるランキング記事のため、以下のステップで完璧なSQLを作ってください。

**ステップ1：** まず全選手のデータを確認してください。

```sql
SELECT * FROM players;
```

全6人の選手の情報が表示されましたか？

**ステップ2：** 得点（`score`）が高い順に並べ替える `ORDER BY DESC` を使います。

```sql
SELECT name, score FROM players ORDER BY score DESC;
```

得点が高い人から順に表示されましたか？

**ステップ3：** さらに「トップ5」だけに絞り込む `LIMIT 5` を追加します。

```sql
SELECT name, score
FROM players
ORDER BY score DESC
LIMIT 5;
```

ちょうど5人が得点の高い順に表示されましたか？

**ステップ4：** チーム名も一緒に表示して、「どのチームの選手が活躍しているか」をわかりやすくします。

```sql
SELECT name, team, score
FROM players
ORDER BY score DESC
LIMIT 5;
```

#### 完成イメージ

```
name      | team | score
---------|------|-------
メッシ    | A    | 35
ハーランド | B    | 34
エムバペ  | C    | 33
ロナウド  | B    | 30
ネイマール | A    | 28
```

> **チェックリスト：**
> - [ ] `SELECT` で必要な列（name, team, score）を指定した？
> - [ ] `ORDER BY score DESC` で得点が高い順に並んだ？
> - [ ] `LIMIT 5` で5人だけに絞れた？
> - [ ] 結果の見た目が上のイメージと同じ？

---

## 🚀 応用：OR を使った複数条件の組み合わせ

「AまたはB」という「どちらかを含む」検索をするときは **`OR`（オア）** を使います。
先週の `AND`（両方）と違い、`OR`（どちらか一方）を理解することが大切です。

### 📚 AND と OR の違い

```
【AND：両方とも必須】
「HPが100以上 AND 属性が炎」
→ 両方を満たすもの（フレイムは属性が炎だがHP120）だけ

【OR：どちらかでOK】
「名前に『ドラゴン』が含まれる OR 属性が炎」
→ どちらかを満たすもの（ドクログール、レッドドラゴンなど）が表示される
```

### 💻 ハンズオン（OR で複数検索）

```sql
/* 「炎属性」または「闇属性」の敵を探す */
SELECT name, type FROM enemies
WHERE type = '炎' OR type = '闇';

/* 「スライム」または「ドラゴン」を含む名前の敵 */
SELECT name FROM enemies
WHERE name LIKE '%スライム%'
   OR name LIKE '%ドラゴン%';
```

### ⚠️ よくあるミス

```sql
❌ ミス：OR の後ろに条件を省略する
WHERE content LIKE '%ばか%' OR '%あほ%';
                            ↑ これはNG

✓ 正しい：OR の後ろにも完全な条件を書く
WHERE content LIKE '%ばか%'
   OR content LIKE '%あほ%';
```

---

## 🚀 早く終わった人へ：ミニプロジェクト「掲示板の危険なNGワードパトロール」

あなたが管理している掲示板（`messages` テーブル）に、不適切な言葉を書き込む人が増えています！
AIパトロール隊員として、特定ワードが含まれる投稿を洗い出してください。

### 📝 ミッション（ステップバイステップ）

**ステップ1：** まず全メッセージを確認します。

```sql
SELECT * FROM messages;
```

全5件のメッセージが表示されましたか？

**ステップ2：** 「ばか」を含む投稿だけを探します。

```sql
SELECT id, user_name, content FROM messages WHERE content LIKE '%ばか%';
```

「ばか」を含む投稿が1件見つかりましたか？

**ステップ3：** `OR` を使って「ばか」**または**「あほ」を含む投稿を両方まとめて探します。

```sql
SELECT id, user_name, content FROM messages
WHERE content LIKE '%ばか%'
   OR content LIKE '%あほ%';
```

問題のある投稿が2件見つかりましたか？

**ステップ4：** チャレンジ問題：「帰る」または「わ」を含む投稿を探してください。

```sql
SELECT id, user_name, content FROM messages
WHERE content LIKE '%帰る%'
   OR content LIKE '%わ%';
```

> **キャプチャ：** OR の後ろには必ず完全な `content LIKE` の条件を書きます！

---

## 📝 小テスト：実力チェック（全5問）

**Q1.** SQLで「一部だけが一致しているもの（曖昧検索）」を探す時に `=` の代わりに使うキーワードは？

- A. `FIND`
- B. `LIKE`
- C. `MATCH`

**Q2.** `LIKE` で検索する時、「ここにどんな文字が入ってもいいよ！」という印（ワイルドカード）として使う記号は？

- A. `*`
- B. `%`
- C. `?`

**Q3.** 「スライム」「ドラゴン」などの中から、「ド」から始まる名前のものだけを探すための正しい書き方は？

- A. `LIKE '%ド'`
- B. `LIKE '%ド%'`
- C. `LIKE 'ド%'`

**Q4.** 全データの中から「上位5件だけ！」のように、表示する件数を絞り込む命令は？

- A. `TOP 5`
- B. `LIMIT 5`
- C. `MAX 5`

**Q5.** データの中にある「炎」「炎」「水」「水」「水」のような表示かぶりを消して、「炎」「水」という種類だけを表示する命令はどれ？

- A. `UNIQUE`
- B. `SINGLE`
- C. `DISTINCT`
