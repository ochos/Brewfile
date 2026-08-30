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

---

## 7. 【2026-08-30 追記】前提の訂正を受けた調査範囲の拡大

**訂正内容**: 「まとまった資料がない」のは**日本語圏のみ**。**英語圏には実務者コミュニティ・ブログが複数存在する**。
→ 以下、第8〜10章を追加。**第3章の不採用判定のうち「個人ブログ」を理由にしていたものは、第8章で再評価している**（不採用のままのもの／条件付きで使えるものを区別した）。

> ⚠️ **本章も WebFetch 検証はできていない**（エグレス遮断は継続）。ライセンス情報も**検索インデックス経由の観測**であり、**本人が各サイトの Terms / Copyright ページを自分の目で確認すること**。特に第9章の判断は金銭が絡むので、確認は必須。

---

## 8. 英語圏コミュニティ・ブログ一覧（D）

### 評価軸の凡例

- **書き手**: 実務者 / 研究者 / マーケ / 不明
- **深さ**: ★★★＝実務レベルの踏み込み（数式・設計判断・失敗事例）／★★＝技術解説として妥当／★＝表面的な用語解説
- **信頼度**: 出典明示の有無、更新頻度、運営主体の透明性で判定
- **ライセンス**: 転載可否。**未確認は「要確認」と明記**

---

### D-1. MapYourTech — **最重要。ただし出典にはできない**

| 項目 | 内容 |
|---|---|
| URL | `https://mapyourtech.com/` |
| 主要記事 | `/osnr-fundamentals/`、`/edfa-noise-figure-and-why-every-span-adds-ase/`、`/bol-and-eol-margin-design-for-osnr-gosnr-and-q/`、`/basics-of-important-parameters-in-dwdm-link-design/`、`/osnr-what-does-this-meanwhy-do-we-need-and-how-to-take-care-of-it/`、`/common-otn-alarms-and-their-troubleshooting-steps/`、`/in-house-multivendor-optical-link-planning-design-and-simulation-for-operators/`、`/automating-span-health-and-margin-analysis-in-multi-vendor-optical-networks/`、`/hollow-core-fiber-amplification-edfa-and-raman/` |
| 運営者 | 個人〜小規模チーム運営（連絡先 contact@mapyourtech.com）。2011 年開始と自称 |
| 書き手 | **実務者**（"created by working professionals" と自称）。個々の記事に署名がない点は減点 |
| 深さ | **★★★**。OSNR シミュレータ・リンクバジェット計算機を備え、BOL/EOL マージン設計、GSNR、多ベンダー環境のスパン健全性分析まで踏み込む。**依頼者が探していた「英語圏のまとまったサイト」の本命はここ** |
| OSNR について | 記事①の全節に対応する内容がある。特に **§5（マージン: BOL/EOL）** と **§7（つまずき）** に効く。後述 D-1-a 参照 |
| 更新頻度 | 高（記事数 905+ と自称）。近年も更新あり |
| 信頼度 | **中**。内容は具体的だが**出典が明示されていない**。数値例（「1200km QPSK リンクで 3 年で 2 dB ドリフト」等）は検証不能 |
| ライセンス | ⚠️ **`https://mapyourtech.com/copyright-disclaimer/` に著作権表示あり。「オリジナルコンテンツ、著作権保護」「海賊行為防止のためセキュアリーダーを使用」と明記。転載・翻訳転載は明確に不可。**企業ライセンスは個別問い合わせ |
| **使い方** | **読んで理解する → 事実は ITU-T / ベンダー AN / 学術論文で裏を取る → 自分の言葉で書く。引用も最小限にとどめ、URL を出典として並べない**（出典明示がないサイトを出典にすると、記事の信頼性が下がる） |

#### D-1-a. MapYourTech から拾った「実務者のつまずき指摘」（**記事①§7の最有力ネタ。ただし要裏取り**）

> **「1スパンの OSNR を `P_TX + G − L − NF` と書いてしまう誤り。増幅器利得 G は相殺されるので、この式はゼロ近傍や負の値を出し、健全なリンクを不良と誤判定する。スケールを決めるのは帯域定数 (+58) のほうである。」**

- **なぜ重要か**: これは**「経験者しか知らない誤り方」**であり、記事①§7「つまずきポイント」の骨格になりうる。
- **注意**: **1ソースのみ。しかも出典明示のないブログ。** そのまま書かない。
- **打つ手**: `+58 = 10log₁₀(h·ν·B_ref)`（1550nm、0.1nm 参照帯域）の導出を A-3-5（UCSB 講義）や A-1-2（G.680）で確認し、**自分の言葉で導出から説明する**。導出できれば「なぜ G が消えるか」も自分で書ける。

---

### D-2. EXFO Blog / Resources — **測定器ベンダー。実務者向けで質が高い**

