# 出典リスト — 光トランシーバ（pluggable）の型番体系

**作成日**: 2026-08-31
**用途**: 本 第6章「呼び方が食い違うもの」の技術的裏付け
**対象読者**: 配属直後の技術者／営業・技術営業

---

## 0. この文書の制約 — 先に読むこと

> **この調査環境からは外部サイトへの直接アクセス（WebFetch）が組織のエグレスポリシーで遮断されている（403）。**
> したがって**本文書の記述はすべて「Web 検索エンジンが返したスニペット」由来**であり、
> **原典（IEEE 規格書、MSA 仕様書、ベンダーデータシート）を直接読んで確認したものは 1 件もない。**

このため以下のルールを守ること。

1. **本文書の記述をそのまま本文に転記しない。** 有料の本に使う以上、著者本人が原典で裏を取ってから書く。
2. **転載は不可。** 各社のブログ・データシートの文章は使わない。事実を複数ソースで確認したうえで**自分の言葉で書き直す**。本文書の表現も要約であり、そのまま使う想定ではない。
3. **確度タグを本文に持ち込まない。** タグは著者の作業用。`[未確認]` のものは本に書かない。

### 確度タグの定義

| タグ | 意味 |
|---|---|
| `[複数一致]` | 3件以上の独立したソース（別ドメイン）のスニペットで一致 |
| `[単一]` | 1ソースのスニペットのみ。裏取り未了 |
| `[未確認]` | 断片的で確証なし。本には書かない |

### ソースの質について（重要）

検索でヒットするのは**大半が光トランシーバ販売業者のブログ**（FS.com、FiberMall、NADDOD、LINK-PP、QSFPTEK、Optcore 等）である。
これらは**内容が相互にコピーされている疑いが強く、「3社で一致」が「独立した3件」を意味しない**可能性がある。
一次情報に近いのは以下のみで、いずれも**未読（スニペットのみ）**。

- `ieee802.org` / `grouper.ieee.org` — IEEE 802.3 タスクフォースの提案資料（PDF、無償公開）
- `100glambda.com` — 100G Lambda MSA の仕様書（無償公開）
- `tiafotc.org` — TIA Fiber Optics Tech Consortium の規格サマリ
- `cisco.com` / `arista.com` / `juniper.net` — ベンダー公式データシート

**著者がブラウザで開いて確認すべきはこの4系統。**販売業者ブログは方向づけにのみ使い、根拠にはしないこと。

---

## 1. A. 型番の読み方の体系

### 1.1 基本フォーマット

```
400GBASE-DR4
└┬─┘└┬─┘ └┬┘└┬
 │   │    │  └─ レーン数（4）
 │   │    └──── 到達距離コード（D = 約500m）
 │   └───────── "BASE" = ベースバンド伝送
 └───────────── 速度（400 Gbit/s）
```

`[速度]BASE-[到達距離コード][レーン数]` という構造 `[複数一致]`

### 1.2 到達距離コード

| コード | 由来（諸説あり） | ファイバ | おおよその到達距離 | 確度 |
|---|---|---|---|---|
| **S**R | Short Reach | MMF（850nm） | 100m 級（世代・OM種別で変わる） | `[複数一致]` |
| **D**R | Data center Reach | SMF（1310nm） | **500 m** | `[複数一致]` |
| **F**R | "Fabric" / "Four hundred"（由来は諸説） | SMF（1310nm 帯） | **2 km** | `[複数一致]` |
| **L**R | Long Reach | SMF | **10 km**（ただし後述の例外あり） | `[複数一致]` |
| **E**R | Extended Reach | SMF（1550nm 帯が多い） | **40 km** | `[単一]` |
| **Z**R | （IEEE の用語ではない） | SMF | 80 km 級。400G では OIF のコヒーレント仕様 400ZR が別に存在 | `[単一]` |

**注意点（章に書く価値がある）**

- **FR の "F" が何の略かは、ソースによって食い違っている。** ある解説は "Fabric Reach"、別の解説は 100G Lambda MSA が DR(500m) と LR(10km) の間を埋めるために作った区分、と書いている `[単一]`。**由来を断定して書かないほうがよい。**
- **LR = 10km は 400G では成立しない場合がある。** IEEE の `400GBASE-LR4-6` は**到達距離 6 km** の仕様である `[単一：tiafotc.org / ieee802.org の提案資料タイトル "400GBASE-LR4 (6 km) Baseline Proposal"]`。一方 100G Lambda MSA には `400G-LR4-10`（10 km）がある `[単一：100glambda.com]`。**市販の「400G LR4」は 10km 品が普通だが、IEEE 名の LR4-6 は 6km。ここは食い違いの実例として使える。**

