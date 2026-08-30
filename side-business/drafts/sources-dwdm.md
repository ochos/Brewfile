# 出典リスト — DWDM / OSNR

**作成日**: 2026-08-30
**担当**: 公開一次情報の収集
**目的**: 前職の社内資料に一切依存せず、**未ログインで誰でも開ける公開情報だけ**で記事①（OSNR）と本（1〜6章）の技術的裏付けを取る

---

## 0. 最初に読むこと — この文書の重大な制約

> **この調査環境（Claude Code Remote）からは、外部サイトへの HTTP アクセスが組織のエグレスポリシーで全面的に遮断されていた。**
> そのため、**当初の任務である「WebFetch による未ログイン検証」は 1 件も実行できていない。**

### 検証を試み、遮断されたドメイン（実測）

| ドメイン | 結果 |
|---|---|
| `www.itu.int` | `EGRESS_BLOCKED` / curl でも `CONNECT tunnel failed, response 403`（組織ポリシーによる拒否） |
| `www.ciena.com` | `EGRESS_BLOCKED` |
| `www.viavisolutions.com` | `EGRESS_BLOCKED` |
| `www.exfo.com` | `EGRESS_BLOCKED` |
| `www.keysight.com` | `EGRESS_BLOCKED` |
| `www.anritsu.com` | `EGRESS_BLOCKED` |
| `courses.ece.ucsb.edu` | `EGRESS_BLOCKED` |
| `par.nsf.gov` | `EGRESS_BLOCKED` |
| `arxiv.org` | `EGRESS_BLOCKED` |
| `en.wikipedia.org` | `EGRESS_BLOCKED` |
| `www.nist.gov` | `EGRESS_BLOCKED` |

`curl` でも `github.com` 以外は全て `CONNECT tunnel failed (403)`。
プロキシの `__agentproxy/status` は `recentRelayFailures: []`、TLS 設定は正常。つまり**証明書の問題ではなく、許可ドメインリストによる拒否**。README の指示どおり、迂回はしていない。

### したがって本文書の位置づけ

- **第1章「採用リスト」は 0 件**である。「開けることを確認した」と言える URL は 1 本も存在しない。
- 代わりに**第2章「検証待ち候補リスト」**を作った。これは WebSearch（検索インデックス）経由で実在と概要を確認した候補群であり、**本人が手元のブラウザで開いて初めて「採用」になる**。
- 各候補には「そこから使えるはずの内容」を書いたが、**これは検索インデックスのスニペット由来であり、原典を直接読んだものではない**。**引用する前に必ず原典で裏を取ること。**
- 第3章「不採用リスト」は、**URL 構造・提供形態から未ログインでは開けないと判断できるもの**（顧客ポータル、有償規格販売サイト等）。これも実測ではなく構造判断である旨を各行に明記した。

### ⚠️ 執筆時の絶対ルール（この制約から自動的に出てくる）

1. **第2章の候補を、本人がブラウザで開いて確認するまで、記事に一切書かない。**
2. **本文書の「使える内容の要点」を、そのまま記事に転記しない。**（原典未読の要約であり、誤りが混入しうる）
3. 第3章の URL は、**記憶からでも書かない**（記事①骨子の方針どおり）。

---

## 1. 採用リスト（検証済み・未ログインで開けた）

**0 件。**

理由: 上記のとおり、この環境から外部 HTTP アクセスが全面遮断されており、検証行為そのものが実行不能だった。
「たぶん開ける」を採用扱いにすると、この文書の唯一の価値（検証済みであること）が失われるため、**空欄のまま残す。**

本人が第2章の候補を検証したら、その結果をこの章に移してください。記入フォーマット:

```
| トピック | タイトル | URL | 発行元 | 検証日 | 未ログイン可否 | 使える内容 |
|---|---|---|---|---|---|---|
```

---

## 2. 検証待ち候補リスト

**すべて「未検証」。本人がブラウザ（シークレットウィンドウ推奨）で開いて確認すること。**
シークレットウィンドウを使う理由: 通常ウィンドウだと既存ログインセッションが効いてしまい、「未ログインで開けるか」の判定にならない。

### A. OSNR（記事① 最優先）

#### A-1. ITU-T 勧告（一次規格。最重要だが最も検証が必要）

ITU-T 勧告は**公式には 2007 年以降、無償ダウンロード可**とされているが、この環境では検証できていない。
`itu.int` の PDF は `dologin_pub.asp` という紛らわしいパスを使うが、これは**課金ログインではない**とされる。**必ず自分で確かめること。**

| # | 勧告 | 内容（記事のどこで効くか） | ランディング URL | PDF 直リンク（検索で観測された形） |
|---|---|---|---|---|
| A-1-1 | **G.697** Optical monitoring for DWDM systems | **OSNR の定義と参照帯域の考え方の本丸。§3節の一次出典候補No.1** | `https://www.itu.int/rec/T-REC-G.697/en` | `https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-G.697-200911-S!!PDF-E&type=items` |
| A-1-2 | **G.680** Physical transfer functions of optical network elements | **多段接続での OSNR 累積。Appendix II に「複数 ONE をカスケードしたときの OSNR への影響の計算例」がある（§4節）** | `https://www.itu.int/rec/T-REC-G.680-200707-I` | `https://www.itu.int/rec/dologin_pub.asp?lang=f&id=T-REC-G.680-200707-I!!PDF-E&type=items` |
| A-1-3 | **G.698.2** Amplified multichannel DWDM applications with single channel optical interfaces | 増幅多重区間のインタフェース規定。OSNR 要求値の記法 | `https://www.itu.int/rec/T-REC-G.698.2/en` | `https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-G.698.2-201811-I!!PDF-E&type=items` |
| A-1-4 | **G.Sup42** (G-series Supplement 42) Guide on the use of ITU-T Recommendations related to optical technology | **勧告間の関係を解説する「地図」。どの勧告を引けばよいか迷ったときの入口** | — | `https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-G.Sup42-201404-S!!PDF-E&type=items` |
| A-1-5 | **G.692** Optical interfaces for multichannel systems with optical amplifiers | 光増幅器つき多重系のインタフェース（古いが OSNR 設計の原型） | `https://www.itu.int/rec/T-REC-G.692/en` | 未取得 |
| A-1-6 | **G.663** Application related aspects of optical amplifier devices and subsystems | **EDFA の ASE と雑音指数、非線形効果の実務的側面（§4節・本4章）** | `https://www.itu.int/rec/T-REC-G.663/en` | 未取得 |
| A-1-7 | **G.661** Definitions and test methods for optical amplifier devices | 光増幅器のパラメータ定義と試験法（NF の定義） | `https://www.itu.int/rec/T-REC-G.661/en` | 未取得 |

