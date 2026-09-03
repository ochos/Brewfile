# 03. 集客・マーケティング調査（2026年8月時点）

対象読者: 日本在住の会社員が、Claude Code で作った小さなウェブサービス／デジタル商品／アフィリエイトサイトを売る前提。
制約: 広告予算ほぼゼロ〜月数千円 / 平日夜1〜2h + 週末数時間（= **週7〜12時間**）/ 最初の目標は **月商1,000円**。

## 調査の信頼度について（先に注意書き）

- 本調査は Web 検索経由で収集した。今回の環境では個別ページの直接取得（WebFetch）がネットワーク制限でブロックされたため、**一次ソースの本文を全文確認できていない項目がある**。
- そこで各数値に信頼度タグを付けた。
  - `[一次]` = 発表元・運営元が自ら出している数値
  - `[二次]` = 調査会社・メディアが引用している数値（引用元は明示）
  - `[推定]` = マーケ系ブログ等の主張で、方法論・母集団が確認できないもの。**そのまま鵜呑みにしない**
- 「バズれば勝ち」型の再現性のない施策には明示的に **⚠️再現性なし** と書いた。

---

# 0. 結論（先出し）

## 0-1. 月商1,000円を最短で取るなら

**結論: 「Zenn / Qiita に技術記事 → その中で自作物を紹介 → 決済は Stripe か BOOTH か Zenn Books」が最短。X は補助エンジン。SEO は3ヶ月目以降の資産。**