| 項目 | 内容 |
|---|---|
| URL | `https://www.exfo.com/en/resources/blog/` |
| OSNR 関連記事（**記事①に直結**） | ・**What should the OSNR values be in DWDM networks?** `https://www.exfo.com/en/resources/blog/osnr-values-dwdm-networks/`<br>・**OSNR Measurement in Coherent 40G/100G Networks** `https://www.exfo.com/en/resources/blog/osnr-measurement-coherent-40g-100g-networks/`<br>・**OSNR in Next-Gen networks（in-band OSNR）** `https://www.exfo.com/en/resources/blog/inband-osnr-measurement/`<br>・**OSNR Flatness \| DWDM** `https://www.exfo.com/en/resources/blog/osnr-flatness-dwdm/`<br>・**Overcoming the challenges of OSA measurements** `https://www.exfo.com/en/resources/blog/challenges-osa-measurements/`<br>・New Standard from IEC: OSNR Measurements `https://www.exfo.com/en/resources/blog/new-iec-standard-osnr-measurements/`<br>・Importance of measuring OSNR across submarine cable networks `https://www.exfo.com/en/resources/blog/understanding-submarine-osnr/` |
| 書き手 | **実務者寄り**（アプリケーションエンジニア／プロダクトマネージャ）。マーケ色はあるが技術的中身がある |
| 深さ | **★★★（OSNR に限れば最良）**。測定の現場で何が起きるかを書いている。**「測ると値がズレる理由」＝記事①§5 の核心** |
| OSNR について | ・受信端の目安 15〜18 dB（100G DPSK で >約18 dB）<br>・必要 OSNR は**変調方式・データレート・ライトパス上の位置・網種別・目標 BER**で変わる<br>・**送信側に近いほど必要 OSNR は高く、受信側に近いほど低い**（増幅器と ROADM が雑音を足していくため）<br>・IEC 61280-2-9 の帯域外補間法が 100G+ / ROADM 網で破綻する理由<br>・OSNR フラットネス（波長間のばらつき）という運用視点 |
| 更新頻度 | 中〜高。継続運営 |
| 信頼度 | **高**。企業公式・技術部門執筆。ただし**自社製品への誘導が入る**点は割り引く |
| ライセンス | ⚠️ **企業サイト。All rights reserved。転載・図表流用は不可。** 事実の参照と、出典明示つきの短い引用のみ |

---

### D-3. NANOG（North American Network Operators' Group）— **オペレータ視点の公開チュートリアル**

| 項目 | 内容 |
|---|---|
| URL | `https://nanog.org/` / アーカイブ `https://archive.nanog.org/` |
| 主要資料 | ・**DWDM & Packet Optical Fundamentals（NANOG 64, Peter Landon）** `https://archive.nanog.org/sites/default/files/meetings/NANOG64/1017/20150602_Landon_Tutorial_Dwdm__v3.pdf`<br>・Tutorial: DWDM & Packet Optical Fundamentals `https://nanog.org/news-stories/nanog-tv/top-talks/tutorial-dwdm-packet-optical-fundamentals/`<br>・Tutorial: Everything You Always Wanted to Know About Optical Networking `https://nanog.org/news-stories/nanog-tv/top-talks/tutorial-tutorial-everything-you-always-wanted-know-about-optical-networking/`<br>・NANOG 講演のキュレーション（第三者 gist）`https://gist.github.com/azet/0d8488426fd2b097b99ee39ce18b0462`<br>・メーリングリスト過去ログ（MIT ミラー）`https://diswww.mit.edu/charon/nanog/` |
| 書き手 | **現役のネットワーク事業者・ベンダーアーキテクト**。NANOG は営利団体ではなくオペレータコミュニティ |
| 深さ | **★★★**。「事業者が実際に何を気にするか」が出る。DWDM の全体像を掴むのに最適 |
| OSNR について | チュートリアル内で扱われる（未確認）。**§2「なぜ現場は OSNR を見るのか」のオペレータ視点の裏付けとして期待できる** |
| 更新頻度 | 年3回のミーティングごと。アーカイブは恒久 |
| 信頼度 | **高**。公開の場での発表であり、聴衆が同業のプロなので誤りが淘汰されやすい |
| ライセンス | ⚠️ **著作権は各発表者に帰属**。スライドの図の流用は不可。**閲覧・参照は自由** |
| 備考 | **PDF 直リンクが残っているのが強い**（`archive.nanog.org`）。まずここを検証すること |

---

### D-4. XKL — NANOG 97 発表の DWDM 入門

| 項目 | 内容 |
|---|---|
| URL | `https://xkl.com/intro-to-dwdm-tutorial/` |
| 書き手 | Chad（XKL Principal Solutions Architect）。**ベンダーの実務アーキテクト** |
| 深さ | **★★**。チャネル、固定グリッド／フレックスグリッド、mux/demux フィルタ、トランシーバ／トランスポンダ／マックスポンダの概念整理 |
| OSNR について | 入門レベル。**本の1〜2章（用語整理）向き**。記事①には浅い |
| 信頼度 | 中〜高（NANOG で発表した内容の再掲） |
| ライセンス | 企業サイト。転載不可 |

---

### D-5. Cisco — 公開ドキュメント＋オペレータコミュニティ