> **補足**: A-1-1〜A-1-3 の PDF 直リンクは検索インデックス上で観測されたものであり、リンク切れの可能性がある。ランディングページ（`/rec/T-REC-G.xxx/en`）から辿るのが確実。
> **代替入口**: IETF が過去に公開した ITU-T ドラフトのミラーが存在する。規格本体の代用にはならないが、内容確認には使える。
> - G.697 改訂ドラフト: `https://www.ietf.org/lib/dt/documents/LIAISON/file1314.pdf`
> - G.694.1 改訂ドラフト（Consent 版）: `https://www.ietf.org/lib/dt/documents/LIAISON/file1313.pdf`
> ※ドラフトであり最終版と異なりうる。**「ITU-T G.697 によれば」と書く根拠には使えない。**

#### A-2. 測定器ベンダーのアプリケーションノート／ホワイトペーパー

| # | タイトル | URL | 発行元 | 使えるはずの内容（**未確認**） | 記事のどこ |
|---|---|---|---|---|---|
| A-2-1 | Measurement of Optical Signal-to-Noise Ratio in Coherent Systems（ホワイトペーパー） | `https://www.viavisolutions.com/en-us/technical-library/white-paper/measurement-optical-signal-noise-ratio-coherent-systems` | VIAVI Solutions | OSNR の定義式、参照帯域、**IEC 61280-2-9 の帯域外補間法がコヒーレントで破綻する理由**、代替手法 | §3, §7（コヒーレント時代の変化） |
| A-2-2 | 同上（PDF 直） | `https://www.viavisolutions.com/en-us/literature/measurement-optical-signal-noise-ratio-coherent-systems-white-papers-books-en.pdf` | VIAVI Solutions | 同上 | 同上 |
| A-2-3 | OSNR Measurement with MAP-300 Platform（ブローシャ） | `https://www.viavisolutions.com/en-us/literature/optical-signal-noise-ratio-osnr-measurement-map-300-platform-brochures-en.pdf` | VIAVI Solutions | 測定系の構成。図の参考 | §3 |
| A-2-4 | **App Note 361: Measuring EDFA gain and noise figure using EXFO's OSA20** | `https://www.exfo.com/contentassets/48bfe48c112644d2b0b8eee9920dd38e/exfo_anote361_measuring-edfa-gain-and-noise-figure-using-osa20_en.pdf` | EXFO | **EDFA の利得と雑音指数の測定法。ASE と NF の関係**（§4節の中核） | §4 |
| A-2-5 | App Note 261: How Poor Specs Can Translate into Incorrect OSNR Results | `https://www.exfo.com/contentassets/48b2819d080d49f8acf0a48ef1358bba/exfo_anote261_product-performance-comparison_en.pdf` | EXFO | **測定器の仕様差で OSNR 実測値がズレる話 → §5「設計値と実測値の差」に直結** | §5, §7 |
| A-2-6 | New Standard from IEC: OSNR Measurements（ブログ） | `https://www.exfo.com/en/resources/blog/new-iec-standard-osnr-measurements/` | EXFO | IEC 61282-12「In-band OSNR」の位置づけ。規格本体は有償なので、この解説記事が無償の入口 | §3, §7 |
| A-2-7 | Importance of measuring OSNR across submarine cable networks（ブログ） | `https://www.exfo.com/en/resources/blog/understanding-submarine-osnr/` | EXFO | 多段中継・長距離での OSNR の効き方 | §4 |
| A-2-8 | Measurement of OSNR for 100G+ signals（ウェビナー） | `https://www.exfo.com/en/resources/webinars/measurement-optical-signal-noise-ratio-osnr-100g/` | EXFO | In-service Pol-Mux OSNR 法。**視聴に登録が必要な可能性が高い → 要確認** | §7 |
| A-2-9 | **アプリケーションノート: 光増幅器(EDFA)の特性評価 — 光スペクトラムアナライザ MS9740A による NF/Gain 測定**（日本語） | `https://dl.cdn-anritsu.com/ja-jp/test-measurement/files/Application-Notes/Application-Note/MS9740A_JF1100.pdf` | アンリツ | **日本語で NF/Gain 測定を扱う数少ない一次資料。§4節の日本語出典として最有力** | §4 |
| A-2-10 | Optical Signal to Noise Ratio (OSNR)（技術ノート） | `https://optiwave.com/wp-content/uploads/2015/10/TC-Optical-Signal-to-Noise-Ratio-OSNR.pdf` | Optiwave | OSNR ↔ BER ↔ Q値 の関係式。**ただしシミュレータベンダー資料。経験式の扱いに注意** | §3 |

#### A-3. 学術・公的機関

