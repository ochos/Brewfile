# Zenn 公開基盤 セットアップ手順書

作成日: 2026-08-30
対象: 記事の無料公開と、Zenn Books で500円の技術書を販売するまで
調査根拠: [`../research/05-zenn-publishing.md`](../research/05-zenn-publishing.md)

---

## この手順書の使い方

- **上から順に、飛ばさずに実行する。**
- `$` で始まる行はターミナルに打つコマンド。`$` は打たない。**コマンドはそのままコピペできる。**
- **`{ }` で囲まれた部分だけ、自分の値に置き換える。**
- Git の操作は最小限（`add` / `commit` / `push` の3つ）しか出てこない。意味が分からなくても、書いてある通りに打てば動く。
- 詰まったら **STEP 9（トラブルシュート）** を見る。
- macOS を前提に書いている。Windows の場合の差分は各所に注記した。

**所要時間の目安**: STEP 1〜5（記事が公開できる状態）で 45〜60分。STEP 6〜8（本の販売開始）で 30分 + 執筆時間。

---

## STEP 0. 事前に用意するもの

| # | 必要なもの | 確認方法 |
|---|---|---|
| 0-1 | GitHub アカウント | https://github.com にログインできる |
| 0-2 | Zenn アカウント | https://zenn.dev にログインできる。**GitHub アカウントでログインするのが後の連携でラク** |
| 0-3 | ターミナル | macOS なら「ターミナル.app」。Windows なら PowerShell |
| 0-4 | 銀行口座（本を売る場合のみ） | 本人名義のもの。STEP 7 で登録する |

**Zenn アカウントをまだ作っていない場合**: https://zenn.dev/enter を開き、**GitHub でログイン**を選ぶ。ユーザー名（`https://zenn.dev/{ユーザー名}` になる）を決める。**このユーザー名は後から変えると全 URL が変わるので、慎重に決めること。**

---

## STEP 1. Node.js を用意する（必要バージョン: 22.12.0 以上）

`zenn-cli` の最新版（0.5.3 / 2026-08-26 公開）は **Node.js 22.12.0 以上**を要求する（`package.json` の `engines` で確認済み）。古い解説記事にある「Node 14 以上」は現在は誤り。

### 1-1. 今のバージョンを確認する

```bash
node -v
```

- `v22.12.0` 以上、または `v24.x` が出れば **STEP 2 へ進む**。
- `v20.x` 以下が出た、または `command not found` の場合は 1-2 へ。

### 1-2. Node.js を入れる（macOS / Homebrew）

```bash
brew install node@22
```

インストール後、パスを通す（Apple Silicon の場合）。

```bash
echo 'export PATH="/opt/homebrew/opt/node@22/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
node -v
```

Intel Mac の場合は `/opt/homebrew` を `/usr/local` に読み替える。

**Windows の場合**: https://nodejs.org/ から **LTS 版（22.x 以上）**のインストーラをダウンロードして実行する。終わったら PowerShell を開き直して `node -v` を確認する。

### 1-3. 確認

```bash
node -v    # v22.12.0 以上であること
npm -v     # 数字が出れば OK
```

---

## STEP 2. GitHub にリポジトリを作る

**重要: 有料本を書く予定があるので、必ず Private で作る。** Public にすると有料チャプターの原稿が誰でも読めてしまう。

1. ブラウザで https://github.com/new を開く
2. **「Repository name」** に `zenn-content` と入力する
3. **「Description」** は空でよい
4. **「Public / Private」** で **「Private」** を選ぶ ← **必ず**
5. **「Add a README file」のチェックは外したまま**にする（zenn-cli が README を作るため）
6. **「Add .gitignore」** は **None** のまま（zenn-cli が作る）
7. **「Choose a license」** は **None** のまま
8. 緑色の **「Create repository」** ボタンを押す

作成後に表示されるページの、`https://github.com/{あなたのGitHubユーザー名}/zenn-content.git` という URL をコピーしておく。

---

## STEP 3. ローカルに作業フォルダを作り、zenn-cli を入れる

以下をターミナルに**1行ずつ**貼り付けて実行する。`{あなたのGitHubユーザー名}` だけ置き換える。