### 1.3 末尾の数字が意味するもの — ここが最大の誤解ポイント

**末尾の数字は「レーン数」であって、「芯数」でも「波長数」でもない。** `[複数一致]`

そして**同じ「4」でも中身が正反対**になる。

| 型番 | 末尾の 4 の意味 | 物理的な帰結 |
|---|---|---|
| 400GBASE-**DR4** | **並列の4本のファイバ**（1波長 × 4本） | 送受で **8芯**、MPO |
| 400GBASE-**FR4** | **1本のファイバ上の4波長**（WDM） | 送受で **2芯**、デュプレックス LC |

→ **「型番の数字を見ても、必要な芯数は分からない」。距離コード（D か F/L か）を見ないと分からない。**
これは章の主題そのもの。`[複数一致]`

**判別の実用ルール（著者の言葉に落とすとよい）**

- `D`（DR / DR4 / DR8）= **並列（パラレル）SMF** → MPO → 芯数 = レーン数 × 2
- `F` / `L` / `E`（FR4 / LR4 / ER8 等）= **WDM** → デュプレックス LC → 芯数 = 2
- 例外: `400GBASE-FR8` / `LR8` は8波長を1対のファイバに載せる（IEEE 802.3bs）`[単一]`

### 1.4 表記ゆれ

観察されたパターン `[複数一致（観察）／断定は避けること]`：

| 表記 | 出どころの傾向 | 例 |
|---|---|---|
| `400GBASE-XXX`（BASE あり） | **IEEE 802.3 が定めた名前** | 400GBASE-DR4, 400GBASE-FR4, 100GBASE-FR1 |
| `400G-XXX`（BASE なし、ハイフン） | **MSA の仕様名** | 400G-FR4, 400G-LR4-10, 100G-FR（すべて 100G Lambda MSA） |
| ベンダー型番 | 各社独自 | QDD-400G-DR4-S（Cisco）, QDD-400G-XDR4（Arista） |

> **ただしこの規則はベンダー資料では守られていない。** 販売サイトは平気で `400GBASE-DR4+` と書く（IEEE 名ではないのに BASE を付けている）`[複数一致：prolabs / approvednetworks / edgeoptic の商品名]`。
> **「BASE が付いていれば IEEE」と読者に教えるのは危険。**「BASE が付いていない＝ほぼ確実に IEEE 名ではない」という**片側だけ**なら比較的安全。

---

## 2. B. 著者が挙げた具体的な型番

### 2.1 400GBASE-DR4

| 項目 | 内容 | 確度 |
|---|---|---|
| 定義元 | **IEEE 802.3bs-2017**。PMD は Clause 124 | `[複数一致]`（Clause 番号は `[単一]`） |
| 到達距離 | **500 m** | `[複数一致]` |
| ファイバ | **並列シングルモード（parallel SMF）**。MMF ではない | `[複数一致]` |
| **芯数** | **8芯（送信4 + 受信4）** | `[複数一致]` |
| コネクタ | **MPO-12 / APC**。12芯コネクタだが**使うのは8芯、4芯は未使用** | `[複数一致]` |
| 波長 | **単一波長 1310 nm 帯**。4本のファイバすべてが同じ波長。WDM ではない | `[複数一致]` |
| 変調・FEC | レーンあたり 100 Gb/s PAM4、RS-FEC（KP4）必須 | `[複数一致]` |
| ブレイクアウト | **可能。4 × 100GBASE-DR へ**（MPO-12 → LC×4 のブレイクアウトケーブル） | `[複数一致]` |

**ブレイクアウトの条件（営業がいちばん外す部分）**

1. **スイッチ側がそのポートを 4×100G に channelize できること。** モジュールの能力とは別問題。ASIC・OS の対応が要る `[単一]`
2. **相手側が「100G シングルラムダ（1波長で100G PAM4）」であること。** すなわち **100GBASE-DR / FR1 / LR1**。
   **旧来の 100GBASE-SR4 / LR4 / CWDM4 / PSM4（4×25G）とはリンクしない** `[複数一致]`
3. **両端で FEC 設定が揃っていること。** 揃っていないと「光は来ているのにリンクしない」`[複数一致]`
4. 距離は DR4 の場合 **各 100G 支線も 500 m まで** `[複数一致]`

**事故になりやすい点**: 100G PSM4 と**同じ MPO-12 コネクタ**を使う。**物理的には挿さるが、レーンレート（25G NRZ × 4 vs 100G PAM4 × 1）が違うのでリンクしない** `[複数一致]`。
「挿さったのにリンクしない」の典型例として章に使える。