| 項目 | 内容 |
|---|---|
| URL | ・**Introduction to DWDM Technology** `https://www.cisco.com/c/dam/global/de_at/assets/docs/dwdm.pdf`<br>・**ONS 15454 DWDM Troubleshooting Guide** `https://www.cisco.com/c/en/us/td/docs/optical/15000r9_2/dwdm/troubleshooting/guide/b_454d92_ts/m_454d91_generalts.html`<br>・**Cisco Community: Optics and Optical Networking**（Ask the Expert: Troubleshooting on Cisco DWDM NCS 2000）`https://community.cisco.com/t5/optics-and-optical-networking/ask-the-expert-troubleshooting-on-cisco-dwdm-ncs-2000-series/m-p/4449336/` |
| 書き手 | Cisco の TAC / エンジニア＋**現場の実務者**（コミュニティ側） |
| 深さ | **★★★（トラブルシューティングに限れば最良の公開資料）** |
| OSNR について | **§6「足りないと言われたときに確認する順序」の唯一の実用的な公開一次資料**。「汚れた接続 or 入力スパンの過大損失」「増幅器の過大ゲインチルト or 対向 TXP/MXP の波長設定誤り」といった切り分けが具体的に書かれている |
| 更新頻度 | ドキュメントは版固定。コミュニティは継続 |
| 信頼度 | **高**（公式ドキュメント）／**中**（コミュニティ投稿は個人の発言） |
| ライセンス | ⚠️ **Cisco 著作物。転載不可。** さらに**機器固有の記述が多い**ので、記事が Ciena 寄りである以上、手順をそのまま写さないこと。**「切り分けの型」の妥当性確認にとどめる** |
| 備考 | **記事①§6は「経験で書く」のが正解**。Cisco を写すと Cisco の記事になってしまう |

---

### D-6. IEEE / 標準化・業界団体の公開解説

| # | サイト | URL | 評価 |
|---|---|---|---|
| D-6-1 | **IEEE 802.3 公開資料（OSNR Link Budget Methodology）** | `https://www.ieee802.org/3/cn/public/18_11/lyubomirsky_3cn_01a_1118.pdf` | **書き手＝実務者（標準化会合の寄書）／深さ★★★／信頼度 高**。`ieee802.org/.../public/` 配下は**完全公開**（会合資料は誰でも閲覧可）。**OSNR リンクバジェットの手法を扱っており、記事①§4・§5 に直結**。⚠️ 802.3cn は Ethernet 系なので DWDM 長距離とは前提が異なる点に注意 |
| D-6-2 | **IEEE ComSoc Technology Blog** | `https://techblog.comsoc.org/category/coherent-optics/` / `/category/optical-transceivers/` | 書き手＝業界ウォッチャー／深さ★★／信頼度 中〜高。**動向把握向き**。技術の深掘りは薄い |
| D-6-3 | IEEE ComSoc CTN | `https://www.comsoc.org/publications/ctn/getting-religious-coherent-technologies-high-speed-optical-access-systems` | コヒーレント技術の論説。深さ★★ |
| D-6-4 | **OIF（Optical Internetworking Forum）** | `https://www.oiforum.com/oif-publishes-implementation-agreement-for-400zr-coherent-optical-interface/` | **400ZR IA の公式アナウンス**。IA 本体は会員向けの可能性あり（要確認）。**本の5〜6章（コヒーレント／DCI）の一次情報** |
| D-6-5 | IEEE Photonics Society | `https://ieeephotonics.org/announcements/ofc-2023-...` | 学会アナウンス。動向のみ |

---

### D-7. FOA（Fiber Optic Association）— **非営利・ベンダー中立の教育リソース**

| 項目 | 内容 |
|---|---|
| URL | ・**FOA Online Reference Guide 目次** `https://www.thefoa.org/tech/ref/contents.html`<br>・Singlemode Fiber Types `https://www.thefoa.org/tech/smf.htm`<br>・**Guide To Fiber Optic Network Design** `https://www.thefoa.org/tech/guides/DesG.pdf`<br>・Guidelines On What Loss To Expect When Testing `https://www.thefoa.org/tech/loss-est.htm`<br>・Fiber Optic Testing FAQs `https://www.thefoa.org/tech/FAQS/FAQ-TEST.HTM`<br>・Fiber Textbook Guide `https://www.thefoa.org/Textbook%20Guides/FRG Fiber Textbook Guide-Q.pdf` |
| 書き手 | **FOA（非営利の認定団体）の技術者**。ベンダー中立を明示 |
| 深さ | **★★**（DWDM/OSNR は浅め、**ロスバジェット・測定・現場作業は★★★**） |
| OSNR について | 直接の OSNR 記述は薄い。ただし**「ロスバジェット」の考え方は §5 の下地**になる。**光パワーと OSNR の混同**という §7 ネタの裏付けにも使える |
| 更新頻度 | 継続更新 |
| 信頼度 | **高**。**販売目的がないため中立**。記事のトーンを Ciena 寄りにする際の「業界一般側」の錨として価値が高い |
| ライセンス | ⚠️ FOA 著作物。**無償公開だが転載は不可**（要 Terms 確認） |

---

### D-8. 販売業者・ベンダー系ブログ（**入門理解用。出典にはしない**）