```bash
mkdir -p ~/zenn-content
cd ~/zenn-content
git init
npm init --yes
npm install zenn-cli
npx zenn init
```

**`npx zenn init` が作るもの**（実装で確認済み）

```
~/zenn-content/
├── articles/       ← 記事を置く（.keep が入る）
├── books/          ← 本を置く（.keep が入る）
├── .gitignore      ← node_modules と .DS_Store が書かれている
└── README.md
```

続けて、GitHub リポジトリと紐づけて最初の push をする。

```bash
git add .
git commit -m "初期セットアップ"
git branch -M main
git remote add origin https://github.com/{あなたのGitHubユーザー名}/zenn-content.git
git push -u origin main
```

**認証を求められたら**: ユーザー名は GitHub のユーザー名、パスワードは **GitHub のログインパスワードではなく Personal Access Token**。作り方は STEP 9-A を参照。

**確認**: ブラウザで GitHub のリポジトリを開き、`articles` と `books` フォルダが見えていれば成功。

---

## STEP 4. Zenn と GitHub を連携する

1. ブラウザで https://zenn.dev にログインする
2. 右上のアイコンから **「ダッシュボード」** を開く
3. 左メニューの **「GitHubからのデプロイ」** を開く
4. **「リポジトリを連携する」** ボタンを押す
5. GitHub の App インストール画面に飛ぶ。アカウントを選ぶ
6. **「Only select repositories」** を選ぶ ← **「All repositories」を選ばないこと**
7. ドロップダウンから **`zenn-content`** を選ぶ
   - **連携できるリポジトリは最大2つ**とされている。3つ以上選ぶと連携に失敗する
8. **「Install」**（または「Save」）を押す
9. Zenn のダッシュボードに戻る。連携済みリポジトリの一覧に `zenn-content` が出ていれば成功
10. リポジトリの設定タブで、**同期対象ブランチが `main` になっていること**を確認する

**これ以降、`main` ブランチに push すると自動で Zenn に反映される。**

---

## STEP 5. 記事を1本、公開する

### 5-1. 記事ファイルを作る

```bash
cd ~/zenn-content
npx zenn new:article --slug osnr-calc-with-claude-code --title "Claude Codeで光ファイバのOSNR計算を自動化した" --type tech --emoji 🔦
```

`articles/osnr-calc-with-claude-code.md` が作られる。

**`--slug` のルール（必ず守る）**
- **英小文字・数字・ハイフン・アンダースコアのみ**
- **12文字以上50文字以下** ← `test` や `article1` は短すぎて弾かれる
- **この slug がそのまま記事の URL（`https://zenn.dev/{ユーザー名}/articles/{slug}`）になる。公開後に変えるとリンクが全部切れるので、最初に決めきる**

### 5-2. frontmatter を書く

ファイルの冒頭を、以下の形に整える。

```markdown
---
title: "Claude Codeで光ファイバのOSNR計算を自動化した"
emoji: "🔦"
type: "tech"
topics: ["claudecode", "python", "network"]
published: false
---

ここから本文
```

**各項目のルール（Zenn 公式実装で確認済み）**

| 項目 | ルール | よくあるミス |
|---|---|---|
| `title` | 必須・**70字以内** | 長すぎる |
| `emoji` | 必須・**絵文字ちょうど1つ** | 2つ入れる / 空にする |
| `type` | **`tech` か `idea` のみ** | `blog` などと書く |
| `topics` | **1〜5個**・各**18字以内**・**記号とスペース禁止** | `C++` と書く（正: `cpp`）、`C#`（正: `csharp`）、6個以上入れる |
| `published` | **`true` / `false`（クオートで囲まない）** | `published: "true"` と書いて型エラー |
| `published_at` | 任意。`YYYY-MM-DD` か `YYYY-MM-DD hh:mm`。**未来日時にするなら `published: true` が必須** | 予約投稿なのに `published: false` にしてしまう |

### 5-3. ローカルでプレビューする

```bash
cd ~/zenn-content
npx zenn preview
```

ブラウザで **http://localhost:8000** を開く（デフォルトポートは 8000）。
ファイルを保存すると自動でリロードされる。

- ポートを変えたいとき: `npx zenn preview --port 3000`
- ブラウザを自動で開きたいとき: `npx zenn preview --open`
- **止めるとき: ターミナルで `Ctrl + C`**

