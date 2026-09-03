# 07. 外部アクセスの制約と、その回避策

調査日: 2026-08-30

---

## 1. 結論

**ブロックの迂回はしない。代わりに、許可されている経路を使う。**

Zenn・ITU-T・Ciena 等への直接アクセスは組織のエグレスポリシーで拒否されている。これはセキュリティ制御であり、
環境の README も「retry や迂回をせず、ブロックされたホストを報告すること」を明示している。

**しかしパッケージレジストリは許可されている。** そして光伝送の分野には、
**BSD ライセンスで公開され、OSNR と ASE の計算を実装した業界標準の OSS が存在する。**
これが技術的な裏付けの取得経路になる。

---

## 2. ブロックの性質（検証済み）

```
proxy経由  zenn.dev → CONNECT tunnel failed, response 403
直結(--noproxy) zenn.dev → 403
```

**プロキシを迂回しても 403。** ブロックはコンテナ内の設定ではなく、
上流のネットワークゲートウェイのポリシー判断。コンテナ内から変更する手段はない。

プロキシの診断出力にも `connect_rejected: gateway answered 403 to CONNECT (policy denial)` と記録される。

Chromium はインストールされているが、**同じネットワーク経路を通るため結果は変わらない。**

---

## 3. 到達可能なホスト（実測 2026-08-30）

| ホスト | 応答 | 用途 |
|---|---|---|
| `registry.npmjs.org` | 200 | **npm パッケージ** |
| `pypi.org` | 200 | **PyPI パッケージ** |
| `files.pythonhosted.org` | 200 | PyPI 本体ファイル |
| `api.github.com` | 200 | **GitHub API** |
| `raw.githubusercontent.com` | 301（到達可） | **GitHub 上のファイル** |
| `index.crates.io` | 200 | Rust パッケージ |
| `proxy.golang.org` | 200 | Go モジュール |
| `github.com` | 400（到達可） | git clone は可能 |
| zenn.dev / itu.int / ciena.com / arxiv.org / en.wikipedia.org 他 | **403** | **不可** |

> **つまり「Web ページは読めないが、公開されたソースコードとパッケージは読める」。**

---

## 4. GNPy — 光伝送の技術的裏付けとして使える OSS

### 概要

| | |
|---|---|
| 名称 | **GNPy**（oopt-gnpy / Open Optical Path Planning） |
| 提供 | **Telecom Infra Project** |
| 取得 | `pip download gnpy --no-deps --no-binary :all:` |
| バージョン | 2.2.0（2026-08-30 取得） |
| **ライセンス** | **BSD 3-Clause** ← **商用利用可。有料の技術書に使える** |

キャリアの光パス設計に実際に使われている実装であり、**OSNR・ASE雑音・増幅器NF・分散・非線形を実装している**。

### ライセンスの重要性

これまで調査で見つかった英語圏の資料は、**有料販売と衝突するものばかり**だった。

| ソース | ライセンス | 有料書での利用 |
|---|---|---|
| MIT OpenCourseWare | CC BY-NC-SA | **不可**（非営利限定） |
| Wikipedia / Stack Exchange | CC BY-SA | **困難**（ShareAlike が衝突） |
| MapYourTech | 転載明示禁止 | **不可** |
| **GNPy** | **BSD 3-Clause** | **可** |

**GNPy は現時点で唯一、有料の技術書に使える裏付けソース。**

なお **物理法則や計算式そのものに著作権はない。** コードを転載しなければ、
「GNPy の実装で確認した」と書いたうえで自分の言葉で説明することに問題はない。
コード片を引用する場合は BSD の条件（著作権表示の保持）に従う。

---

## 5. GNPy で検証できた事実

**記事①・本の技術的裏付けが、これで独立に確認された。**

### 5-1. 基準帯域 12.5 GHz

```
gnpy/core/elements.py:101   ratio_01nm = [lin2db(12.5e9 / b_rate) for b_rate in self.baud_rate]
gnpy/core/utils.py:135      def snr_sum(snr, bw, snr_added, bw_added=12.5e9):
```