| # | タイトル | URL | 発行元 | 使えるはずの内容（**未確認**） | 記事のどこ |
|---|---|---|---|---|---|
| A-3-1 | Estimating system OSNR with a digital coherent transceiver | `https://par.nsf.gov/servlets/purl/10283019` | NSF PAR（米国科学財団 公開リポジトリ） | **コヒーレント受信機側から OSNR を推定する話。§7「コヒーレント時代に意味がどう変わったか」の一次出典候補** | §7 |
| A-3-2 | Black-Box Assessment of Optical Spectrum Services | `https://arxiv.org/pdf/2110.15207` | arXiv | 事業者視点での光スペクトラムサービス評価。OSNR/GSNR の実測的扱い | §5 |
| A-3-3 | Employing Channel Probing to Derive End-of-Life Service Margins for Optical Spectrum Services | `https://arxiv.org/pdf/2302.04623` | arXiv（JOCN 掲載予定版） | **EOL マージンの導出。§5「マージンをどう考えるか」の一次出典候補No.1** | §5 |
| A-3-4 | Practical considerations for near-zero margin network design and deployment [Invited] | `https://opg.optica.org/jocn/fulltext.cfm?uri=jocn-11-9-C25&id=417055` | Optica / JOCN | **設計マージンの実務論。「システムマージン EOL 2〜3 dB」等の記述あり（未確認）。`fulltext.cfm` なのでオープンアクセスの可能性** | §5 |
| A-3-5 | ECE228B Lecture 8: Intro to Optical Amplifiers（講義スライド） | `https://courses.ece.ucsb.edu/ECE228/228B_S11Blumenthal/Lecture8_228B_S11pdf.pdf` | UC Santa Barbara / Prof. D. J. Blumenthal | **大学の公開講義資料。EDFA / ASE / NF / 多段 OSNR の導出。§4節の理論的裏付け** | §4 |
| A-3-6 | Moment-generating function method ... linearized optical noise amplified by EDFAs | `https://arxiv.org/pdf/1207.3362` | arXiv | ASE の統計的扱い。深掘り用（記事①には重すぎる） | 本4章 |
| A-3-7 | Neural Network Training for OSNR Estimation: From Prototype to Product | `https://arxiv.org/pdf/2003.02333` | arXiv | 近年の OSNR 推定手法。記事①には不要だが本の後半で使える | 本 |
| A-3-8 | Understanding Lasers and Fiberoptics (RES.6-005) | `https://ocw.mit.edu/courses/res-6-005-understanding-lasers-and-fiberoptics-spring-2008/` | MIT OpenCourseWare | ファイバ増幅器の基礎。⚠️ **MIT OCW は CC BY-NC-SA（非営利限定）。有料の技術書には図表も文章も転載できない。**理解のための読み物として使い、事実だけを自分の言葉で書く（→第9章） | §4 |
| A-3-9 | Optical Signals, Devices, and Systems (6.637) | `https://ocw.mit.edu/courses/6-637-optical-signals-devices-and-systems-spring-2003/` | MIT OpenCourseWare | 光信号・デバイス・システムの基礎 | 本1〜2章 |

#### A-4. 日本語の解説（一次資料ではないが、用語の日本語対応を取るのに有用）

| # | タイトル | URL | 発行元 | 用途 |
|---|---|---|---|---|
| A-4-1 | 光通信の鍵を握る！OSNR の基礎とその重要性とは？ | `https://jpn.nec.com/products/fod/column/osnr.html` | NEC | **日本語の用語対応（OSNR＝光信号対雑音比 等）の確認。メーカー公式コラム** |
| A-4-2 | 雑音指数（Noise Figure：NF） | `https://www.fiberlabs.co.jp/tech-word/nf/` | フィバーラボ | NF の日本語定義 |
| A-4-3 | 光ファイバー増幅器の雑音 | `https://optipedia.info/laser/fiberlaser/fiber-amp-noise/` | 光響 | ASE の日本語説明 |
| A-4-4 | 超大容量デジタルコヒーレント光伝送技術（NTT技術ジャーナル 2011.3） | `https://journal.ntt.co.jp/backnumber2/1103/files/jn201103013.pdf` | NTT | **100G コヒーレントの OSNR 耐力。日本語の公的技術文献** |
| A-4-5 | デジタルコヒーレント通信用光部品技術の研究開発（同号） | `https://journal.ntt.co.jp/backnumber2/1103/files/jn201103062.pdf` | NTT | **OSNR と Q値 の関係の日本語記述（§3・§7）** |
| A-4-6 | デジタルコヒーレント光伝送技術の今後の展開 | `https://journal.ntt.co.jp/article/18123` | NTT | 近年の動向 |
| A-4-7 | Beyond 100G 光トランスポートネットワークに向けたデバイス技術開発（2016.7） | `https://journal.ntt.co.jp/backnumber2/1607/files/jn20160710.pdf` | NTT | 本の後半 |
| A-4-8 | 光ネットワークの大容量化と長距離化を実現する非線形ひずみ補償技術 | `https://www.fujitsu.com/jp/documents/about/resources/publications/technicalreview/topics/article001.pdf` | 富士通テクニカルレビュー | 非線形補償と OSNR 改善 |
| A-4-9 | 光通信ネットワークの大容量化に向けたディジタルコヒーレント信号処理技術の研究開発 | `https://www.ieice.org/jpn/books/kaishikiji/2012/201212.pdf` | 電子情報通信学会 会誌 | 日本語の学会解説記事 |
| A-4-10 | 新たな社会インフラを担う革新的光ネットワーク技術の研究開発（5Tbps級） | `https://www.soumu.go.jp/main_content/000829523.pdf` | 総務省 | 公的機関資料。国内の技術動向 |

---

### B. DWDM 全般（本の 1〜6 章）

