# Week 10: 膨大なデータから宝を探す「SELECT」

データベースに何万、何百万というデータを詰め込んだあと、そこから「自分の欲しいデータだけを一瞬で見つけ出す」のがデータベースの本当の力です。
オンラインショッピングで「5000円以下」「黒色」などで検索する裏側も、今日学ぶ **`SELECT`（セレクト）** と **`WHERE`（ウェア）** の魔法が動いています。

---

## 🛠️ 事前準備（※授業の最初に必ず実行！）

先生が配る以下のSQLを、オンラインSQLエディタに貼り付けて一番最初に Run（実行）してください。
これを実行することで、今日使うデータが全て準備できます。

```sql
CREATE TABLE students (id INTEGER, name TEXT, grade INTEGER);
INSERT INTO students VALUES (1, 'たろう', 1), (2, 'はなこ', 2), (3, 'さぶろう', 1);

CREATE TABLE monsters (id INTEGER, name TEXT, type TEXT, hp INTEGER);
INSERT INTO monsters VALUES (1, 'スライム', '水', 30), (2, 'フレイム', '炎', 120), (3, 'ドラゴン', '炎', 500), (4, 'ゴブリン', '土', 80);

CREATE TABLE health_data (id INTEGER, name TEXT, height INTEGER, weight INTEGER);
INSERT INTO health_data VALUES (1, 'たかやま', 185, 80), (2, 'なかむら', 160, 50), (3, 'さとう', 170, 65), (4, 'すずき', 155, 62);

CREATE TABLE citizens (id INTEGER, name TEXT, age INTEGER, gender TEXT, height INTEGER);
INSERT INTO citizens VALUES (1, 'ジョン', 25, '男', 170), (2, 'マイク', 35, '男', 180), (3, 'エマ', 32, '女', 165), (4, 'ボブ', 40, '男', 172);
```

---

## 🕒 レッスン 1: 欲しい「列」だけを見る

先週は `SELECT * FROM heroes;` と書きました。この `*`（アスタリスク）は「**すべての列（カラム）を見せろ！**」という意味です。
でも、現実のデータベースは「パスワード」や「住所」など、見せてはいけない列が混ざっています。
そこで、「**名前と点数だけ欲しい**」「**IDと生年月日だけ見たい**」など、必要な列だけを取り出す技を学びます。

### 📊 「すべて」と「選別」の違い

```
【* で全部取出】
id | name     | hp
---|----------|-----
1  | スライム | 30
2  | フレイム | 120

【特定の列だけ取出】
name     
---------|
スライム
フレイム
```

### 💻 ハンズオン（やってみよう）

事前準備コードを実行したら、以下のSQLを実行して「名前だけ」や「名前とHPだけ」を抽出してみましょう。

```sql
/* 生徒の名前だけを抜き出す */
SELECT name FROM students;

/* モンスターの名前と、HPの列だけを抜き出す（, で区切る） */
SELECT name, hp FROM monsters;
```

### 📖 SELECT の構文（列を選ぶ）

```
SELECT 列名1, 列名2, 列名3 FROM テーブル名;
```

| 部分 | 意味 |
|------|------|
| `SELECT` | 「このカラムを選ぶ」という命令 |
| `name, hp` | 欲しい列。複数は `,`（カンマ）で区切る |
| `*` | 「全部」という意味（すべての列を取出） |
| `FROM` | 「どのテーブルから」という区切り言葉 |

### ✍️ ドリル 1-1：名前と属性

`monsters` テーブルから、「名前（`name`）」と「属性（`type`）」の2つの列だけを抽出して表示してください。

```sql
/* ここに SELECT 文を書こう！ */
SELECT name, type FROM monsters;
```

> **確認：** 4匹のモンスターの名前と属性（炎・水・土）が表示されましたか？

---

## 🕒 レッスン 2: 魔法のフィルター `WHERE`（条件絞り込み）

データが何万件もあるとき、上から全部見るのは不可能です。
「HPが100以上のやつだけ出ろ！」と条件をつける魔法が **`WHERE`（ウェア）** です。これは Pythonの `if` と同じ考え方ですね。

### 📚 WHERE の考え方

データベースは「フィルター機能」を持っています。スマートフォンのアプリで「★4以上の口コミだけ表示」「価格1000円以下だけ見る」という機能と同じです。

```
【全部見る】
スライム（HP 30）
フレイム（HP 120） ← 100以上のやつ
ドラゴン（HP 500） ← 100以上のやつ
ゴブリン（HP 80）

【WHERE hp >= 100 でフィルター】
フレイム（HP 120）
ドラゴン（HP 500）
```

### 💻 ハンズオン（WHEREで絞り込む）

```sql
/* HPが「100以上 (>=)」のモンスターだけを抽出する */
SELECT name, hp
FROM monsters
WHERE hp >= 100;
```

### 📖 WHERE の構文と比較記号

```
SELECT 列名 FROM テーブル名 WHERE 条件;
```

**比較記号の一覧：**

