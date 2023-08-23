# BulkBuddy要件定義書

作成日時: August 23, 2023 2:18 PM

# 基本情報

- 設計方針：基本機能（無料機能から作っていく）
- ログイン必須（コラム無料だけ開放）
- Userテーブル（id、名前、パスワード、身長、体重、年齢、消費カロリー、目標体重、目標期日）
- Snsテーブル（id、名前、タイムスタンプ、内容、返信、いいね（ソートキー）、カテゴリー）

→ category：食事内容、トレーニング内容

- 強制有料プラン（7days）
- フロント、バック担当は一緒

### 目標設定機能

- 目標カロリーの設定
- 初回ログイン時のアンケート機能

→基本アンケート項目

1. あなたの目標は？（希望体重）
2. 名前は？
3. 生年月日は？
4. 身長は？
5. 体重は？
6. アカウントの設定（パスワード、〇〇でサインアップなど）
7. （ポリシー、利用規約、Cookieポリシー）

→プラン診断

1. あなたの目標体重は？（number > number の形状）
2. ペース（2023年、12月、1日達成する！など）
3. 増量へのアプローチ方法は？（食事中心、食事とバランスよく、運動中心 <目標摂取カロリーと目標消費カロリーの表示> ）
4. コース、手段の提示（基本コース、〇〇コースなど）
5. 結果の表示（〇〇コースで、〇〇までに、〇〇kg、一日の摂取カロリー、朝昼晩の摂取カロリー）

### フロントについて

- 

Userテーブル（id（プライマリーキー）、名前、パスワード、身長、体重、年齢、消費カロリー、目標体重、目標期日）

### API仕様書

|  |  |  | リクエストパラメータ |  |  | レスポンス内容 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| メゾット | エントリーポイント | 処理の内容 | 変数名 | 型 | 必須 | 変数名 | 型 |
| POST | /user/signup | ユーザの登録 | userId | string | ○ | userId | string |
|  |  |  | name | string | ○ | name | string |
|  |  |  | password | string | ○ |  |  |
|  |  |  | height | number | ○ | height | number |
|  |  |  | weight | number | ○ | weight | number |
|  |  |  | age | number | ○ | age | number |
|  |  |  | calorie | number |  |  |  |
|  |  |  | targetWeight | number |  | targetWeight | number |
|  |  |  | targetDate | number |  | targetData | number |
|  |  |  |  |  |  | token | string |
| POST | /user/login | ユーザの認証 | userId | string | ○ | token | string |
|  |  |  | password | string | ○ |  |  |
| GET | /user | ユーザ情報の取得 | userId | string | ○ | userId | string |
|  |  |  |  |  |  | name | string |
|  |  |  |  |  |  | height | number |
|  |  |  |  |  |  | weight | number |
|  |  |  |  |  |  | age | number |
|  |  |  |  |  |  | calorie | number |
|  |  |  |  |  |  | targetWeight | number |
|  |  |  |  |  |  | targetDate | number |
|  |  |  |  |  |  |  |  |
| PUT | /user | ユーザ情報の更新 | userId | string | ○ | userId | string |
|  |  |  | name | string | ○ | name | string |
|  |  |  | password | string | ○ |  |  |
|  |  |  | height | number | ○ | height | number |
|  |  |  | weight | number | ○ | weight | number |
|  |  |  | age | number | ○ | age | number |
|  |  |  | calorie | number |  |  |  |
|  |  |  | targetWeight | number |  | targetWeight | number |
|  |  |  | targetDate | number |  | targetData | number |
| DELETE | /user | ユーザの削除 | userId | string | ○ | エラー401 |  |
|  |  |  |  |  |  |  |  |
| PUT | /user/record | カロリーの登録 | userId | string | ○ | userId | string |
|  |  |  | date | number | ○ | date | number |
|  |  |  | calorie | number | ○ | calorie | number |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

### コミュニティ機能

- sns写真なし、投稿、返信機能のみ

Snsテーブル（id（プライマリーキー）、名前、タイムスタンプ、内容、返信、いいね（ソートキー））

### API仕様書

|  |  |  | リクエストパラメータ |  |  | レスポンス内容 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| メゾット | エントリーポイント | 処理の内容 | 変数名 | 型 | 必須 | 変数名 | 型 |
| POST | /article | 投稿 | userId | string | ○ | userId | string |
|  |  |  | name | string | ○ | name | string |
|  |  |  | text | string | ○ | text | string |
|  |  |  | category | string |  | category | string |
|  |  |  |  |  |  | timestamp | number |
|  |  |  | reply | array (0) |  |  |  |
|  |  |  | likePost | number (0) |  |  |  |
| GET | /article/search | 検索 | userId | string |  | userId | string |
|  |  |  | category | string |  | name | string |
|  |  |  | likePost | number |  | text | string |
|  |  |  | timestamp | number |  | category | string |
|  |  |  |  |  |  | reply | array (0) |
|  |  |  |  |  |  | likePost | number (0) |
| GET | /article | 表示 |  |  |  | articles | array |
| DELETE | /article | 削除 | userId | string | ○ |  |  |
|  |  |  | timestamp | number | ○ |  |  |
|  |  |  |  |  |  |  |  |

### コラム機能

- snsテーブルに保存
- 内容をtokenありとなしで表示方法を変える

### Todoリストとリマインダー

- 時間余ったら

### APIの外部提供（アドバンス）

- 時間余ったら