**未確認**: IEEE 規格上の中心波長の許容範囲（1304.5〜1317.5 nm 程度と思われるが未裏取り）`[未確認]`

---

### 2.2 400GBASE-FR4

| 項目 | 内容 | 確度 |
|---|---|---|
| 定義元 | **IEEE 802.3cu-2021**。PMD は Clause 151。**802.3bs ではない**（bs にあるのは FR8/LR8） | `[複数一致]`（Clause 番号は `[単一]`） |
| 前史 | **先に 100G Lambda MSA が `400G-FR4` を策定**し、IEEE 802.3cu が後から取り込んだ | `[複数一致]` |
| 到達距離 | **2 km** | `[複数一致]` |
| ファイバ | **デュプレックス SMF（1対）** | `[複数一致]` |
| **芯数** | **2芯（送信1 + 受信1）** | `[複数一致]` |
| **波長** | **4波。CWDM グリッドの 1271 / 1291 / 1311 / 1331 nm** | `[複数一致]` |
| **波長間隔** | **20 nm**（上記4波から算術的に自明。CWDM グリッド） | `[複数一致]` |
| コネクタ | **デュプレックス LC**。市販品は **UPC** 研磨の記載が多い | `[複数一致]`（UPC/APC の別は `[単一]`） |
| レーン | 100 Gb/s PAM4 × 4波を1対のファイバに多重 | `[複数一致]` |
| **ブレイクアウト** | **不可。**4波が1本のファイバに多重されているので、光学的に分けられない。400G 1本として使う | `[複数一致]`（「不可」と明示した記述は `[単一]`。多重方式から論理的に自明） |

> **著者の主張「FR4 は SM ファイバーで400G渡し」は正しい。** `[複数一致]`
> 補強するなら「**FR4 は分けられない**、DR4 は分けられる」という対比が最も効く。

---

### 2.3 400G-DR+ / DR4+ — **最重要**

**結論: `DR4+`（`DR+`）は IEEE の名前でも MSA の仕様名でもない。ベンダー発の通称である。** `[複数一致]`

#### 何を指しているのか

| 項目 | 内容 | 確度 |
|---|---|---|
| 実体 | **DR4 と同じ並列 SMF 構成（8芯、MPO-12/APC、1310nm 単一波長）のまま、レーンごとの光パワーバジェットを上げて 2 km 対応にしたもの** | `[複数一致]` |
| 別の言い方 | **「4 × 100G-FR」**。各レーンが 100G Lambda MSA の 100G-FR ＝ IEEE 100GBASE-FR1 と同じ光仕様 | `[複数一致]` |
| DR4 との違い | **到達距離の延伸（500 m → 2 km）。構成・コネクタ・芯数・波長は同じ** | `[複数一致]` |
| ブレイクアウト先 | **4 × 100GBASE-FR1（2 km）**。DR4 が 4×100G-DR(500m) なのに対し、こちらは 2km の支線が引ける | `[複数一致]` |

#### 同じものに付いている名前（章の主題そのもの）

| 呼び名 | 出どころ | 確度 |
|---|---|---|
| `400G-DR4+` / `400GBASE-DR4+` | 販売業者・一部ベンダーの通称（IEEE 名ではないのに BASE を付けている例） | `[複数一致]` |
| `400G-XDR4` / `400GBASE-XDR4` | **Arista の型番 `QDD-400G-XDR4`**（eXtended reach DR4） | `[複数一致]` |
| `QDD-4X100G-FR-S` | **Cisco の型番**。名前に DR も XDR も入っていない | `[複数一致]` |
| `4x 100G-FR` | 汎用的な機能名 | `[複数一致]` |
| **`400GBASE-DR4-2`** | **IEEE 802.3df-2024 で後から標準化された正式名**（`-2` は 2 km の意） | `[複数一致]` |

> **これが章のいちばん強い実例になる。**
> **同一の機能に、少なくとも5通りの呼び名がある。**
> しかも**時系列で意味が変わった**:
> 1. IEEE には 500m（DR4）と 2km（FR4、デュプレックス）しかなかった
> 2. 市場は「2km の並列SMF／ブレイクアウト用」を欲しがった → **各社が勝手に DR4+ / XDR4 / 4x100G-FR と名付けた**（＝著者の言う「標準化が終わってないから各社バラバラ」の状態）
> 3. **2024年、IEEE 802.3df がこれを `400GBASE-DR4-2` として標準化した** `[複数一致]`
>
> つまり**「標準化が終わっていない → バラバラ → 後から標準名が付く → でも現場と型番には旧称が残り続ける」**という、
> 著者の主張の**完全な1サイクル**が観測できている。**ここは本章の核にできる。**