| # | トピック | タイトル / 規格 | URL | 発行元 |
|---|---|---|---|---|
| B-1 | 波長グリッド | **ITU-T G.694.1** Spectral grids for WDM applications: DWDM frequency grid（10/2020） | `https://www.itu.int/rec/T-REC-G.694.1-202010-I/en` | ITU-T |
| B-2 | 波長グリッド（要約のみ、HTML） | G.694.1 Summary | `https://www.itu.int/dms_pubrec/itu-t/rec/g/T-REC-G.694.1-202010-I!!SUM-HTM-E.htm` | ITU-T |
| B-3 | 波長グリッド | G.694.1 電子出版ページ | `https://www.itu.int/epublications/publication/itu-t-g-694-1-2020-10-spectral-grids-for-wdm-applications-dwdm-frequency-grid` | ITU-T |
| B-4 | CWDM グリッド | **ITU-T G.694.2** CWDM wavelength grid | `https://www.itu.int/rec/T-REC-G.694.2-200312-I/en` | ITU-T |
| B-5 | ファイバ | **ITU-T G.652** (08/2024) Characteristics of a single-mode optical fibre and cable | `https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-G.652-202408-I%21%21PDF-E&type=items` | ITU-T |
| B-6 | ファイバ | G.652 電子出版ページ | `https://www.itu.int/epublications/publication/itu-t-g-652-2024-08-characteristics-of-a-single-mode-optical-fibre-and-cable` | ITU-T |
| B-7 | ファイバ | **ITU-T G.655** NZ-DSF | `https://www.itu.int/rec/T-REC-G.655/en` | ITU-T |
| B-8 | ファイバ | **ITU-T G.656 / G.657** | `https://www.itu.int/rec/T-REC-G.656/en` / `https://www.itu.int/rec/T-REC-G.657/en` | ITU-T |
| B-9 | ファイバ（中立解説） | Singlemode Fiber Types | `https://www.thefoa.org/tech/smf.htm` | **FOA（Fiber Optic Association、非営利）**。ベンダー中立で引用しやすい |
| B-10 | ネットワーク構成 | **ITU-T G.872** Architecture of optical transport networks | `https://www.itu.int/rec/T-REC-G.872/en` | ITU-T |
| B-11 | ROADM/WSS | **ITU-T G.672** Characteristics of multi-degree ROADM | `https://www.itu.int/rec/T-REC-G.672/en` | ITU-T ※検索では未ヒット。存在確認から要 |
| B-12 | ROADM/WSS | Wavelength-Selective Switches for ROADM Applications | `https://ieeexplore.ieee.org/iel5/2944/5594752/05512667.pdf` | IEEE JSTQE。**`iel5` 直リンクは購読要の可能性が高い → 要確認** |
| B-13 | 非線形効果 | Linear and nonlinear effects in optical transmission（M. H. Eiselt） | `https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5281/0000/Linear-and-nonlinear-effects-in-optical-transmission/10.1117/12.530103.pdf` | SPIE。**購読要の可能性 → 要確認** |
| B-14 | 非線形補償 | A survey on fiber nonlinearity compensation for 400 Gbps and beyond | `https://arxiv.org/pdf/1708.06313` | arXiv（オープン） |
| B-15 | FEC | Forward Error Correction (FEC): A Primer | `https://www.cablelabs.com/blog/forward-error-correction-fec-a-primer-on-the-essential-element-for-optical-transmission-interoperability` | **CableLabs（業界団体、無償公開）。FEC の入門として引用しやすい** |
| B-16 | コヒーレント | System and device technologies for coherent optical communication | `https://www.merl.com/publications/docs/TR2018-010.pdf` | **MERL（三菱電機研究所）。技術レポートを無償公開している** |
| B-17 | GN モデル | Joint Power and Gain Allocation ... Enhanced Gaussian Noise Model | `https://arxiv.org/pdf/2107.08602` | arXiv |
| B-18 | PMD/非線形 | Influence of Modeling Methods on the Estimation of the Nonlinear Noise Statistics Considering Joint PMD and Kerr Effects | `https://arxiv.org/pdf/2002.06268` | arXiv |
| B-19 | デジタルツイン/運用 | Lifecycle Management of Optical Networks with Dynamic-Updating Digital Twin | `https://arxiv.org/pdf/2504.19564` | arXiv |

---

### C. Ciena 公開資料

**方針**: `www.ciena.com` と `media.ciena.com` 配下＝公開候補。`my.ciena.com` 配下＝顧客ポータル（不採用、第3章）。

#### C-1. 用語対応（最優先。「Ciena 固有の呼称 ↔ 業界一般の呼称」）

| # | タイトル | URL | 備考 |
|---|---|---|---|
| **C-1-1** | **Today's Top Optical Acronyms and Terms Explained**（eBook） | `https://www.ciena.com/insights/ebooks/todays-top-optical-acronyms-and-terms-explained.html` | **依頼にあった「用語の橋渡し」に最も近い資料。最優先で検証すること。**⚠️ Ciena の eBook はダウンロード時にフォーム（氏名・会社名・メール）を要求することが多い。**フォーム入力が必要なら「未ログインで開ける」とは言えない → その場合は不採用**。ページ本体だけで内容が読めるかを確認する |
| C-1-2 | Telecom Glossary | `https://www.ciena.com/insights/telecom-glossary` | 用語集。フォーム不要の可能性が高い（HTML ページ） |
| C-1-3 | Network Virtualization Glossary | `https://www.ciena.com/insights/infobriefs/Network-Virtualization-Glossary.html` | 参考 |
| C-1-4 | Fiber Deep Acronyms Guide | `https://www.ciena.com/insights/ebooks/fiber-deep-acronyms-guide.html` | 参考。同じくフォーム要注意 |

#### C-2. OSNR / マージンに直接効く Ciena 記事