| # | サイト | URL | 評価 |
|---|---|---|---|
| D-8-1 | FS.com Blog / Community | `https://www.fs.com/blog/mastering-optical-link-budgets-for-embedded-wdm-network-optimization-11760.html` / `https://community.fs.com/article/itu-t-standards-for-various-optical-fibers.html` / `https://www.fs.com/blog/a-brief-introduction-to-wavelength-selective-switch-wss-of-roadm-4617.html` | 書き手＝マーケ寄り／深さ★★／**信頼度 中**。図が分かりやすく用語の当たり付けに便利。**出典にはしない** |
| D-8-2 | PacketLight | `https://www.packetlight.com/technology/dwdm-network-technology` / `/resources/articles/dwdm-technology-high-capacity-optical-networking` | 同上。深さ★★ |
| D-8-3 | ADTRAN "What is DWDM?" | `https://www.adtran.com/en/products-and-services/technology/what-is-dwdm` | 深さ★。用語確認のみ |
| D-8-4 | DWDM.ME Blog | `https://dwdm.me/blog/how-to-reduce-the-cost-of-an-optical-transport-network/` | 書き手＝不明（実務者の可能性）／深さ★★／**要 About ページ確認**。経済性の視点は珍しい |
| D-8-5 | MercuryZ | `https://www.mercuryz.com/modern-dwdm-engineering-high-capacity-optical-transport/` | 書き手不明／深さ★★／**信頼度 低〜中**。要確認 |
| D-8-6 | EDGE Optical Solutions KB | `https://edgeoptic.com/kb_article/osnr-meaning-and-calculation` | 深さ★★／信頼度 低〜中 |
| D-8-7 | Fibre Systems（業界誌） | `https://www.fibre-systems.com/white-paper/40g100g-osnr-measurements-pol-mux-osa` | 業界誌。ホワイトペーパー窓口。**登録要の可能性** |

---

### D-9. 実務者フォーラム — **調査結果: 期待したほど無い**

| 対象 | 結果 |
|---|---|
| Reddit（r/networking, r/fiberoptics 等） | **DWDM/OSNR に特化した実質的な議論を検索で確認できなかった。**光伝送は Reddit では層が薄い。一次調査としては空振り。※本人が直接 Reddit 内検索する価値はある |
| Stack Exchange（Network Engineering / Electrical Engineering） | **DWDM・OSNR の実質的な Q&A を確認できなかった。**光伝送レイヤ0は SE の守備範囲外に近い |
| **Cisco Community（Optics and Optical Networking）** | **○ 実在し、実務者が質問・回答している**（D-5 参照）。**現時点で最も実務者フォーラムに近い** |
| **NANOG メーリングリスト** | **○ 過去ログが公開**（`https://diswww.mit.edu/charon/nanog/`）。事業者の生の議論 |
| **my.ciena.com の Q&A** | **× 顧客ポータル内（例: `https://my.ciena.com/CienaPortal/s/question/0D54z00007VgHyuCAF/how-to-interpret-snr-margin-and-prefec-fail-alarms`）。ログイン必須。第3章のとおり不採用。**⚠️ タイトルが「SNR margin と pre-FEC fail アラームの解釈」という記事①§6 ど真ん中の内容だが、**絶対に開かない・書かない** |

> **結論**: 英語圏の「まとまったサイト」の実体は、**フォーラムではなくブログ／コミュニティサイト（D-1, D-2）とオペレータ団体のチュートリアル（D-3）**である。

---

## 9. 引用ルール（**有料の技術書を作る以上、ここが最重要**）

> ⚠️ 以下は法律の専門家の助言ではない。**金額が絡む出版なので、判断に迷ったら弁護士か出版社に確認すること。**
> ただし「これをやったらアウト」の線は明確なので、**その線だけは絶対に越えないこと。**

### 9-1. 絶対にやってはいけないこと

| ❌ NG 行為 | なぜ |
|---|---|
| **英語記事を翻訳して掲載する** | **翻訳は「翻案」であり著作権者の専有権（日本著作権法27条）。無断翻訳掲載は明確な著作権侵害。**「出典を書いたから大丈夫」は成立しない |
| **図・表・グラフをコピーして貼る** | 図表は独立した著作物。**ライセンスが明示されていない限り不可。**（→ 9-4） |
| 記事の構成をそのままなぞる | 「編集著作物」に触れうる。加えて**読者にバレる** |
| MapYourTech / EXFO / Cisco / Ciena の文章を要約と称して切り貼りする | 要約でも表現に依拠していれば翻案。**自分の言葉で再構成すること** |
| MIT OCW の教材を有料書に転載する | **CC BY-NC-SA = 非営利限定。有料書は商用利用でありライセンス違反** |
| Wikipedia / Stack Exchange の文章を有料書に取り込む | **CC BY-SA の ShareAlike 条項により、派生物も同ライセンスでの公開が必要になる。有料書と両立しない** |
| `my.ciena.com` 配下の内容を、記憶からでも書く | **守秘義務・ライセンス違反。第3章のとおり** |

### 9-2. やってよいこと（**これだけで技術書は書ける**）