#### 未確認・要注意

- **`DR+` と `DR4+` が同じものかは確認できていない。** 検索では `DR4+` が圧倒的で、`DR+` 単独の用例は拾えなかった `[未確認]`。著者が現場で聞いた言い方（`DR+`）は口語の省略の可能性が高いが、断定できない。
- **Cisco `QDD-4X100G-FR-S` が 400GbE 1本として（=対向の同型モジュールと）リンクできるかは不明。** Cisco データシートのスニペットは「**100G ブレイクアウトで最大2km**」としか書いておらず、400G エンドツーエンドの記述が見当たらない `[単一・要確認]`。
  **一方 Arista `QDD-400G-XDR4` は 400G 名を冠している。**「同じ機能」と言い切る前に両社データシートの確認が必要。
- `400GBASE-DR4-2` の IEEE 上の到達距離が「2 km」であることは `[単一：tiafotc.org]`。TIA FOTC のページは「到達距離はファイバ種別による」という書き方をしている点に注意。

---

## 3. C. 標準化の主体と、そのズレ

### 3.1 誰が何を決めているか

| 主体 | 決めているもの | 例 |
|---|---|---|
| **IEEE 802.3** | **光の PMD（波長・パワー・距離）と MAC/PCS**。`xxxBASE-yyy` という名前 | 400GBASE-DR4, 400GBASE-FR4 |
| **100G Lambda MSA** | **1波長100G(PAM4) の光仕様**。IEEE より先行することが多い | 100G-FR, 100G-LR, 400G-FR4, 400G-LR4-10 |
| **QSFP-DD MSA / OSFP MSA** | **筐体の機械寸法・ケージ・電気ピン配置・熱**。**光の仕様は決めていない** | QSFP-DD, OSFP, OSFP-XD |
| **OIF** | コヒーレント（400ZR 等） | 400ZR |
| **ベンダー独自** | 上のどれでもない通称・型番 | DR4+, XDR4, 各社 SKU |

`[複数一致]`

> **読者（特に営業）に効く整理**:
> **「モジュールが挿さるか」＝ 形状 MSA（QSFP-DD / OSFP）**
> **「光がつながるか」＝ IEEE / 100G Lambda MSA の PMD**
> **この2つは完全に別の話で、別の団体が決めている。**「QSFP-DD だから大丈夫」は何の保証にもならない。`[複数一致]`

### 3.2 同じ機能に複数の名前がついている例（章に直接使える一覧）

| # | 実体 | 呼び名 | 確度 |
|---|---|---|---|
| 1 | 2km・並列SMF・8芯・4×100G ブレイクアウト可 | **DR4+ / DR4-2 / XDR4 / 4x100G-FR / 400GBASE-DR4-2** | `[複数一致]` |
| 2 | 1波長100G・2km・デュプレックス | **100G-FR（MSA）** = **100GBASE-FR1（IEEE 802.3cu）** | `[複数一致]` |
| 3 | 1波長100G・10km・デュプレックス | **100G-LR（MSA）** = **100GBASE-LR1（IEEE）** | `[複数一致]` |
| 4 | 400G・CWDM4・2km・デュプレックス | **400G-FR4（100G Lambda MSA）** = **400GBASE-FR4（IEEE 802.3cu）** | `[複数一致]` |
| 5 | 400G・CWDM4・長距離 | **400GBASE-LR4-6（IEEE, 6km）** と **400G-LR4-10（MSA, 10km）**。市販の「400G LR4」はたいてい 10km 品 | `[単一〜複数一致（要確認）]` |
| 6 | 800G・500m・並列SMF | **800GBASE-DR8（MPO-16, 16芯 1個）** と **800G-2×DR4（MPO-12 × 2個, 8芯×2）**。**距離は同じ 500m だがコネクタが違う** | `[単一]` |

**#6 は特に危ない。**「800G DR8 でお願いします」で MPO-16 が来たが、実際は 2×DR4（MPO-12 二口）が必要だった、という食い違いが起こりうる `[単一]`。

### 3.3 名前が同じで中身が違う例

- **`QDD-400G-FR4` という同じ型番文字列を Juniper と Arista の両方が使っている。**
  光学的には同等だが **EEPROM のベンダーコーディングが違い、他社機では unsupported transceiver になる** `[単一・要裏取り]`。
  → 「型番が一致していても動くとは限らない」の実例。ただし**1ソースのみ**なので、本に書くなら両社のデータシートで確認すること。
- 「400GBASE-DR4+」のように、**IEEE 名ではないものに BASE を付けた商品名が流通している** `[複数一致]`。

---

## 4. D. 物理的な接続

