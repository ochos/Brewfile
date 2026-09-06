# 04. 技術・運用設計 — 一人 × 低コスト × Claude Code で売れるものを作る

作成日: 2026-08-29 / 担当: 技術・運用設計
前提: 日本在住個人、平日夜1〜2h + 週末数時間、インフラ月額1,000円以内（できれば無料枠のみ）、月商1,000円 → 1万円 → 10万円

---

## 0. この文書の価格情報について（重要）

**確認方法の制約**: 本セッションのネットワーク送信ポリシーにより、`developers.cloudflare.com` / `vercel.com` / `stripe.com` / `supabase.com` / `resend.com` 等への**直接アクセス（WebFetch・curl）は遮断**されている。したがって本文の数値は **ウェブ検索経由で公式ページの内容を参照した結果（確認時点: 2026年8月29日）** であり、一次情報URLは併記するが「公式ページを自分の目で開いて確認した」レベルではない。

**運用ルール**:
- 金額が意思決定を左右する箇所（月次固定費が発生する契約、超過課金）は、**着手前に必ず下記URLを自分のブラウザで開いて再確認**すること。
- 為替は **1 USD = 155円** で概算（2026年8月時点の想定値。**実レートは未確認**）。ドル建てサービスは為替で±20%動く前提で見積もる。
- 本文中で確度が低いものには **［要確認］** または **［未確認］** を明記した。

| サービス | 一次情報URL |
|---|---|
| Cloudflare Workers 料金 | https://developers.cloudflare.com/workers/platform/pricing/ |
| Cloudflare D1 料金 | https://developers.cloudflare.com/d1/platform/pricing/ |
| Cloudflare Pages 制限 | https://developers.cloudflare.com/pages/platform/limits/ |
| Vercel Hobby プラン | https://vercel.com/docs/plans/hobby |
| Supabase 料金 | https://supabase.com/pricing |
| Neon 無料枠 | https://neon.com/faqs/free-plan-limits-and-quotas |
| Turso 料金 | https://turso.tech/pricing |
| Clerk 料金 | https://clerk.com/pricing |
| Resend 料金 | https://resend.com/pricing |
| Amazon SES 料金 | https://aws.amazon.com/ses/pricing/ |
| Stripe 料金（日本） | https://stripe.com/jp/pricing |
| GitHub Actions 課金 | https://docs.github.com/en/billing/concepts/product-billing/github-actions |
| Claude プラン | https://claude.com/pricing |
| Sentry 料金 | https://sentry.io/pricing/ |
| UptimeRobot 料金 | https://uptimerobot.com/pricing/ |

---

## 1. 技術スタックの推奨

### 結論を先に

> **パターンA（Cloudflare 一本足）を推す。** 迷ったらこれ。
> 理由: (1) 無料枠が「月あたり」ではなく「日あたり」でリセットされ、事故っても翌日回復する、(2) 従量課金の下限が月$5と低く、無料→有料の段差が小さい、(3) ホスティング・DB・KV・ストレージ・DNS・ドメインが1社に閉じるので、一人運営の「管理面の数」が最小になる、(4) **Vercel Hobby は商用利用が禁止**なので、無料枠で課金サービスを回すという選択肢がそもそも取れない。

パターンB・Cは「Aが合わない場合の代替」として提示する。3つ全部を試すのは時間の無駄なので、**最初の1本はAで、Aで詰まったらBへ**というのが正しい順序。

---

### パターンA（推奨・最小構成）: Cloudflare フルスタック

| 層 | 選定 | 理由 |
|---|---|---|
| フレームワーク | **Hono**（サーバーサイドJSXでHTML返す） | ビルドが速く、Workersにネイティブ。SPAを作らないので実装量が1/3になる |
| ホスティング | **Cloudflare Workers**（静的アセット同梱） | 無料枠 100,000 req/日 |
| DB | **Cloudflare D1**（SQLite） | 無料枠 5GB / 500万行読/日 / 10万行書/日 |
| 認証 | **自前マジックリンク**（署名付きトークン + HttpOnly Cookie セッション） | パスワードを持たない = 漏洩リスクと実装量が同時に減る。外部SaaS費用ゼロ |
| 決済 | **Stripe Checkout + Billing Customer Portal** | 決済画面・解約画面・領収書を全部Stripe側に置ける |
| メール | **Resend** | 無料 3,000通/月（100通/日）。DKIM設定がGUIで済む |
| 監視 | Sentry Developer（無料） + UptimeRobot（無料） | 後述 |

**無料枠だけでどこまで持つか（数字）**