### 5-4. 公開前チェック（[`../research/05-zenn-publishing.md`](../research/05-zenn-publishing.md) の第5章の短縮版）

```
[ ] frontmatter の5項目にミスがない（上の表で照合した）
[ ] 勤務先・顧客名・社内システム名が本文とスクショに入っていない
[ ] APIキー・トークン・社内IP・実在ホスト名がコード中に残っていない
[ ] AIに書かせた部分の内容を自分で検証した（実際に動かした）
[ ] slug は「一生変えない」と言える
```

### 5-5. 公開する

`published: false` を **`published: true`** に書き換えて保存し、以下を実行する。

```bash
cd ~/zenn-content
git add .
git commit -m "記事を公開: OSNR計算の自動化"
git push
```

### 5-6. デプロイ結果を必ず確認する ← **飛ばさない**

**push が成功しても、Zenn 側の公開が成功したとは限らない。**

1. https://zenn.dev/dashboard/deploys を開く
2. 最新のデプロイが **成功** になっていることを確認する
3. 記事ページ（`https://zenn.dev/{あなたのユーザー名}/articles/{slug}`）を開いて表示を確認する

**反映されないときは STEP 9-C を見る。**

### 5-7. 投稿ペースの制限（重要）

Zenn には**公表されていない投稿レート制限**があるとされ、**直近24時間に5本以上投稿するとブロックされる**という報告が複数ある。しかも**エラー通知が出ず、静かに公開されない**。さらに**制限が明けても自動では再判定されず、新しいコミットを push し直す必要がある**。

> **ルール: 記事の投稿は 1日1本まで。まとめて一括投入しない。**
> これは Zenn のコミュニティガイドライン（「記事を乱造しない」）の方針とも一致する。

---

## STEP 6. 500円の本を作る

### 6-1. 本の雛形を作る

```bash
cd ~/zenn-content
npx zenn new:book --slug fiber-design-practice --title "光ファイバ設計の実務計算 12題" --price 500 --summary "OSNR・分散・非線形の実務計算を、Pythonの実装つきで12題ぶん解説します。"
```

`books/fiber-design-practice/` に `config.yaml` と `example1.md` `example2.md` が作られる。

**本の slug（＝ディレクトリ名）も、記事と同じく英小文字・数字・ハイフンの12〜50文字。URL になるので後から変えない。**

### 6-2. `config.yaml` を仕上げる

`books/fiber-design-practice/config.yaml` を開き、以下の形にする。

```yaml
title: "光ファイバ設計の実務計算 12題"
summary: "OSNR・分散・非線形の実務計算を、Pythonの実装つきで12題ぶん解説します。現場で使う数字の出し方を、手を動かして身につける本です。"
topics: ["network", "python", "光ファイバ"]
published: false
price: 500
chapters:
  - intro
  - osnr-basics
  - dispersion
  - nonlinear
  - summary
```

**全項目のルール（Zenn 公式実装で確認済み）**

| 項目 | 必須 | ルール |
|---|---|---|
| `title` | 必須 | 70字以内 |
| `summary` | **必須** | **1文字以上。空だと検証エラーになる。** 購入判断に直結するので手を抜かない |
| `topics` | 必須 | 1〜5個・各18字以内・記号とスペース禁止 |
| `published` | 必須 | `true` / `false`（クオートなし） |
| `price` | 有料時 必須 | **`0`（無料）または `200`〜`5000` かつ 100円単位**。**半角数字・クオートなし・カンマなし** |
| `chapters` | 任意だが必須級 | **文字列の一次元配列。`.md` を付けない。ここに書いたチャプターだけが Zenn に同期される** |

> ### price について（確認済みの結論）
> - 指定できる値は **`0`、または `200` 〜 `5000` の 100円刻み**（`200, 300, 400, **500**, 600, ..., 5000`）
> - **`price: 500` は有効。** この案件の「500円の技術書」はそのまま作れる
> - **NG例**: `price: "500"`（クオート → 型エラー）、`price: 1,000`（カンマ → エラー）、`price: 150`（下限未満）、`price: 550`（100円刻みでない）

### 6-3. チャプターファイルを作る