### 4.1 MPO コネクタの種類

| 種別 | 芯数 | 主な用途 | 確度 |
|---|---|---|---|
| MPO-8 | 8 | 8芯だけ必要な用途（DR4 等）向けの省芯版 | `[単一]` |
| **MPO-12** | **12** | **400GBASE-DR4（うち8芯使用、4芯は未使用）**、100G PSM4、800G 2×DR4 | `[複数一致]` |
| **MPO-16** | **16** | **800GBASE-DR8 / 400GBASE-SR8 など8レーン品**（8送8受で16芯を使い切る） | `[複数一致]` |
| MPO-24 | 24 | 高密度幹線 | `[単一]` |
| MPO-32 / 48 | 32 / 48 | 幹線・パッチパネル | `[単一]` |

**研磨（端面）**

- **SMF の並列（DR4 / DR8）→ APC**（斜め研磨、緑色）`[複数一致]`
- **MMF の並列（SR8 等）→ UPC** `[単一]`
- **APC と UPC は混ぜられない。** 挿さっても反射が増えてリンクしない／不安定になる（原理上自明だが、明示したソースは拾えていない）`[未確認]`

### 4.2 デュプレックス LC との違い

| | デュプレックス LC | MPO |
|---|---|---|
| 芯数 | **2芯**（Tx 1 / Rx 1） | 8〜48芯 |
| 使う型番 | FR4 / LR4 / ER4、100GBASE-FR1 など **WDM 系** | DR4 / DR8 / SR4 / SR8 など **並列系** |
| ブレイクアウト | 不可 | 可（ハーネスで分岐） |

`[複数一致]`

### 4.3 ブレイクアウトケーブルの構成

**400G DR4 → 4×100G の場合** `[複数一致]`

```
[MPO-12 / APC メス]───┬── LC デュプレックス ①（Tx1 + Rx1）
     8芯使用          ├── LC デュプレックス ②
                      ├── LC デュプレックス ③
                      └── LC デュプレックス ④
```

- **MPO 側 1 個 → LC デュプレックス 4 本**（＝ LC コネクタとしては 8 個）`[複数一致]`
- ケーブル自体は **8芯**（MPO-12 の12芯すべてを配線した製品もあるが、使うのは8芯）`[複数一致]`
- **極性（ポラリティ）は Type B** が DR4 / PSM4 系で使われる `[単一・要確認]`
- SN / MDC コネクタで出す製品もある（高密度用）`[単一]`

### 4.4 3つの接続形態の使い分け

| 形態 | 型番の例 | 使う場面 | 確度 |
|---|---|---|---|
| **MPO-MPO** | 400G DR4 ⇔ 400G DR4 | 400G を 400G のまま、DC 内で 500m（DR4+/XDR4 なら 2km）渡す | `[複数一致]` |
| **MPO-breakout（MPO→LC×4）** | 400G DR4 ⇔ 100G DR × 4台 | **1台の400Gポートを4本の100Gに分けて、4台の機器に配る** | `[複数一致]` |
| **SM-SM（デュプレックス LC ⇔ LC）** | 400G FR4 ⇔ 400G FR4 | **400G を1対のファイバで丸ごと渡す。**キャリア回線・既設2芯を使う場合はこれしかない | `[複数一致]` |

> **著者の指摘どおり、「どのファイバか」は波長と同格に重要。**
> **既設が2芯しかない区間に DR4 は使えない**（8芯必要）。
> **逆に、4台に分配したいのに FR4 を買っても分けられない。**

### 4.5 物理的に挿さらない／挿さるのにつながらない組み合わせ

**(a) 物理的に挿さらない** `[複数一致]`

- **MPO-16 ⇔ MPO-12**: **MPO-16 はキー（位置決め突起）がオフセットしており、MPO-12 のアダプタと勘合しない。**
  誤挿入で端面を壊さないための設計。無理に挿すと MT フェルールを損傷する `[複数一致]`
- **MPO ⇔ LC**: 形状が全く違う（自明）
- **QSFP-DD ⇔ OSFP**: **ケージが違うので入らない。**「どちらも400Gだから同じ」は誤り `[複数一致]`

**(b) 挿さるのにリンクしない（こちらが本当の事故）** `[複数一致]`