| ✅ OK 行為 | 根拠・条件 |
|---|---|
| **事実・数値・物理法則を、自分の言葉で書く** | **アイデア・表現二分論**。事実そのものに著作権はない。「1550nm で 0.1nm ≒ 12.5GHz」は誰が書いても同じ事実 |
| **複数のソースで同じ事実を確認し、自分の理解で再構成する** | **これが本作業の本筋**。第10章がそのための材料 |
| 数式を自分で導出して書く | 数式に著作権はない。**導出過程を自分で書けば完全に安全**（かつ記事の価値も上がる） |
| **出典を明示して、必要最小限を「引用」する** | 日本著作権法32条の要件を全て満たすこと（→9-3） |
| **図を自分で描き直す** | データ・事実に基づき**自分で新規に作図**する。既存図のトレースは不可 |
| URL を出典として示す（リンクする） | リンク自体は複製ではない |
| 標準規格の**番号と要旨**に言及する（「ITU-T G.694.1 は 193.1 THz を基準とするグリッドを定めている」） | 事実の記述。**条文の逐語転載は不可** |

### 9-3. 「引用」の4要件（日本著作権法32条・判例）— **全部満たさないと引用にならない**

1. **主従関係**: 自分の文章が主、引用が従。**引用が段落の過半を占めたらアウト**
2. **明瞭区別**: 引用部分が明確に区別されている（`>` の引用ブロック、鉤括弧）
3. **必然性**: その引用でなければならない理由がある（批評・検証・比較のため）
4. **出所明示**: 著作者名・タイトル・URL・参照日を書く

**実務上の目安**: 英語原文を短く（1〜2文）引用ブロックに入れ、**直後に自分の解説を長く書く**。訳文を併記する場合も「拙訳」と明記し、原文と併置する。**訳文だけを載せない。**

### 9-4. ソース別ライセンス判定表（**要本人確認**）

| ソース | ライセンス（観測） | 図表流用 | 本文引用 | 事実の利用 |
|---|---|---|---|---|
| **ITU-T 勧告** | ITU 著作権。**無償ダウンロード ≠ 自由利用**。複製には ITU の許諾が必要 | ❌ | △（32条の引用要件内で最小限） | ✅ |
| **IEC 規格** | 有償。そもそも入手不可 | ❌ | ❌ | △（第三者の解説経由で） |
| **MapYourTech** | ⚠️ **著作権保護を明示（`/copyright-disclaimer/`）。「セキュアリーダーで海賊行為を防止」と記載** | ❌ | ❌（実質不可） | ✅（**別ソースで裏取り必須**） |
| **EXFO / VIAVI / Keysight / Anritsu / Cisco / Ciena / XKL** | 企業著作物、All rights reserved | ❌ | △（32条内） | ✅ |
| **NANOG 発表資料** | **著作権は各発表者**。閲覧自由 | ❌ | △ | ✅ |
| **IEEE 802 公開寄書** | IEEE / 寄稿者。**閲覧は完全公開** | ❌ | △ | ✅ |
| **FOA** | FOA 著作物。無償公開 | ❌ | △ | ✅ |
| **MIT OpenCourseWare** | ⚠️ **CC BY-NC-SA 4.0（非営利限定）** | ❌**（有料書では不可）** | ❌**（有料書では不可）** | ✅ |
| **arXiv 論文** | ⚠️ **論文ごとに違う**（arXiv perpetual license / CC BY / CC BY-NC-SA / CC0）。**各論文ページのライセンス表示を必ず見る** | CC BY なら △（要 attribution） | △ | ✅ |
| **Optica / IEEE / Springer / SPIE 論文** | 購読制。OA 論文のみ CC ライセンス | 論文ごと | △ | ✅ |
| **Wikipedia** | **CC BY-SA**（ShareAlike が有料書と衝突） | ❌ | ❌ | ✅ |
| **Stack Exchange / Reddit** | SE は **CC BY-SA 4.0**（ShareAlike）／Reddit は投稿者が著作権保持 | ❌ | ❌ | ✅ |
| **NTT技術ジャーナル / 富士通 / IEICE / 総務省** | 各社・各機関著作物。総務省資料は**政府標準利用規約（CC BY 互換）の可能性** → **要確認** | ❌（総務省のみ要確認） | △ | ✅ |
| **プレスリリース（BusinessWire / PR TIMES 等）** | 報道用途で配布されているが著作権は発行元 | ❌ | ✅（事実の引用は通例許容） | ✅ |

### 9-5. 執筆時の実務手順（**これをチェックリストとして使う**）

```
1. ソースを読む（英語でよい）
2. 画面を閉じる          ← ★これが最重要。開いたまま書くと表現が写る
3. 自分の言葉でメモを書く（日本語）
4. 数値・事実は、別の独立したソースで最低もう1つ確認する
   → 一致しなければ「諸説ある」と書くか、書かない
5. 図が要るなら、事実に基づいて自分でゼロから描く
6. 参考文献リストを記事末尾に置く（URL + 参照日）
7. 公開前に、原文と自分の文章を並べて読み返す
   → 語順や比喩が似ていたら書き直す
```

**「2. 画面を閉じる」を守れば、著作権侵害はほぼ起きない。** 開いたまま書くと無自覚に写す。

### 9-6. 有料書に特有の追加注意