| 記号 | 意味 | 例 |
|------|------|-----|
| `=` | 等しい（同じ） | `grade = 1`（1年生） |
| `>` | より大きい | `hp > 100`（100より大） |
| `<` | より小さい | `hp < 50`（50より小） |
| `>=` | 以上 | `age >= 18`（18以上） |
| `<=` | 以下 | `weight <= 60`（60以下） |

> **⚠️ 超重要：Pythonとの違い**
> Pythonでは「等しい」を `==`（イコール2個）と書きますが、**SQLでは `=`（イコール1個）** です。
> 
> ```python
> # Pythonの場合
> if age == 18:
> ```
> 
> ```sql
> -- SQLの場合
> SELECT * FROM students WHERE age = 18;
> ```
> 
> `WHERE hp == 100` と書くとエラーになります。要注意！

### ⚠️ WHERE で文字（TEXT）を検索するときの注意

数字（INTEGER）と文字（TEXT）では、シングル引用符の有無が異なります：

```sql
-- 【数字の場合】シングル引用符なし
SELECT * FROM students WHERE grade = 1;

-- 【文字の場合】シングル引用符で囲む
SELECT * FROM monsters WHERE type = '炎';
```

### ✍️ ドリル 2-1：属性で絞り込む

`type` が `'炎'` のモンスターだけを抽出して、名前と属性を表示してください。

```sql
SELECT name, type
FROM monsters
WHERE type = '炎';
```

**ステップバイステップ：**
1. 全モンスターを見る：`SELECT * FROM monsters;`
2. 条件を追加：`WHERE type = '炎'`
3. 必要な列だけ：`SELECT name, type`

> **確認チェック：**
> - [ ] フレイムとドラゴンの2匹だけが表示された？
> - [ ] `'炎'` のようにシングルクォーテーションで囲めた？
> - [ ] `WHERE` の条件は正しい？

---

## 🕒 レッスン 3: 順番に並べ替える `ORDER BY`

ゲームの「スコアランキング」と同じように、数字が大きい順や小さい順に並べ替える魔法が **`ORDER BY`（オーダーバイ）** です。
Youtubeで「再生数が多い順」「最新アップロード順」という検索フィルターと同じですね。

### 📚 ORDER BY の考え方

データはそのままだと「登録した順番」で表示されます。これを「HPの高い順」「名前のあいうえお順」など、好きな順番に並べ替えられます。

```
【元の順番：登録順】
スライム（HP 30）
フレイム（HP 120）
ドラゴン（HP 500）
ゴブリン（HP 80）

【ORDER BY hp DESC：HPが大きい順】
ドラゴン（HP 500）
フレイム（HP 120）
ゴブリン（HP 80）
スライム（HP 30）

【ORDER BY hp ASC：HPが小さい順】
スライム（HP 30）
ゴブリン（HP 80）
フレイム（HP 120）
ドラゴン（HP 500）
```

### 💻 ハンズオン（ORDER BYで並べ替える）

```sql
/* HPが「大きい順」に並べ替える（DESC = 降順） */
SELECT name, hp
FROM monsters
ORDER BY hp DESC;

/* HPが「小さい順」に並べ替える（ASC = 昇順） */
SELECT name, hp
FROM monsters
ORDER BY hp ASC;
```

### 📖 ORDER BY の構文

```
SELECT 列名 FROM テーブル名 ORDER BY 並べ替え対象の列 DESC;
```

| 部分 | 意味 |
|------|------|
| `ORDER BY` | 「順番を並べ替える」という命令 |
| `hp` | 何の列で並べ替えるか |
| `DESC` | **D**escending（降順）= 大きい順 |
| `ASC` | **A**scending（昇順）= 小さい順 |

> **💡 覚え方のコツ**
>
> - `DESC`：**D**own（下降） → ダウン → スコアが下がる → 大きい順
> - `ASC`：**A**scend（上昇） → 上昇 → スコアが上がる → 小さい順
> 
> または「ランキング」で考える：
> - `DESC`：1位（高い）から下へ = 大きい順
> - `ASC`：最下位（低い）から上へ = 小さい順

### ✍️ ドリル 3-1：身長が高い順に並べ替え

`health_data` テーブルから、全員の名前と身長を、身長が高い順（`DESC`）に表示してください。

```sql
SELECT name, height FROM health_data ORDER BY height DESC;
```

**期待される結果：** 身長の高い人から順に表示される

> **確認チェック：**
> - [ ] `ORDER BY height DESC` と書けた？
> - [ ] 一番身長の高い人が最初に表示された？
> - [ ] 降順（DESC）で正しく動作した？

---

### ⚠️ よくあるミス

```sql
❌ ミス1：ORDER BY の後に ASC/DESC を忘れる
SELECT name, hp FROM monsters ORDER BY hp;
                                      ↑ ASC か DESC がない

❌ ミス2：WHERE と ORDER BY の順番を間違える
SELECT name, hp FROM monsters ORDER BY hp WHERE hp > 100;
                                        ↑ これは間違い！

正しい順番：
SELECT name, hp FROM monsters WHERE hp > 100 ORDER BY hp DESC;
                                  ↑ WHERE が先、ORDER BY が後
```