| # | タイトル | URL | 記事のどこ |
|---|---|---|---|
| **C-2-1** | **Q&A with EXFO: Understanding Submarine OSNR** | `https://www.ciena.com/insights/articles/QA-with-EXFO-Understanding-Submarine-OSNR.html` | **§2「なぜ OSNR なのか」。「OSNR は高速光海底網の健全性の主要 KPI のひとつ」という位置づけの記述あり（未確認）** |
| **C-2-2** | **Optical Network Expert Series: Guide to improving future network economics with near-zero margin networking** | `https://www.ciena.com/insights/articles/optical-network-expert-series-a-guide-to-improving-future-network-economics-with-near-zero-margin-networking.html` | **§5「マージン」。設計マージンを削って容量に変える考え方** |
| C-2-3 | Optical Network Expert Series: How near-zero margin networking changes network economics | `https://www.ciena.com/insights/articles/optical-network-expert-series-how-near-zero-margin-networking-changes-network-economics.html` | §5 |
| C-2-4 | Designing programmable infrastructure to achieve near-zero margin networks | `https://www.ciena.com/insights/articles/designing-programmable-infrastructure-to-achieve-near-zero-margin-networks.html` | §5 |

#### C-3. 製品・技術（HTML ページ／公開 PDF）

| # | タイトル | URL | 種別 |
|---|---|---|---|
| C-3-1 | RLS（旧 6500 Reconfigurable Line System）製品ページ | `https://www.ciena.com/products/rls` | 製品ページ |
| C-3-2 | 6500 Reconfigurable Line System 製品ページ | `https://www.ciena.com/products/6500-reconfigurable-line-system` | 製品ページ |
| C-3-3 | 6500 Reconfigurable Line System データシート | `https://www.ciena.com/insights/data-sheets/6500-reconfigurable-line-system.html` | データシート（フォーム要否 要確認） |
| C-3-4 | WaveLogic family / Coherent Optics | `https://www.ciena.com/products/wavelogic/coherent-optics` | 製品ページ |
| C-3-5 | Chalk Talk: WaveLogic 5 Nano | `https://www.ciena.com/insights/videos/wavelogic-5-nano.html` | 動画 |
| **C-3-6** | **White Paper: High-performance Coherent in CMOS: Foundational Technology** | `https://media.ciena.com/documents/High_performance_coherent_in_CMOS_WP-page1.pdf` | **PDF 直リンク。`media.ciena.com` はフォーム不要の可能性が高い → 最有力の Ciena 一次資料** |
| **C-3-7** | **Increasing Competitive Advantage by Leveraging WaveLogic Photonics（6500 Integrated Optical Intelligence）** | `https://media.ciena.com/documents/6500_Integrated_Optical_Intelligence_PB.pdf` | **PDF 直リンク。同上** |
| C-3-8 | Ciena Unveils WaveLogic 6, Industry's First 1.6Tb/s Coherent Optic Solution | `https://www.ciena.com/about/newsroom/press-releases/ciena-unveils-wavelogic-6` | プレスリリース（確実に公開） |
| C-3-9 | Ciena 関連プレスリリース（BusinessWire 経由） | `https://www.businesswire.com/news/home/20230314005012/en/` / `https://www.businesswire.com/news/home/20230221005322/en` | プレスリリース（確実に公開） |

---

## 3. 不採用リスト — **使ってはいけない資料**

> ⚠️ **この章の判定は、URL 構造・提供形態・検索結果に現れたページタイトルからの構造判断**である（前述のとおり WebFetch 検証は実行不能だった）。
> ただし「顧客ポータル」「有償規格販売」「購読制ジャーナル」「会員登録制アップロードサイト」は**性質上明確に未ログイン不可**であり、判定の確度は高い。

### 3-1. Ciena 顧客ポータル（ライセンス対象・記憶からでも書かない）

| URL | 理由 |
|---|---|
| `https://my.ciena.com/CienaPortal/login?locale=us` | **ログインページそのもの**。検索結果のタイトルが "Login \| Ciena Portal" |
| `https://my.ciena.com/login` | 同上（"Login \| myCiena Root Placeholder"） |
| `https://my.ciena.com/CienaPortal/s/login/` | 同上 |
| `https://my.ciena.com/CienaPortal/s/Ciena-Portal-Home` | 顧客ポータルのホーム。**アクティブなサービス契約を持つ顧客向け** |
| `https://my.ciena.com/CienaPortal/s/documentation` | **顧客向け技術ドキュメント。ライセンス対象。絶対に使わない** |
| `https://my.ciena.com/CienaPortal/s/article/Ciena-Products-Converged-Packet-Optical-Wavelogic-Coherent-Optics-WaveLogic-5-Nano` | 検索には出るが**ポータル記事**。WaveLogic 5 Nano の詳細はここではなく C-3-4 / C-3-6 から取る |
| `https://my.ciena.com/CienaPortal/s/topic/0TOVR0000001i734AA/myciena-portal` | ポータル内トピック |
| `https://cienalearning.freshdesk.com/support/solutions/articles/1000258938-...` | **Ciena Learning のログイン手順ページ**。学習コンテンツ自体は登録制 |

> **`my.ciena.com` 配下は一律不採用。** 検索エンジンにインデックスされていても、それは公開を意味しない。

### 3-2. 有償規格販売サイト（規格本体は購入が必要）

| URL | 理由 |
|---|---|
| `https://webstore.iec.ch/en/publication/5094`（IEC 61280-2-9:2009） | **IEC 規格は有償販売**。本文は購入しないと読めない。→ 内容に触れたいときは A-2-1（VIAVI）や A-2-6（EXFO ブログ）の**解説を経由して**書く |
| `https://standards.globalspec.com/std/1160780/iec-61280-2-9` | 有償リセラー（GlobalSpec） |
| `https://standards.globalspec.com/std/10165255/ITU-T G.872` | 同上。**ITU-T 勧告は itu.int で無償のはずなので、わざわざ有償サイトを引く理由がない** |
| `https://standards.globalspec.com/std/14362263/itu-t-g-694-1` | 同上 |
| `https://global.ihs.com/doc_detail.cfm?document_name=ITU-T+G.694.1&...` | 有償リセラー（IHS） |