- **無料記事（Zenn）と有料書で基準を変えない。** 有料のほうが権利者に発見されやすく、また「営利目的」で不利になる
- **フェアユースは日本にはない。** 米国サイトの記事だからといって米国法の fair use は使えない
- **AI に翻訳させても同じ。** 翻訳の主体が誰かは関係ない
- **参考文献リストは必ず載せる。** 免責にはならないが、誠実さの証明になり、読者の信頼も上がる

---

## 10. 複数ソースで一致している事実の一覧（記事①で使えるもの）

**信頼度の見方**:
- **A（複数の独立した信頼できるソースで一致）**: 裏取り済みとして書いてよい。ただし**本人が原典を1つは開いて確認すること**
- **B（2ソース、または1ソースが信頼できる企業/団体）**: 書いてよいが、**断定を弱める**か、原典確認を優先する
- **C（1ソースのみ、または出典不明のブログのみ）**: **そのまま書かない。**必ず原典で裏を取る

> ⚠️ 以下はすべて**検索インデックス経由で観測した内容**であり、**原典を直接読んでいない**。「ソース数」は「そう書いていると観測されたソースの数」であって、「本人が確認した数」ではない。

### 10-1. §2「なぜ現場は OSNR を見るのか」

| # | 事実 | ソース数 | 信頼度 | ソース |
|---|---|---|---|---|
| 10-1-1 | **OSNR は光伝送網の健全性を示す主要 KPI のひとつとして扱われている** | 4 | **A** | Ciena/EXFO(C-2-1)、EXFO blog(D-2)、MapYourTech(D-1)、NEC(A-4-1) |
| 10-1-2 | **BER を決める要因は、光パワー・非線形歪み・電気系の雑音と歪み・OSNR の4つ。その中で OSNR の寄与が支配的** | 2 | **B** | XKL/NANOG 系解説(D-4)、MapYourTech(D-1) |
| 10-1-3 | **OSNR が低いと再生中継までの到達距離が制限される** | 3 | **A** | EXFO(D-2)、MapYourTech(D-1)、FS.com(D-8-1) |
| 10-1-4 | **OSNR が足りないと、より低次の変調方式に落とさざるを得ない**（例: 18dB では QPSK 止まり、25dB あれば 16QAM で周波数利用効率2倍） | 1 | **C** | MapYourTech のみ。**具体的な dB 値はそのまま書かない**。定性的な「OSNR が変調方式の選択を縛る」だけなら B 相当 |

### 10-2. §3「OSNR は何と何を比べているのか」

| # | 事実 | ソース数 | 信頼度 | ソース |
|---|---|---|---|---|
| 10-2-1 | **OSNR ＝ 信号光パワー / 雑音光パワー、dB 表記。`OSNR = 10log₁₀(S/N)`** | 6+ | **A** | NEC、EXFO、VIAVI、Ciena、Optiwave、MapYourTech |
| 10-2-2 | **参照帯域は 0.1 nm。1550nm 帯において 0.1nm ≒ 12.5 GHz** | 4 | **A** | VIAVI(A-2-1)、NSF PAR 論文(A-3-1)、MapYourTech、ITU-T 系解説 |
| 10-2-3 | **測定帯域 B_m が参照帯域 B_r と異なる場合、ASE は B_r/B_m で重み付けして換算する** | 2 | **B** | 学術資料(A-3 系)、VIAVI。**§7「参照帯域の違いによる値のズレ」の核心なので、必ず原典で確認** |
| 10-2-4 | **OOK/ガウス統計の前提で `BER = ½·erfc(Q/√2)`** | 3 | **A** | Optiwave(A-2-10)、学術資料、一般教科書 |
| 10-2-5 | **BER < 10⁻⁹ には Q > 6、BER < 10⁻¹² には Q > 7 が必要** | 2 | **B** | Optiwave、学術資料。**教科書的に広く知られた値** |
| 10-2-6 | 経験式 `log₁₀(BER) = 10.7 − 1.45×OSNR` | 1 | **C** | Optiwave のみ。**適用条件が不明。書かないほうがよい** |

### 10-3. §4「なぜ劣化するのか」