| 組み合わせ | 挿さるか | つながるか | 理由 |
|---|---|---|---|
| 400G DR4 ⇔ 100G PSM4 | **MPO-12 同士なので挿さる** | **× つながらない** | レーンレートが違う（100G PAM4×1 vs 25G NRZ×4） |
| 400G DR4 ⇔ 100GBASE-SR4/LR4/CWDM4 | ケーブル次第で挿さる | **×** | 4×25G 系はシングルラムダ100Gと非互換 |
| 400G DR4(500m) ⇔ 100G FR1(2km) を 2km で | 挿さる | **△〜×** | DR4 のパワーバジェットは 500m 想定。2km なら DR4+/XDR4 が要る |
| 400G DR4 ⇔ 400G FR4 | **そもそもコネクタが違う（MPO vs LC）** | × | PMD が違う。両端は同じ PMD でなければならない |
| 片端 FEC 有効 / 片端無効 | 挿さる | **×** | KP4 RS-FEC は両端一致必須 |
| 型番同一でもベンダーコーディング違い | 挿さる | **×（機器が拒否）** | EEPROM の vendor ID チェック `[単一]` |

> **章に書くべき一言**: 「**両端は同じ PMD でなければならない**」`[複数一致]`。
> 「400G 同士だから」でも「QSFP-DD 同士だから」でもなく、**PMD 名（400GBASE-DR4 なのか FR4 なのか）が一致しているか**が唯一の判定基準。

---

## 5. E. 認識の食い違いの実例（英語圏）

### 結論: **具体的な事例（フォーラムのスレッド、事故報告、ポストモーテム）は見つからなかった。**

以下を試したが、該当するものは検索結果に出てこなかった。

- reddit / NANOG / Cisco Community 等での「400G を発注したら DR4 と FR4 が食い違った」系のスレッド → **ヒットなし**
- 「carrier provided FR4, customer had DR4, link down」的な事例談 → **ヒットなし**
- 「ordered wrong 400G optics」「400G interface mismatch story」 → **販売業者の一般論しか出ない**

**検索エンジン経由では、この種の生々しい事例は販売業者ブログの SEO 記事に埋もれて拾えない**というのが実感。
（WebFetch が使えれば NANOG のメーリングリストアーカイブ等を直接当たれるが、この環境では不可）

### 代わりに拾えた「一般論としての注意喚起」

いずれもベンダー／販売業者の記述であり、**個別事例ではない**。

| 内容 | 出どころ | 確度 |
|---|---|---|
| 「400G 光は全部同じで距離だけ違う、という思い込みが混乱の出発点」 | heyoptics.net "A Guide to 400G Transceiver: Same Name but Different Specs" | `[単一]` |
| 「MPO コネクタの形式が 400G 導入失敗の最大の原因」 | network-switch.com | `[単一]` |
| 「400G に不慣れな技術者は DR4 をマルチモードだと思い込む／OSFP と QSFP-DD が差し替え可能だと思い込む」 | network-switch.com | `[単一]` |
| 「1λ トランシーバの運用でいちばん多いミスは FEC の設定」 | Viavi 4×100GE DR4 Breakout Testing アプリケーションノート | `[単一]` |
| 「ブレイクアウトケーブルはスイッチのモデルではなく ASIC 単位で検証すべき」 | vitextech.com | `[単一]` |

> **章の書き方の提案**: 事例が一次情報として取れていない以上、**「英語圏でもこう注意喚起されている」というレベルに留め、
> 生々しい事例は著者自身の実務経験（一般化・匿名化したもの）で書くのが安全**。
> 「よくキャリアと客の認識するインターフェースが異なった」は著者の一次体験であり、これ自体が本書の価値。

---

## 6. 参考にした URL 一覧（**すべて未読・検索スニペット由来**）

### 一次情報に近いもの（**著者が優先して開くべき**）