### 3-3. 購読制ジャーナル／論文（本文が有料の可能性が高い）

| URL | 理由 |
|---|---|
| `https://ieeexplore.ieee.org/document/10496760` | IEEE Xplore。**購読または個別購入が必要**（オープンアクセス指定がない限り） |
| `https://ieeexplore.ieee.org/iel5/2944/5594752/05512667.pdf` | 同上（`iel5` 直リンク） |
| `https://www.sciencedirect.com/science/article/abs/pii/S0030401823001797` | **`/abs/` はアブストラクトのみ**。本文は購読要 |
| `https://link.springer.com/article/10.1007/s12596-025-02492-2` | Springer。オープンアクセス表示がなければ購読要 |
| `https://link.springer.com/article/10.1007/s12596-025-02581-2` | 同上 |
| `https://opg.optica.org/jocn/abstract.cfm?uri=jocn-18-1-A88` | **`abstract.cfm` はアブストラクトのみ** |

> **代替**: これらの多くは著者版が arXiv に上がっている。**arXiv 版を探して、そちらを引く。**

### 3-4. 会員登録制アップロードサイト／著作権が疑わしい再配布

| URL | 理由 |
|---|---|
| `https://www.researchgate.net/publication/261019363_...` | **閲覧・DL にアカウント登録が必要**。かつ著者アップロードの合法性が不透明 |
| `https://www.researchgate.net/figure/A-ROADM-using-...` | 同上 |
| `https://www.researchgate.net/publication/303293674_...` | 同上 |
| `https://www.academia.edu/37578882/...` | **登録要。査読を経ていないアップロードも混在** |
| `https://www.academia.edu/127538188/...` | 同上 |
| `https://www.scribd.com/doc/118417047/Ciena-Acronyms-Guide` | **Scribd は登録・課金制。かつ Ciena 文書の第三者再アップロードであり著作権上も不可** |
| `https://www.accessengineeringlibrary.com/content/book/9780071499194/...` | McGraw-Hill AccessEngineering。**機関購読制** |

### 3-5. Ciena 公式文書の第三者ミラー（内容が正しくても出典にしない）

| URL | 理由 |
|---|---|
| `https://telecomcauliffe.com/wp-content/uploads/2023/10/Ciena_6500_Reconfigurable_Line_System_DS.pdf` | **個人ブログによる Ciena データシートの再アップロード**。版が古い可能性・削除リスク・著作権上の問題。→ C-3-3 の Ciena 公式を使う |
| `https://anycomm.net/datasheet/6500-RLS/6500_Reconfigurable_Line_System_DS.pdf` | **販売業者による再アップロード**。同上 |
| `https://en.sekorm.com/doc/531042805.html` | **部品商社サイトによる再掲**。同上 |
| `http://media.corporate-ir.net/media_files/IROL/99/99134/Coherent_Optical_Processing_for_High_Capacity_Networks_AN.pdf` | **旧 IR ホスティング（corporate-ir.net）。HTTP かつ現存しない可能性が高い。**内容が有用でも恒久リンクとして不適 |

### 3-6. 一次情報でないもの／AI 生成

| URL | 理由 |
|---|---|
| `https://qiita.com/dabide/items/a67a08e6aa4efd98b953`（光伝送エンジニアが押さえるべきリンクバジェットとOSNR設計 powered by claude） | **タイトルに "powered by claude" と明記された AI 生成記事**。一次情報ではない。**同じ土俵で戦う競合記事でもあるので、内容を参照しないこと**（無自覚な模倣を避ける） |
| `https://mapyourtech.com/osnr-fundamentals/` ほか mapyourtech 各記事 | **「出典としては」不採用**（出典明示がなく、数式・事例値の裏付けが取れない）。ただし**実務者コミュニティとしての価値は高い**ため、2026-08-30 の方針変更を受けて**第8章 D-1 に再評価して収録した**。使い方は「読んで理解し、事実は別の一次資料で裏を取り、自分の言葉で書く」。※式の形（`OSNR = 58 + P_launch − L_span − NF − 10log₁₀(N)`）自体は業界標準なので、A-3-5（UCSB 講義）や A-1-2（G.680）で裏を取ってから書く |
| `https://www.fs.com/blog/...` / `https://community.fs.com/article/...` | 販売業者のブログ。**一次出典にはしない**が、入門理解と用語の当たり付けには使える（→第8章 D-8） |
| `https://edgeoptic.com/kb_article/osnr-meaning-and-calculation` | 同上 |
| `https://www.fiberoptics4sale.com/blogs/wave-optics/receiver-sensitivity-and-q-factor` | 同上 |
| `https://htfuture.com/dwdm-system-dwdm/` / `https://aaanetworkx.com/dwdm-pre-fec-ber-alarm/` / `https://www.link-pp.com/knowledge/...` | 出所不明の SEO 記事。**AI 生成の疑いが強い** |
| `https://medium.com/@stevendylan/g-652-single-mode-fiber-vs-g-655-...` / `https://www.linkedin.com/pulse/...` | 個人投稿。一次出典にしない |
| `https://iown.city/glossary/osnr/` | 用語集サイト。運営主体が不明瞭 |
| `https://eureka.patsnap.com/article/what-is-coherent-optics-qpsk-vs-16-qam-in-400g-systems` | 特許 DB ベンダーの生成コンテンツ |
| 米国特許（`image-ppubs.uspto.gov/...` 多数） | **公開文書ではあるが、特許明細書は「技術の一般的説明」の出典として不適切**（出願人の主張であり、査読も規格化もされていない）。§7 の「業界の共通理解」を語る根拠にはならない |
| `https://patents.google.com/patent/US9112604B2/ko` / `https://patents.google.com/patent/JP2011024189A/ja` | 同上 |
| `https://www.lightwaveonline.com/test/network-test/article/16673614/...` | 業界ニュース。製品発表の事実確認には使えるが技術根拠にはしない |
| `https://www.fibre-systems.com/news/ciena-uses-machine-learning-create-liquid-spectrum` | 同上 |
| `https://en.wikipedia.org/wiki/G.655` | Wikipedia。**執筆時の当たりをつけるのには使えるが、技術書の出典にはしない** |