| # | 事実 | ソース数 | 信頼度 | ソース |
|---|---|---|---|---|
| 10-3-1 | **EDFA は ASE（自然放出光が誘導放出で増幅されたもの）を必ず付加し、これが主要な雑音源** | 6+ | **A** | アンリツ(A-2-9)、EXFO(A-2-4)、フィバーラボ、光響、UCSB 講義、NEC |
| 10-3-2 | **雑音指数 NF は「増幅によって SN 比がどれだけ劣化するか」を表す** | 4 | **A** | アンリツ、フィバーラボ、EXFO、UCSB 講義 |
| 10-3-3 | **ASE は消えない。次段の増幅器は信号と既存の ASE を両方増幅し、さらに自前の ASE を足す。多段では ASE パワーが線形に加算される** | 4 | **A** | MapYourTech、UCSB 講義、ITU-T G.680 Appendix II（要確認）、EXFO |
| 10-3-4 | **同一スパンを N 段カスケードすると、OSNR は `10log₁₀(N)` だけ劣化する** | 3 | **A** | MapYourTech、UCSB 講義、教科書的な標準式。**式の導出は自分で書けるので、そうすること** |
| 10-3-5 | **1スパンの OSNR ≒ `P_ch − NF − L_span + 58`（0.1nm・1550nm 基準）** | 2 | **B** | MapYourTech、業界標準式。**`+58` の由来（`10log₁₀(h·ν·B_ref)`）を自分で導出してから書く** |
| 10-3-6 | **必要 OSNR はライトパス上の位置で変わる。送信側に近いほど高く、受信側に近いほど低い**（増幅器と ROADM が雑音を足していくため） | 1 | **B** | EXFO(D-2) のみだが、**測定器ベンダー公式の記述であり信頼度は高い**。§4 の締めに効く良い視点 |
| 10-3-7 | **増幅器のゲインチルトにより、C帯の中で波長ごとに OSNR がばらつく（一部の波長だけ落ちる）** | 3 | **A** | Cisco(D-5)、EXFO「OSNR Flatness」(D-2)、MapYourTech |

### 10-4. §5「設計値と実測値の差 — マージン」

| # | 事実 | ソース数 | 信頼度 | ソース |
|---|---|---|---|---|
| 10-4-1 | **測定器の仕様（分解能帯域幅、ダイナミックレンジ等）の違いだけで、同じリンクでも OSNR 実測値がズレる** | 2 | **B** | EXFO AN261(A-2-5)、EXFO「OSA 測定の課題」(D-2)。**「なぜ設計値と実測値がズレるか」を、経験でなく公開資料で説明できる貴重なネタ** |
| 10-4-2 | **GSNR = P_ch/(P_ASE + P_NLI)。非線形干渉(NLI)をガウス雑音として扱う（GN モデル）のが実務上の近似** | 4 | **A** | arXiv 複数(A-3-2, B-17)、JOCN(A-3-4)、MapYourTech |
| 10-4-3 | **EOL（寿命末期）でのシステムマージンとして 2〜3 dB 以上を設計目標に置く**（部品劣化・融着修理・モデル誤差を吸収するため） | 2 | **B** | JOCN/arXiv 系(A-3-3, A-3-4)、MapYourTech。**具体的な dB 値を書くなら必ず原典を開いて確認。前職の値と混ざらないよう注意** |
| 10-4-4 | **「マージンをゼロ近くまで削って容量に変える」という設計思想（near-zero margin networking）が業界に存在する** | 3 | **A** | Ciena(C-2-2〜C-2-4)、JOCN(A-3-4)、arXiv(A-3-3) |
| 10-4-5 | **必要 OSNR は変調方式・データレート・網種別・目標 BER で変わる（単一の閾値は存在しない）** | 3 | **A** | EXFO(D-2)、MapYourTech、Cisco。**§5 の主張の骨格になる。「〇〇dB あれば OK」という書き方をしない根拠** |
| 10-4-6 | 受信端の目安として OSNR > 15〜18 dB（100G DPSK で >約18 dB） | 2 | **B** | EXFO(D-2)、MapYourTech。⚠️ **「目安」以上には書かない。**10-4-5 と必ずセットで書くこと |

### 10-5. §6「足りないと言われたときに確認する順序」

| # | 事実 | ソース数 | 信頼度 | ソース |
|---|---|---|---|---|
| 10-5-1 | **コネクタ端面の汚れ・傷は損失と反射を増やし、受信端 OSNR を下げて BER を悪化させる** | 3 | **A** | Cisco(D-5)、FOA(D-7)、MapYourTech |
| 10-5-2 | **単一波長だけ落ちる場合は、増幅器のゲインチルト、または対向 TXP/MXP の波長設定誤りを疑う** | 2 | **B** | Cisco(D-5)、MapYourTech。**「1波長だけか、全波長か」で切り分けが分岐するという構造は §6 の骨格に使える** |
| 10-5-3 | **入力パワー低下の切り分けは、まずファイバの物理的損傷・損失増を確認するのが定石** | 3 | **A** | Cisco(D-5)、FOA(D-7)、複数の実務系記事 |
| 10-5-4 | 実劣化の内訳例（EDFA ポンプ劣化、コネクタ汚れ、融着劣化がそれぞれ 1.2 / 0.5 / 0.3 dB） | 1 | **C** | MapYourTech のみ。**具体的な内訳値は書かない。**「複数の小さな劣化が積み上がる」という定性的な話にとどめる |

> **§6 についての結論**: **公開資料で書けるのは「何を疑うか」までで、「どの順で疑うか」は経験でしか書けない。**
> だからこそ**この節が記事①の価値の中心**になる。出典で埋めようとしないこと。

### 10-6. §7「つまずきポイント」