`config.yaml` の `chapters` に書いた slug と**同じ名前**の `.md` を、本のディレクトリ直下に作る。

```bash
cd ~/zenn-content/books/fiber-design-practice
rm example1.md example2.md
touch intro.md osnr-basics.md dispersion.md nonlinear.md summary.md
```

**チャプター slug のルール**
- 英小文字・数字・ハイフン・アンダースコアの **1〜50文字**（記事と違い、12文字未満でもよい）
- `1.intro.md` のような**数字プレフィックス形式**も使えるが、**`config.yaml` の `chapters` で順番を指定する方式を推奨する**（章の入れ替えでファイル名＝URL を変えずに済むため）

**並び順の決まり方**（実装で確認済み）
1. `config.yaml` の `chapters` に書いた順（**これが最優先。推奨**）
2. 書いていない場合は、ファイル名 `数字.slug.md` の数字順
3. どちらでもないチャプターは「999番目」扱いで末尾に回る

### 6-4. **試し読み（無料公開チャプター）を設定する ← 購入率を左右する**

**設定場所は `config.yaml` ではない。各チャプターの Markdown ファイルの frontmatter に書く。**

`intro.md` の冒頭:

```markdown
---
title: "はじめに — この本で何ができるようになるか"
free: true
---

本文...
```

`osnr-basics.md` の冒頭:

```markdown
---
title: "第1章 OSNRを手計算で出す"
free: true
---

本文...
```

有料にする章（`dispersion.md` など）は `free` を**書かない**。

```markdown
---
title: "第2章 波長分散の見積もり"
---

本文...
```

**ルール**
- `free: true` の章は、**本を買っていない人でも全文読める**
- `free` を書かない章は**有料**
- **`free: "true"`（クオート付き）は型エラー。** 真偽値で書く
- 本の `price` が `0` のときは `free` の指定は無視される

**500円の本で購入率を最大化する試し読み設計（推奨）**

| 章 | `free` | 役割 |
|---|---|---|
| はじめに（誰向けか / 何ができるようになるか / 前提知識） | **true** | 「自分向けの本か」を判定させる。ミスマッチをここで弾くと低評価が減る |
| 第1章（1つのテーマを**最後まで完結**させる実践章） | **true** | **購入判断の核心。** 「この粒度と文体で残りも書かれている」と示す。目次だけ見せても買われない |
| 第2章以降 | 指定なし | 本体 |
| まとめ・付録 | 指定なし | |

**設計の原則**: **無料章を読み終えた時点で、読者が「1つ成果を得ていて」かつ「次の壁にぶつかっている」状態を作る。**
- 導入だけ無料 → 価値が測れず離脱する
- 無料章で全部解決 → 買う理由が消える
- **正解は「1つ解決 → 応用でつまずく点を提示 → その解決は第2章」**

### 6-5. 表紙画像を置く

- **サイズ: 500 × 700 px**（比率 1:1.4。最終的にこのサイズにリサイズされる）
- **ファイルサイズ: 1MB 以内**
- ファイル名: **`cover.png`**（`cover.jpg` でも可）
- 置き場所: `books/fiber-design-practice/cover.png`

置かないと「本のカバー画像を /books/{slug} ディレクトリに配置してください」という検証エラーが出る。

### 6-6. プレビューで確認する

```bash
cd ~/zenn-content
npx zenn preview
```

http://localhost:8000 で本を開き、**以下を必ず確認する**。

```
[ ] チャプターが意図した順に並んでいる
[ ] free: true にした章だけが無料表示になっている
[ ] 有料にすべき章に free: true を付け忘れていない
[ ] 表紙が表示されている
[ ] price が 500 になっている
[ ] 無料章だけを読んだ状態で「買いたくなるか」を自分で音読して判定した
```

---

## STEP 7. 販売の準備（口座登録と、確認すべきこと）

> **この STEP の情報は zenn.dev への直接アクセスが遮断されていたため未確認である。実際の画面を見て、[`../research/05-zenn-publishing.md`](../research/05-zenn-publishing.md) の第7章の表を埋めること。**

### 7-1. 振込先口座を登録する

