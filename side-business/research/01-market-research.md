# 市場・ニッチ調査レポート — Claude Code を使った個人副業の収益モデル比較

- 作成日: 2026-08-29
- 対象: 日本在住・会社員・一人運営・初期投資 数千円〜1万円
- 最初のマイルストーン: **月商 1,000 円**
- 担当: 市場・ニッチ調査

---

## 0. 先に結論（TL;DR）

| # | 推薦 | 理由の要約 |
|---|---|---|
| 1 | **業務自動化の受託・小口サービス販売**（GAS / Excel / スクレイピング / 小規模ツール） | 月1,000円到達が**最速かつ最も確実**（1件で達成）。Claude Code の生産性が「納期短縮＝時給」に直結。在庫・審査・集客のリスクが最小。 |
| 2 | **Chrome 拡張（フリーミアム／小額サブスク）** | 初期費用 **$5 一回きり**。配布チャネルが Chrome Web Store に内蔵され、集客ゼロからでも検索流入が発生する数少ない領域。1本 × 課金10人 × 500円 = 5,000円という積み上げ設計が可能。 |
| 3 | **デジタル商品の買い切り販売**（テンプレート／コード／実務ノウハウ） | 在庫ゼロ・返金以外の下振れなし。数百円 × 数本で月1,000円に届く。Claude Code で「成果物そのもの」を量産できる。ただし**集客が全ボトルネック**。 |

**この3つは競合しないので、同時並行が正解**（1で現金を作りつつ、3で認知を作り、2で資産化する）。