| URL | 内容 |
|---|---|
| https://www.tiafotc.org/ieee-802-3-ethernet-standards-update/singlemode-standards-update/400gbase-dr4/ | 400GBASE-DR4 の規格サマリ |
| https://www.tiafotc.org/ieee-802-3-ethernet-standards-update/singlemode-standards-update/400gbase-dr4-2/ | **400GBASE-DR4-2（＝DR4+ の標準名）** |
| https://www.tiafotc.org/ieee-802-3-ethernet-standards-update/singlemode-standards-update/400gbase-fr4/ | 400GBASE-FR4 |
| https://www.tiafotc.org/ieee-802-3-ethernet-standards-update/singlemode-standards-update/400gbase-lr4-6/ | **400GBASE-LR4-6（6km）** |
| https://www.tiafotc.org/ieee-802-3-ethernet-standards-update/singlemode-standards-update/800gbase-dr8-2/ | 800GBASE-DR8-2 |
| http://100glambda.com/specifications/download/2-specifications/7-400g-fr4-technical-spec-d2p0-2 | **100G Lambda MSA 400G-FR4 仕様書** |
| https://100glambda.com/specifications/send/2-specifications/10-400g-lr4-10-technical-spec-rev1-0 | 100G Lambda MSA 400G-LR4-10 仕様書 |
| https://100glambda.com/specifications/send/2-specifications/11-100g-lr1-20-er1-30-er1-40-technical-specs-rev-1p1 | 100G Lambda MSA 100G-LR1-20 等 |
| https://grouper.ieee.org/groups/802/3/cu/public/May19/lewis_3cu_01a_0519.pdf | IEEE 802.3cu 400GBASE-FR4 ベースライン提案 |
| https://grouper.ieee.org/groups/802/3/cu/public/Sept19/lewis_3cu_02a_0919.pdf | IEEE 802.3cu 400GBASE-LR4(6km) ベースライン提案 |
| https://www.ieee802.org/3/df/public/22_05/22_0602/welch_3df_01a_220602.pdf | IEEE 802.3df 800GBASE-DR4-2 等ベースライン提案 |
| https://www.ieee802.org/3/dj/public/23_03/welch_3dj_01a_2303.pdf | IEEE 802.3dj 400GBASE-DR2-2 提案 |
| https://www.ieee802.org/3/cn/public/tf_interim/19_0924/cole_3cn_01a_190924.pdf | IEEE 802.3cn 400GBASE-ER8 等 |
| https://grouper.ieee.org/groups/802/3/hssg/email/msg01702.html | **IEEE 802.3ba の PHY 命名文字についての議論（命名規則の由来）** |
| https://osfpmsa.org/ | OSFP MSA |
| https://www.ethernetalliance.org/ ※ https://ethernetalliance.org/wp-content/uploads/2018/02/OFC_400G_18_0314_Final.pdf | Ethernet Alliance の 400G 規格まとめ |
| https://www.viavisolutions.com/en-us/literature/4x100ge-dr4-breakout-testing-application-notes-en.pdf | **4×100GE DR4 ブレイクアウト試験（FEC の注意点）** |

### ベンダー公式データシート

| URL | 内容 |
|---|---|
| https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/qsfp-400g-dr4-transceiver-modules-ds.html | Cisco QSFP-400G-DR4 |
| https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/datasheet-c78-743172.html | **Cisco 400G QSFP-DD 一覧（DR4-S / 4X100G-FR-S / FR4-S の違い）** |
| https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/400g-qsfp-transceiver-modules-ds.html | Cisco 400G QSFP 一覧 |
| https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/solution-overview-c22-743387.html | Cisco シングルラムダ100G 概要 |
| https://www.arista.com/assets/data/pdf/Datasheets/Arista-400G_Optics_FAQ.pdf | **Arista 400G Optics FAQ（XDR4 の位置づけ）** |
| https://www.arista.com/assets/data/pdf/Datasheets/Transceiver-Data-Sheet.pdf | Arista トランシーバ一覧 |
| https://www.juniper.net/documentation/us/en/hardware/800g-optics-cables-guide/optics/topics/concept/800g-know-your-800gtransceiver.html | Juniper 800G トランシーバ解説 |
| https://www.cisco.com/c/dam/en/us/products/collateral/interfaces-modules/transceiver-modules/fiber-optic-trans.pdf | Cisco ブレイクアウトケーブル発注ガイド |
| https://www.cisco.com/c/dam/en/us/products/collateral/interfaces-modules/transceiver-modules/cabling-guide-100-400g.pdf | Leviton/Cisco 100G・400G 配線ガイド |
| https://www.jabil.com/dam/jcr:85ca8c5a-2847-4015-9289-d694268d08e3/Jabil_400G%20PAM4%20QSFP-DD%20DR4-DR4+%20Transceiver_DS_16_DRAFT.pdf | **Jabil 400G DR4/DR4+ データシート（DR4+ の各レーンが 100G-FR 準拠と明記）** |
| https://www.intel.com/content/www/us/en/products/sku/135329/intel-silicon-photonics-400g-dr4-qsfpdd-optical-transceiver/specifications.html | Intel シリコンフォトニクス 400G DR4 |

### 販売業者・解説ブログ（**方向づけのみ。根拠にしない**）