根拠となる実測事例:
- 無名アカウントが Zenn Books で500円の技術書を出し、**Zenn+Qiita 合算 約2,000PV / 本ページ閲覧 400回超 で5冊（2,500円）** 売れている。`[二次]` → [Zenn Books に500円の技術書を出して5冊売れた話](https://qiita.com/sakutto-panda/items/62a973b2ddce6da4437f)
- これは「**月商1,000円 = 有効閲覧 200〜400 回程度で届く**」ことを意味する。バズは不要。
- 逆に Product Hunt / Hacker News は数千〜数万の到達が出るが、日本の会社員が英語で運用する工数が重く、**最初の1,000円には過剰**。月10万円フェーズで使う。

## 0-2. 3段階のチャネル戦略

| フェーズ | 目標 | 主力チャネル | 補助 | 週工数目安 |
|---|---|---|---|---|
| Phase 1 (0〜30日) | 月商1,000円 | Zenn / Qiita 記事 + 手動DM・知人 | X（記事の告知） | 集客3h / 開発5h |
| Phase 2 (31〜90日) | 月1万円 | Zenn/Qiita 継続 + SEO記事の仕込み + メルマガ開始 | はてブ、note、IDEAVALU | 集客5h / 開発5h |
| Phase 3 (90日〜) | 月10万円 | SEO/GEO資産 + メルマガ + 英語圏（PH / Show HN / Reddit） | YouTube Shorts | 集客6h / 開発4h |

成功している個人開発者は**開発:マーケの時間配分を 5:5 から 2:8 に振っている**という指摘がある `[推定]` → [個人開発の成功事例15選（2026年最新）](https://shiftb.dev/articles/indie-dev-success-stories)。Phase 3 に近づくほどこの比率に寄せる。

---

# 1. ゼロ予算チャネルの実効性比較（2026年）

## 1-1. 一覧比較表

「到達見込み」は**1本の良い投稿あたり**の見込み。「初成果まで」は月商1,000円相当の反応が出るまでの目安。

| チャネル | 到達見込み（1本） | 週工数 | 初成果まで | 日本市場での有効性 | 自己宣伝の可否 | 信頼度 |
|---|---|---|---|---|---|---|
| **Zenn** | 300〜3,000PV（初期は100〜300） | 2〜4h/本 | 2〜6週 | ◎ 開発者購買層に直結 | ○ 技術的価値があれば告知OK。宣伝のみはNG | `[二次]` |
| **Qiita** | 500〜5,000PV | 2〜4h/本 | 2〜6週 | ◎ 到達はZennより広い | △ 規約で「広告・宣伝／商用勧誘（SEO・アフィ目的投稿含む）」を明示禁止。記事本体が知識共有であることが必須 | `[一次]` |
| **X (Twitter)** | フォロワー<500なら 200〜2,000imp | 3〜5h（毎日15分） | 1〜3ヶ月 | ○ 日本の個人開発クラスタが濃い | ◎ 歓迎。ただし**外部リンク投稿は強く抑制** | `[推定]` |
| **note** | 100〜1,000PV | 2〜3h/本 | 1〜3ヶ月 | ○ 非エンジニア向け商材なら◎ | ◎ 有料記事機能が公式にある | `[二次]` |
| **はてなブックマーク** | 3users で新着、数百usersで数千流入 | 0h（Zenn/note経由の副産物） | 不定（⚠️再現性なし） | ○ 技術・時事ネタに強い | ○ 自薦タグ運用は嫌われる | `[二次]` |
| **Reddit** | 数百〜数万views（sub次第） | 3〜5h（先に参加が必要） | 1〜3ヶ月 | × 日本語ユーザーは薄い（英語プロダクト用） | △ 90/10ルールは廃止、**行動・アカウント年齢・リンク比率で判定**に移行 | `[二次]` |
| **Hacker News (Show HN)** | 成功時 3,500〜43,000訪問 / **失敗率90%** | 2h（投稿自体は軽い） | 1発勝負（⚠️再現性なし） | × 日本語商材は不可 | ◎ Show HN は自作物の発表が公式に歓迎 | `[推定]` |
| **Product Hunt** | Top3で5,000〜15,000 / Top10で1,000〜3,000 / 圏外<500 | 準備10〜15h（一度きり） | 1発勝負 | × 日本語商材は不可 | ◎ 歓迎 | `[二次]` |
| **YouTube (Shorts含む)** | 初期は数十〜数百再生 | 5〜8h/週 | 3〜6ヶ月 | ○ ただし工数が重い | ◎ 歓迎 | `[二次]` |
| **TikTok** | アルゴリズム次第で初期でも数千 | 5〜8h/週 | 1〜3ヶ月 | △ 開発者向け商材とは客層がズレる | ◎ 歓迎 | `[二次]` |
| **Discord / Slack コミュニティ** | 1コミュニティ 数十〜数百人にリーチ | 2〜3h/週 | 2〜8週 | ◎ **最初の10人には最有力の一つ** | △ 多くが宣伝専用チャンネル限定。無断投下は即アウト | `[二次]` |
| **メルマガ（ニュースレター）** | 登録者数×開封40〜56%×CTR数% | 1〜2h/週 | 2〜4ヶ月（リスト構築後） | ◎ 一度作れば最強の再訪チャネル | ◎ 自分のリストなので完全自由 | `[二次]` |

## 1-2. チャネル別の詳細

### Zenn `[推奨度: ★★★★★]`
- **規模**: Zenn 全体で会員10万人突破、月間PV 1,000万（2023年10月時点の公式発表）`[一次]` → [クラスメソッド プレスリリース](https://prtimes.jp/main/html/rd/p/000000357.000014901.html)
- **個人アカウントの現実的PV**: 開始2週間・10記事で 150〜200PV、9ヶ月継続で週平均PVが100→1,500（約15倍）という実測公開あり `[二次]` → [Zennを1年間運営した結果](https://zenn.dev/gachigachi/articles/c1ed7372f23252) / [zennのPVって正直どれくらいなの？](https://zenn.dev/miya_tech/articles/8d4cbb0ff52147)
- **決定的な事例**: 前述の「累計2,000PV → 500円本が5冊」。**月商1,000円の再現可能な最小経路**。`[二次]`
- **規約**: コミュニティガイドラインあり（[https://zenn.dev/guideline](https://zenn.dev/guideline)）。技術的な学びを含む記事の中で自作物を紹介するのは一般的に受容されている。純粋な広告記事は違反報告の対象。2026年3月にAI執筆に関する方針が更新され、**AI執筆を禁止はしないが「人主体」を要求**する方向 `[二次]` → [AIによるコンテンツ執筆に関するZennの方針](https://info.zenn.dev/2026-03-10-ai-contents-guideline)
- **工数**: 良い記事1本 2〜4時間。週1本が現実的上限。
- **⚠️注意**: Claude Code で量産した薄い記事は、Zenn の AI ポリシーと Google の「AI 大量生成コンテンツ」取り締まりの両方に触れる。**必ず自分の実測データ・失敗談を入れる。**

### Qiita `[推奨度: ★★★★☆]`
- 到達は Zenn より広いことが多いが、**規約が厳しい**。利用規約は「広告・宣伝や商用を目的とした勧誘と認められる行為（検索サイト最適化またはアフィリエイトを目的とする投稿行為を含む）」を禁止 `[一次]` → [Qiita 利用規約](https://qiita.com/terms) / [コミュニティガイドライン](https://help.qiita.com/ja/articles/qiita-community-guideline)
- **実務上の解釈**: 「作ったツールの技術解説記事の末尾でリンクを1つ置く」は通っている実例が多数（前掲の500円本の事例も Qiita 記事を併用）。「アフィリエイトリンク」「集客だけが目的の記事」はNG。
- **戦術**: Zenn に本命記事、Qiita には切り口を変えた別記事（同一内容のコピペは避ける）。

### X (Twitter) `[推奨度: ★★★☆☆ / 補助エンジンとして★★★★☆]`
- **2026年の最重要変更**: 外部リンク付き投稿が強く抑制されている。非 Premium アカウントのリンク投稿は中央値エンゲージメントがほぼゼロという報告 `[推定]` → [How to Grow on X (Twitter) 2026](https://grahammann.net/blog/how-to-grow-on-x-twitter-2026)
  - **対策**: 本文は画像＋テキストのネイティブ投稿にし、**リンクは1つ目のリプライに置く**。またはプロフィール欄に置く。
- リプライの重み付けが大きい（「リプライはいいねの27倍、会話成立で150倍」という主張あり）`[推定]` → [The X Algorithm in 2026](https://opentweet.io/blog/how-twitter-x-algorithm-works-2026)
  - **対策**: 自分の投稿より **他人の投稿への良質なリプライ** に時間を使う。フォロワー<500 の段階ではこれが唯一効く。
- build in public の期待値: 継続12ヶ月で 500〜5,000フォロワー、24ヶ月で自作物由来の有料顧客 20〜200人 `[推定]` → [Indie Hacker Marketing: 7-Channel Playbook (2026)](https://www.buildinpublic.so/blog/indie-hacker-marketing)
  - つまり **X 単体で月商1,000円を狙うのは遅すぎる**。記事の配信路として使う。

### note `[推奨度: ★★★☆☆（非エンジニア向け商材なら★★★★★）]`
- 有料記事・メンバーシップが標準装備。ただし**手数料が重い**（後述）。
- 個人開発の収益報告が読まれるジャンルとして機能している。実例:
  - [個人開発で月1万円を達成！収益化のリアルな工夫と数字を全公開](https://note.com/tty215/n/n8d9b13f5d83b)（記念日管理アプリ、広告＋サブスクで月1万円）`[二次]`
  - [【個人開発で暮らす】月1万円の売上を達成しました🎉 #5](https://note.com/nosuke0926/n/n3e06b6b48c94)（スマホ制限アプリ Zentime）`[二次]`
- **使い道**: プロダクト自体ではなく「作った過程・数字」を note に書き、その中でプロダクトを紹介する。日本では**収益公開記事そのものが集客コンテンツ**として機能する。

### はてなブックマーク `[推奨度: ★★☆☆☆ ⚠️再現性なし]`
- 3users で新着エントリー入り。そこからホットエントリーに乗るかは運。
- 実測: **41ブクマでホットエントリー掲載 → その日722PV** という小規模事例 `[二次]` → [はてなブックマークでバズった威力](https://www.taikimedia.com/entry/Hatena.Bookmark.access)
- 数百ブクマ以上で「はてな経由数千流入 + 他ブログ波及の方が多い」`[二次]` → [「はてなブックマーク数」と「流入」の関係](https://analytics.hatenadiary.com/entry/20090822/p1)（※2009年の古い分析。構造は今も概ね同じだが数値は要割引）
- **⚠️ これは狙って起こせない。** Zenn/note 記事の副産物として期待する程度に留め、**計画に組み込まない**。

### Reddit `[推奨度: 日本語商材 ★☆☆☆☆ / 英語商材 ★★★★☆]`
- **2026年のルール変更**: 有名な「90/10ルール」は公式には廃止され、モデレーターと AutoModerator が **アカウント年齢・カルマ・リンク比率・行動** で判定する方式に移行。また 2026年半ばから、サイレントな shadowban ではなく**明示的なサスペンド**に変わった `[二次]` → [The complete guide to Reddit self-promotion rules in 2026](https://redship.io/blog/reddit-self-promotion-rules) / [Reddit Self-Promotion Rules: The Complete Guide (2026)](https://founderreply.com/guides/reddit-self-promotion-rules)
- **安全な手順**: 数週間ふつうに参加 → ベータ版テスター募集系 sub でテスター募集 → 相手からリンクを求められる形にする。
- 日本語ユーザーが薄いので、**英語プロダクトを持つまでは投資対効果が悪い**。

### Hacker News (Show HN) `[推奨度: ★★☆☆☆ ⚠️再現性なし]`
- 成功時 3,500〜43,000訪問、ただし **投稿の約90%は失敗（フロントページに乗らない）** `[推定]` → [How to Launch Your Startup on Hacker News - Show HN](https://www.stackmatix.com/blog/launching-on-hacker-news)
- フロントページに乗れば1日で1万以上の技術者流入。ただし **技術者は end buyer とは限らない**という指摘 `[推定]`
- **無料**・工数ほぼゼロ（投稿自体は10分）なので、英語版があるなら「ダメ元で1回撃つ」価値はある。計画の中心には置かない。

### Product Hunt `[推奨度: ★★★☆☆（Phase 3で）]`
- **トラフィック実測レンジ** `[二次]` → [Product Hunt traffic 2026: real numbers by daily rank](https://hub.causo.ai/guides/product-hunt-traffic-data-2026) / [Product Hunt Launch Statistics for 2026](https://www.shno.co/marketing-statistics/product-hunt-launch-statistics)

| 順位 | ローンチ日の訪問者 |
|---|---|
| Top 3 | 5,000〜15,000 |
| Top 10 | 1,000〜3,000 |
| 圏外 | 500未満 |

- **必要 upvote 数**: 情報が割れている。「Top5に200〜350」という記述と「Top5に平日500〜900・週末300〜500、#1は800〜1,500」という記述が併存 `[推定]` → [Product Hunt Launch: Get Upvotes & Rank #1 in 2026](https://trendgap.io/blog/product-hunt-launch-upvotes-rank-2026) / [Product Hunt launch 2026: the realistic playbook](https://hub.causo.ai/guides/product-hunt-launch-2026-realistic-playbook)。**「数百 upvote を自力で集められる知り合いネットワークがあるか」が事実上の参加資格**と考える。
- 転換率: 訪問→サインアップ 2〜4%（B2C）/ 1〜2%（B2B）が健全レンジ。上位ローンチでは サインアップ→30日以内の有料化 5〜10% `[推定]`
- **最重要の知見**: サインアップ数の差の大半は **Product Hunt ではなく「事前に持っていた自分のオーディエンス」で説明できる**。ウェイトリスト経由はコールドトラフィックの約10倍転換する `[推定]` → [Product Hunt Launch Data: 5 Founders, 8 Questions](https://happysupport.ai/blog/product-hunt-launch-roundup-2026)
  - → **PH は「オーディエンスを増やす場」ではなく「持っているオーディエンスを換金する場」。順番を間違えない。**
- 仕様: ローンチは全て **太平洋時間 0:01 AM に公開**、23:59 PT まで。時刻選択は不可（日本時間だと夏時間期間は 16:01、冬は 17:01）`[二次]`
- **日本版の代替**: [IDEAVALU](https://www.ideavalu.com/)（個人開発者・学生起業家・スタートアップ向けの国内ローンチ掲載プラットフォーム）。日本語商材はこちらを先に試す方が費用対効果が高い `[二次]`
- 参考（日本語のPH体験記）: [ProductHuntへ個人開発サービスを投稿するまでにやったこと](https://zenn.dev/nice2have/articles/120b1df8fcea2a) / [個人開発サービス「Moyuk」をProduct Huntでローンチするまでの道のりと教訓](https://note.com/kohii/n/n6db88c7f429d)

### YouTube / TikTok `[推奨度: ★★☆☆☆（Phase 3の選択肢）]`
- 週3回以上の投稿を継続して 3〜6ヶ月で安定してくる `[推定]` → [ショート動画トレンド2026](https://0120.co.jp/blog/video-43/)
- TikTok は「発見」に強く、YouTube Shorts は「検索流入」に強い。開発者向けツールなら YouTube 寄り。
- 収益化条件（アドセンス目的の場合）: YouTube Shorts は登録者1,000人＋90日で1,000万Shorts再生、TikTok Creator Rewards は1万フォロワー＋30日10万再生 `[二次]`
- **判定: 週7〜12時間の制約では、動画は最も割に合わない。** ただし「作ったツールの30秒デモ動画」を X / Zenn 記事の中に埋める用途では極めて有効（動画制作ではなく素材制作として扱う）。

### Discord / Slack コミュニティ `[推奨度: ★★★★★（最初の10人において）]`
- 日本にも大規模な個人開発コミュニティが存在し、非エンジニアも在籍、もくもく会・作業通話が日常的に行われている `[二次]` → [起業家向けオンラインコミュニティ10選](https://harmonic-society.co.jp/online-community-startup/) / [新人プログラマが入っておくといいSlack/Discordサーバー](https://qiita.com/asakuraTsukazaki/items/b980ab16c242229cd8bc) / [DISBOARD: エンジニアタグ](https://disboard.org/servers/tag/%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2)
- **なぜ最初の10人に効くか**: 到達数は小さいが「相手の顔が見える」ため、**フィードバックと最初の課金が同時に取れる**。ここで得たコメントがそのまま Zenn 記事のネタになる。
- **規約**: ほぼ全てのコミュニティで宣伝は専用チャンネル限定。**参加初日に宣伝を投げるのは最悪手**。2週間は質問に答える側に回る。
- 工数: 週2〜3時間（うち宣伝は10分、残りは貢献）。

### メルマガ / ニュースレター `[推奨度: ★★★★☆（Phase 2から必須）]`
- 一般的な良好なメール転換率は 2〜3% `[二次]` → [Email Newsletter Stats 2026](https://designmodo.com/email-newsletter-stats/)
- indie hacker の事例で **12日で1,000登録・開封率56%・広告費0** `[推定]` → [$0 CAC, 1,000 email subscribers, and a 56% open rate](https://www.indiehackers.com/post/0-cac-1-000-email-subscribers-and-a-56-open-rate-heres-how-23c73c5553)
- **最重要**: 「早くニュースレターを始めた人はローンチ先のオーディエンスを持ち、待った人は持たない」`[推定]`
- **今日やること**: プロダクトが未完成でも、**LP にメール登録フォームを置く**。無料枠のあるサービス（Buttondown / MailerLite / Resend + 自前フォーム等）で十分。

---

## 1-3. 「最初の10人の有料顧客」に最も効率的なチャネルは何か

### 判定基準
月商1,000円 = 500円 × 2人。10人取るなら 5,000円。
必要な有効閲覧数は、前掲の実測（**400ページ閲覧 → 5本販売、転換率約1.25%**）から逆算すると **約800ページ閲覧**。`[二次]`

### 各チャネルの「10人取るためのコスト」試算 `[推定：上記転換率を全チャネルに適用した机上計算]`

| チャネル | 必要な到達 | 必要投稿数 | 必要期間 | 総工数 | 効率 |
|---|---|---|---|---|---|
| Zenn + Qiita | 800PV | 記事2〜4本 | 3〜6週 | **8〜16h** | ◎ 最良 |
| Discord/Slack | 直接会話20〜40人 | — | 3〜6週 | 12〜18h | ○（転換率は上記より高いはず） |
| X 単独 | 80,000imp相当 | 毎日投稿90日 | 3ヶ月+ | 40h+ | △ |
| note | 800PV | 記事3〜6本 | 6〜12週 | 15〜30h | △ |
| Product Hunt | 1回のローンチ | — | 準備2週 | 10〜15h + 英語化 | ×（日本語商材では不可） |
| Show HN | 1回の投稿 | — | 即日 | 2h（ただし成功率10%） | ⚠️宝くじ |
| YouTube | — | 動画30本 | 3〜6ヶ月 | 60h+ | × |

### 結論

> **最初の10人は「Zenn/Qiita 記事（主）× Discord/Slack コミュニティ（副）× X（記事の配信路）」の3点セットで取る。**
> **他のチャネルは Phase 2 以降に回す。特に Product Hunt / Show HN / YouTube は最初の10人には過剰投資。**

理由:
1. **転換率が実測で裏付けられている唯一の経路**が Zenn Books の事例（2,000PV → 5本）である。
2. Zenn/Qiita の読者は「開発者向けツールに金を払う」層と重なる。X のフォロワーは重ならないことが多い。
3. Discord/Slack は到達数が小さい代わりに、**有料化を断られた理由が直接聞ける**。10人フェーズでは売上より学習の方が価値が高い。
4. 「単一チャネルで最初の100人は取れない。4〜5チャネルを意図的な順序で回すことで複利が効く」という2026年の共通見解とも整合する `[推定]` → [Indie Hacker Marketing Playbook: 7 Channels That Actually Work in 2026](https://prems.ai/blog/indie-hacker-marketing-playbook-2026)

### 補足: 見落とされがちな最強チャネル = 手動アウトリーチ
- 2026年の複数の playbook が「**operator DM は最もスキップされるが、時間あたり転換率が最も高いチャネル**」と一致して指摘している `[推定]` → [Indie Hacker Marketing: 7-Channel Playbook (2026)](https://www.buildinpublic.so/blog/indie-hacker-marketing)
- 実例として、Proxycurl の Steven Goh は**コールドメールで最初の10人の有料顧客を獲得**している `[推定]` → [Indie hackers share how they got their first 10, 100, and 1,000 customers](https://www.indiehackers.com/post/indie-hackers-share-how-they-got-their-first-10-100-and-1-000-customers-620ce768ba)
- **日本での実装**: X で「〇〇で困っている」と呟いている人に、宣伝ではなく**その人の課題に対する回答＋（求められたら）リンク**を返す。1日3件×週5日 = 週30分。これが最も費用対効果が高い可能性が高い。

---

# 2. SEOの現状（2026年）

## 2-1. AI検索普及後、個人サイトのSEOはどうなったか

### 起きていること（数値）

| 指標 | 数値 | 出典 | 信頼度 |
|---|---|---|---|
| AI Overviews の到達 | 月間20億ユーザー超 | 各種2026年集計 | `[推定]` |
| 情報系クエリでの AIO 表示率 | 業界により 80〜88% | 同上 | `[推定]` |
| AIO 表示時の1位ページ CTR | **-58%**（Ahrefs） | [Ahrefs: AI Overviews Reduce Clicks](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update) | `[二次]` |
| 日本語メディアの報道 | **CTR -62.7%**、Google検索1位でもCTRは約9% | [Web担当者Forum（Ahrefs調べ）](https://webtan.impress.co.jp/n/2026/07/29/53036) | `[二次]` |
| Pew 調査 | AIO あり8% / なし15% のクリック率 | 各種2026年集計 | `[推定]` |
| AIO をトリガーするキーワード | **99.2%が情報収集意図**（Ahrefs） | 同上 | `[推定]` |
| 8語以上のロングテール・質問形クエリ | 短尾より AIO 表示率が**有意に高い** | 同上 | `[推定]` |
| 日本の AI検索利用率 | 8ヶ月で約3.5倍に拡大 | [月刊AI検索業界レポート2026年4月号](https://prtimes.jp/main/html/rd/p/000000023.000166736.html) | `[二次]` |

### 冷静な反対意見（重要）
「流入減の原因を全部AIのせいにするな」という指摘がある。SERP のレイアウト変更・コアアップデート・季節性など他要因との分離が必要 `[二次]` → [流入減の原因、本当にAIのせい？（株式会社JADE）](https://blog.ja.dev/entry/blog/2026/04/30/traffic-decline-not-always-ai)

### 個人サイトにとっての結論

**SEO は「死んだ」のではなく「効く領域が狭く・深くなった」。**

1. **情報収集型（"〇〇とは"）のロングテールは最も打撃を受けた。** ここを狙う従来型ブログ／アフィリ設計は 2026 年時点で成立しにくい。
2. **一方で、AI に引用されること（GEO）自体が新しい可視性資産になった。** クリックではなく引用が成果物。
3. **AI検索経由の訪問者は、従来検索経由より有料転換率が4〜5倍高い**という主張がある `[推定]` → [Generative Engine Optimization (GEO): The Complete 2026 Guide](https://www.enrichlabs.ai/blog/generative-engine-optimization-geo-complete-guide-2026)。数は減るが質は上がる。
4. **ChatGPT の Web 検索は Bing 由来。Bing Webmaster Tools への登録が実質必須。** また ChatGPT のトップ引用の約47.9%が Wikipedia という偏りがあり、**権威性のない新規ドメインは引用されにくい** `[推定]`

## 2-2. どんなキーワードなら個人が勝てるか

### 勝てる領域 ✅

| 領域 | なぜ勝てるか | 例 |
|---|---|---|
| **一次体験・実測データ** | AIが生成できない。「実際にやった数字」は引用もされる | 「Claude Code で〇〇を作った実測コスト」「Cloudflare Workers 無料枠を1ヶ月使い切った結果」 |
| **極端にニッチな技術の組み合わせ** | 大手が書く経済合理性がない | 「Hono + D1 + Stripe Webhook の実装」 |
| **新しすぎて記事が存在しない領域** | 先行者が居ない。リリース直後72時間が勝負 | 新SDK/新API/新モデルのリリース直後の解説 |
| **自作ツール名（指名検索）** | 競合ゼロ | プロダクト名そのもの |
| **エラーメッセージ全文** | 完全一致で刺さる。AIOも出にくい | `Error: xxx is not a function in yyy` |
| **体験ベースのYMYL周縁** | 「闘病記」「実際の投資体験」など体験談は個人が競合できる領域 `[二次]` → [YMYLとは？（2026年版）](https://www.webries.co.jp/seo/ymyl) | — |

大手が追わないニッチ専門領域では、専門性の高い個人が有利、という点は2026年の日本語SEO解説でも一貫している `[二次]` → [【2026年版】SEOキーワード選定の全手順](https://rank-quest.jp/column/column/keyword-selection/)

### 絶対に勝てない領域 ❌
- **YMYL のコア領域**: 医療（治療法・薬）、金融（投資商品・保険・ローン）、法律（相続手続き等）。E-E-A-T の壁で個人は上位化不可能 `[二次]`
- **Wikipedia / 官公庁 / 大手企業公式が上位を占める一般語**
- **「購入」「申込」「料金」等の商業キーワード**: 広告予算の殴り合いになる `[二次]`
- **AI で大量生成できる薄いページ全般**: 2025年8月・2026年3〜6月のアップデートで、薄いページ・重複した地域/サービスページ・AI大量生成コンテンツ・スパムリンクが繰り返し標的になっている `[二次]` → [Google June 2026 Spam Update](https://orangemonke.com/blogs/google-june-2026-spam-update/)
- **サイトレピュテーション濫用（他人のドメインを借りた寄生）**: 2025年8月〜9月の SpamBrain 更新でアルゴリズム対応化。**回復に3〜6ヶ月**かかる `[二次]` → [Google's Site Reputation Abuse: A 2026 Survival Guide](https://khalidseo.com/google-site-reputation-abuse-guide/)

## 2-3. ロングテール／ニッチキーワードの探し方（全部無料）

### 手順（週1時間で回す）

1. **Google Search Console**（要サイト所有）: 「検索パフォーマンス > クエリ」で **表示回数はあるがCTRが低い / 掲載順位11〜30位** のクエリを抽出。ここが最も費用対効果が高い。`[一次]`
2. **Google Keyword Planner**: 広告アカウント作成のみで無料。ボリューム帯の把握。`[一次]`
3. **Google Trends**: 上昇トレンドの検出。新技術は「まだ記事がない」領域を作る。`[一次]`
4. **サジェスト & 関連質問（People Also Ask）**: 検索窓に打つだけ。質問形をそのまま H2 にする（GEO対策と兼用）。
5. **Answer Socrates**: 1トピックで1,000以上のキーワードを生成できる無料ツール `[推定]` → [9 Best Free SEO Keyword Research Tools](https://blog.answersocrates.com/best-free-seo-keyword-research-tools/)
6. **LowFruits**: 低競合キーワードの発見に特化（無料枠あり）`[推定]`
7. **Ubersuggest**: 無料枠に日次制限あり `[推定]`
8. **Reddit / X / Discord のログ検索**: 「実際に困っている人の言葉」をそのままキーワードにする。**ツールより精度が高い場合が多い。**
9. **Bing Webmaster Tools**: ChatGPT 引用の前提となる Bing インデックス確認。無料。`[一次]`

参考: [The 5 Best Free Keyword Research Tools in 2026 (Zapier)](https://zapier.com/blog/best-keyword-research-tool/) / [The 10 Best Free Keyword Research Tools in 2026](https://gracker.ai/blog/best-free-keyword-research-tools)

### 選定基準（個人サイト用）
- 月間検索 **100〜1,000** のロングテール（3語以上）を狙う `[二次]`
- SERP 1ページ目に **個人ブログ・Zenn・Qiita が1件以上ある** → 参入可能のサイン
- 1ページ目が全て企業公式・Wikipedia・官公庁 → **撤退**

## 2-4. GEO（AI検索に引用されるための最低限）

工数: 記事1本あたり **+15分** で実装できる。やらない理由がない。

- [ ] 冒頭に **TL;DR / 結論の3行要約** を置く
- [ ] **Q → A 形式の見出し**（PAAの質問文をそのまま H2 に）
- [ ] **主張 → 根拠（数値・出典）** の構造で書く。AIはそのまま引用できる文を好む
- [ ] **データを表にする**
- [ ] **著者名・公開日・更新日を可視化**
- [ ] **1文を短く**（AIが逐語引用しやすい長さに）
- [ ] Schema.org 構造化データ（Article / FAQPage）
- [ ] **Bing Webmaster Tools に登録**（ChatGPT の引用元は Bing 経由）

出典: [Generative Engine Optimization (GEO) 2026 Guide (Frase)](https://www.frase.io/blog/what-is-generative-engine-optimization-geo) / [GEO: Getting Cited in ChatGPT, Claude, and Perplexity in 2026](https://www.aimagicx.com/blog/generative-engine-optimization-chatgpt-perplexity-2026) `[推定]`

---

# 3. ローンチ戦術

## 3-1. 「作る前に売る」検証（最優先。ここをサボると全部無駄になる）

### 検証の3段階

| 段階 | やること | 合格ライン | 工数 |
|---|---|---|---|
| **L0: 会話** | 想定ユーザー10人に「この課題、いくらまで払う？」と直接聞く（Discord/X DM） | 3人以上が「金額を口にする」 | 3h |
| **L1: LP + ウェイトリスト** | 1枚 LP を公開しメール登録を集める | 訪問→登録 **10%以上** | 4h |
| **L2: プレオーダー** | 完成前に実際に決済させる（返金保証付き） | **2件の課金** = 月商1,000円達成 | 3h |

### ウェイトリストの現実的なベンチマーク `[推定]`
- LP のメール登録転換率: **中央値2%、優秀20%、トップ20〜40%**。10%未満ならコピーかオファーが刺さっていない → [15 Waitlist Landing Page Examples That Convert (2026)](https://getlaunchlist.com/blog/waitlist-landing-page-examples-that-convert) / [Waitlist Landing Page Examples: 7 That Convert at 20%](https://www.flowjam.com/blog/waitlist-landing-page-examples-10-high-converting-pre-launch-designs-how-to-build-yours)
- 500人以上のウェイトリストを持つプロダクトは、コールドローンチの**3倍**転換する → [Pre-Launch Waitlist Strategy](https://beyondlabs.io/blogs/how-to-build-a-waitlist-that-turns-into-customers)

### ⚠️ 決定的な落とし穴
> **「ウェイトリストは興味を測るが、購買意図は測らない」**
> ウェイトリストを開く前に「登録者の何%が課金したら検証成功か」を決めておくこと。目標10%に対し実測1%なら、**登録数が増えていても検証は失敗している**。
> `[推定]` → [Pre-launch waitlists measure curiosity, not intent](https://www.saasvalidation.tech/pre-launch-waitlists-measure-curiosity-not-intent/)

→ **この制約下（週7〜12h）では、L1 をスキップして L0 → L2（プレオーダー）に直行するのが最も速い。** 「2人が実際に500円払う」で月商1,000円は達成であり、同時に最強の検証でもある。

### 高転換 LP の共通パターン `[推定]`
1. **成果を名指しするヘッドライン**（機能名ではなく結果）
2. **ファーストビューに CTA は1つだけ**
3. **具体的な社会的証明**（「〇人が使っています」より「Aさんの実測でX分短縮」）
4. **確認ページに紹介インセンティブ**
5. **ナビゲーションを置かない**（離脱先を作らない）

## 3-2. ローンチ実践手順

### A. Zenn ローンチ（日本語商材・最優先）

**タイミング**: 平日 **火〜木の 8:00〜9:30 または 21:00〜22:30**（通勤・帰宅後の閲覧ピーク帯）`[推定]`

手順:
1. **記事の主題を「プロダクト紹介」にしない。** 「◯◯という技術課題をこう解いた」にする。
2. 記事構成: 課題 → ハマった点 → 実装（コード） → 実測数値 → 「ついでに作ったのがこれです」（末尾で1回だけリンク）
3. **必ず数字を入れる**（実行時間、コスト、削減した手作業の分数）。数字がある記事は引用され、はてブされる。
4. 公開直後に X で告知（**本文はネイティブ、リンクは1リプ目**）
5. 24時間後に Qiita へ「切り口を変えた別記事」を投稿（コピペ不可）
6. 1週間後に note で「作った経緯と収益」記事

工数: 1ローンチあたり **6〜8時間**

### B. X ローンチ

**タイミング**: 平日 **12:00〜13:00 / 21:00〜23:00**（日本の個人開発クラスタの活動時間）`[推定]`

投稿テンプレ（本文にリンクを入れない）:
```
【作った】〇〇を△分で終わらせるツールを作りました

きっかけ: 毎週△時間かけて手作業していた〇〇が苦痛だったから

・◇◇ができる
・◆◆は不要
・料金は月500円（無料枠あり）

作るのにかかった時間: XX時間 / 運用コスト: 月XX円

↓ リプに詳細と記事のリンク置きます
[GIF or スクショ]
```
1リプ目: `記事: <Zenn URL>` `プロダクト: <URL>`

### C. Product Hunt ローンチ（英語版がある場合のみ / Phase 3）

準備タイムライン（合計10〜15h）:
| いつ | やること | 工数 |
|---|---|---|
| T-14日 | PH アカウント作成、他プロダクトに毎日コメント（アカウント信用の蓄積） | 15分/日 |
| T-10日 | サムネイル（240×240）、ギャラリー画像5枚、60秒デモ動画 | 4h |
| T-7日 | ウェイトリスト／メルマガ／Discord に「◯日にローンチします」と予告 | 1h |
| T-1日 | 支援を頼む相手20〜50人に個別に連絡（**「upvote して」とは書かない＝規約違反リスク**。「見てフィードバックください」と書く） | 2h |
| T日 0:01 PT | 公開。最初の4時間が最重要 | 当日張り付き4h |
| T日 | 全コメントに1時間以内に返信 | 3h |
| T+1日 | 結果をブログ化（これ自体が次のコンテンツ） | 2h |

**⚠️ 2026年の前提**: 「PH #1 を取った」だけでアクティベーション数値がないと、むしろマイナス評価に読まれる。**順位より、受け皿（オンボーディング・課金導線）が整っているかが重要。** `[推定]`

### D. Show HN（英語版がある場合 / ダメ元）
- タイトルは `Show HN: <一言で何か> (<URL>)` の形式。宣伝文句を入れない。
- 投稿は **米国東部時間の平日 8:00〜10:00 頃**（HN のアクティブ帯）`[推定]`
- 最初のコメントに自分で「作った動機・技術構成・料金」を書く。
- 工数2h、成功率10%。**期待値ゼロで撃つ。**

## 3-3. 無料 → 有料の転換設計

### ベンチマーク（2026年）

| 指標 | 数値 | 出典 | 信頼度 |
|---|---|---|---|
| フリーミアム → 有料（中央値） | **2〜5%** | [Freemium Conversion Rate Benchmarks 2026](https://www.artisangrowthstrategies.com/blog/freemium-conversion-rate-benchmarks) | `[二次]` |
| 良い / 優秀 | 3〜5% / 8〜12% | 同上 | `[二次]` |
| 広い市場向けツール | 1〜5% | [ChartMogul SaaS Conversion Report](https://chartmogul.com/reports/saas-conversion-report/) | `[二次]` |
| 狙いを絞った高インテント SaaS | 5〜15% | 同上 | `[二次]` |
| 分布 | 4分の1が2.5%未満 / 約3分の1が2.5〜7.5% / 4分の1が10〜15% | [Free-to-Paid Conversion Benchmarks by Product Type](https://knowledgelib.io/finance/saas-benchmarks/free-to-paid-conversion-benchmarks/2026) | `[二次]` |
| **使用量制限は機能制限より 1.5〜2倍 転換が高い** | 1.5〜2× | 同上（200製品調査 / 2026年1月） | `[二次]` |
| 7日トライアル | 約40.4% | [Free Trial Conversion Statistics for 2026](https://www.shno.co/marketing-statistics/free-trial-conversion-statistics) | `[推定]` |
| 14日トライアル（3日目・7日目のチェックイン付き） | **44.1%（最高）** | 同上 | `[推定]` |
| 61日以上 | 約30.6% | 同上 | `[推定]` |
| 14日が標準 | 調査200製品の **62%** が採用 | 同上 | `[推定]` |

### 設計の定石（この規模での推奨）

> **推奨: 「使用量制限型フリーミアム」。機能は全部見せて、回数だけ絞る。**

理由: 使用量制限は機能制限より1.5〜2倍転換が高い `[二次]`。かつ機能ゲートの実装コストが低い（カウンター1つで済む）。

具体例:
- 「月10回まで無料 / 500円で無制限」
- 「3ファイルまで無料 / 500円で無制限」
- 「直近7日分の履歴まで無料 / 500円で全期間」

やってはいけない設計:
- ❌ 無料版が使いにくすぎる（価値を体験する前に離脱）
- ❌ 30日以上のトライアル（転換率が落ちる `[推定]`）
- ❌ クレジットカード登録を最初に要求（会員登録なしで価値を出してから）

### 逆算表: 月商目標に必要な数字（500円/月のサブスクの場合）

| 月商 | 必要有料ユーザー | 転換率3%なら必要無料ユーザー | 転換率1%なら | LP転換5%なら必要訪問（3%時） |
|---|---|---|---|---|
| 1,000円 | 2人 | 67人 | 200人 | 1,340訪問 |
| 1万円 | 20人 | 667人 | 2,000人 | 13,400訪問 |
| 10万円 | 200人 | 6,667人 | 20,000人 | 134,000訪問 |

> **重要な示唆: 月10万円を「500円 × 200人」で取るのは、個人の集客量では現実的に厳しい。**
> 月10万円フェーズでは以下のいずれかへの転換が必要:
> - **価格を上げる**（2,000円 × 50人 / 5,000円 × 20人 = B2B寄りに寄せる）
> - **買い切りの高単価商品**（技術書・テンプレート 3,000〜10,000円）
> - **広告収益モデル**（月100万PV級。文字数カウンターアプリが70万DL・累計700万円超という事例あり `[推定]` → [個人開発の成功事例15選](https://shiftb.dev/articles/indie-dev-success-stories)）

### 決済プラットフォーム別の手取り（500円の商品を1本売った場合）`[二次]`

| プラットフォーム | 手数料 | 500円販売時の手取り目安 | 備考 |
|---|---|---|---|
| **Stripe（自前）** | 3.6% | 約482円 | 国内向けサービスなら第一候補 |
| **BOOTH（デジタル）** | 決済3.6%+22円 + 販売5.6% ≒ 約9% | 約455円 | すぐ売りたい国内向けに最適 |
| **Zenn Books** | Zenn の販売手数料に準拠 | — | 技術書に最適。読者と販路が一体 |
| **note** | 利用料10% + 決済5〜15% ≒ 15〜25% | 約375〜425円 | **最も手数料が重い**。集客力とのトレードオフ |
| **Gumroad** | 10%（直販） | 約450円 | 英語圏向け |
| **Polar.sh** | — | — | 海外向け SaaS/開発者ツールの推奨先 |

出典: [【2026年版】デジタル商品販売プラットフォーム「手数料・特徴」徹底比較マップ](https://note.com/ngr_id/n/n850e38ef413d) / [【2026年最新版】個人開発の決済プラットフォーム徹底比較](https://note.com/karanobu/n/n29b20e81b333) / [デジタルコンテンツ販売の手数料比較【2026年版】](https://fuku-mitsu.com/article/digital-content-platform-hikaku/)

---

# 4. 測定

## 4-1. アクセス解析ツールの比較（2026年）

| ツール | 無料枠 | Cookie/同意バナー | 特徴 | 推奨度 |
|---|---|---|---|---|
| **Cloudflare Web Analytics** | **完全無料**（Cloudflare 利用時） | 不要 | サンプリングあり。導入が最も楽 | ★★★★☆ 最初はこれ |
| **Umami Cloud** | **無料 Hobby 枠あり**（10万イベント/月・3サイト） | 不要 | MIT ライセンス、セルフホストも無料 | ★★★★★ **本命** |
| **Umami（セルフホスト）** | 無料（サーバー代のみ） | 不要 | 完全自前 | ★★★★☆ |
| **Plausible** | **無料枠なし**（$9/月〜） | 不要 | UI が最も洗練。スクリプト1KB未満 | ★★★☆☆ 予算が出るなら |
| **GA4** | 無料 | **必要**（Cookie利用） | 高機能だが重い（gtag は gzip 後で約50KB超）。UI が個人には過剰 | ★★☆☆☆ |

出典: [Privacy-First Analytics Compared (2026)](https://scripts.nuxt.com/learn/privacy-first-analytics-compared) / [Best Free Web Analytics in 2026](https://klymentiev.com/blog/best-free-analytics-2026) / [10 Best Web Analytics Tools in 2026](https://bootstrap.build/articles/best-web-analytics-tools/) `[二次]`

### 推奨構成（月0円）
```
Umami Cloud（無料枠）        … サイト行動の計測
+ Google Search Console      … 検索クエリと順位（SEOの唯一の一次情報源）
+ Bing Webmaster Tools       … ChatGPT 引用の前提となる Bing インデックス確認
+ Stripe ダッシュボード       … 売上・解約
```
GA4 は「後で必要になったら」で良い。**同意バナーを置く必要が生じる時点で、個人サイトにはコストの方が大きい。**

## 4-2. 最初期に見るべき指標は3つだけ

「PV」「フォロワー数」「いいね数」は**全部見るな**。行動を変えない数字だから。

| # | 指標 | 定義 | 見方 | なぜこれか |
|---|---|---|---|---|
| **1** | **有料顧客数（実数）** | 実際に課金した人の頭数 | 週次で数える。0→1→2 と整数で追う | 唯一の真実。月商1,000円は「2」という整数 |
| **2** | **アクティベーション率** | 訪問者のうち「価値を一度体験した人」の割合（例: ツールを1回実行完了した割合） | 週次%。**20%を下回るならプロダクトかオンボーディングの問題**で、集客を増やしても無駄 | 集客の問題か製品の問題かを切り分ける唯一の指標 |
| **3** | **チャネル別の「アクティベーション到達者数」** | 流入元ごとに #2 を満たした人数 | 週次。**PVではなく人数で比較** | どのチャネルに次週の時間を投じるかを決める。PVで比較すると必ず判断を誤る |

### 補助指標（月次で見る、週次では見ない）
- Search Console の「掲載順位11〜30位のクエリ数」（=SEO資産の育ち具合）
- メルマガ登録者数（=次のローンチの弾薬）

### ⚠️ アンチパターン
- 「Product Hunt で1万PV来た！」→ **アクティベーション到達者が5人なら、Zenn記事1本（300PV / 到達者8人）に負けている。**
- ダッシュボードを毎日見る → 意思決定は週1回で十分。**毎日見る時間を1本の記事に回す。**

---

# 5. 90日集客カレンダー

## 前提
- 週の予算: **平日夜 5〜10h + 週末 2〜4h = 週7〜12h**
- 各週の配分を「作る」「書く」「話す」の3つに固定する
- 月商目標: Day 30 で1,000円 / Day 90 で1万円

## Phase 1: Day 1〜30 —「売れるかを確かめて、2人から金を取る」

| 週 | 作る（開発） | 書く（コンテンツ） | 話す（コミュニティ/DM） | 週工数 |
|---|---|---|---|---|
| **W1** | LP 1枚 + メール登録フォーム。Umami / GSC / Bing 設置 | Zenn記事①「〇〇という課題をこう解いた」（プロダクト未完成でOK） | 個人開発 Discord/Slack を3つ選んで参加。**宣伝しない。質問に3回答える** | 10h |
| **W2** | MVP のコア機能1つだけ実装（使用量制限のカウンター含む） | Zenn記事②（技術の深掘り） / X 毎日1投稿（進捗＋スクショ） | 想定ユーザー10人に DM で「いくらなら払う？」を聞く（**L0検証**） | 11h |
| **W3** | Stripe or BOOTH の決済導線を通す。**返金保証を明記** | 記事①②の末尾に「作りました」リンクを追記 / Qiita に切り口違いで1本 | Discord の宣伝チャンネルに初投稿（参加3週目なので許容される） | 10h |
| **W4** | **プレオーダー開始**（未完成でも売る／返金保証付き） | note①「〇〇を作って売るまでの全記録」 / X でローンチ投稿 | W2 で「払う」と言った人に個別に案内 → **ここで2件取る** | 11h |

**Day 30 チェックポイント**: 有料顧客2人 = 月商1,000円 ✅
- 未達なら → **プロダクトを変えるのではなく、DM の相手を変える**（30人に聞いて誰も払わないなら課題設定が間違い）

## Phase 2: Day 31〜60 —「経路を1本に絞って太らせる」

| 週 | 作る | 書く | 話す | 週工数 |
|---|---|---|---|---|
| **W5** | 顧客2人のフィードバックだけを実装（他は無視） | Zenn記事③ / **メルマガ開始（第1号）** | 顧客2人に30分ヒアリング（録音して記事化） | 10h |
| **W6** | オンボーディング改善（アクティベーション率を測って20%超を目指す） | Zenn記事④ / SEO用ロングテール記事①（GSCの11〜30位クエリから選定） | X で「困っている人」に3件/日リプライ（宣伝せず助ける） | 11h |
| **W7** | 使用量制限のチューニング（無料枠を狭める/広げるA/B） | 記事⑤ / note②「月商1,000円までの実数字」（**収益公開は日本で最も読まれる**） | IDEAVALU に掲載申請 | 10h |
| **W8** | 課金導線の摩擦を1つ削る | 記事⑥ / メルマガ第2号 | Discord で「使ってくれた人」に感謝DM → 紹介依頼 | 10h |

**Day 60 チェックポイント**: 有料顧客 5〜8人 / メルマガ 30〜50人 / Zenn 累計6本
- **最も伸びたチャネル1つを特定し、Day 61 以降は工数の70%をそこに寄せる**

## Phase 3: Day 61〜90 —「資産化と英語圏の一撃」

| 週 | 作る | 書く | 話す | 週工数 |
|---|---|---|---|---|
| **W9** | 英語 LP を用意（Claude Code で翻訳＋自分で校正） | SEO記事②③（GEOチェックリスト適用） | Reddit の関連 sub に参加開始（**宣伝せず4週間**） | 11h |
| **W10** | 高単価プラン or 買い切り商品を設計（2,000円 or 3,000円の技術書） | Zenn Books の執筆開始 / メルマガ第3号 | Product Hunt アカウント育成（毎日コメント15分） | 11h |
| **W11** | PH 用アセット（サムネ・ギャラリー5枚・60秒動画） | 記事⑦ / PH 予告をメルマガとXへ | 支援を頼む相手20〜50人に個別連絡 | 12h |
| **W12** | **Product Hunt ローンチ（0:01 PT）+ Show HN（ダメ元）** | 当日: 全コメント1時間以内返信 / 翌日: 結果記事 | 新規流入をメルマガに落とす | 12h |

**Day 90 チェックポイント**: 有料顧客 15〜25人 or 買い切り販売20本前後 = **月商1万円**
- 未達で最も多い原因は「記事本数の不足」。Day 90 時点で **Zenn/Qiita 累計10本未満なら、それが唯一のボトルネック**。

## 毎週の固定ルーティン（合計 約3.5h）

| 曜日 | 時間 | やること |
|---|---|---|
| 月〜金 | 各15分 | X: 他人の投稿に良質リプライ3件（自分の投稿より優先） |
| 火 or 木 | 2h | 記事執筆（1本を2週で仕上げる） |
| 水 | 20分 | Discord/Slack で誰かの質問に答える |
| 土 | 30分 | 指標レビュー（有料顧客数 / アクティベーション率 / チャネル別到達者数の3つだけ） |
| 日 | 30分 | 翌週の計画。**「捨てるチャネル」を1つ決める** |

---

# 6. すぐ使えるテンプレート

## 6-1. Zenn / Qiita 記事テンプレ（規約に触れない構造）

```markdown
# 〈技術課題〉を〈手法〉で解決した話

## TL;DR
- 〈課題〉に〈X時間/回〉かかっていた
- 〈手法〉で〈Y分〉になった（〈Z%〉削減）
- コストは月〈N〉円

## 背景（なぜ困っていたか）
（自分の実体験。ここが一次情報になる）

## やったこと
（コード。動くもの）

## ハマったポイント
（他の記事に書いてない失敗。ここが最も読まれる）

## 実測結果
| 項目 | Before | After |
|---|---|---|
| 所要時間 | | |
| コスト | | |

## おわりに
この処理を Web からも使えるようにしたものを公開しています → 〈リンク1つだけ〉
```

**禁止事項**: 記事の主題をプロダクト紹介にしない / アフィリエイトリンクを貼らない / 同一内容を複数プラットフォームにコピペしない。

## 6-2. コミュニティでの自己紹介 → 宣伝の型（参加3週間目に投げる）

```
（宣伝チャンネルにて）
〇〇です。3週間ほどこちらで質問に答えていました。

自分が毎週△時間かけていた〈作業〉が嫌すぎて、自動化ツールを作りました。
・〈できること〉
・月10回まで無料 / それ以上は月500円

正直まだ粗いので、辛口のフィードバックが一番ありがたいです。
使ってダメだった点を教えてくれた方には、有料版を無期限で無料にします。
〈URL〉
```
ポイント: **「買ってください」ではなく「壊してください」と言う。** 最初の10人フェーズでは、フィードバックを対価にする方が反応が取れる。

## 6-3. 課題ヒアリングDM（L0検証用）

```
はじめまして。〇〇の投稿を拝見しました。

自分も〈同じ課題〉で困っていて、解決するツールを作ろうとしています。
売り込みではなく、3つだけ教えていただけませんか。

1. その作業、月にどれくらい時間を取られていますか？
2. 今はどうやって回避していますか？
3. 月いくらまでなら、それがゼロになることにお金を払いますか？

お礼にできたら無料でお使いいただけるようにします。
```
**「3. いくら払うか」を必ず聞く。** ここで金額を口にしない人は、完成しても買わない。

## 6-4. メルマガ 第1号テンプレ

```
件名: 〈プロダクト名〉を作っています（第1号）

登録ありがとうございます。〇〇です。
このメールは月2回、〈テーマ〉について、実際にやって出た数字だけを書きます。

今回の数字:
・〈指標〉: 〈値〉
・〈指標〉: 〈値〉

わかったこと:
（3行）

来週やること:
（3行）

返信で「今こういうことに困っている」と教えてもらえると、次回それを調べます。
```
**返信を求める。** 開封率よりも返信数の方が、初期の役に立つ情報が多い。

---

# 7. リスクと注意点

| リスク | 内容 | 対策 |
|---|---|---|
| **Qiita の規約違反** | 「広告・宣伝／商用勧誘（SEO・アフィリエイト目的の投稿を含む）」は明示的に禁止 `[一次]` | 記事本体を知識共有として成立させ、リンクは末尾に1つ |
| **Zenn の AI コンテンツ方針** | 2026年3月に方針更新。AI執筆は禁止されないが「人主体」が求められる `[二次]` | 必ず自分の実測データ・失敗談を入れる |
| **Reddit のサスペンド** | 2026年半ばからサイレントBANではなく明示的サスペンドに `[二次]` | 参加4週間・宣伝は求められてから |
| **X のリンク抑制** | 2026年3月以降、非Premiumのリンク投稿は到達がほぼ消える `[推定]` | リンクは1リプ目 or bio |
| **Google のスパム/AI量産対策** | 薄いページ・AI大量生成が繰り返し標的に。回復に3〜6ヶ月 `[二次]` | 記事数より1本の一次情報密度を優先 |
| **AI Overviews による情報系流入の消滅** | 情報収集型ロングテールは CTR が半減以下 `[二次]` | 「実測データ」「エラーメッセージ」「新技術直後」へ寄せる + GEO |
| **⚠️ バズ依存** | はてブ・Show HN・PH #1 はいずれも再現性がない | **計画に組み込まない。** 起きたらボーナスとして扱う |
| **note の手数料** | 実質15〜25%が抜ける `[二次]` | 集客記事は note、決済は Stripe/BOOTH に分ける |

---

# 8. 出典一覧

## 日本語
- [Qiita 利用規約](https://qiita.com/terms) / [Qiita コミュニティガイドライン](https://help.qiita.com/ja/articles/qiita-community-guideline)
- [Zenn コミュニティガイドライン](https://zenn.dev/guideline) / [AIによるコンテンツ執筆に関するZennの方針](https://info.zenn.dev/2026-03-10-ai-contents-guideline)
- [Zenn 会員数10万人突破（クラスメソッド プレスリリース）](https://prtimes.jp/main/html/rd/p/000000357.000014901.html)
- [Zenn Books に500円の技術書を出して5冊売れた話](https://qiita.com/sakutto-panda/items/62a973b2ddce6da4437f)
- [Zennを1年間運営した結果、PV数やフォロワー数はどう変化したのか？](https://zenn.dev/gachigachi/articles/c1ed7372f23252)
- [zennのPVって正直どれくらいなの？](https://zenn.dev/miya_tech/articles/8d4cbb0ff52147)
- [個人開発で月1万円を達成！収益化のリアルな工夫と数字を全公開](https://note.com/tty215/n/n8d9b13f5d83b)
- [【個人開発で暮らす】月1万円の売上を達成しました](https://note.com/nosuke0926/n/n3e06b6b48c94)
- [個人開発の成功事例15選 — 収益化の共通点を徹底分析【2026年最新】](https://shiftb.dev/articles/indie-dev-success-stories)
- [フリーランスエンジニアの個人開発で稼ぐ方法2026](https://syusodo.co.jp/workee-freelance-blog/articles/freelance-engineer-indie-dev-income-2026)
- [AI Overviewsでクリック率が62.7％減（Web担当者Forum / Ahrefs調べ）](https://webtan.impress.co.jp/n/2026/07/29/53036)
- [流入減の原因、本当にAIのせい？（株式会社JADE）](https://blog.ja.dev/entry/blog/2026/04/30/traffic-decline-not-always-ai)
- [月刊AI検索業界レポート2026年4月号（AI検索利用率が8ヶ月で約3.5倍）](https://prtimes.jp/main/html/rd/p/000000023.000166736.html)
- [【2026年版】SEOキーワード選定の全手順](https://rank-quest.jp/column/column/keyword-selection/) / [YMYLとは？【2026年版】](https://www.webries.co.jp/seo/ymyl)
- [生成AI時代にアフィリエイトサイトはどう生き残るか](https://qask.tech/blog/ai-affiliate-new-revenue-models/)
- [【2026年版】デジタル商品販売プラットフォーム 手数料・特徴 徹底比較マップ](https://note.com/ngr_id/n/n850e38ef413d)
- [【2026年最新版】個人開発の決済プラットフォーム徹底比較](https://note.com/karanobu/n/n29b20e81b333)
- [デジタルコンテンツ販売の手数料比較【2026年版】](https://fuku-mitsu.com/article/digital-content-platform-hikaku/)
- [ProductHuntへ個人開発サービスを投稿するまでにやったこと](https://zenn.dev/nice2have/articles/120b1df8fcea2a)
- [個人開発サービス「Moyuk」をProduct Huntでローンチするまでの道のりと教訓](https://note.com/kohii/n/n6db88c7f429d)
- [IDEAVALU（国内向けプロダクトローンチ）](https://www.ideavalu.com/)
- [はてなブックマークでバズった威力](https://www.taikimedia.com/entry/Hatena.Bookmark.access) / [はてなブックマーク数と流入の関係](https://analytics.hatenadiary.com/entry/20090822/p1)
- [起業家向けオンラインコミュニティ10選](https://harmonic-society.co.jp/online-community-startup/) / [新人プログラマが入っておくといいSlack/Discordサーバー](https://qiita.com/asakuraTsukazaki/items/b980ab16c242229cd8bc)
- [ショート動画トレンド2026](https://0120.co.jp/blog/video-43/) / [ショート動画の収益化条件2026](https://0120.co.jp/blog/video-114/)

## 英語
- [Ahrefs: AI Overviews Reduce Clicks](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update)
- [Product Hunt Launch Statistics for 2026 (shno.co)](https://www.shno.co/marketing-statistics/product-hunt-launch-statistics)
- [Product Hunt traffic 2026: real numbers by daily rank](https://hub.causo.ai/guides/product-hunt-traffic-data-2026) / [Product Hunt launch 2026: the realistic playbook](https://hub.causo.ai/guides/product-hunt-launch-2026-realistic-playbook)
- [Product Hunt Launch Data: 5 Founders, 8 Questions](https://happysupport.ai/blog/product-hunt-launch-roundup-2026)
- [Product Hunt Launch: Get Upvotes & Rank #1 in 2026](https://trendgap.io/blog/product-hunt-launch-upvotes-rank-2026)
- [How to Launch Your Startup on Hacker News - Show HN](https://www.stackmatix.com/blog/launching-on-hacker-news)
- [The complete guide to Reddit self-promotion rules in 2026](https://redship.io/blog/reddit-self-promotion-rules) / [Reddit Self-Promotion Rules: The Complete Guide (2026)](https://founderreply.com/guides/reddit-self-promotion-rules)
- [Reddit Promotion for Indie iOS Apps: The Honest 2026 Playbook](https://screenfast.app/blog/reddit-promotion-indie-ios-app)
- [How to Grow on X (Twitter) 2026](https://grahammann.net/blog/how-to-grow-on-x-twitter-2026) / [The X Algorithm in 2026 (OpenTweet)](https://opentweet.io/blog/how-twitter-x-algorithm-works-2026)
- [Indie Hacker Marketing: 7-Channel Playbook (2026)](https://www.buildinpublic.so/blog/indie-hacker-marketing) / [Indie Hacker Marketing Playbook: 7 Channels That Actually Work in 2026](https://prems.ai/blog/indie-hacker-marketing-playbook-2026)
- [Indie hackers share how they got their first 10, 100, and 1,000 customers](https://www.indiehackers.com/post/indie-hackers-share-how-they-got-their-first-10-100-and-1-000-customers-620ce768ba)
- [$0 CAC, 1,000 email subscribers, and a 56% open rate](https://www.indiehackers.com/post/0-cac-1-000-email-subscribers-and-a-56-open-rate-heres-how-23c73c5553)
- [12 Free Distribution Channels for Indie Hackers (Tested on 30+ Channels)](https://shippedsolo.com/blog/12-free-distribution-channels-for-indie-hackers/)
- [ChartMogul: The SaaS Conversion Report](https://chartmogul.com/reports/saas-conversion-report/)
- [Freemium Conversion Rate Benchmarks 2026 (2–5% Typical)](https://www.artisangrowthstrategies.com/blog/freemium-conversion-rate-benchmarks)
- [Free-to-Paid Conversion Benchmarks by Product Type](https://knowledgelib.io/finance/saas-benchmarks/free-to-paid-conversion-benchmarks/2026)
- [Free Trial Conversion Statistics for 2026](https://www.shno.co/marketing-statistics/free-trial-conversion-statistics)
- [15 Waitlist Landing Page Examples That Convert (2026)](https://getlaunchlist.com/blog/waitlist-landing-page-examples-that-convert)
- [Pre-launch waitlists measure curiosity, not intent](https://www.saasvalidation.tech/pre-launch-waitlists-measure-curiosity-not-intent/)
- [Pre-Launch Waitlist Strategy: Build & Convert 400+ Leads](https://beyondlabs.io/blogs/how-to-build-a-waitlist-that-turns-into-customers)
- [What is Generative Engine Optimization (GEO)? 2026 Guide (Frase)](https://www.frase.io/blog/what-is-generative-engine-optimization-geo)
- [Generative Engine Optimization (GEO): The Complete 2026 Guide (Enrich Labs)](https://www.enrichlabs.ai/blog/generative-engine-optimization-geo-complete-guide-2026)
- [GEO: Getting Cited in ChatGPT, Claude, and Perplexity in 2026](https://www.aimagicx.com/blog/generative-engine-optimization-chatgpt-perplexity-2026)
- [The 5 Best Free Keyword Research Tools in 2026 (Zapier)](https://zapier.com/blog/best-keyword-research-tool/) / [The 10 Best Free Keyword Research Tools in 2026](https://gracker.ai/blog/best-free-keyword-research-tools) / [9 Best Free SEO Keyword Research Tools](https://blog.answersocrates.com/best-free-seo-keyword-research-tools/)
- [Privacy-First Analytics Compared (2026)](https://scripts.nuxt.com/learn/privacy-first-analytics-compared) / [Best Free Web Analytics in 2026](https://klymentiev.com/blog/best-free-analytics-2026) / [10 Best Web Analytics Tools in 2026](https://bootstrap.build/articles/best-web-analytics-tools/)
- [Google's Site Reputation Abuse: A 2026 Survival Guide](https://khalidseo.com/google-site-reputation-abuse-guide/) / [Google June 2026 Spam Update](https://orangemonke.com/blogs/google-june-2026-spam-update/)
- [Email Newsletter Stats: Open Rate, CTR & ROI Data in 2026](https://designmodo.com/email-newsletter-stats/)

---

*作成日: 2026年8月29日 / 調査手法: Web検索ベース。一次ソース本文の直接取得はネットワーク制限により不可のため、信頼度タグを併記した。数値を意思決定に使う前に、`[推定]` タグのものは元記事の方法論を確認すること。*
