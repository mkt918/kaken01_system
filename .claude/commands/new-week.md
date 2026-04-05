新しい週のコンテンツファイルを作成します。

## 使い方
`/new-week` の後に以下を指定してください：
- 科目: `boki`（簿記）または `prog`（プログラミング）
- 週番号: 例 `09`
- テーマ: 例 `売掛金・買掛金`

例: `/new-week boki 09 売掛金・買掛金`

## 作業内容
1. 既存の週（直前の週）の `student.md` と `teacher.md` を参考にする
2. 同じ構成・フォーマットで新しい週のファイルを作成する
3. 作成先:
   - 簿記: `website/content/boki_week{XX}/student.md` と `teacher.md`
   - プログラミング: `website/content/week{XX}_{テーマ}/student.md` と `teacher.md`
4. 作成後にファイルパスを報告する

$ARGUMENTS