---

## 4. 検証不能リスト（プロキシ制限等） — **本人が手元で再検証すべきもの**

**この調査環境では第2章の全 URL が検証不能**である。以下は特に「アクセス制限が判定を左右する」ため、**優先して手元検証すべきもの**を抜き出したもの。

### 4-1. 最優先（記事①の根幹。ここが開けないと記事の骨格が変わる）

| 優先 | URL | 確認すべきこと |
|---|---|---|
| ★★★ | `https://www.itu.int/rec/T-REC-G.697/en` | **ITU-T 勧告が本当に無償 DL できるか。**これが可否の分かれ目。`dologin_pub.asp` で課金を要求されないかを確認 |
| ★★★ | `https://www.itu.int/rec/T-REC-G.680-200707-I` | 同上 + **Appendix II（多段 ONE の OSNR 計算例）が実在するか** |
| ★★★ | `https://www.ciena.com/insights/ebooks/todays-top-optical-acronyms-and-terms-explained.html` | **ダウンロードにフォーム入力（氏名・会社名・メール）を要求されないか。** 要求されるなら不採用 |
| ★★★ | `https://media.ciena.com/documents/High_performance_coherent_in_CMOS_WP-page1.pdf` | **フォームなしで PDF が直接開くか。** 開くなら Ciena 系の最有力一次資料 |
| ★★★ | `https://www.exfo.com/contentassets/.../exfo_anote361_measuring-edfa-gain-and-noise-figure-using-osa20_en.pdf` | 同上（§4 の中核） |
| ★★★ | `https://dl.cdn-anritsu.com/ja-jp/.../MS9740A_JF1100.pdf` | 同上（§4 の日本語出典） |
| ★★★ | `https://www.viavisolutions.com/en-us/literature/measurement-optical-signal-noise-ratio-coherent-systems-white-papers-books-en.pdf` | 同上（§3・§7） |

### 4-2. 次点

| 優先 | URL | 確認すべきこと |
|---|---|---|
| ★★ | `https://opg.optica.org/jocn/fulltext.cfm?uri=jocn-11-9-C25&id=417055` | **オープンアクセスか購読要か。**`fulltext.cfm` でも購読要のことがある |
| ★★ | `https://par.nsf.gov/servlets/purl/10283019` | NSF PAR は公開のはずだが要確認 |
| ★★ | `https://courses.ece.ucsb.edu/ECE228/228B_S11Blumenthal/Lecture8_228B_S11pdf.pdf` | 2011 年の講義資料。**リンク切れの可能性** |
| ★★ | `https://www.ciena.com/insights/data-sheets/6500-reconfigurable-line-system.html` | データシートがフォームなしで見られるか |
| ★★ | `https://www.exfo.com/en/resources/webinars/measurement-optical-signal-noise-ratio-osnr-100g/` | **ウェビナーは登録制の可能性が高い** |
| ★ | `https://www.itu.int/rec/T-REC-G.672/en` | **G.672 が ROADM の勧告として実在するか**（検索で確認できていない） |
| ★ | `https://www.spiedigitallibrary.org/.../10.1117/12.530103.pdf` | SPIE が購読要かどうか |
| ★ | `http://media.corporate-ir.net/.../Coherent_Optical_Processing_for_High_Capacity_Networks_AN.pdf` | **おそらく死んでいる。**生きていたとしても恒久リンクにしない |
| ★ | arXiv 各 PDF（A-3-2, A-3-3, A-3-6, A-3-7, B-14, B-17, B-18, B-19） | arXiv は原則オープン。**リンク切れ確認のみでよい** |
| ★ | NTT技術ジャーナル各 PDF（A-4-4 〜 A-4-7） | バックナンバー PDF が公開のままか |

### 4-3. 手元での検証手順（そのまま実行できる形）

```
1. ブラウザのシークレット / プライベートウィンドウを開く
   （通常ウィンドウだと既存ログインが効いてしまい判定にならない）
2. URL を貼る
3. 次の3つを記録する
   a) ページ本文が読めたか（Yes / ログイン要求 / フォーム要求 / 403 / 404）
   b) PDF ならフォーム入力なしで直接開いたか
   c) 開けた場合、記事のどの節で使う内容が実際に書かれていたか（1〜2行）
4. 開けたものだけを第1章「採用リスト」に移す
5. ログイン・フォーム要求だったものは第3章に理由付きで移す
```

**目安**: 4-1 の 7 本だけなら 30 分ほどで終わる。記事①を書き始める前に、まずこの 7 本を潰すこと。

---

## 5. 記事①（OSNR）節 ↔ 出典 対応表

記事①骨子（`article-01-osnr.md`）の節番号に対応。
**「◎」= 第一候補、「○」= 補強、「—」= 出典不要（本人の経験で書く領域）**