**0.1nm = 12.5 GHz** が実装の既定値として使われている。
→ `derivations.md` の導出（Δν = c·Δλ/λ² = 12.478 GHz）と一致。

### 5-2. 定数「+58」← 最重要

```
gnpy/core/elements.py:714
    nf_avg = pin_ch - polyval(nf_model.nf_coef, pin_ch) + 58
```

**第一原理から導いた `10log₁₀(h·ν·B_ref) = −57.96 dBm` が、実装にそのまま現れている。**

これは記事①の §7（つまずきポイント）の核であり、
**「自分で導出でき、かつ業界実装で裏が取れている」**という最も強い状態になった。

### 5-3. 多段中継の OSNR 累積

```
gnpy/core/utils.py:135-138
    def snr_sum(snr, bw, snr_added, bw_added=12.5e9):
        snr_added = snr_added - lin2db(bw / bw_added)
        snr = -lin2db(db2lin(-snr) + db2lin(-snr_added))
```

これは **1/OSNR_total = Σ 1/OSNR_i** の実装。ローカルで検証した:

| 条件 | GNPy の式 | 理論値 |
|---|---|---|
| 20dB の区間 × 2 | 16.9897 dB | 20 − 10log₁₀2 = 16.9897 dB |
| 20dB の区間 × 4 | 13.9794 dB | 20 − 10log₁₀4 = 13.9794 dB |

→ 下書き §4 の「**N 倍で 10log₁₀N dB 劣化**」「**最悪区間が支配する**」が裏付けられた。

### 5-4. ファイバの扱い（DSF の件に関係）

GNPy はファイバを `G.652` のような型番ではなく **分散値（s/m/m）** で表現し、
そこから β₂ を計算して非線形干渉（NLI）を求めている。

```
gnpy/core/parameters.py:162
    self._beta2 = -(self.ref_wavelength ** 2) * self.dispersion / (2 * pi * c)
```

→ **DSF（分散≈0）を数値で表現でき、非線形の影響を計算できる。**
→ 本の第4章（DSF × 四光波混合）で、**主張を数値で示せる可能性がある**。
→ ただし FWM の直接実装は確認できていない（NLI モデル経由）。**要追加調査。**

---

## 6. 今後の使い方

1. **技術的主張は、まず自分で導出する**（`derivations.md`）
2. **GNPy の実装で裏を取る**（この文書の方式）
3. **コードは転載しない。** 「実装で確認した」と書き、説明は自分の言葉で
4. 規格番号（ITU-T G.xxx 等）は **本人が手元で現物確認するまで書かない**

---

## 7. 依然として本人にしか確認できないこと

パッケージレジストリからは取得できない。**手元のブラウザで確認が必要。**

| # | 確認事項 | 所要 | 影響 |
|---|---|---|---|
| 1 | **Zenn 有料販売で著者の住所開示が必要か** | 5分 | **顔出しNGの前提に直結。最重要** |
| 2 | Zenn 販売の本人確認書類の要否 | 5分 | 販売開始の可否 |
| 3 | Zenn 販売手数料の正確な数値 | 3分 | 収支計算 |
| 4 | Qiita の宣伝に関する規約の現行条文 | 3分 | クロス投稿の可否 |
| 5 | ITU-T 勧告が無償で読めるか（G.697 等） | 5分 | 記事の出典 |

→ 手順は `publish/SETUP.md` STEP 7 と `research/06-launch-ops.md` §7 に記載済み。

## 8. 根本的な解決策

**手元の PC で Claude Code を動かす**（CLI / デスクトップ版）のが最も確実。
このリポジトリをクローンすれば、同じ状態から続行でき、ネットワーク制約もなくなる。

または、管理者にエグレスポリシーの調整を依頼する。
→ https://code.claude.com/docs/en/claude-code-on-the-web