1. https://zenn.dev/dashboard を開く
2. 設定（または「売上」「振込」）から、**振込先口座の登録**画面を開く
3. 本人名義の銀行口座情報を入力する
4. **このとき、本人確認書類（免許証・マイナンバー等）の提出を求められるかどうかを確認し、調査ファイルに追記する**

### 7-2. 公開前に、自分の目で確認すべき3ページ

| URL | 確認すること |
|---|---|
| https://zenn.dev/faq/sales | 手数料が「決済 3.6% → 残額に 10%」か。振込手数料 350円 / 最低残高 1,000円 / 5ヶ月ルールが正しいか |
| https://zenn.dev/terms/transaction-law | **著者個人の住所・氏名・電話番号を開示する必要があるか**（顔出しNGの制約に直結） |
| https://zenn.dev/terms と https://zenn.dev/guideline | 記事末尾に本への導線を置いてよい範囲。AI 執筆の扱い |

### 7-3. お金の見込み（500円の本の場合）

| 項目 | 金額 |
|---|---|
| 販売価格 | 500円 |
| 決済手数料 3.6% | −18円 |
| Zenn 利用料 10%（決済手数料を引いた残額に対して） | −48円 |
| **1冊あたりの受取額** | **約433円** |

- **月商1,000円（500円 × 2冊）の実際の手取りは約867円。**
- **振込は申請ベースで、1回 350円が引かれる。現金で受け取るには残高1,000円以上が必要。**
- → **毎月出金してはいけない。** 数ヶ月ためて1回で申請する。
- → ただし**確定日から5ヶ月以内に申請しないと Amazon ギフト券に切り替わる**ので、放置しすぎない。

---

## STEP 8. 本を公開して販売を開始する

### 8-1. 最終チェック

```
[ ] リポジトリが Private になっている（有料原稿が公開されていない）
[ ] config.yaml の summary を書いた（空だとエラー）
[ ] price: 500（クオートなし、カンマなし）
[ ] chapters に全チャプターを正しい順で列挙した。.md 拡張子は付けていない
[ ] 書きかけの章が chapters に紛れ込んでいない
[ ] cover.png（500×700px / 1MB以内）を置いた
[ ] 導入章と第1章に free: true を入れた
[ ] 有料章に free: true を付けすぎ / 付け忘れしていない
[ ] 全チャプターを通しで読み直した（有料で売る以上の正確性があるか）
[ ] 手順を書いた章は、まっさらな環境で実際に通して動くことを確認した
[ ] 勤務先・顧客名・機密情報が入っていない
[ ] 振込先口座を登録した
[ ] STEP 7-2 の3ページを自分の目で確認した
```

### 8-2. 公開する

`config.yaml` の `published: false` を **`published: true`** に書き換えて保存する。

```bash
cd ~/zenn-content
git add .
git commit -m "本を公開: 光ファイバ設計の実務計算 12題（500円）"
git push
```

### 8-3. 公開後の確認 ← **飛ばさない**

1. https://zenn.dev/dashboard/deploys でデプロイ成功を確認する
2. **ブラウザのシークレットウィンドウ（＝ログアウト状態）**で本のページを開く
3. **無料章だけが読めて、有料章にはロックがかかっていることを目視で確認する** ← ここを間違えると本文が全部タダで読まれる
4. 価格が 500円と表示されていることを確認する

**事前審査はない。** デプロイが完了した時点で販売開始になる。

---

## STEP 9. トラブルシュート

### 9-A. `git push` でパスワードを聞かれて弾かれる

GitHub はパスワード認証を廃止している。**Personal Access Token** を作る。

1. https://github.com/settings/tokens を開く
2. **「Generate new token」→「Generate new token (classic)」**
3. **Note**: `zenn-content`
4. **Expiration**: 90 days など
5. **Select scopes**: **`repo`** にチェック
6. **「Generate token」** を押し、表示された文字列（`ghp_...`）を**その場でコピー**（二度と表示されない）
7. `git push` でパスワードを聞かれたら、**そのトークンを貼り付ける**

毎回聞かれるのが面倒なら、一度だけ以下を実行して保存する。

```bash
git config --global credential.helper store
```

（macOS なら `osxkeychain` でもよい）

### 9-B. `npx zenn` が動かない / バージョンが古い