| # | 事実 | ソース数 | 信頼度 | ソース |
|---|---|---|---|---|
| 10-6-1 | **IEC 61280-2-9 の帯域外補間法**（隣接チャネルとの中間点で雑音を測り線形補間）**は、100G+ のコヒーレント信号や ROADM 経由の網では成立しない** | 3 | **A** | VIAVI(A-2-1)、EXFO(A-2-6, D-2)、IEC 規格要旨。**§7 の最有力ネタ。「昔のやり方が通じなくなった」という物語になる** |
| 10-6-2 | **その後 IEC 61282-12「In-band OSNR」が策定された** | 2 | **B** | EXFO(A-2-6)、業界記事 |
| 10-6-3 | **コヒーレント受信機（DSP）側から OSNR を推定できる／するようになった** | 3 | **A** | NSF PAR 論文(A-3-1)、arXiv NN 推定(A-3-7)、Ciena(C-2-2) |
| 10-6-4 | **偏波多重信号では、従来の OSA による OSNR 測定がそのままでは使えず、Pol-Mux 対応の手法が必要** | 3 | **A** | EXFO(D-2 複数記事)、VIAVI(A-2-1)、業界誌(D-8-7) |
| 10-6-5 | **1スパン OSNR を `P_TX + G − L − NF` と書く誤り**（G が相殺され、値がゼロ近傍や負になり、健全なリンクを不良と誤判定する。スケールを決めるのは帯域定数 +58 のほう） | 1 | **C** | MapYourTech のみ。⚠️ **裏取り必須だが、記事①§7 の最有力候補。**自分で式を導出できれば、出典なしで自分の言葉として書ける |
| 10-6-6 | **SD-FEC は数 dB 分の OSNR ペナルティを取り返す（代償は複雑さと 20% 程度のオーバーヘッド、遅延）** | 3 | **A** | CableLabs(B-15)、MERL(B-16)、MapYourTech |
| 10-6-7 | **OSNR が 3 dB 下がると BER は数桁悪化する（急峻な依存性）** | 1 | **C** | MapYourTech のみ。**定性的に「急峻」と書くだけならA相当**（Q-BER の erfc 特性から自明）。**具体的な桁数は書かない** |

### 10-7. 本（1〜6章）向けに一致が取れているもの

| # | 事実 | ソース数 | 信頼度 |
|---|---|---|---|
| 10-7-1 | **DWDM グリッドは 193.1 THz を基準に定義。固定グリッドは 12.5 / 25 / 50 / 100 GHz 間隔。フレキシブルグリッドは中心 6.25 GHz 粒度、スロット幅 12.5×m GHz** | 3 | **A**（ITU-T G.694.1 要旨、IETF ドラフト、複数解説） |
| 10-7-2 | **G.652 は 1310nm ゼロ分散。1550nm での波長分散は約 17 ps/nm/km、損失約 0.2 dB/km、PMD 概ね 0.1 ps/√km 未満** | 3 | **A**（FOA、複数解説。**原典 G.652 で必ず確認**） |
| 10-7-3 | **G.655（NZ-DSF）は 1550nm 帯で意図的に小さな分散を残し、四光波混合(FWM)を抑える設計** | 3 | **A** |
| 10-7-4 | **SPM / XPM / FWM はいずれもカー効果（パワー依存の屈折率）に由来。SPM と SBS は単一チャネルでも起きるが、XPM / FWM / SRS は多重系(DWDM)特有** | 4 | **A**（複数の学術資料） |
| 10-7-5 | **ROADM の第3世代は WSS ベース。WSS は任意の出力ポートに任意の波長を出せる（ポートと波長が独立）** | 3 | **A**（IEEE JSTQE、FS.com、複数解説） |
| 10-7-6 | **400ZR は OIF の Implementation Agreement（2020-04-29 公開）。80km 級の増幅系 DCI 向けにマルチベンダ相互接続を規定** | 2 | **A**（OIF 公式、業界誌） |

---

## 11. 追記後の作業順序（本人向け）

```
【1日目・30分】第4章 4-1 の ★★★ 7本をシークレットウィンドウで検証
              → 開けたものを第1章「採用リスト」へ

【2日目・30分】第8章の D-1 / D-2 / D-3 / D-5 / D-7 を開いて、
              ライセンス表示（Terms / Copyright / Legal）を確認
              → 第9章 9-4 の表を実測値で埋め直す

【3日目・60分】第10章の信頼度 C の項目（10-1-4, 10-2-6, 10-5-4, 10-6-5, 10-6-7）を
              一次資料で裏取り。取れなければ記事から落とす
              ※ 10-6-5 だけは、式を自分で導出できれば出典不要になる

【4日目〜】   記事①執筆。9-5 の手順を守る（特に「画面を閉じる」）
```

---

## 12. 更新履歴

| 日付 | 内容 |
|---|---|
| 2026-08-30 | 初版。WebSearch により候補 60 件超を収集。**外部エグレス遮断により WebFetch 検証は 0 件**。採用 0 / 不採用 40 / 検証待ち・検証不能 55 |
| 2026-08-30（追記） | 前提訂正（英語圏には実務者コミュニティが存在する）を受け、第8章（英語圏コミュニティ 9 系統・30 サイト超）、第9章（引用ルール・ライセンス判定表）、第10章（複数ソース一致事実 33 項目）を追加。あわせて **MIT OCW のライセンス記述の誤り（CC BY-NC-SA＝非営利限定であり有料書には使えない）を訂正**し、MapYourTech 等を第3章から第8章に再分類 |