**正しい文の順番：`SELECT → FROM → WHERE → ORDER BY`**

---

## 🕒 ボーナスレッスン：2つの条件を組み合わせる `AND`

今までは「HPが100以上」のような「1つの条件」だけでしたが、現実はもっと複雑です。
「HPが100以上 **かつ** 火属性」のように「2つの条件を両方満たす」ことが多いです。その魔法が **`AND`（アンド）** です。

### 💻 ハンズオン（AND で2つの条件を組み合わせる）

```sql
/* HPが100以上 AND 属性が「炎」のモンスターだけ */
SELECT name, type, hp
FROM monsters
WHERE hp >= 100 AND type = '炎';
```

### 📖 AND の構文

```
SELECT 列名 FROM テーブル名 WHERE 条件1 AND 条件2;
```

**複数条件の例：**

```sql
-- 年齢が20以上 AND 性別が「女」
WHERE age >= 20 AND gender = '女'

-- 身長が170より大きい AND 体重が60以下
WHERE height > 170 AND weight <= 60
```

> **💡 AND の意味**
> - `AND` = 「かつ」「両方とも」「同時に満たす」
> - 条件1も条件2も **両方とも** クリアしたやつだけが表示される
> - 「Aまたはどちらか」という場合は `OR` を使いますが、今週は `AND` だけ覚えましょう

---

## 🚀 今日の総仕上げ：ミニプロジェクト「クラスの身体測定ランキング」

事前準備で作った `health_data`（身体測定）テーブルを使います。
カラムは `id`, `name`, `height`（身長）, `weight`（体重）です。

### 📝 ミッション（ステップバイステップ）

**ステップ1：** まず全データを確認

```sql
SELECT * FROM health_data;
```

全員の身長と体重が表示されましたか？

**ステップ2：** 身長が高い順に並べ替え

```sql
SELECT name, height FROM health_data ORDER BY height DESC;
```

一番背の高い人から順に表示されましたか？

**ステップ3：** 体重が60キロ以上の人だけを抽出

```sql
SELECT name, weight FROM health_data WHERE weight >= 60;
```

体重が60キロ以上の人だけが表示されましたか？

**ステップ4：** 複合条件：「身長が170cm以上 **かつ** 体重が60kg以上」

```sql
SELECT name, height, weight
FROM health_data
WHERE height >= 170 AND weight >= 60;
```

両方の条件を満たす人が表示されましたか？

---

## 🚀 早く終わった人へ：ミニプロジェクト「スパイを探せ！条件検索ゲーム」

巨大な `citizens`（市民）データベースの中に、たった1人の「重大なスパイ」が紛れ込んでいます！
警察からの情報（条件）を元に、スパイが誰なのかを特定してください。

> **💡 `AND` とは？**
> 2つの条件を「どちらも満たす」ときに使う言葉です。「HPが100以上 **かつ** 炎属性」のように書けます。

### 📝 ミッション（スパイを探せ）

**警察からの極秘情報：**

- スパイの年齢（`age`）は **30歳以上** である。
- スパイの性別（`gender`）は **'男'** である。
- スパイの身長（`height`）は **175より大きい**。

以下のSQLを一行ずつ試して、犯人を絞り込んでいきましょう。

**ステップ1：** 年齢30以上の人を探す

```sql
SELECT * FROM citizens WHERE age >= 30;
```

**ステップ2：** 年齢30以上 AND 男性 に絞り込む

```sql
SELECT * FROM citizens WHERE age >= 30 AND gender = '男';
```

**ステップ3：** さらに身長175より大きい という条件を追加

```sql
SELECT * FROM citizens
WHERE age >= 30
  AND gender = '男'
  AND height > 175;
```

最後に絞り込まれて残った1人が犯人です。犯人の名前を当ててください！

---

## 📝 小テスト：実力チェック（全5問）

**Q1.** 全ての列（カラム）を取り出したいときに使う、Pythonの「かけ算」と同じ記号はどれ？

- A. `#`
- B. `$`
- C. `*`

**Q2.** SQLで「条件を指定して、欲しいデータだけを絞り込む」ための命令（魔法）はどれ？

- A. `IF`
- B. `FIND`
- C. `WHERE`

**Q3.** SQLで「同じ（等しい）」という条件を書くとき、正しい記号はどれ？（Pythonとは違います！）

- A. `==`
- B. `=`
- C. `===`

**Q4.** データを「大きい順（降順）」に並べ替えたいときに `ORDER BY` の後ろにつける飾りの言葉はどれ？

- A. `DESC`
- B. `ASC`
- C. `UP`

**Q5.** 2つの条件を両方ともクリア（Aであり、かつBである）するために使う結合の言葉はどれ？

- A. `OR`
- B. `PLUS`
- C. `AND`