```bash
cd ~/zenn-content
node -v                      # v22.12.0 以上か
npm install zenn-cli@latest  # 最新版に更新
npx zenn --version
```

### 9-C. push したのに Zenn に反映されない

**上から順に確認する。**

1. **https://zenn.dev/dashboard/deploys を開く** — デプロイが失敗していないか。失敗ならエラー内容を読む
2. **frontmatter のエラーではないか** — `npx zenn preview` をローカルで開くと、検証エラーが赤字で表示される。よくあるのは topics に記号（`C++`）、`published: "true"`（クオート）、slug が12文字未満
3. **`published: true` になっているか**
4. **`config.yaml` の `chapters` に、そのチャプターの slug を書いたか** — **書いていないチャプターは同期されない**
5. **push したブランチが `main` か** — `git branch` で確認。Zenn 側の設定ブランチと一致しているか
6. **投稿レート制限に引っかかっていないか** — 直近24時間に5本以上投稿していないか。該当する場合、**約24時間待ったうえで「新しいコミット」を push し直す**必要がある（待つだけでは再判定されない）

```bash
# 空コミットで再デプロイを促す
git commit --allow-empty -m "再デプロイ"
git push
```

### 9-D. ローカルのプレビューが表示されない

- ポート 8000 が他のプロセスに使われている → `npx zenn preview --port 3001`
- `Ctrl + C` で止めてから再実行する
- コマンドを実行する場所が `~/zenn-content`（`articles/` と `books/` がある階層）になっているか確認する

### 9-E. うっかり機密情報を push してしまった

**Git 履歴から消しても、GitHub にアップロードされた時点で流出したものとして扱う。**

1. **該当する API キー・トークンを、発行元で即座に無効化（revoke）する** ← 最優先
2. その後にファイルを修正して push し直す
3. リポジトリが Private であっても、この順序は変えない

---

## 付録A. 毎日使うコマンドはこれだけ

```bash
# 作業フォルダに移動
cd ~/zenn-content

# 新しい記事を作る（slugは12文字以上）
npx zenn new:article --slug my-new-article-slug --title "タイトル" --type tech

# プレビューする（http://localhost:8000）
npx zenn preview

# 公開する（3行セット）
git add .
git commit -m "何をしたかを一言で"
git push
```

**この3行が Git 操作の全部である。** ブランチもマージもプルリクも要らない。
分からなくなったら Claude Code に **「zenn-content を commit して push して」** と言えばよい。

## 付録B. Claude Code に執筆させるときの指示のコツ

- **「`~/zenn-content/articles/{slug}.md` に、frontmatter 付きで記事を書いて」**と、パスと形式を明示する
- **frontmatter のルール（topics は記号禁止、slug は12文字以上、published は真偽値）を毎回伝える**か、リポジトリの `CLAUDE.md` に書いておく
- **書かせたあと、必ず自分でコードを動かして検証する。** Zenn のガイドラインは「内容の正確性を確認せずに投稿すること」を明確に戒めている
- **社名・顧客名・社内システム名が残っていないか、公開前に必ず自分で grep する**

```bash
cd ~/zenn-content
grep -rniE "(勤務先の社名|顧客名|社内システム名)" articles/ books/
```

## 付録C. 「やってはいけない」まとめ

| やってはいけないこと | 理由 |
|---|---|
| 有料本のリポジトリを Public にする | 原稿が誰でも読める |
| 記事を1日に5本以上まとめて push する | 非公開レート制限で静かにブロックされる |
| slug（記事・本・チャプター）を公開後に変える | URL が変わり、全リンクが切れる |
| `price: "500"` とクオートで書く | 型エラーで公開されない |
| topics に `C++` `C#` など記号を入れる | 検証エラー（正: `cpp` `csharp`） |
| push しただけで公開されたと思い込む | デプロイが失敗していても通知されない |
| 毎月出金申請する | 1回350円で、月2冊分の手取りの4割が消える |
| 出金申請を5ヶ月以上放置する | Amazon ギフト券に自動で切り替わる |
| AI の出力を検証せずに公開する | ガイドライン違反かつ、有料本では信用を失う |
| 記事本文を薄くして本の宣伝を主目的にする | 「広告を主目的とする記事」として規約違反になりうる |