| 記事の節 | 目標字数 | 出典が要るか | 第一候補 | 補強候補 | 備考 |
|---|---|---|---|---|---|
| **1. TL;DR** | 3行 | — | — | — | 本文の要約なので出典不要 |
| **2. なぜ OSNR なのか** | 400字 | **薄くてよい** | ◎ C-2-1（Ciena/EXFO: Submarine OSNR。「主要 KPI のひとつ」） | ○ A-4-1（NEC コラム） | **ここは経験で書く勝負所**。出典は「業界でも KPI 扱いされている」という裏付け1本で足りる |
| **3. OSNR は何と何を比べているのか** | 600字 | **必須** | ◎ **A-1-1（ITU-T G.697）** — 定義と参照帯域 | ○ A-2-1/A-2-2（VIAVI WP: 定義式）<br>○ A-2-10（Optiwave: OSNR-BER-Q）<br>○ A-4-5（NTT: OSNR と Q値） | **参照帯域 0.1nm＝1550nm で約 12.5GHz** の根拠を必ず一次で取る。G.697 が開けなければ VIAVI WP が代替 |
| **4. なぜ劣化するのか（増幅と雑音、多段中継）** | 800字 | **必須** | ◎ **A-2-4（EXFO AN361: EDFA gain / NF）**<br>◎ **A-1-2（ITU-T G.680 Appendix II: 多段 ONE の OSNR 計算例）** | ○ A-3-5（UCSB 講義: ASE/NF/多段 OSNR の導出）<br>○ **A-2-9（アンリツ AN: 日本語の NF/Gain 測定）**<br>○ A-1-6（G.663）/ A-1-7（G.661）<br>○ A-4-2, A-4-3（日本語の NF・ASE 定義） | **記事①で最も出典が厚くできる節**。物理の話なので守秘義務の心配ゼロ。`10log₁₀(N)` の形は必ず一次で裏を取る（mapyourtech は使わない） |
| **5. 設計値と実測値の差 — マージン** | 800字 | **半分だけ** | ◎ **A-3-3（arXiv: EOL Service Margins）**<br>◎ **C-2-2（Ciena: near-zero margin networking）** | ○ A-2-5（EXFO AN261: **測定器の仕様差で OSNR 実測値がズレる** → 「なぜズレるか」の一次根拠）<br>○ A-3-4（JOCN: near-zero margin の実務論）<br>○ A-3-2（arXiv: Black-Box Assessment） | **2番目の勝負所**。「どういう考え方でマージンを取るか」の一般論は出典で支え、**前職の具体的な設計値・閾値は書かない**。A-2-5 は「実測がズレる理由」を測定器側から説明できるので、経験談の代わりに使える |
| **6. 足りないと言われたときに確認する順序** | 1,000字 | **ほぼ不要** | ○ 中立の切り分け例として Cisco の公開トラブルシューティングガイド（下記） | — | **この記事の核。経験で書く**。出典は「一般的な切り分けの型」の確認用にとどめる。**現時点で「順序」を体系的に示した無償一次資料は見つかっていない**（→ 第6章の不足参照） |
| **7. つまずきポイント** | 600字 | **1点だけ必須** | ◎ **A-3-1（NSF PAR: Estimating system OSNR with a digital coherent transceiver）** — コヒーレントで OSNR の意味がどう変わったか | ○ A-2-1（VIAVI: **IEC 61280-2-9 の帯域外補間法がコヒーレントで破綻する理由**）<br>○ A-2-6（EXFO: IEC 61282-12 In-band OSNR）<br>○ A-4-4/A-4-5（NTT: OSNR 耐力、OSNR と Q値） | dB / dBm の混同、参照帯域違いによるズレは**経験で書く**（出典不要）。**「コヒーレント時代の変化」だけは一次出典が要る** |
| **8. まとめ** | 200字 | — | — | — | |
| **9. 導線** | — | — | — | — | |

### 節6で参照しうる公開トラブルシューティング資料（**中立性に注意して使う**）

| URL | 発行元 | 扱い |
|---|---|---|
| `https://www.cisco.com/c/en/us/td/docs/optical/15000r9_2/dwdm/troubleshooting/guide/b_454d92_ts/m_454d91_generalts.html` | Cisco（ONS 15454 DWDM Troubleshooting Guide, Rel 9.2） | **無償公開のベンダー公式ガイド**。機器固有の記述が多いので**「型」の確認にとどめる**。記事は Ciena 寄りなので、Cisco の手順をそのまま写さないこと |

---

## 6. 現時点で「記事①に足りない」出典

| 不足しているもの | なぜ問題か | 打つ手 |
|---|---|---|
| **§6「確認する順序」を支えるベンダー中立の公開資料** | 記事①で最も読まれる節なのに、無償・中立・一次の裏付けが見つかっていない。Cisco ガイドは機器固有、mapyourtech は出典不明 | **経験で書き切る**のが正解。ただし「一般的な切り分けの型」として書けば出典なしで成立する（骨子の方針どおり）。補強したければ FOA（`thefoa.org`）の現場向け資料を追加調査する |
| **参照帯域 0.1nm の「なぜ 0.1nm なのか」を説明した一次資料** | §3 と §7（参照帯域違いによるズレ）の核心。0.1nm＝1550nm で約 12.5GHz という換算の**規格上の根拠**が確定していない | ITU-T G.697 / IEC 61280-2-9 を当たる。IEC は有償なので、**G.697 が開けるかどうかが決定的** |
| **日本語で「OSNR バジェット／マージン」を扱った公開資料** | A-4 系は原理説明が中心で、**設計マージンの考え方を日本語で書いた無償資料がない** | 英語（A-3-3, A-3-4, C-2-2）で裏を取り、日本語化して書く。**これは記事の差別化要因になる**（日本語で存在しない情報を出せる） |
| **Ciena 固有呼称 ↔ 業界一般呼称の対応表** | 依頼の最優先項目だが、C-1-1 がフォーム制の可能性がある | C-1-1 を検証。ダメなら C-1-2（Telecom Glossary、HTML なのでフォーム不要の見込み）で代替。それでも足りなければ **対応表は本人の知識で作り、各用語の「業界一般側」だけに出典を付ける**（Ciena 側の呼称は公開製品ページで裏が取れる） |

---