| 制約 | 無料枠 | 換算（1ユーザー1日30リクエスト、1リクエスト平均5行読み込みと仮定） | 超えたときの課金 |
|---|---|---|---|
| Workers リクエスト | 100,000 req/**日** | **約 3,300 DAU**（MAU換算で概ね1万前後） | Paid $5/月（≒775円）で1,000万req込み、超過$0.30/百万req ［要確認: 込み枠の正確な数値］ |
| Workers CPU時間 | 10ms/リクエスト（無料） | DB1〜2クエリ + HTML生成なら十分収まる。重い処理は不可 | Paid で 3,000万 CPU-ms 込み、超過 $0.02/百万ms |
| D1 行読み込み | 5,000,000 行/**日** | 100,000 req × 5行 = 50万行 → **10倍の余裕** | Paid 250億行読/月込み、超過 $0.001/百万行 ［要確認］ |
| D1 行書き込み | 100,000 行/**日** | 書き込みは読み込みの1/20程度が普通 → 余裕 | 同上 |
| D1 ストレージ | 5GB（無料プランは1DBあたり500MB、最大10DB） | 数万ユーザー分のメタデータなら余裕 | — |
| Resend | 3,000通/月・**100通/日** | ここが**最初に詰まる**。1日100通 = サインアップ + 通知の合計 | 有料は $20/月〜［未確認］。または Amazon SES へ逃がす（$0.10/1,000通 ≒ 15円/1,000通） |
| Cloudflare Pages（LP用） | 500ビルド/月、帯域無制限 | 週5デプロイでも余裕 | — |

> **実務上の律速は Resend の「100通/日」**。マジックリンクを使う設計だとログインのたびにメールが飛ぶので、有料100人規模で1日100通に接近する。対策は後述（セッション長期化 + SES併用）。

**代表的なつまずき**: Workers の無料CPU制限10ms は「壁時計時間」ではなく実CPU時間なので、DB待ちやfetch待ちは加算されない。テンプレート描画やJSONの巨大なパースが重い場合だけ問題になる。

---

### パターンB（バランス型）: Next.js + マネージドDB

Reactのエコシステム（UIコンポーネント、Claude Codeが最も学習量を持っている領域）を使いたい場合。

| 層 | 選定 | 無料枠 |
|---|---|---|
| フレームワーク | **Next.js (App Router)** | — |
| ホスティング | **Cloudflare Workers（OpenNext経由）** ※Vercelは後述の理由で不可 | Workers 無料枠と同じ |
| DB | **Supabase**（Postgres + Auth + Storage） | DB 500MB / Auth 50,000 MAU / egress 5GB / ストレージ500MB / プロジェクト2つ |
| DB代替 | **Neon**（Postgres） | 0.5GB/プロジェクト、**100 CU-hours/月**、転送5GB |
| DB代替 | **Turso**（SQLite） | 5GBストレージ、月5億行読/1,000万行書、DB 100個 |
| 認証 | **Supabase Auth**（DBと同居） or **Clerk** | Clerkは無料 50,000 MRU（2026-02-05に10,000 MAU→50,000 MRUへ拡大）。有料Proは$25/月 |

**⚠️ Vercel Hobby は使えない**: Hobby プランは **非商用・個人利用限定**で、商用利用には Pro（$20/月 ≒ 3,100円）が必須。無料枠 100GB転送・100万関数実行はあるが、**課金サービスを載せた時点で規約違反**になる。「無料枠で始めて売上が立ったら払う」が成立しないので、本件の前提とは合わない。Netlifyも同様に無料プランの商用可否は［要確認］。

**⚠️ Neon 無料枠の落とし穴**: 100 CU-hours/月 は、最小の 0.25 CU インスタンスで常時稼働換算 **約400時間/月**（月は730時間）。scale-to-zero（アイドル時に自動停止）が効かない＝定期的にアクセスがある本番サービスだと、**月の途中で枯渇する**。cronで死活監視を打つと確実に枯渇する。

**⚠️ Supabase 無料枠の落とし穴**: **1週間アクセスがないとプロジェクトが自動一時停止**され、手動復旧が必要。ローンチ直後の「誰も来ない期間」に止まる。Uptime監視を当てておけば実質回避できるが、規約上のグレー領域なので過度に依存しない。

**判断**: BのDBは **Turso が最も無料枠が素直**（日次リセットではなく月次だが上限が大きく、scale-to-zeroの罠がない）。Postgresが必須でないなら Turso、認証もまとめて任せたいなら Supabase。

---

### パターンC（ノーコード寄り・最速）: 静的LP + Stripe Payment Links

**「デジタル商品（テンプレート、PDF、Notionテンプレ、プロンプト集、CSVデータ）を売る」なら、そもそもアプリを作る必要がない。**

| 層 | 選定 | コスト |
|---|---|---|
| サイト | **Astro** → Cloudflare Pages（静的） | 無料 |
| 決済 | **Stripe Payment Links**（コード0行）or Checkout | 手数料のみ |
| 商品配信 | Stripe の「購入後リダイレクト先」を署名付きURLにする / メール添付 / Cloudflare R2 の期限付きURL | 無料〜 |
| 顧客管理 | Stripe ダッシュボードのみ（自前DBなし） | 無料 |

- **サーバーもDBも認証も存在しない**ので、障害もセキュリティインシデントも起きようがない。
- 月商1,000円という最初の目標に**最短で到達する**のはこれ。土日1日で出せる。
- 弱点: サブスク（継続課金）に向かない、単価が上がりにくい、差別化しにくい。
- **推奨する使い方**: パターンCで「売れるかどうか」を1〜2週間で検証してから、パターンAで本体を作る。Cは捨てる前提の実験台。

---

### 選定サマリ

| | A: Cloudflare | B: Next.js + マネージド | C: 静的 + Payment Link |
|---|---|---|---|
| 初回リリースまで | 2週間 | 3〜4週間 | 1〜2日 |
| 完全無料で回せるか | ✅ 回せる | △ Neon/Supabaseの罠あり | ✅ 回せる |
| 月商10万円時の固定費 | 約 1,000円 | 約 4,000〜8,000円 | 約 160円 |
| サブスク適性 | ◎ | ◎ | ✕ |
| Claude Code との相性 | ◎（依存が少なく生成が安定） | ○（Next.jsの世代差でハルシネーション起きやすい） | ◎ |
| **推奨度** | **本命** | Reactが必要なら | 検証用・単発商品用 |

---

## 2. コスト表と損益分岐点

**共通の前提**
- 商品: 月額 **500円**のサブスク（税込）
- Stripe手数料: 国内カード **3.6%** + Stripe Billing（サブスク管理）**+0.7%** = **4.3%** ［要確認: 消費税の扱い。「3.6%に消費税10%が乗って実効3.96%」とする解説が複数あるが、Stripe公式での確認が取れていない。**保守的に実効5%で見積もる**のが安全］
- 為替 1 USD = 155円［未確認］
- ドメイン: `.com` を Cloudflare Registrar で年 $11.84 ≒ 1,835円 → **月 160円**［要確認: $4.82 という記載も見られ、TLD・年度で変動］
- **自社プロダクトにAI機能を載せない**前提（載せる場合は後述）

### 段階別 月額コスト内訳

| 費目 | 月商 0円 | 月商 1,000円<br>(有料2人) | 月商 1万円<br>(有料20人) | 月商 10万円<br>(有料200人 / MAU約2,000) |
|---|---:|---:|---:|---:|
| ドメイン（.com 按分） | 160 | 160 | 160 | 160 |
| ホスティング（CF Workers） | 0 | 0 | 0 | 775（Paid $5・保険） |
| DB（D1） | 0 | 0 | 0 | 0（Paid枠内） |
| メール | 0（Resend Free） | 0 | 0 | 3,100（有料 $20相当）［未確認］ |
| 監視（Sentry / UptimeRobot） | 0 | 0 | 0 | 0 |
| CI（GitHub Actions） | 0 | 0 | 0 | 0 |
| **Stripe手数料（4.3%）** | 0 | 43 | 430 | 4,300 |
| **インフラ小計** | **160** | **203** | **590** | **8,335** |
| — | | | | |
| Claude Code（Pro $20） | 3,100 | 3,100 | 3,100 | 3,100 |
| **総支出** | **3,260** | **3,303** | **3,690** | **11,435** |
| **営業利益** | **▲3,260** | **▲2,303** | **+6,310** | **+88,565** |

> **月商10万円で Claude Code を Max 5x（$100 ≒ 15,500円）に上げても、利益は約76,000円で黒字**。ツール代をケチる局面ではない。

### 「インフラ月1,000円以内」という制約について

**インフラ小計は月商1万円まで590円で収まる。制約は余裕でクリアできる。**
唯一の大きな固定費は **Claude Code の Pro プラン（$20/月 ≒ 3,100円）** で、これは「インフラ費」ではなく**開発ツール費**。Claude Code は Pro / Max プランに含まれ、無料プランでは使えないため、この3,100円は本件の実質的な最低ランニングコストになる。これを「制約に含めるか」は本人判断だが、**含めない整理を推奨**する（PCや電気代と同じカテゴリ）。

### 損益分岐点（500円プラン、粗利 = 500 × (1 - 0.043) = 478円/人）

| 何を賄うか | 月額固定費 | 必要有料ユーザー数 |
|---|---:|---:|
| インフラのみ（ドメイン+送信） | 160円 | **1人**（初日に達成可能） |
| インフラ + Claude Code Pro | 3,260円 | **7人** |
| インフラ + Claude Code Max 5x | 15,660円 | **33人** |
| 上記 + 「時給2,000円 × 月30時間」の機会費用 | 63,260円 | **133人** |

**読み方**: 「月商1,000円」の目標は有料2人で達成、これは**技術的にはほぼ何のコストもかからない**。ボトルネックはインフラではなく**集客**。したがって技術選定に時間を溶かすのは合理的でない ── だからこそパターンAで即決すべき。

### 自社プロダクトにAI機能を載せる場合の追加コスト

Claude API の従量課金（2026年6月時点のキャッシュ値）:

| モデル | 入力 $/1M tok | 出力 $/1M tok |
|---|---:|---:|
| Claude Opus 5 (`claude-opus-5`) | $5.00 | $25.00 |
| Claude Sonnet 5 (`claude-sonnet-5`) | $2.00 | $10.00 |
| Claude Haiku 4.5 (`claude-haiku-4-5`) | $1.00 | $5.00 |

一次情報: https://claude.com/pricing （API料金は https://www.anthropic.com/pricing ）

**概算**: 1リクエストあたり入力2,000tok・出力500tokを Sonnet 5 で処理 → $0.004 + $0.005 = **約1.4円/回**。500円プランで月100回まで使わせるなら原価140円/人 = 粗利率が478円→338円に落ちる。

**AI機能を載せるなら必須の3点**:
1. **プロンプトキャッシュ**を必ず使う（システムプロンプトを固定して `cache_control` を置く）。長いシステムプロンプトのコストが桁で落ちる。
2. **1ユーザーあたりの月間実行回数に上限**を設ける。無制限にすると原価が青天井になる。
3. **Anthropic Console 側で使用量上限（spend limit）を設定**する。バグやスクレイピングで一晩で数万円が飛ぶ事故を防ぐ。

> **MVPではAI機能を載せないことを強く推奨**。原価管理・レイテンシ・出力品質のブレという3つの難問が一度に増える。まず「AIなしで金を取れるか」を検証する。

---

## 3. Claude Code を最大限使う開発フロー

### 3.1 CLAUDE.md の設計指針

CLAUDE.md は**毎ターン読まれるコンテキスト**なので、「長い正しい文書」より「短い効く文書」が価値を持つ。**200行を超えたら削る**。

**書くべきこと（優先順）**

```markdown
# プロジェクト名

## これは何か
1文。「〇〇する人向けの、〇〇するサービス」。

## 絶対のルール
- 新しい依存パッケージを追加する前に必ず確認を取る（無料枠設計が壊れるため）
- DBスキーマ変更は migrations/ にSQLファイルを追加する。既存ファイルは編集しない
- 個人情報はメールアドレス以外を保存しない
- 本番シークレットは wrangler secret のみ。.env をコミットしない

## コマンド
- 開発: npm run dev
- テスト: npm test
- 型チェック: npm run typecheck
- デプロイ: npm run deploy

## ディレクトリの意味
src/routes/   ... HTTPハンドラ。1ファイル1機能
src/db/       ... クエリ関数。SQLはここ以外に書かない
src/lib/      ... 純粋関数のみ。副作用を持たせない

## やらないこと（スコープ外）
- チーム機能 / 権限管理 / 多言語対応 / モバイルアプリ
- 管理画面（Cloudflareダッシュボードと直SQLで足りる）
```

**書いてはいけないこと**
- 一般的なコーディング規約（「変数名は意味のある名前に」等）── モデルは既に知っている、トークンの無駄
- 頻繁に変わる情報（現在のタスク、TODO）── ここではなく Issue や `docs/` に置く
- ディレクトリ構造の全ファイル列挙 ── 自動で探索できる

**運用**: 「同じ指摘を Claude Code に2回した」ら、その瞬間 CLAUDE.md に1行追加する。それ以外では触らない。

### 3.2 サブエージェント / スキルの活用

一人開発で効くのは以下の3つだけ。全部作ろうとしない。

| 使うもの | 何のために | 作り方 |
|---|---|---|
| **`/security-review`（標準スキル）** | 実装が一段落するたびに脆弱性を洗う | 標準で入っている。使うだけ |
| **`/code-review`（標準スキル）** | 週末にまとめて書いたコードの品質チェック | 標準で入っている |
| **自作スキル1つ: `ship`** | 「型チェック → テスト → ビルド → デプロイ → 疎通確認」を1コマンドに | `.claude/skills/ship/SKILL.md` に手順を書くだけ |

**サブエージェント（Task tool）の使いどころ**: 「調査だけで大量のファイルを読む作業」（例: 「この機能に関係するファイルを全部探して」）をサブエージェントに投げると、メインの会話にコンテキストを汚さずに済む。**逆に、実装そのものをサブエージェントに投げるのは一人開発では非推奨** ── レビューできない量のコードが一度に出てくる。

### 3.3 テストの自動化

**書くテストは3種類だけに絞る。カバレッジは追わない。**

| 種類 | 対象 | 目安 |
|---|---|---|
| **課金ロジックのユニットテスト** | 「このユーザーは有料機能を使えるか」の判定関数 | 必須。ここがバグると金の問題になる |
| **Webhook ハンドラのテスト** | Stripe イベントのJSONを固定ファイルで用意して流す | 必須。本番でしか起きないバグの温床 |
| **主要導線のスモークテスト** | サインアップ → ログイン → ダッシュボード表示 の HTTP レベル | 各1本 |

書かなくていいもの: UIコンポーネントのテスト、getterのテスト、外部SDKのモックが必要なテスト。

**Claude Code への指示の型**:
> 「`canUseFeature()` のテストを書いて。以下の6ケースを網羅: 未課金 / trialing / active / past_due / canceled かつ期間内 / canceled かつ期間外。実装は変更しないで、テストだけ。」

「テストを書いて」だけだと網羅性のないテストが大量に出るので、**ケースを列挙して渡す**。

### 3.4 最小限のCI（GitHub Actions 無料枠）

**無料枠**: GitHub Free で **プライベートリポジトリ 2,000分/月**。パブリックリポジトリは標準ランナーなら無制限。
一次情報: https://docs.github.com/en/billing/concepts/product-billing/github-actions

```yaml
# .github/workflows/ci.yml
name: ci
on:
  pull_request:
  push:
    branches: [main]

concurrency:                       # 連続pushで古いジョブを殺す = 分数節約
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  check:
    runs-on: ubuntu-latest
    timeout-minutes: 5             # 暴走ジョブで枠を溶かさない保険
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm run typecheck
      - run: npm test
      - run: npx gitleaks detect --no-git -v || true   # シークレット混入検知
```

**予算計算**: 1回2分 × 月100回 = 200分 → 無料枠2,000分の **10%**。全く問題にならない。
**デプロイはCIから自動化しない**。`npm run deploy` を手で叩く。一人なので承認フローは不要だし、CIにデプロイ権限のあるトークンを置くとそれ自体がリスクになる。

**ブランチ保護**: `main` に「CI通過を必須」を設定する。自分1人でも設定する ── 深夜に壊れたコードを直push する自分から自分を守るため。

### 3.5 「作りすぎ」を防ぐスコープ管理の型

個人開発の最大の失敗要因は技術力でも集客でもなく、**リリース前に機能を増やし続けて力尽きること**。以下を機械的に運用する。

**① 「1画面1機能」ルール**
新しい画面を作りたくなったら、既存の画面に置けないか3分考える。置けるなら置く。MVPの画面数は**5枚**（後述）を上限とする。

**② 「Not Doing リスト」を CLAUDE.md に書く**
やらないことを明文化すると、Claude Code が勝手に実装するのも防げる。思いついた機能は削除せず `docs/backlog.md` に流す（捨てると「もったいない」感情が働いて実装してしまうため、**捨てずに寝かせる**）。

**③ 2週間タイマー**
着手日から14日後の日付をリポジトリのREADME先頭に書く。その日に、**できている範囲でリリースする**。「あと1機能だけ」を1回でも許すと無限に伸びる。

**④ 「課金導線に繋がるか」テスト**
新機能を実装する前に自問: **「これがないと客は金を払わないか？」** NOなら backlog 行き。設定画面のダークモード、プロフィール画像アップロード、通知設定 ── 全部NO。

**⑤ Claude Code への防御的な指示**
CLAUDE.md に以下を入れる:
```
実装依頼に対して、依頼されていない機能・設定項目・エラーハンドリング以外の
「あると便利な機能」を追加しないこと。必要だと思ったら提案だけして実装しない。
```
これがないと、「ログイン機能を作って」で 2FA とパスワードリセットとレート制限とアカウントロックが付いてくる。

### 3.6 AI生成コードのセキュリティレビュー観点

Claude Code が書いたコードは**動くが、脅威モデルを知らない**。以下は毎リリース前に機械的に確認する。実装が一段落したら `/security-review` を回し、その上で人間が下記を目視する。

#### (1) シークレット管理
- [ ] `.env` / `.dev.vars` が `.gitignore` に入っているか
- [ ] 本番シークレットは `wrangler secret put` のみ（`wrangler.toml` の `[vars]` に書かない ── **あそこはリポジトリにコミットされる平文**）
- [ ] Stripe の**シークレットキー（`sk_live_`）がクライアントに渡るコードパスがないか**。Claude Code は SSR とクライアントの境界を間違えることがある
- [ ] `gitleaks` をCIに入れる（上記ymlに記載済み）
- [ ] エラーレスポンスにスタックトレースや環境変数を含めていないか

#### (2) 認可漏れ（最頻出・最重大）
**AI生成コードで最も多いのが「認証はあるが認可がない」**。ログイン済みかは見ているが、**そのリソースがそのユーザーのものか**を見ていない。

- [ ] すべてのDBクエリの `WHERE` 句に `user_id = ?` が入っているか。**`getItem(id)` ではなく `getItem(userId, id)` を関数シグネチャの強制にする**
- [ ] 「有料ユーザーのみ」の判定を**クライアント側だけでやっていないか**（ボタンを隠すのは認可ではない）
- [ ] URLのIDを他人のIDに書き換えて手で試す（IDOR / 水平権限昇格）。これは実際にブラウザで1回やる
- [ ] Webhookエンドポイントに**署名検証**があるか（`stripe.webhooks.constructEvent`）。ないと誰でも「課金完了」を偽装できる

#### (3) レート制限
- [ ] **メール送信を伴うエンドポイント**（マジックリンク要求、問い合わせ）に IP + メールアドレス単位のレート制限があるか。**ないと Resend の1日100通を他人に溶かされる**（コストの直接被害）
- [ ] ログイン試行のレート制限
- [ ] Cloudflare の WAF / Rate Limiting Rules を無料枠で1本入れておく

#### (4) SQLインジェクション
- [ ] SQL文字列の**テンプレートリテラル埋め込みがゼロ**か。`` db.prepare(`SELECT * FROM x WHERE id = ${id}`) `` を grep で探す
- [ ] すべて `.bind()` によるプレースホルダになっているか
- [ ] ORDER BY のカラム名をユーザー入力から作っていないか（プレースホルダが使えない箇所 → **許可リストで照合**する）

#### (5) その他
- [ ] Cookie に `HttpOnly` `Secure` `SameSite=Lax` が付いているか
- [ ] 状態を変えるフォームに CSRF 対策（SameSite=Lax + POST なら概ね足りるが、意識して確認する）
- [ ] ユーザー入力をHTMLに出す箇所のエスケープ（HonoのJSXは自動エスケープするが、`dangerouslySetInnerHTML` 相当を使っていないか）
- [ ] 依存パッケージ数を数える。**20個を超えたら多すぎる**。サプライチェーンリスクは依存数に比例する

---

## 4. MVPリファレンス設計 — 「2週間で作れて課金までつながる」

### 4.1 画面構成（これで全部。5枚）

| # | 画面 | パス | 中身 | 実装目安 |
|---|---|---|---|---|
| 1 | **LP（ランディング）** | `/` | 1文の価値提案 / 3つの機能 / 料金 / FAQ / CTA×2。**静的HTML** | 1.5日 |
| 2 | **サインアップ・ログイン** | `/login` | メールアドレス1つ入力 → マジックリンク送信。**パスワードなし、画面は1枚で兼用** | 1日 |
| 3 | **ダッシュボード** | `/app` | プロダクトの本体。無料枠での制限表示 + アップグレードCTA | 5日 |
| 4 | **課金** | `/billing` | 未課金 → Stripe Checkout へリダイレクト。課金済 → Stripe Customer Portal へリダイレクト。**自前の画面は「ボタン2つ」だけ** | 1日 |
| 5 | **設定** | `/settings` | メールアドレス表示 / **アカウント削除ボタン** / 問い合わせ先 | 0.5日 |

さらに法令上必要な静的ページ（テキストのみ、実装0.5日）:
`/terms`（利用規約）、`/privacy`（プライバシーポリシー）、`/legal`（**特定商取引法に基づく表記** ── 日本で有料サービスを売る場合は必須。詳細は法務担当の資料を参照）

**合計: 約10.5日** → 平日夜1.5h×10日 + 週末6h×4日 = 39時間。2週間でぎりぎり収まる。**バッファがないので、機能を1つでも足すと破綻する。**

### 4.2 Stripe サブスク（月額500円）の実装ステップ

> **重要**: JPY は Stripe の「ゼロ小数通貨」。500円は `unit_amount: 500` と書く（`50000` ではない）。ここを間違えると100倍の請求になる。

**Step 0: 準備（1日目・待ち時間があるので最初にやる）**
1. Stripe アカウント作成、事業情報・銀行口座を登録して本人確認を出す（審査に数日かかることがある）
2. **テストモードで全部作る。** ダッシュボード右上のトグルで切り替え

**Step 1: 商品の定義（Stripe ダッシュボード上、コード0行）**
3. Products → 「Pro プラン」を作成 → Price を「**継続 / 月次 / JPY / 500**」で追加
4. 生成された `price_xxx` を控える（`wrangler secret` ではなく `wrangler.toml` の vars でよい。秘密情報ではない）

**Step 2: Checkout（購入導線）**
5. サーバ側に `POST /billing/checkout` を作り、`stripe.checkout.sessions.create()` を呼ぶ:
   - `mode: 'subscription'`
   - `line_items: [{ price: PRICE_ID, quantity: 1 }]`
   - `client_reference_id: <アプリ内のuser_id>` ← **これが後でwebhookと突き合わせる鍵**
   - `customer_email: <ユーザーのメール>`（既存顧客なら `customer: cus_xxx`）
   - `success_url` / `cancel_url`
6. 返ってきた `session.url` へ 303 リダイレクト。**自前でカード番号フォームを作らない**（PCI DSS の対象になるため）

**Step 3: Webhook（状態の同期・ここが本番）**
7. `POST /webhooks/stripe` を作り、**必ず生のリクエストボディで署名検証**する:
   ```
   stripe.webhooks.constructEventAsync(rawBody, sigHeader, WEBHOOK_SECRET)
   ```
   （Cloudflare Workers では非同期版を使う）
8. 処理するイベントは**4つだけ**:
   | イベント | やること |
   |---|---|
   | `checkout.session.completed` | `client_reference_id` から user を引き、`stripe_customer_id` と `subscription_id` を保存 |
   | `customer.subscription.updated` | `status` と `current_period_end` を更新 |
   | `customer.subscription.deleted` | `status = 'canceled'` に更新 |
   | `invoice.payment_failed` | `status` を更新 + 自分に通知メール |
9. **冪等性**: `processed_events(event_id TEXT PRIMARY KEY)` テーブルを作り、`INSERT` が競合したら即 200 を返して処理をスキップ。Stripeは同じイベントを複数回送る
10. 検証失敗以外は**常に 200 を返す**。エラーで500を返し続けるとStripeがリトライを止め、状態がずれる

**Step 4: 認可（最も重要な1関数）**
11. 判定を**1箇所に集約**する。この関数以外で課金状態を判定しない:
    ```
    canUseProFeature(sub) =
      (sub.status === 'active' || sub.status === 'trialing')
      && sub.current_period_end > now()
    ```
    ※ `canceled` でも期間内なら使わせるなら条件を追加。**仕様をここに1行コメントで書く**

**Step 5: 解約・支払い方法変更（自前実装しない）**
12. `POST /billing/portal` で `stripe.billingPortal.sessions.create({ customer: cus_xxx, return_url })` → リダイレクト
13. これで**解約・カード変更・請求履歴・領収書ダウンロードが全部Stripe側で完結**する。一人運営における最大の工数削減ポイント

**Step 6: 本番切替（リリース日）**
14. 本番APIキーを `wrangler secret put STRIPE_SECRET_KEY`
15. **本番用のWebhookエンドポイントを改めて登録**（テストモードの設定は引き継がれない）し、新しい `whsec_` を secret に入れる
16. 本番で自分のカードで **500円を実際に1回課金して、解約まで通す**。これをやらずにリリースしない
17. Stripe Tax / インボイス制度対応の要否は法務担当の資料を参照

**Step 7: ローカルでの動作確認**
```
stripe listen --forward-to localhost:8787/webhooks/stripe
stripe trigger checkout.session.completed
```

### 4.3 個人情報を極力持たない設計

**原則: 持っていない情報は、漏れない。**

| 項目 | 方針 |
|---|---|
| 氏名・住所・電話番号 | **取得しない。** デジタルサービスに配送先は不要 |
| パスワード | **持たない。** マジックリンク（メールに使い捨てリンク）または Google OAuth |
| クレジットカード情報 | **一切触れない。** Stripe Checkout / Portal に完全委譲。自サーバを通過させない |
| メールアドレス | **これだけ持つ。** 用途は認証と重要通知のみ |
| 決済履歴・請求先 | **Stripe側に置く。** 自DBには `stripe_customer_id` と `status` と `current_period_end` のみ |
| アクセスログ | IPは保存しない（レート制限用にハッシュ化して短期TTLのKVに置く程度） |
| アプリケーションログ | **メールアドレスをログに書かない。** user_id（UUID）のみ |
| エラー監視（Sentry） | `sendDefaultPii: false` を明示。`beforeSend` でメールアドレスをマスク |
| アクセス解析 | Google Analytics ではなく **Cloudflare Web Analytics**（Cookie不要・個人特定なし）を使う。同意バナーが不要になる |
| 退会 | **物理削除**。論理削除で残すと「保有し続けている」状態になる。Stripe側の顧客も削除 |

**自DBに置く個人データはこれだけ**:
```sql
CREATE TABLE users (
  id            TEXT PRIMARY KEY,   -- UUID
  email         TEXT UNIQUE NOT NULL,
  created_at    INTEGER NOT NULL
);
```
これにより、万一DBが流出しても被害は「メールアドレスのリスト」に限定される。

### 4.4 リポジトリのディレクトリ構成（パターンA）

```
my-service/
├── CLAUDE.md                    # Claude Code への指示（200行以内）
├── README.md                    # 先頭に「リリース期限: YYYY-MM-DD」
├── wrangler.toml                # Workers設定。[vars]に秘密を書かない
├── package.json
├── tsconfig.json
├── .gitignore                   # .env / .dev.vars / node_modules
├── .dev.vars.example            # 必要な環境変数名の一覧（値は空）
│
├── .github/
│   └── workflows/ci.yml         # typecheck + test + gitleaks
│
├── .claude/
│   └── skills/
│       └── ship/SKILL.md        # デプロイ手順の自動化
│
├── migrations/                  # D1マイグレーション。追記のみ、既存は編集しない
│   ├── 0001_init.sql
│   └── 0002_add_subscriptions.sql
│
├── src/
│   ├── index.ts                 # Honoアプリのエントリ。ルーティング登録のみ
│   │
│   ├── routes/                  # HTTPハンドラ。1ファイル1関心事
│   │   ├── landing.tsx          # GET /            LP
│   │   ├── auth.ts              # GET|POST /login, /auth/verify, /logout
│   │   ├── app.tsx              # GET /app         ダッシュボード（本体）
│   │   ├── billing.ts           # POST /billing/checkout, /billing/portal
│   │   ├── settings.tsx         # GET /settings, POST /settings/delete
│   │   ├── legal.tsx            # /terms, /privacy, /legal
│   │   └── webhooks/
│   │       └── stripe.ts        # POST /webhooks/stripe（署名検証必須）
│   │
│   ├── db/                      # ★SQLはこのディレクトリ以外に書かない★
│   │   ├── client.ts            # D1バインディングのラッパ
│   │   ├── users.ts             # createUser / findUserByEmail / deleteUser
│   │   ├── subscriptions.ts     # upsertSubscription / getSubscription
│   │   └── events.ts            # markEventProcessed（webhook冪等性）
│   │
│   ├── lib/                     # 純粋関数のみ。DBもfetchも呼ばない
│   │   ├── entitlement.ts       # ★canUseProFeature() — 課金判定の唯一の場所★
│   │   ├── token.ts             # マジックリンクトークンの署名/検証
│   │   ├── session.ts           # Cookieセッションの発行/検証
│   │   └── ratelimit.ts         # KVベースのレート制限
│   │
│   ├── services/                # 外部SaaSのラッパ。SDKを直接importするのはここだけ
│   │   ├── stripe.ts
│   │   └── email.ts             # Resend。将来SESに差し替える際もここだけ触る
│   │
│   ├── views/                   # 共通レイアウト・UI部品（HonoのJSX）
│   │   ├── layout.tsx
│   │   └── components.tsx
│   │
│   └── types.ts                 # Env（バインディング型）と共通型
│
├── public/                      # 静的アセット
│   ├── style.css                # ★CSSフレームワークを入れない。1ファイルで足りる★
│   └── favicon.ico
│
├── tests/
│   ├── entitlement.test.ts      # 課金判定の全ケース
│   ├── webhook.test.ts          # Stripeイベントの固定JSONを流す
│   └── fixtures/                # Stripeイベントのサンプルjson
│
└── docs/
    ├── backlog.md               # ★実装しないと決めた機能の墓場★
    ├── runbook.md               # 障害時の手順（後述）
    └── faq.md                   # FAQページの原稿
```

**この構成の意図**
- `src/db/` 以外にSQLを書かない → SQLインジェクション監査が `src/db/` の目視だけで完了する
- `src/lib/entitlement.ts` に課金判定を1つだけ置く → 認可漏れの調査範囲が1ファイルになる
- `src/services/` で外部SDKを包む → Resend→SESの移行が1ファイルの書き換えで済む
- `src/lib/` を純粋関数に限定 → テストがモックなしで書ける（＝Claude Codeが正しいテストを書ける）
- `docs/backlog.md` を用意 → 思いつきを「捨てずに寝かせる」場所ができ、スコープが守れる

---

## 5. 運用

### 5.1 監視・エラー通知（すべて無料）

| 目的 | ツール | 無料枠 | 設定 |
|---|---|---|---|
| アプリ例外の捕捉 | **Sentry Developer** | 5,000エラー/月、1ユーザー、30日保持 | `sendDefaultPii: false`。`beforeSend` でメールをマスク。**アラートは「新規issue発生時のみメール」** に絞る（全通知ONにすると麻痺する） |
| 外形監視（死活） | **UptimeRobot Free** | 50モニター / 5分間隔 | 監視するのは **`/` と `/app` の2本だけ**。5分ダウンで通知 |
| 決済系の異常 | **Stripe** の組み込み通知 | 無料 | `invoice.payment_failed` を webhook で受けて自分にメール |
| アクセス解析 | **Cloudflare Web Analytics** | 無料 | Cookie不要 = 同意バナー不要 |
| リクエストログ | **Cloudflare Workers Logs / `wrangler tail`** | 無料枠あり［要確認: 保持日数と上限］ | 障害時に `wrangler tail` でリアルタイム確認 |
| 支出の暴走防止 | Stripe / Anthropic Console の上限設定 | 無料 | AI APIを使うなら**必ず**上限を設定 |

**通知先は1箇所に集約する。** メールならメール1つ、Slackなら個人Slackの1チャンネル。複数に散らすと見なくなる。

**5分間隔監視は Supabase/Neon 併用時に注意**: 前述の通り Neon の 100 CU-hours を外形監視が食い潰す可能性がある。パターンAのCloudflare構成ならこの問題はない（Workersはリクエスト課金で、無料枠は日10万req）。

### 5.2 バックアップ

| 対象 | 方法 | 頻度 |
|---|---|---|
| D1（本体データ） | `wrangler d1 export <DB> --output backup.sql` | **週1回、手動 or GitHub Actions のスケジュール実行**。出力を private リポジトリまたは R2 に保存 |
| D1（緊急復旧） | D1 の Time Travel（過去の任意時点へ復元）［要確認: 無料プランでの保持期間。30日という記載を見るが未検証］ | 自動 |
| ソースコード | GitHub | 常時 |
| シークレット | **パスワードマネージャに手動で控える**。`wrangler secret` は取り出せない | 変更時 |
| Stripe のデータ | Stripe側が保持。自分では取らない | — |

**「バックアップは復元テストをして初めてバックアップ」。** リリース前に1回だけ、エクスポートしたSQLをローカルの空DBに流し込んで起動することを確認する。以後はやらなくてよい。

### 5.3 障害時の対応（`docs/runbook.md` に書いておく）

深夜にアラートが来たときの自分は判断力がないので、**手順を書いておいて、その通りにやるだけにする**。

```markdown
# Runbook

## 判断基準
- 「金が動く経路」（Checkout / Webhook）が壊れている → 即対応
- 「表示が壊れている」 → 翌朝でよい
- 「一部ユーザーだけ」 → 翌朝でよい

## サイトが落ちた
1. https://www.cloudflarestatus.com/ を見る → Cloudflare障害なら待つ以外にない。SNSで一言告知
2. `wrangler tail` でエラーを見る
3. 直近デプロイが原因と思われる → Cloudflareダッシュボードから前のバージョンへロールバック（デプロイ履歴 → Rollback）
4. 復旧しない → LPに「メンテナンス中」の静的ページを出す（`public/maintenance.html` を用意しておく）

## Stripe Webhook が失敗している
1. Stripeダッシュボード → 開発者 → Webhook → 失敗イベントを確認
2. 原因を直してデプロイ後、**Stripe画面から失敗イベントを再送**（自分でデータを手打ちしない）
3. 課金済なのに使えないユーザーがいたら、DBを直接UPDATEして復旧 + 本人に謝罪メール

## データを壊した
1. すぐに書き込みを止める（Workersを一時的にメンテナンスモードへ）
2. D1 Time Travel で事故直前へ復元
3. 復元不能なら週次バックアップから復旧し、失われた期間を本人に連絡

## 事後
- 原因を docs/runbook.md に1行追記する。それだけ。ポストモーテムを書く時間はない
```

**告知先を1つ決めておく**（X のアカウント or サイト内のお知らせ欄）。障害時に「どこで知らせるか」を考えなくて済むようにする。

### 5.4 退会・返金フロー

| フロー | 設計 | 自分の作業 |
|---|---|---|
| **サブスク解約** | `/billing` → Stripe Customer Portal のボタン1つ | **ゼロ**（全自動） |
| **アカウント削除** | `/settings` の削除ボタン → 確認 → Stripe側の顧客削除 + `users` から物理削除 | **ゼロ**（全自動） |
| **返金** | 規約に「原則返金不可。ただし初回課金から7日以内の申し出には全額返金する」と明記 → Stripeダッシュボードから返金ボタン | 1件2分 |
| **支払い失敗** | Stripe の自動リトライ（Smart Retries）に任せる。最終失敗で subscription が `canceled` になり、webhook で自動的にアクセスが切れる | **ゼロ** |

**返金ポリシーを規約に明記する意義**: 判断コストがゼロになる。「7日以内なら無条件で返す」と決めておけば、交渉も検討も発生しない。個人開発で返金を渋って炎上するリスクの方が、返金額よりはるかに大きい。

**退会理由は聞かない**（フォームを作らない）。任意記入欄を1つ置く程度に留める。

### 5.5 一人運営で消耗しないためのサポート体制

**設計思想: 「対応が速いこと」ではなく「期待値が正確なこと」で満足度を作る。**

| 施策 | 具体 |
|---|---|
| **問い合わせ窓口は1つ** | メール（`support@ドメイン`）のみ。フォームは作らない（作る工数 > 得られるもの）。チャットは絶対に入れない |
| **対応時間の明示** | サイトのフッターと自動返信に固定文言を置く:<br>「本サービスは個人が運営しています。お問い合わせへの返信は**平日夜および週末に、原則2営業日以内**に行います。緊急のご要望には対応できない場合があります。」 |
| **自動返信を設定** | 受信時に上記の文言を自動返信。**これだけで「返事が来ない」不安の8割が消える** |
| **FAQを先に書く** | `/faq` に最低10項目。**問い合わせが来たら必ずFAQに追記**する（同じ質問に2回答えない）。FAQへの誘導リンクを自動返信に入れる |
| **返信テンプレを持つ** | 「返金依頼」「使い方が分からない」「機能要望」「不具合報告」の4パターンをテンプレ化。1件5分以内で返す |
| **機能要望への標準回答** | 「ご要望ありがとうございます。検討リストに追加しました」＋ `docs/backlog.md` に記録。**その場で実装を約束しない** |
| **通知の絞り込み** | Sentryは「新規issueのみ」、UptimeRobotは「5分ダウン」、Stripeは「支払い失敗」のみ。それ以外の通知は全部切る |
| **対応枠を決める** | 問い合わせ対応は「週末の朝30分」にまとめる。平日夜に来たメールは翌週末に返す（自動返信で期待値を合わせてあるので問題にならない） |
| **休止の予告** | 「〇月〇日〜〇日は対応をお休みします」をサイトに出せる場所を作っておく（お知らせ欄1つ） |

**やってはいけないこと**: 「24時間以内に返信します」と書く / Discordコミュニティを作る / 電話番号を公開する / 個別の機能要望に個別対応する。いずれも一人運営を確実に破壊する。

---

## 6. 最初の2週間のチェックリスト

```
[ ] Day 0   Stripeアカウント作成・本人確認提出（審査待ちがあるので最初にやる）
[ ] Day 0   ドメイン取得（Cloudflare Registrar）
[ ] Day 0   README先頭に「リリース期限: <14日後の日付>」を書く
[ ] Day 1   Hono + Workers + D1 の雛形を起動、Hello Worldをデプロイ
[ ] Day 1   CLAUDE.md を書く（Not Doingリストを含める）
[ ] Day 2   CI（typecheck + test + gitleaks）を通す
[ ] Day 3-4 認証（マジックリンク）
[ ] Day 5-9 プロダクト本体（ダッシュボード）
[ ] Day 10  Stripe Checkout + Webhook + entitlement判定 + テスト
[ ] Day 11  Billing Portal / 設定画面 / アカウント削除
[ ] Day 12  LP + 規約 + プライバシーポリシー + 特商法表記 + FAQ
[ ] Day 13  /security-review 実施 → 指摘を潰す
[ ] Day 13  Sentry / UptimeRobot / 自動返信メール 設定
[ ] Day 13  本番Stripeキー切替、自分のカードで実際に500円課金→解約まで通す
[ ] Day 14  リリース。できていない機能は docs/backlog.md へ
```

---

## 付録: 未確認・要再確認リスト

着手前に一次情報URLで必ず確認すること。

| 項目 | 状態 | 影響 |
|---|---|---|
| Stripe 日本の決済手数料への消費税の扱い（実効3.6%か3.96%か） | ［要確認］ | 粗利率が0.4pt変わる。保守的に5%で見積もれば安全 |
| Stripe Billing の +0.7% が「月商全額」にかかるか「Billing経由分のみ」か | ［要確認］ | 同上 |
| Cloudflare Workers Paid（$5）に含まれる req / CPU-ms の正確な数値 | ［要確認］ | 月商10万円以降の見積 |
| Cloudflare D1 Paid の超過単価 | ［要確認］ | 同上 |
| Cloudflare Registrar の `.com` 実売価格（$4.82 と $11.84 の両方の記載あり） | ［要確認］ | 月あたり100円程度の差。影響小 |
| Resend 有料プランの正確な価格 | ［未確認］ | 月商10万円時の見積 |
| D1 Time Travel の無料プランでの保持期間 | ［要確認］ | バックアップ戦略 |
| Cloudflare Workers Logs の無料枠（保持日数・件数） | ［要確認］ | 障害調査の可否 |
| Netlify 無料プランの商用利用可否 | ［未確認］ | 代替ホスティングの選択肢 |
| USD/JPY の実レート | ［未確認］ | ドル建て費用全般に±20% |
| Amazon SES の2026年7月改定後の新プラン（Essentials/Pro/Enterprise）の料金 | ［要確認］ | メール移行先の見積。従来の $0.10/1,000通 が維持されるか |

---

## 出典

- [Pricing · Cloudflare Workers docs](https://developers.cloudflare.com/workers/platform/pricing/)
- [Pricing · Cloudflare D1 docs](https://developers.cloudflare.com/d1/platform/pricing/)
- [Limits · Cloudflare Pages docs](https://developers.cloudflare.com/pages/platform/limits/)
- [Vercel Hobby Plan](https://vercel.com/docs/plans/hobby)
- [Pricing & Fees | Supabase](https://supabase.com/pricing)
- [What are the limits and quotas for Neon's Free plan?](https://neon.com/faqs/free-plan-limits-and-quotas)
- [Turso Database Pricing](https://turso.tech/pricing)
- [Clerk Pricing](https://clerk.com/pricing) / [Updated Pricing: new plans](https://clerk.com/changelog/2026-02-05-new-plans-more-value)
- [Pricing · Resend](https://resend.com/pricing)
- [Amazon SES pricing](https://aws.amazon.com/ses/pricing/) / [Amazon SES introduces pricing plans](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ses-pricing-plans/)
- [料金体系 & 手数料 | Stripe](https://stripe.com/jp/pricing) / [Stripe Billing | 料金体系](https://stripe.com/billing/pricing)
- [GitHub Actions billing - GitHub Docs](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Plans & Pricing | Claude by Anthropic](https://claude.com/pricing) / [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Who Should Use UptimeRobot's Free Plan?](https://help.uptimerobot.com/en/articles/11604710-who-should-use-uptimerobot-s-free-plan)
- [Sentry Pricing](https://sentry.io/pricing/)