- https://www.naddod.com/blog/understanding-the-400g-dr4-and-fr4-optical-transceivers （**DR4+ は「MSA としての仕様がないベンダー独自の呼称」と明記**）
- https://www.heyoptics.net/blogs/wiki/400g-transceiver-name-specs （**"Same Name but Different Specs"**）
- https://www.heyoptics.net/products/qsfpdd-xdr4-400g （XDR4 = DR4+ = 4x100G-FR）
- https://www.heyoptics.net/blogs/wiki/400gbase-standardization-trend
- https://www.l-p.com/blog/reviews-comparisons/fr4-vs-dr4-differences-in-400g-optics.htm
- https://www.link-pp.com/knowledge/400g-qsfp-dd-fr4-datacenter-optical-guide.html （FR4 = 802.3cu Clause 151）
- https://www.l-p.com/blog/compatibility-alternatives/qdd-400g-xdr4-interoperating-with-100g-fr1-optical-nodes.htm （XDR4 と 100G-FR1 の相互接続）
- https://www.fibermall.com/blog/mpo-connectors-400g-800g.htm
- https://www.fibermall.com/blog/osfp-connector-types-guide.htm （MPO-16 のキーオフセット）
- https://www.fibermall.com/blog/psm4.htm
- https://network-switch.com/blogs/networking/osfp-400g-dr4-optical-modules
- https://network-switch.com/blogs/networking/mpo-connectors-explained-2025
- https://www.vitextech.com/blogs/blog/400gdr4-to-4-100g-breakout-planning-guide
- https://www.optcore.net/400g-dr4-transceiver-guide-w6/
- https://stordis.com/compatibility-guide-for-switch-ports-transceivers-fiber/
- https://www.flexoptix.net/en/s2-ta4l-x.html （MPO-APC → LC×4 ブレイクアウト、8芯）
- https://store.10gtek.com/400gb-s-qsfp-dd-4x-100g-fr-xdr4-mpo-12-apc-smf-2-km/p-26732 （「4x 100G-FR (XDR4)」という商品名そのもの）

---

## 7. 著者が確認すべき項目（チェックリスト）

**原典を開いて裏を取るべきもの。優先度順。**

### 最優先（章の核に関わる）

- [ ] **`400GBASE-DR4-2` が IEEE 802.3df-2024 に本当に入っているか、到達距離は 2km か** → tiafotc.org の DR4-2 ページと IEEE 802.3df の目次
- [ ] **`DR4+` / `XDR4` / `4x100G-FR` / `DR4-2` が本当に同一の光仕様か** → Arista 400G Optics FAQ と Cisco 400G QSFP-DD データシートを突き合わせる
- [ ] **Cisco `QDD-4X100G-FR-S` が 400GbE 単体リンクをサポートするか（ブレイクアウト専用か）** → Cisco データシート
- [ ] **著者が現場で聞いた `DR+` が `DR4+` と同じものか** → 著者の記憶・当時の資料での確認。同じでない可能性を排除できていない
- [ ] **`400GBASE-DR4` の IEEE Clause 番号（124）と `400GBASE-FR4`（151）** → IEEE 802.3 の目次（無償版 Get IEEE 802 で確認可）

### 高（数字を本に書くなら必須）

- [ ] **FR4 の4波長 1271/1291/1311/1331 nm と、規格上の波長許容範囲** → 100G Lambda MSA 400G-FR4 仕様書
- [ ] **DR4 の中心波長の規格上の範囲**（本文書は `[未確認]`）
- [ ] **`400GBASE-LR4-6` が 6km、`400G-LR4-10` が 10km** → tiafotc + 100glambda の両方
- [ ] **DR4 が MPO-12 の何番の芯を使うか**（配列・極性 Type B の確認） → Cisco 配線ガイド or TIA-568
- [ ] **APC / UPC の使い分け**（DR4=APC、SR8=UPC）→ ベンダーデータシートの Connector 欄

### 中（書き方の安全性に関わる）

- [ ] **「FR」の F が何の略か。**ソース間で食い違っている。**由来を断定して書かないほうが安全**
- [ ] **「BASE 有無で IEEE / MSA が分かる」という説明を本に入れてよいか。**ベンダー商品名では守られていない
- [ ] **Juniper と Arista が同じ `QDD-400G-FR4` を使っている件** → 両社データシート（1ソースのみで危険）
- [ ] **800G の `DR8`(MPO-16) と `2×DR4`(MPO-12×2) の違い** → Juniper 800G ガイド
- [ ] **FEC（KP4 RS-FEC）の設定不一致がリンク不良の主因、という記述** → Viavi アプリケーションノート

### ライセンス・体裁

- [ ] **本文書のどの表現も本文に転記しない。**必ず自分の言葉に置き換える
- [ ] **図（MPO-12 → LC×4 の分岐図、DR4 と FR4 の芯数対比図）は自作する。**ベンダー図の流用は不可
- [ ] **IEEE 規格書本文の引用は不可**（有償規格）。規格「名」と「番号」の言及は問題ない
- [ ] **E章（食い違いの実例）は、公開事例が取れていないため著者の実務経験ベースで書く。**特定の顧客・キャリアが識別できる書き方は避ける