一方で **「マイクロSaaS でいきなりサブスク」は最初の一手としては非推奨**。統計上、マイクロSaaS の $1K MRR 到達は中央値で 12〜18 ヶ月、70% は月 $1,000 未満に留まる（[SaaSRanger](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/) / [MicroConf State of Independent SaaS](https://microconf.com/state-of-indie-saas)）。月1,000円マイルストーンには遅すぎる。

---

## 1. 調査手法と情報源の信頼度（重要な但し書き）

### 実施した検索
日本語 12 クエリ・英語 8 クエリ相当を WebSearch で実施（2026年8月時点）。

### 制約 — 必ず読んでください
本セッションのネットワーク egress プロキシにより、**以下のドメインへの直接フェッチがブロックされました**：
`zenn.dev` / `note.com` / `qiita.com` / `prtimes.jp` / `japan-affiliate.org` / `dreamnews.jp`

つまり、日本の個人開発者の一次情報が集中するプラットフォームは**検索エンジンの要約スニペット経由でしか取得できていません**。該当箇所は本文中で「スニペット由来」と明示します。数値の最終確認は、記載した URL を直接開いて裏取りしてください。

### 情報源の信頼度ランク
本レポートでは出典を 3 段階で区別します。

| ランク | 定義 | 例 |
|---|---|---|
| **A（一次／公式）** | 事業者の公式ドキュメント、業界団体の調査、当事者の実測公開 | developer.chrome.com、Apple Developer、JAO 市場調査、個人開発者の収益公開記事 |
| **B（実務者記事）** | 実名・実数値を伴う実務者のブログ・技術記事 | Zenn / note の収益公開記事 |
| **C（要注意）** | 2026年に大量発生している SEO/AI生成と思われるまとめ記事。数値の根拠が示されないことが多い | 「〇〇 2026年最新ガイド」系ドメイン多数 |

**特筆すべき所見**: 今回「Claude Code 副業」「マイクロSaaS 2026」で検索した結果の**上位の大半がランク C**でした。「月5万円稼いだ正直な話」「月8万円稼ぐまで」といったタイトルの記事群が同一ドメイン（`thchblogsite.xsrv.jp` 等）に量産されており、これ自体が「AI で量産されたアフィリエイト記事が飽和している」という市場シグナルです（→ 第4章アンチパターン参照）。C ランクの数値は本レポートでは**参考値**扱いとし、意思決定の根拠には使いません。

---

## 2. ベースレート（地の数字）— まずここを直視する

意思決定の前に、「個人開発者の収益分布」という母集団の形を押さえます。**上振れ事例だけを見ると必ず判断を誤ります。**

### 2-1. 収益分布（グローバル）

| 収益帯 | 割合 | 出典 |
|---|---|---|
| 月 $1,000 未満 | **約 50%** | [Better Launch: Indie Hacker in 2026](https://www.betterlaunch.co/blog/indie-hacker)（C） |
| 月 $1,000〜$10,000 | 約 20% | 同上 |
| 月 $10,000〜$100,000 | 約 10% | 同上 |
| 月 $100,000 超 | 5% 未満 | 同上 |
| マイクロSaaS で月 $1,000 未満 | **約 70%** | [SaaSRanger（1,000+ founders 分析）](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/)（B/C） |
| 小規模 SaaS の売上中央値 | **年 $24,000（月 $2,000）** | 同上 |
| Shopify アプリの中央値 | **月 $1,000 未満** | [Week One Labs: Shopify App Revenue Benchmarks 2026](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026/)（C） |

> **読み方**: どのデータソースも「約半数〜7割が月 $1,000（約15万円）未満」で一致しています。逆に言えば、**月商1,000円（$7）というマイルストーンは、この分布の中でも下端の目標であり、達成確率は高い**。目標設定として妥当です。問題は 1,000 円ではなく、その先で失速することです。

### 2-2. 到達までの期間

| マイルストーン | 期間の目安 | 出典 |
|---|---|---|
| $1K MRR（約15万円） | 中央値 **12〜18 ヶ月** | [SaaSRanger](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/)（B/C） |
| $5K MRR | 2〜4 年（到達できた人の中で） | 同上 |
| $10K MRR | 最初の有料顧客から中央値 12〜18 ヶ月、上位層で 6〜9 ヶ月 | [SoftwareSeni](https://www.softwareseni.com/solo-founder-saas-metrics-from-0-to-10k-mrr-in-6-months-with-realistic-timelines/)（C） |

### 2-3. 日本のアフィリエイト市場（一次データ・最重要）

一般社団法人 日本アフィリエイト協議会（JAO）『アフィリエイト市場調査2025』（調査期間 2025年12月1〜4日、有効回答 1,000名）:

| 項目 | 数値 |
|---|---|
| 月間収入 **1,000円未満**（＝ほぼ収益化できていない層） | **52.5%** |
| 月間収入 **ゼロ** | **38.4%** |
| 月 3万円以上 | **12.4%**（12年間で 5倍以上に拡大） |

出典: [JAO アフィリエイト市場調査2025](https://www.japan-affiliate.org/news/survey2025/)（A・ただし本セッションでは直接フェッチ不可、検索スニペット由来）／[プレスリリース](https://www.dreamnews.jp/press/0000353074)

> **読み方**: アフィリエイトは**参加者の 9 割超が月3万円未満**。本件クライアントの最初の目標「月1,000円」ですら、アフィリエイター全体の下位 52.5% はクリアできていません。**(d) アフィリエイト/コンテンツ を主戦場にするのは合理的でない**、というのが最も明確に数字で言える結論です。

---

## 3. 実例集（実名・実数値・出典付き）

### 3-1. Chrome 拡張

**ktg 氏 — Chrome 拡張を 17〜20 本個人開発**
- 拡張 1 本が月500円の課金ユーザーを 10 人持てば 5,000円。10 本で 5万円、20 本で 10万円が射程、という積み上げモデルを提示
- ユーティリティ拡張の適正価格は **$3〜5/月。$10 を超えると離脱が急増**
- 「無料で使えるが、もっと便利にしたい人は課金できる」フリーミアム設計が必須
- 出典: [Zenn: Chrome拡張17本を個人開発して学んだこと](https://zenn.dev/ktg/articles/chrome-extension-17-lessons) / [Zenn: Chrome拡張機能を17本個人開発して運営する話](https://zenn.dev/ktg/articles/da898f8587df5d) / [note: Chrome拡張を20本以上個人開発している話](https://note.com/happy_guppy7416/n/n90f9258e12f8)（B・スニペット由来）

**Kleo（LinkedIn 向け拡張）— 90日未満で $0 → $62K MRR**
- ただし出典自身が明記: 「プロダクトが売上を作ったのではなく、**オーディエンスが作った**」。創業者は LinkedIn で 18万人＋30万人のフォロワーを既に保有
- 出典: [Medium: 8 Solo Founders Who Quietly Hit $20K–$62K MRR](https://medium.com/@tamimbuilds/8-solo-founders-who-quietly-hit-20k-62k-mrr-in-the-last-6-months-5032e610badc)（C）
- **→ 本件クライアントは既存オーディエンスゼロなので、この事例は再現不可能。参考にしてはいけない上振れ事例の典型。**

### 3-2. モバイルアプリ（広告 / サブスク）— 最も現実的な下振れが見える領域

| 事例 | 数値 | 出典 |
|---|---|---|
| AdMob 実測 | **約3年間で累計 $180**（月平均 $5 = 約750円）。「ラーメン一杯分近い収益があった月もある」 | [Zenn: 【AdMob使ってみた】個人開発してるアプリの収益見てみた](https://zenn.dev/killit/articles/37d3e4856fa0fc)（B） |
| 熊鈴アプリ | **累計3万DL で月1万円超** | [はてな: AdMobの収益が月1万円を超えるまでにやった5つのこと](https://www.tfsappsone.com/entry/2025/08/16/103050)（B） |
| 月10万円達成アプリ | **リリース当初は月100円程度。3年以上の運用で月10万円へ** | [note: 【個人開発】月10万円の収益を達成したスマホアプリの詳細](https://note.com/wakanao_banana/n/n58c1fc7af929)（B・スニペット由来） |
| 「365日記念日」アプリ | **サブスク機能リリースから2ヶ月で月1万円** 到達（バナー広告＋サブスク） | [note: 個人開発で月1万円を達成！収益化のリアルな工夫と数字を全公開](https://note.com/tty215/n/n8d9b13f5d83b)（B・スニペット由来） |
| ASO 施策 | AdMob 収益を伸ばそうと ASO に1年取り組んで**失敗**した記録 | [Zenn: 【個人開発】ASOでAdMob収益を伸ばそうとして失敗した1年の記録](https://zenn.dev/ambr_inc/articles/1e302f625059c5)（B） |

> **読み方**: 広告単体は**桁が違う**（3年で$180）。サブスクを載せた瞬間に2ヶ月で月1万円という事例があり、**「広告 vs 課金」の差が収益の本体**。

### 3-3. コンテンツ販売（Zenn / note / Kindle）

| 事例 | 数値 | 出典 |
|---|---|---|
| Zenn Books 無名アカウント初収益 | **500円の技術書（15章）が 5 冊 → 2,500円** | [Zenn: Zenn Books に500円の技術書を出して5冊売れた話](https://zenn.dev/sktt_panda/articles/zenn-books-individual-dev-first-paid)（B） |
| Zenn 継続販売 | 500円本 88冊 + 1,000円本 6冊 = **年間約 50,500円（月平均 約4,200円）** | [Zenn 収益公開系記事](https://ohina.work/post/zenn_sales/)（B・スニペット由来） |
| note 有料記事 | 初回記事は**1ヶ月で2件・600円**。戦略見直し後、3ヶ月でフォロワー1,200人・**月3.2万円** | [note: note有料記事の売り方](https://note.com/hamaken777/n/n5a1cba957276)（C・スニペット由来） |
| Kindle KDP | 2024年開始、**2026年4月時点で18冊出版。最高月が 2026年3月の ¥1,088**。最初の1年はほぼゼロ | [Kindle自費出版のやり方](https://mamou.biz/kindle-self-publishing/)（B） |
| Notion テンプレート | 単月で **55件 × $3（約450円）** ≒ 約2.5万円（Notion マーケットプレイスのみ） | [note: 初心者が2ヶ月で実現！Notionテンプレート販売で収益化した実体験](https://note.com/o_m_g_da_yo/n/ncc945dfeeec3) / [note: 副業Notionテンプレ販売で見えた現実と10万円達成までの道](https://note.com/o_m_g_da_yo/n/nba84f5b09fea)（B・スニペット由来） |

> **読み方**: **Zenn の「500円 × 5冊 = 2,500円」が、本件の月1,000円マイルストーンに対する最も直接的な達成事例**です。無名アカウント・既存フォロワーなしで達成されている点が重要。KDP の「18冊で最高月1,088円」は逆に、**冊数を積むだけでは伸びない**ことの実証。

### 3-4. 受託・クラウドソーシング

| 項目 | 数値 | 出典 |
|---|---|---|
| ココナラ Web制作 | 1件 3〜5万円、手数料22%差引後の手取り **2.3〜3.9万円** | [＠SOHO: ココナラの販売手数料2026](https://atsoho.com/blog/coconala-fee-2026-breakdown)（C） |
| クラウドソーシング小口 | Python スクリプト作成 / Excel自動化 / スクレイピングで **1件 5,000〜30,000円** | [romptn: Claude Code 副業の実例まとめ](https://romptn.com/article/105319)（C） |
| AI関連案件の伸び | クラウドソーシングの AI 関連案件が 2024年比 **約3.2倍** | 同上（C・裏取り未了、**推定扱い**） |
| GAS 案件 | ランサーズで増加傾向。「JavaScript基本＋スプレッドシート操作」で参画可能な案件が存在 | [Remogu: 【GAS】業務委託の報酬相場とスキルロードマップ2026](https://remogu.jp/c/%E3%80%90gas%E3%80%91%E6%A5%AD%E5%8B%99%E5%A7%94%E8%A8%97%E3%81%AE%E5%A0%B1%E9%85%AC%E7%9B%B8%E5%A0%B4%E3%81%A8%E3%82%B9%E3%82%AD%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%89%E3%83%9E%E3%83%83%E3%83%97/)（C） |

**注意すべき逆風**: 2026年2月のクラウドワークス決算で**営業利益が前年同期比 84.4% 減、純利益 95.6% 減**。手数料依存モデルの限界が指摘されています（[＠SOHO](https://atsoho.com/blog/crowdworks-lancers-hikaku)（C）／**IR の一次資料での裏取り推奨**）。プラットフォーム側の手数料引き上げリスクを織り込むべきです。

### 3-5. MCP サーバー / Claude Code エコシステム

| 項目 | 数値 | 出典 |
|---|---|---|
| MCP SDK ダウンロード | 2026年3月時点で **月間 約9,700万** | [MCP Marketplace: The State of MCP Monetization in 2026](https://mcp-marketplace.io/blog/state-of-mcp-monetization-2026)（C） |
| MCP サーバー総数 | 11,000〜17,000+ | 同上 |
| **収益化されている割合** | **5% 未満** | 同上 |
| Apify のレベニューシェア | 開発者 80%（コンピュート費控除後）。月 $2,000 稼ぐ開発者の例 | 同上 |
| 上振れ事例 | ソロ開発者の MCP サーバーが 6週間で $10,000 MRR | 同上（**裏取り不能・推定/宣伝の可能性高**） |
| Claude Code 公式プラグイン | 2026年3月時点で公式マーケットプレイスに **101 プラグイン**（Anthropic製 33 + パートナー 68） | [Agensi: Claude Code Plugin Marketplace Guide 2026](https://www.agensi.io/learn/claude-code-plugin-marketplace-guide)（C） |
| コミュニティ側 | 442 カタログプラグイン / 3,068 スキル | [alexcloudstar](https://www.alexcloudstar.com/blog/claude-code-plugin-marketplace-skills-2026/)（C） |

> **読み方**: MCP/プラグイン領域は**需要指標（DL数）は巨大だが、課金インフラと課金文化が未成熟**（収益化 5% 未満）。しかも Claude Code プラグイン／スキルは**事実上すべて無償の OSS 配布**が慣行で、直接課金チャネルとして機能していません。「先行者利益がある領域」ではあるが、**月1,000円を確実に取りに行く手段ではない**。

---

## 4. コスト・手数料の実データ（2026年8月時点）

### 4-1. プラットフォーム登録費

| プラットフォーム | 費用 | 出典 |
|---|---|---|
| Chrome Web Store | **$5 一回きり** | [Chrome for Developers: Register your developer account](https://developer.chrome.com/docs/webstore/register)（A） |
| Google Play | **$25 一回きり**（＋新規は12テスター要件） | [Play Console Help](https://support.google.com/googleplay/android-developer/answer/6112435)（A） |
| Apple Developer Program | **$99 / 年（毎年更新）** | [Apple Developer Program](https://developer.apple.com/programs/)（A） |
| Gumroad / BOOTH / Zenn / note | **無料**（売上手数料のみ） | 各公式 |

### 4-2. 決済・販売手数料

| サービス | 手数料 | 備考 | 出典 |
|---|---|---|---|
| Stripe（日本・国内カード） | **3.6%** | サブスク（Billing）利用時は **+0.7% = 計 4.3%** | [PAY.JP: Stripe手数料まとめ2026](https://pay.jp/column/stripe-fees-guide)（C）／[DevelopersIO: Stripe Billing手数料](https://dev.classmethod.jp/articles/stripe-billing-fee-and-tax/)（B） |
| Gumroad | **10% + $0.50**（直販）／**30%**（Discover 経由） | 2025-01-01 より完全 Merchant of Record。VAT/消費税を代行 | [Gumroad Fees 2026](https://roo.beehiiv.com/p/gumroad-fees-2026)（C）／[Checkout Page](https://checkoutpage.com/blog/gumroad-fees)（C） |
| Lemon Squeezy / Paddle | **5% + $0.50**（MoR） | Lemon Squeezy は 2024年に Stripe が買収 | [stilllater: MoR比較](https://stilllater.com/dev-tools/lemonsqueezy-vs-stripe-vs-paddle/)（C） |
| BOOTH | **5.6% + 22円** | 国内デジタル販売で最安水準 | [Togetter: Kindle と BOOTH の比較](https://togetter.com/li/2386147)（B） |
| note 有料記事 | クレカ決済 **15%** / キャリア決済 **25%**（＋振込手数料） | メンバーシップ10%、定期購読20% | [note収益化の手数料解説](https://hanapapa-side-business.com/note-monetization/)（C・**note公式での裏取り必須**） |
| ココナラ | **22%**（ビデオチャット 27.5%）。振込は3,000円未満で160円 | 国内最高水準の手数料 | [＠SOHO](https://atsoho.com/blog/coconala-fee-2026-breakdown)（C） |
| ランサーズ | **16.5% 一律** | 「パッケージ」で出品型が可能 | [＠SOHO: CW/ランサーズ比較](https://atsoho.com/blog/crowdworks-lancers-hikaku)（C） |
| クラウドワークス | 段階制（少額案件で割高） | 少額ならランサーズが有利 | 同上 |
| Figma Community | **15%** | | [Dodo Payments](https://dodopayments.com/blogs/sell-figma-plugins)（C） |
| Shopify App Store | **年間最初の $100万 まで 0%**、以降 15% | ソロ開発者に極めて有利 | [alternativeto（Shopify公式発表を報じたもの）](https://alternativeto.net/news/2021/6/shopify-app-store-will-offer-0-commissions-on-devs-first-million-dollars-in-revenue-yearly)（B） |
| Kindle KDP | **70%**（税込250〜1,650円の価格帯）／それ以外 35% | 2026年8月時点の Amazon.co.jp 条件 | [Kindle出版の印税](https://tosakablog.com/kindle/royalty/)（C・**KDP公式で裏取り推奨**） |
| VS Code Marketplace | Microsoft **5%**（有料拡張） | 実質は外部決済併用が主流 | [Markaicode](https://markaicode.com/sell-vs-code-extensions-2025/)（C） |

### 4-3. インフラ（初期投資 数千円〜1万円 の枠内に収める前提）

| 項目 | 想定コスト |
|---|---|
| ドメイン（.com / .dev） | 年 1,500〜2,500円 |
| ホスティング（Vercel / Cloudflare Pages / Netlify 無料枠） | **0円** |
| DB（Supabase / Neon / Cloudflare D1 無料枠） | **0円** |
| Chrome Web Store 登録 | 約 750円（$5） |
| Claude Code（Claude Pro/Max） | 月 3,000円〜（**既に利用中と仮定**） |
| **合計初期費用の現実解** | **約 2,500〜4,000円**（ドメイン + Chrome $5 + 予備） |

> **初期投資 1万円以内という条件は、(a)〜(d) のうち「物理物販」を除けば全て余裕でクリアします。** 唯一 Apple Developer $99/年（約15,000円）だけが予算超過なので、**iOS アプリは初手から除外**。

---

## 5. 候補 12 モデルの詳細評価

各候補について「概要／顧客／課金」「月1,000円到達」「スケール性とボトルネック」「コスト」「競合」「Claude Code 相性」を記載。

---

### 候補1: 業務自動化の受託・小口サービス販売 ★推薦1位
（GAS / Excel VBA / Python スクリプト / スクレイピング / 小規模ツール制作）

- **概要**: 「Excelの手作業を自動化」「スプレッドシートで請求書を自動生成」「特定サイトからの定期データ取得」など、1件 5,000〜30,000円の小口案件を受注。
- **想定顧客**: 中小企業の総務・経理・営業事務、個人事業主。**発注者は非エンジニア**。
- **課金形態**: 案件ごとの買い切り。将来的に保守月額。
- **月1,000円到達**: **1件受注で即達成。現実的には初回受注まで 2〜6 週間**（プロフィール作成 → 提案 10〜30 件 → 初受注）。作業量: 提案文作成に週 3〜5 時間、初回案件の実装に 5〜15 時間。
- **月1万円**: 月1〜3件で到達。3〜4ヶ月目に十分射程。
- **月10万円**: 月4〜8件、または単価5万円級 × 2件。**ボトルネック = 自分の時間**（労働集約）。ココナラ手数料22%も効く。ここを越えるには「同じ型の案件をテンプレ化して単価維持のまま時間を削る」か「保守月額に転換する」必要。
- **初期費用**: **0円**。ランニング 0円。
- **競合**: 激しい（クラウドソーシングは価格破壊が常態）。ただし **AI活用を前提とした「速さ」で明確に差別化可能**。手数料の安いランサーズ（16.5%）優先。
- **Claude Code 相性**: **◎ 最高**。仕様が明確で小規模＝ AI が最も得意な領域。工数が 1/3〜1/5 になれば実質時給が跳ね上がる。**「AIが書いたコードでも、動いて納品されれば発注者には関係ない」という、AI利用が完全に正当化される数少ない領域。**
- **下振れリスク**: 初受注できずに終わる（実績ゼロは提案が通りにくい）。低単価案件に沈む。クラウドワークスの業績悪化に伴う手数料改定リスク。

---

### 候補2: Chrome 拡張機能（フリーミアム / 小額サブスク） ★推薦2位

- **概要**: 特定サイト・特定業務のペインを解決する軽量拡張。無料で使えて、便利機能を月300〜700円で課金。
- **想定顧客**: 特定 SaaS のヘビーユーザー、EC 出品者、SNS 運用者、業務でブラウザに張り付く人。
- **課金形態**: 月額 $3〜5（**$10 超で離脱急増** — ktg 氏の実測）。または買い切り。
- **月1,000円到達**: **課金ユーザー 2〜3人で達成**。開発 1〜3週間 ＋ 審査 数日〜2週間 ＋ ユーザー獲得 1〜3ヶ月。**現実的には 2〜4 ヶ月**。
- **月1万円**: 課金 20〜30人。1本では厳しく、**複数本の積み上げ**が定石（ktg氏モデル: 10本で5万円）。
- **月10万円**: 課金 200人 or 20本。**ボトルネック = Chrome Web Store 内の検索順位と、拡張の権限承認への心理的抵抗**。加えて Manifest V3 / ストアポリシー変更で一夜にして機能が使えなくなるプラットフォームリスク。
- **初期費用**: **$5（約750円）一回きり**。ランニングは決済まわりのみ（Stripe 4.3% or Lemon Squeezy 5%+$0.50）。
- **競合**: 中程度。ニッチを絞れば空白地帯が残っている。「特定 SaaS × 特定業務」の粒度なら競合ゼロもありうる。
- **Claude Code 相性**: **◎**。拡張はコード量が小さく、Manifest V3 / content script / service worker という定型構造。AI が一発で骨格を作れる。**ただし審査対応・ストア説明文・スクショは人力**。
- **下振れリスク**: ストア審査でリジェクト（権限要求が広いと厳しい）。プラットフォーム依存。無料版だけ使われて課金ゼロ。

---

### 候補3: デジタル商品の買い切り販売 ★推薦3位
（テンプレート／ボイラープレート／実務ノウハウ PDF／プロンプト集／Notion テンプレ）

- **概要**: 一度作れば複製コストゼロの成果物を BOOTH / Gumroad / note / Zenn Books で販売。
- **想定顧客**: 同業のエンジニア、個人開発者、非エンジニアの業務担当者。
- **課金形態**: 買い切り 300〜3,000円。
- **月1,000円到達**: **500円 × 2冊/本**。実例: [Zenn Books で 500円本が 5冊 → 2,500円（無名アカウント）](https://zenn.dev/sktt_panda/articles/zenn-books-individual-dev-first-paid)。**制作 1〜3週間 ＋ 販売開始後 1〜2ヶ月**。
- **月1万円**: 500円 × 20本/月。実例では Zenn で年間 5万円（月平均4,200円）、Notion テンプレで単月 2.5万円。**商品数と告知の反復が必要**。
- **月10万円**: **ボトルネック = 集客そのもの**。X / Zenn / note でのフォロワー基盤なしに月10万円は極めて困難。KDP で 18冊出して最高月 1,088円という事例が、**「量を積むだけでは伸びない」ことの決定的な証拠**。
- **初期費用**: **0円**（BOOTH/Gumroad は登録無料）。ランニング 0円。
- **競合**: 激しい。特に「AI で稼ぐ系」「プロンプト集」は完全に飽和（→ 第6章）。**逆に「自分が実際に業務で使っているもの」は競合が薄い**。
- **Claude Code 相性**: **○〜◎**。ボイラープレート／CLI ツール／技術書の下書きは AI が量産できる。**ただし「AI が書いたと分かる薄い商品」は返金・評判リスク直結**。差別化は「自分の実務経験」に依存し、そこは AI では埋まらない。
- **下振れリスク**: 出しただけでは1本も売れない（実際、Gumroad で22商品出して「公開しただけで売れたことはほとんどない」という証言あり — [Stillworks Lab](https://stillworks-lab.hatenablog.com/entry/2026/05/20/150408)（C））。

---

### 候補4: マイクロSaaS（Web サービスのサブスク）

- **概要**: ニッチ業務向け Web アプリを月額課金。
- **想定顧客**: 特定業種の中小事業者（例: 整体院の予約管理、士業の書類生成、EC の在庫連携）。
- **課金形態**: 月額 980〜4,980円。
- **月1,000円到達**: **有料顧客1人で達成**。ただし**それが最も難しい**。MVP 構築 1〜2ヶ月 ＋ 顧客発見 3〜12ヶ月。統計上 **$1K MRR まで中央値 12〜18ヶ月**。**月1,000円だけなら 3〜6ヶ月が現実的な下限**。
- **月1万円**: 顧客 3〜10人。B2B なら十分可能。
- **月10万円**: 顧客 30〜100人。**ボトルネック = 営業チャネル**。日本の中小企業向けは Web だけでは取れず、電話・紹介・展示会が要る。加えて**個人事業者への信用不安**（「会社じゃないと契約できない」）。さらにサポート対応が個人の時間を食い潰す。
- **初期費用**: ドメイン 2,000円 + インフラ無料枠 = **約2,000円**。ランニングは Stripe 4.3% ＋ ユーザー増に伴う従量課金。
- **競合**: ニッチ次第。日本語・特定業種はまだ空白が多い。
- **Claude Code 相性**: **◎**（開発）／**×**（営業）。**Claude Code が解決するのは工数の 3 割程度で、残り 7 割の「顧客を見つける」には効かない。**
- **下振れリスク**: **高い**。70%が月$1,000未満。個人開発の最頻失敗パターン（作ったが誰も使わない）に最も当たりやすい。**最初の一手としては非推奨。**

---

### 候補5: モバイルアプリ（Android 先行・アプリ内課金）

- **概要**: Android アプリを Google Play で公開。広告 + サブスク or 買い切り。
- **想定顧客**: 一般消費者（C向け）。
- **課金形態**: AdMob 広告 ＋ アプリ内課金。
- **月1,000円到達**: **広告のみなら数ヶ月〜数年**（実測: 3年で累計$180）。**サブスク導入なら2ヶ月で月1万円という事例あり**。→ **広告だけでやるのは時間の無駄**。
- **月1万円**: 累計3万DL相当（広告）／課金 20人（サブスク）。
- **月10万円**: 実例で **3年以上の運用**。ボトルネック = ASO と DL 数の獲得。ASO に1年費やして失敗した記録も公開されている。
- **初期費用**: Google Play **$25 一回きり（約3,700円）**。iOS は $99/年で**予算超過のため除外**。
- **競合**: 極めて激しい。C向けアプリは世界中の個人開発者と競合。
- **Claude Code 相性**: **○**。Flutter / React Native なら AI 生産性は高いが、実機デバッグ・ストア審査・ASO は人力。
- **下振れリスク**: **高い**。C向けは「使われない」確率が最大。加えて Google Play の新規開発者向け12テスター要件が参入摩擦。

---

### 候補6: 既存プラットフォームのアドオン（Shopify App / Figma Plugin / VS Code 拡張 / WordPress プラグイン）

- **概要**: 巨大プラットフォームのマーケットプレイスに寄生し、集客をプラットフォームに任せる。
- **想定顧客**: そのプラットフォームの有料ユーザー（＝**既に金を払う習慣がある**）。
- **課金形態**: 月額 or 買い切り。
- **月1,000円到達**: 顧客1〜3人。開発 2〜6週間 ＋ 審査。**2〜5ヶ月**。
- **月1万円 / 月10万円**: Shopify は **年間最初の $100万まで手数料 0%** という破格の条件があり、B2B（EC事業者は課金抵抗が低い）なので単価を上げやすい。ただし中央値は月$1,000未満。VS Code は Marketplace 自体に課金機構が弱く、外部ライセンス管理を自作する必要あり。
- **初期費用**: ほぼ0円（Shopify パートナー登録無料、開発ストア無料）。
- **競合**: Shopify は激戦（アプリ数万本）。Figma / VS Code は有料化率が低く（VS Code は有料拡張が 15% 程度との指摘）、**空白はあるが課金文化も薄い**。
- **Claude Code 相性**: **◎**。各プラットフォームの API が明確にドキュメント化されており、AI が最も強い条件。
- **下振れリスク**: プラットフォーム依存（API 変更・ポリシー変更で一夜にして死ぬ）。**英語での UI・サポート対応が必須**。

---

### 候補7: AI 導入支援・Claude Code 活用コンサル / 研修

- **概要**: 「社内で Claude Code を使えるようにする」「AI で業務をどう自動化するか」の設計・実装・伴走。
- **想定顧客**: 中小企業の情シス・経営者、非エンジニアのチーム。
- **課金形態**: 時間単価 or 月額顧問。
- **月1,000円到達**: 案件が取れれば即。ただし**信用が必要**で、実績ゼロからの初回受注が最難関。**3〜9ヶ月**。
- **月10万円**: 月額顧問 3〜5社。**ボトルネック = 会社員としての時間と守秘・競業リスク**。
- **初期費用**: 0円。
- **競合**: 2026年時点で急増中だが、**「実際に手を動かして納品できる人」は依然少ない**。
- **Claude Code 相性**: **◎**（テーマそのもの）。
- **下振れリスク**: 本業の就業規則・競業避止に最も抵触しやすい。会社バレのリスクも最大。**副業禁止規定の確認が必須。**

---

### 候補8: MCP サーバー / AI エージェント向けツールの提供

- **概要**: Claude / ChatGPT などのエージェントから呼ばれるツールを作り、呼び出し単位 or サブスクで課金。
- **想定顧客**: AI エージェントを業務に組み込んでいる開発者・企業。
- **課金形態**: per-call / サブスク / フリーミアム。
- **月1,000円到達**: **不確実**。市場は巨大（MCP SDK 月間 約9,700万DL）だが**収益化されているサーバーは 5% 未満**＝課金導線もユーザーの支払い意思も未成熟。**6ヶ月〜見通せず**。
- **月10万円**: 理論上は青天井だが、実績データが薄い。
- **初期費用**: ほぼ0円。
- **競合**: サーバー数 11,000〜17,000 だが**有料はごく少数** → 空白はある。
- **Claude Code 相性**: **◎**（Anthropic 自身のプロトコル）。
- **下振れリスク**: **高い**。「先行者利益」を狙う投機的な賭け。**月1,000円という確実性を求める最初の一手には不適。ただし候補1〜3で足場を作った後の第2弾としては有力。**

---

### 候補9: 技術コンテンツ + アフィリエイト / 広告

- **概要**: ブログ・Zenn・YouTube で AI 開発の知見を発信し、ツール紹介や広告で収益化。
- **月1,000円到達**: JAO 調査で **52.5% が月1,000円未満、38.4% が収入ゼロ**。**期待値が最も低い**。到達まで 6〜18ヶ月。
- **月10万円**: 月3万円以上が全体の 12.4% しかいない世界。
- **初期費用**: ドメイン 2,000円程度。
- **競合**: **極めて激しく、かつ AI 量産記事で急速に悪化中**。今回の検索でも上位が SEO 記事で埋まっていることを確認。
- **Claude Code 相性**: 記事量産には使えるが、**それこそが Google のスパムポリシー（scaled content abuse）の標的**。
- **判定**: **単体では非推奨。候補1〜3の「集客手段」としてのみ位置づけるべき。**

---

### 候補10: 有料 API / データ提供

- **概要**: 特定データを整形して API or CSV で販売（例: 業界の公開統計、地域データ）。
- **月1,000円到達**: 顧客1人。ただし**顧客発見が非常に難しい**。
- **競合**: ニッチなら薄い。
- **リスク**: **スクレイピング由来のデータは規約違反・著作権リスクが直撃**（→ 第6章）。公的オープンデータ由来なら安全。
- **Claude Code 相性**: ◎（パイプライン構築）。
- **判定**: **法務リスクの見極めが前提。初手としては優先度低。**

---

### 候補11: 物理物販（在庫あり）

- **概要**: 自作グッズ・小ロット輸入品などの物販。
- **月1,000円到達**: 1個売れれば達成だが、**仕入れ・在庫・発送・返品対応が発生**。
- **初期費用**: 在庫仕入れで**1万円枠を容易に超える**。
- **Claude Code 相性**: **×**。コードを書く優位性がほぼ活きない。
- **判定**: **明確に除外**。前提条件（初期投資1万円以内・一人運営・Claude Code 活用）と全て衝突する。

---

### 候補12: 既存 SaaS の日本語ローカライズ・代理販売 / リセール

- **概要**: 海外ツールの日本語版提供・導入代行。
- **月1,000円到達**: 契約次第。
- **リスク**: 契約・許諾が前提で、個人では締結困難なケースが多い。
- **Claude Code 相性**: △。
- **判定**: **個人の初手としては非現実的。除外。**

---

## 6. 比較表（総覧）

評価: ◎ 優 / ○ 良 / △ 可 / × 不可

| # | モデル | 月1,000円到達 | 月1万円 | 月10万円 | 初期費用 | ランニング | 競合 | Claude Code相性 | 総合 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **業務自動化の受託** | **2〜6週** ◎ | 3〜4ヶ月 ◎ | 労働集約が壁 △ | **0円** | 0円 | 激（差別化可） | **◎** | **★1** |
| 2 | **Chrome 拡張** | 2〜4ヶ月 ○ | 4〜8ヶ月 ○ | 複数本必須 ○ | **約750円** | 決済手数料のみ | 中 | **◎** | **★2** |
| 3 | **デジタル商品買い切り** | 1〜2ヶ月 ◎ | 3〜6ヶ月 ○ | 集客が壁 △ | **0円** | 0円 | 激 | ○ | **★3** |
| 4 | マイクロSaaS | 3〜6ヶ月 △ | 6〜12ヶ月 △ | 営業が壁 △ | 約2,000円 | Stripe 4.3% | 中 | ◎(開発)/×(営業) | 4 |
| 5 | モバイルアプリ | 2〜6ヶ月 △ | 6〜12ヶ月 △ | 3年規模 × | 約3,700円 | 0円 | 極激 | ○ | 6 |
| 6 | PF アドオン(Shopify等) | 2〜5ヶ月 ○ | 6〜12ヶ月 ○ | Shopifyは手数料0% ○ | 0円 | 決済手数料 | 激〜中 | ◎ | 4 |
| 7 | AI導入支援・コンサル | 3〜9ヶ月 △ | 単価高く速い ◎ | 時間が壁 △ | 0円 | 0円 | 中 | ◎ | 5 |
| 8 | MCPサーバー | 不確実 △ | 不確実 △ | 未知数 △ | 0円 | 0円 | 薄(課金文化も薄) | ◎ | 7 |
| 9 | アフィリエイト/コンテンツ | 6〜18ヶ月 × | 期待値低 × | 上位12.4%のみ × | 約2,000円 | 0円 | 極激 | △(規約リスク) | 9 |
| 10 | 有料API/データ | 不確実 △ | 不確実 △ | 顧客発見が壁 △ | 0円 | 従量 | 薄 | ◎ | 8 |
| 11 | 物理物販 | 在庫次第 △ | △ | 在庫・発送が壁 × | **1万円超** | 在庫 | 激 | **×** | 除外 |
| 12 | ローカライズ/リセール | 契約次第 × | × | × | — | — | — | △ | 除外 |

---

## 7. アンチパターン（やめておくべきこと）

### 7-1. 汎用 AI ラッパー（最重要の地雷）

- 2024〜2025年に ChatGPT/Claude/Gemini の API を呼ぶだけの「AIラッパー」が大量投入され、**大半が短命に終わった**。理由: **基盤モデル提供者が同じ機能を内製してくる**。「PDF要約サービス」を作っても半年後に ChatGPT 本体が PDF をネイティブ対応する、というパターンの反復（[Zenn: 個人開発はなぜ誰も使わないのか](https://zenn.dev/yun_bow/articles/6e6bcbf127072a)（B）／[秋霜堂](https://syusodo.co.jp/workee-freelance-blog/articles/freelance-engineer-indie-dev-income-2026)（C））。
- **App Store 側も明確に締めている**: 2026年6月の App Review Guidelines 更新で 4.3 の文言が強化され「既に広く出回っているものと区別がつかないアプリを出すな」に。**飽和カテゴリとして扱われているのは: 汎用AIチャットボット、AI画像生成クローン、AI要約、AIロゴメーカー、AIコンパニオン、AI学習支援**（[PTKD Journal: Why did Apple reject my AI app under Guideline 4.3?](https://ptkd.com/journal/rejection-guideline-4-3-ai-spam)（C）／[Push My App: App Store Rejection Reasons Index 2026](https://pushmyapp.ai/blog/app-store-rejection-reasons)（C））。
- **→ 「Claude Code で AI チャットアプリを作る」は、審査で落ちるか、落ちても売れない。**

### 7-2. AI 記事の量産による SEO アフィリエイト

- Google は 2024年3月コアアップデートで **scaled content abuse（大規模コンテンツ不正利用）と site reputation abuse** をスパムポリシーに明記。2026年6月・8月にもスパムアップデートが実施されている（[Google 検索セントラル: site reputation abuse](https://developers.google.com/search/blog/2024/11/site-reputation-abuse)（A）／[ペコプラ: 2026年8月Googleスパムアップデート](https://pecopla.net/seo-column/google-august-2026-spam-update)（C））。
- Google は AI 生成を一律禁止していないが、**検索順位操作目的の薄いページの大量生成は明確に対象**。
- **→ Claude Code の「速く書ける」という強みを最も安直に使う方向であり、最も高確率で無に帰す。**

### 7-3. 「作ってから集客を考える」

- 個人開発で最頻の失敗。**「まずプロダクトを完成させてから集客を考えよう」が最大のアンチパターン**であり、メディア（集客チャネル）を先に作ってから、その層の需要があるものを作るほうが失敗確率が大幅に下がる（[ShiftB: 個人開発のマーケティング戦略](https://shiftb.dev/articles/indie-dev-marketing)（C）／[Zenn: 個人開発はなぜ誰も使わないのか](https://zenn.dev/yun_bow/articles/6e6bcbf127072a)（B））。
- 2026年は AI で「作る壁」が消えた結果、**「誰も使わないアプリ」問題はむしろ深刻化している**。
- 「個人開発の成否の8割は"何を作るか"で決まる」。

### 7-4. 上振れ事例の再現を狙う

- 「90日で $62K MRR」の Chrome 拡張（Kleo）は、**創業者が既に LinkedIn で 18万＋30万フォロワーを持っていた**。出典自身が「プロダクトではなくオーディエンスが売上を作った」と明記している。
- **既存オーディエンスゼロの人間がこの数字を目標に置くのは、単に誤った期待値設定。**

### 7-5. 広告収益だけで始める

- AdMob 実測: **3年間で累計 $180**。同じ開発者層でもサブスクを載せた途端に2ヶ月で月1万円に届く事例がある。**広告は「月1,000円」ですら数年かかりうる。**

### 7-6. スクレイピング依存 / 規約グレー

- 特定サービスのデータを無断取得して再配布・販売するモデルは、利用規約違反・著作権・不正競争防止法のリスクを負う。**プラットフォームの API 変更や法的通知で一夜にして事業が消える。** 受託でスクレイピングを請ける場合も、対象サイトの規約確認を発注者と文書で握ること。

### 7-7. 在庫を持つ物販

- 初期投資1万円の枠、一人運営、Claude Code 活用という3条件すべてと衝突。**除外。**

### 7-8. 会社バレ・税務まわりの取りこぼし（事業リスク）

- **20万円ルールは所得税のみ**。副業所得が年20万円以下でも**住民税の申告は必要**（[弥生: 副業所得20万以下なら確定申告と住民税の申告は不要？](https://www.yayoi-kk.co.jp/fukugyo/oyakudachi/fukugyo_20manika/)（A））。
- 住民税の特別徴収通知から勤務先に副業が伝わるリスクがある（[マネーフォワード: 副業は住民税でバレる？](https://biz.moneyforward.com/tax_return/basic/55747/)（A））。
- **「収入」ではなく「所得（収入−経費）」で判定**する点に注意。
- **→ 着手前に自社の就業規則（副業可否・許可制・競業避止）を必ず確認すること。**特に候補7（AI導入支援）は本業と競合しやすい。

---

## 8. 上位3候補の推薦と根拠

### 【第1位】業務自動化の受託・小口サービス販売

**推薦理由**

1. **月1,000円マイルストーンの達成確度が圧倒的に高い。** 他の全候補が「不特定多数に見つけてもらう」ゲームなのに対し、受託だけは「1人の発注者に選ばれる」ゲーム。母数が1で済む。クラウドソーシングの小口案件は 1件 5,000〜30,000円 なので、**1件で目標の5〜30倍**。
2. **Claude Code の優位が最もダイレクトに金額に変換される。** 仕様が明確・小規模・単発という条件は、AI コーディングが最も強い領域。実装工数が下がった分がそのまま実質時給になる。しかも受託は「AIで書いた」ことが問題にならない（発注者が求めるのは動く成果物）。
3. **下振れが小さい。** 初期費用0円、在庫なし、審査なし、プラットフォームリスクは手数料改定のみ。最悪でも「時間を使ったが受注できなかった」で終わり、金銭損失はゼロ。
4. **他の候補への踏み台になる。** 実案件で「中小企業が本当に困っていること」の一次情報が得られる。これは候補2/3/4 の**ネタ探しそのもの**。個人開発最大の失敗要因である「誰も欲しがらないものを作る」を、受託が構造的に潰してくれる。

**根拠データ**: 小口案件単価 5,000〜30,000円（[romptn](https://romptn.com/article/105319)）／ランサーズ手数料 16.5%（ココナラ22%より有利、[＠SOHO](https://atsoho.com/blog/crowdworks-lancers-hikaku)）／GAS 案件は増加傾向（[Remogu 2026](https://remogu.jp/c/%E3%80%90gas%E3%80%91%E6%A5%AD%E5%8B%99%E5%A7%94%E8%A8%97%E3%81%AE%E5%A0%B1%E9%85%AC%E7%9B%B8%E5%A0%B4%E3%81%A8%E3%82%B9%E3%82%AD%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%89%E3%83%9E%E3%83%83%E3%83%97/)）

**現実的な下振れ**: 実績ゼロのアカウントは提案が通りにくく、**初受注まで 10〜30 件の提案が必要**。最初の1〜2件は相場割れの単価を飲む必要がある可能性が高い。労働集約なので月10万円で頭打ちになる（そこがこのモデルの天井）。

---

### 【第2位】Chrome 拡張機能（フリーミアム / 小額サブスク）

**推薦理由**

1. **初期費用 $5（約750円）一回きり**。全候補中で最も資本効率が良い。Apple の $99/年 とは桁違い。
2. **Chrome Web Store が集客チャネルを内蔵している。** 個人開発最大のボトルネックである「見つけてもらう」を、ストア内検索が部分的に肩代わりする。ゼロから SNS フォロワーを作る必要がない数少ないモデル。
3. **積み上げが効く資産型。** ktg 氏の実測モデル（1本 × 課金10人 × 500円 = 5,000円、10本で5万円）は、**一発当てる必要がなく、打席数で勝てる**設計。受託と違い、寝ている間も課金される。
4. **Claude Code との相性が構造的に良い。** 拡張は Manifest V3 / content script / service worker という定型構造でコード量が小さく、AI が骨格を一発で出せる。**1本あたりの開発コストが劇的に下がる = 打席数を増やせる**というのが、まさに ktg 氏モデルの前提条件を強化する。
5. **価格帯の実測値が存在する。** 「$3〜5/月が適正、$10 超で離脱急増」という実務者の一次情報があり、価格設計で迷わずに済む。

**根拠データ**: [Chrome Web Store 登録料 $5（公式）](https://developer.chrome.com/docs/webstore/register)／[ktg 氏 Chrome拡張17本の実践知](https://zenn.dev/ktg/articles/chrome-extension-17-lessons)／[Chrome拡張ニッチ分析2026](https://chromegoldmine.com/blog/profitable-chrome-extension-niches/)

**現実的な下振れ**: 1本目が全く使われない確率は高い（ktg 氏が17〜20本作っているのはそういうこと）。ストア審査でのリジェクト、Manifest 仕様変更、権限要求への利用者の警戒心。**「10本作る覚悟」が前提のモデルであり、1本目で諦めると何も残らない。**

---

### 【第3位】デジタル商品の買い切り販売

**推薦理由**

1. **月1,000円への最短距離が実証されている。** [Zenn Books で無名アカウントが 500円本を 5冊販売 → 2,500円](https://zenn.dev/sktt_panda/articles/zenn-books-individual-dev-first-paid) という、本件の目標そのものを既存フォロワーゼロで達成した事例が存在する。
2. **金銭的下振れが構造的にゼロ。** 在庫なし、初期費用なし、ランニングなし、審査なし。失うのは時間だけ。
3. **候補1（受託）と完全に補完関係。** 受託で書いたコード・手順・ハマりどころが、そのままデジタル商品の原材料になる。**同じ作業から2回収益を得られる**のはこの組み合わせだけ。
4. **手数料が安い。** BOOTH 5.6%+22円、Gumroad 10%+$0.50（MoR で税務代行込み）。ココナラ22%と比べて手取りが大きい。

**根拠データ**: [Zenn 500円本5冊の実例](https://zenn.dev/sktt_panda/articles/zenn-books-individual-dev-first-paid)／Zenn 年間5万円の実例（[ohina.work](https://ohina.work/post/zenn_sales/)）／[BOOTH 手数料 5.6%+22円](https://togetter.com/li/2386147)／[Gumroad 10%+$0.50・MoR](https://roo.beehiiv.com/p/gumroad-fees-2026)

**現実的な下振れ**: **最大のリスクは「出したのに1本も売れない」**。Gumroad で22商品を出して「公開しただけで売れたことはほとんどない」という証言、KDP で18冊出して最高月1,088円という実例がある。**商品を作る時間より、告知に使う時間のほうが重要**という認識がないと必ず失敗する。また、AI で薄く作った商品は返金・評判毀損に直結する。

---

## 9. 推薦しない候補と理由（明示）

| 候補 | 不推薦理由 |
|---|---|
| マイクロSaaS（初手として） | $1K MRR 中央値 12〜18ヶ月、70%が月$1,000未満。月1,000円という短期目標に対して回収期間が長すぎる。**候補1〜3で顧客課題を掴んでからの第2弾なら有力。** |
| iOS アプリ | Apple Developer $99/年（約15,000円）が初期投資1万円の制約を超える。 |
| アフィリエイト/コンテンツ（単体） | JAO 調査で 52.5% が月1,000円未満、38.4% が収入ゼロ。**期待値が全候補中最低。**集客手段としてのみ使う。 |
| MCP サーバー / Claude Code プラグイン | 市場は巨大だが収益化率 5% 未満。プラグイン/スキルは OSS 無償配布が慣行で課金導線が未成熟。**投機的。** |
| 物理物販 | 初期投資・一人運営・Claude Code 活用の3条件すべてと衝突。 |

---

## 10. 未検証・要追加調査の項目

正直に記載します。以下は本レポートで裏取りが不十分です。

1. **note / Zenn / BOOTH の正確な手数料**: 公式ページへの直接アクセスがブロックされたため、二次情報（ランク C）に依存。**各公式ヘルプでの確認必須。**
2. **JAO アフィリエイト市場調査2025 の詳細分布**: 検索スニペット由来。「1,000円未満 52.5%」と「収入ゼロ 38.4%」は別ソースからの引用で、同一調査内の整合性を原文で確認すべき。
3. **「AI関連案件が2024年比3.2倍」**: ランク C の単一ソース。**推定扱い。**
4. **MCP サーバーで $10,000 MRR という事例**: 出典が MCP マーケットプレイス自身のブログ（利害関係あり）。**宣伝の可能性が高く、信用すべきでない。**
5. **VS Code 拡張で月 $6,800 という事例**: dev.to の記事だが、内容・文体から AI 生成コンテンツの疑いが強い。**採用していない。**
6. **日本の中小企業向けニッチSaaS の具体的な空白領域**: 今回は業種レベルまで特定できていない。**受託を通じた一次情報収集が最も確実な調査手段**（これが候補1を推す理由の一つでもある）。
7. **クラウドワークス 2026年2月決算の数値（営業利益 -84.4%）**: 二次情報。IR 資料での確認推奨。

---

## 付録: 出典一覧

### 一次・公式（A）
- [Chrome for Developers: Register your developer account](https://developer.chrome.com/docs/webstore/register)
- [Apple Developer Program](https://developer.apple.com/programs/)
- [Google Play Console Help: Get started](https://support.google.com/googleplay/android-developer/answer/6112435)
- [Google 検索セントラル: site reputation abuse](https://developers.google.com/search/blog/2024/11/site-reputation-abuse)
- [JAO: アフィリエイト市場調査2025](https://www.japan-affiliate.org/news/survey2025/)
- [弥生: 副業所得20万以下なら確定申告と住民税の申告は不要？](https://www.yayoi-kk.co.jp/fukugyo/oyakudachi/fukugyo_20manika/)
- [マネーフォワード クラウド: 副業は住民税でバレる？](https://biz.moneyforward.com/tax_return/basic/55747/)
- [Zenn 公式: 本を有料で販売しよう](https://zenn.dev/zenn/books/how-to-create-book/viewer/set-price)

### 実務者記事（B）
- [Zenn: Chrome拡張17本を個人開発して学んだこと](https://zenn.dev/ktg/articles/chrome-extension-17-lessons)
- [Zenn: Chrome拡張機能を17本個人開発して運営する話](https://zenn.dev/ktg/articles/da898f8587df5d)
- [Zenn: Zenn Books に500円の技術書を出して5冊売れた話](https://zenn.dev/sktt_panda/articles/zenn-books-individual-dev-first-paid)
- [Zenn: 【AdMob使ってみた】個人開発してるアプリの収益見てみた](https://zenn.dev/killit/articles/37d3e4856fa0fc)
- [Zenn: 【個人開発】ASOでAdMob収益を伸ばそうとして失敗した1年の記録](https://zenn.dev/ambr_inc/articles/1e302f625059c5)
- [Zenn: 個人開発はなぜ誰も使わないのか](https://zenn.dev/yun_bow/articles/6e6bcbf127072a)
- [note: 個人開発で月1万円を達成！収益化のリアルな工夫と数字を全公開](https://note.com/tty215/n/n8d9b13f5d83b)
- [note: 【個人開発】月10万円の収益を達成したスマホアプリの詳細【Admob】](https://note.com/wakanao_banana/n/n58c1fc7af929)
- [note: 初心者が2ヶ月で実現！Notionテンプレート販売で収益化した実体験](https://note.com/o_m_g_da_yo/n/ncc945dfeeec3)
- [note: 副業Notionテンプレ販売で見えた現実と10万円達成までの道](https://note.com/o_m_g_da_yo/n/nba84f5b09fea)
- [note: Chrome拡張を20本以上個人開発している話](https://note.com/happy_guppy7416/n/n90f9258e12f8)
- [はてな: AdMobの収益が月1万円を超えるまでにやった5つのこと](https://www.tfsappsone.com/entry/2025/08/16/103050)
- [DevelopersIO: Stripe Billingによる定額支払い時の手数料と消費税](https://dev.classmethod.jp/articles/stripe-billing-fee-and-tax/)
- [Togetter: KindleとBOOTHの比較（ロイヤリティ・POD）](https://togetter.com/li/2386147)
- [Kindle自費出版のやり方【完全版】](https://mamou.biz/kindle-self-publishing/)
- [地方SEナビ: Zennでどれくらい稼げるのか?](https://ohina.work/post/zenn_sales/)
- [alternativeto: Shopify App Store 0% commission on first $1M](https://alternativeto.net/news/2021/6/shopify-app-store-will-offer-0-commissions-on-devs-first-million-dollars-in-revenue-yearly)

### 二次・要注意（C）
- [MicroConf: State of Independent SaaS](https://microconf.com/state-of-indie-saas)
- [SaaSRanger: Micro-SaaS Revenue: What 1,000+ Founders Earn](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/)
- [Better Launch: Indie Hacker in 2026](https://www.betterlaunch.co/blog/indie-hacker)
- [Week One Labs: Shopify App Revenue Benchmarks 2026](https://weekonelabs.com/blog/shopify-app-revenue-benchmarks-2026/)
- [SoftwareSeni: Solo Founder SaaS Metrics](https://www.softwareseni.com/solo-founder-saas-metrics-from-0-to-10k-mrr-in-6-months-with-realistic-timelines/)
- [Medium: 8 Solo Founders Who Quietly Hit $20K–$62K MRR](https://medium.com/@tamimbuilds/8-solo-founders-who-quietly-hit-20k-62k-mrr-in-the-last-6-months-5032e610badc)
- [MCP Marketplace: The State of MCP Monetization in 2026](https://mcp-marketplace.io/blog/state-of-mcp-monetization-2026)
- [Agensi: Claude Code Plugin Marketplace Guide 2026](https://www.agensi.io/learn/claude-code-plugin-marketplace-guide)
- [PTKD Journal: Why did Apple reject my AI app under Guideline 4.3?](https://ptkd.com/journal/rejection-guideline-4-3-ai-spam)
- [Push My App: App Store Rejection Reasons Index 2026](https://pushmyapp.ai/blog/app-store-rejection-reasons)
- [PAY.JP: Stripe手数料まとめ【2026年最新】](https://pay.jp/column/stripe-fees-guide)
- [Gumroad Fees 2026（roo.beehiiv）](https://roo.beehiiv.com/p/gumroad-fees-2026)
- [Checkout Page: Gumroad fees 2026](https://checkoutpage.com/blog/gumroad-fees)
- [stilllater: Lemon Squeezy vs Stripe vs Paddle vs Polar](https://stilllater.com/dev-tools/lemonsqueezy-vs-stripe-vs-paddle/)
- [＠SOHO: ココナラの販売手数料2026](https://atsoho.com/blog/coconala-fee-2026-breakdown)
- [＠SOHO: クラウドワークスとランサーズの違い2026](https://atsoho.com/blog/crowdworks-lancers-hikaku)
- [Remogu: 【GAS】業務委託の報酬相場とスキルロードマップ2026](https://remogu.jp/c/%E3%80%90gas%E3%80%91%E6%A5%AD%E5%8B%99%E5%A7%94%E8%A8%97%E3%81%AE%E5%A0%B1%E9%85%AC%E7%9B%B8%E5%A0%B4%E3%81%A8%E3%82%B9%E3%82%AD%E3%83%AB%E3%83%AD%E3%83%BC%E3%83%89%E3%83%9E%E3%83%83%E3%83%97/)
- [romptn: Claude Code 副業の実例まとめ](https://romptn.com/article/105319)
- [ShiftB: 個人開発のマーケティング戦略【最初の100人を集める方法】](https://shiftb.dev/articles/indie-dev-marketing)
- [ShiftB: 個人開発SaaSの作り方 2026年版](https://shiftb.dev/articles/indie-dev-saas)
- [ペコプラ: 2026年8月Googleスパムアップデート完全ガイド](https://pecopla.net/seo-column/google-august-2026-spam-update)
- [Dodo Payments: How to Monetize Figma Plugins in 2026](https://dodopayments.com/blogs/sell-figma-plugins)
- [Markaicode: How to Sell VS Code Extensions](https://markaicode.com/sell-vs-code-extensions-2025/)
- [ChromeGoldmine: Profitable Chrome Extension Niches 2026](https://chromegoldmine.com/blog/profitable-chrome-extension-niches/)
- [Stillworks Lab: Gumroadとは？使い方から商品販売・入金まで【2026年版】](https://stillworks-lab.hatenablog.com/entry/2026/05/20/150408)
- [秋霜堂: フリーランスエンジニアの個人開発で稼ぐ方法2026](https://syusodo.co.jp/workee-freelance-blog/articles/freelance-engineer-indie-dev-income-2026)
- [hanapapa: note手数料は何パーセント？](https://hanapapa-side-business.com/note-monetization/)
- [tosakablog: Kindle出版の印税はいくら？](https://tosakablog.com/kindle/royalty/)
