# 英語圏アウトリーチ テンプレ（Reddit / LinkedIn）

設計理由と規約の出典: [`../../research/06-launch-ops.md` §4-2](../../research/06-launch-ops.md)

> **位置づけ: M1（月商1,000円）には不要。M2以降。**
> ただし「アカウントの信用は時間でしか買えない」ため、**参加だけ先に始める**（週15分）。
> 商材が日本語の技術書である以上、**英語圏から直接の売上は期待しない**。期待するのは信用と、記事ネタになる質問。

---

# 1. Reddit

## 1-1. 投稿前に必ずやること（各サブ5分・合計20分）

各サブレディットの **Rules を自分で開いて読む**。サイト全体で許されていても、そのコミュニティでBANされる。

- [ ] [r/networking](https://www.reddit.com/r/networking/) の Rules を読んだ
- [ ] [r/fiberoptics](https://www.reddit.com/r/fiberoptics/) の Rules を読んだ
- [ ] [r/telecom](https://www.reddit.com/r/telecom/) の Rules を読んだ
- [ ] [r/datacenter](https://www.reddit.com/r/datacenter/) の Rules を読んだ

**確認する項目**: `self-promotion` / `blogspam` / `no links to personal blogs` / `weekly promotion thread` の有無。

> 多くの技術系サブは **self-promotion を全面禁止**しているか、**週次の promotion thread のみ許可**している。禁止のサブでは**永久にリンクを貼らない**（回答だけする）。

## 1-2. ルール（守る）

| ルール | 内容 |
|---|---|
| **90/10** | 活動の90%以上は普通の参加（コメント・回答）。自己言及は10%以下 |
| **開示** | 自分のものを挙げるときは**必ず自分のものだと明示する**。隠すことが違反であり、開示にコストはない |
| **クロスポスト禁止** | 同一の宣伝内容を複数サブに投げない |
| **水増し禁止** | 比率を合わせるための低品質コメントはパターンで検出される |

出典: [The complete guide to Reddit self-promotion rules in 2026](https://redship.io/blog/reddit-self-promotion-rules) / [Reddit Self-Promotion Rules: The Complete Guide (2026)](https://founderreply.com/guides/reddit-self-promotion-rules)

## 1-3. 手順（4週間の助走 → 以後 週15分）

| 週 | やること | 時間 |
|---|---|---|
| 1〜4週 | **回答だけ**する。リンクは一切貼らない | 週15分 |
| 5週以降 | 相手が求めた場合のみ、**自分のものだと明示して**リンクを出す | 週15分 |

## 1-4. テンプレ

### A. 質問への回答（リンクなし・1〜4週目はこれのみ）

```text
Optical transport engineer here (about 10 years on DWDM design, mostly Ciena gear).

Short answer: OSNR is the ratio of signal power to noise power within a reference bandwidth. The reason it gets looked at first is that it's largely fixed by span loss and the number of amplifier stages — you can't recover it downstream.

If your measured value is off from the design value, I'd check in this order:

1. Measured span loss vs. design
2. Amplifier output / gain vs. design
3. Per-channel power deviation (tilt)
4. Extra loss at connectors and splices

In my experience 1 and 2 explain most of the gap. Chasing the transponder before checking those tends to make troubleshooting take much longer.
```

### B. 相手が資料・詳細を求めてきたとき（**ここで初めてリンク**）

```text
There isn't much written up in one place for this, which is why I ended up writing my own notes on it.

Disclosure: this is my own post — https://zenn.dev/【username】/articles/【slug】

It's in Japanese, so a translated view may be needed, but the tables and the ordering of the checks should still be readable. Happy to answer follow-ups here instead if that's easier.
```

**ルール**:
- `Disclosure: this is my own post` を**必ず入れる**
- 日本語であることを先に伝える（相手の時間を無駄にしない）
- 「ここで答えてもいい」と添える（リンクを踏ませることが目的ではない、という姿勢を明示）

### C. 訂正されたとき

```text
You're right, thanks for the correction — 【what was wrong】 was inaccurate on my part. 【the correct statement】.

I've updated my notes accordingly.
```

## 1-5. やってはいけないこと（Reddit）

- ❌ 参加実績なしでいきなり自分の記事リンクを投稿する
- ❌ 自分のものだと明示せずにリンクを出す
- ❌ 同じ内容を複数サブにクロスポストする
- ❌ 比率調整のための中身のないコメント
- ❌ Rules で self-promotion 禁止のサブにリンクを貼る（例外なし）

---

# 2. LinkedIn

## 2-1. ⚠️ 使う前に読む警告

**LinkedInは、この副業で最も守秘義務リスクが高いプラットフォーム。**

理由: **現職・前職がプロフィールに紐付いている**。ここで光伝送の実務知識を発信すると、Xやはてなよりも遥かに強く「前職での業務内容」として読まれる。

> **本プロジェクトの決定: M1・M2では使わない。**

## 2-2. それでも使う場合のルール（M3以降）

| 事実 | 対応 |
|---|---|
| 外部リンクを含む投稿は初期リーチが抑制される。**投稿者自身がコメント欄にリンクを書いた場合も、そのコメントの可視性が低下している** `[二次]` → [LinkedInアルゴリズムの仕組みと攻略法（2026）](https://flagout.co.jp/linkedin-algorithm-basics/) | **リンクを貼らない。** 投稿本文だけで完結させる |
| プラットフォーム内で価値が完結するコンテンツが有利 | 記事の要約ではなく、**その投稿だけで読み切れる短い技術メモ**にする |
| 自己宣伝の可否は Professional Community Policies に従う → [LinkedIn Professional Community Policies](https://www.linkedin.com/legal/professional-community-policies) | 投稿前に一度読む |

**投稿してよい内容の範囲**:

- ✅ 一般に公開された規格・技術の解説（ITU-T G.694.1 の波長グリッドの話 など）
- ✅ 自分で行った計算・検証
- ❌ 前職の業務プロセス・体制・顧客に関わる一切
- ❌ 「前職では〜していました」という形の実務詳細

### テンプレ（リンクなし・自己完結型）

```text
A note on OSNR, for anyone who just moved into optical transport.

OSNR is the ratio of signal power to noise power in a reference bandwidth. It matters because it is largely determined by span loss and the number of amplifier stages — which means it is set by the line design, not by the transponder.

Practical consequence: when measured OSNR is short of the design value, the answer is usually in the span, not in the equipment. Checking measured span loss and amplifier gain against design first will resolve most cases faster than starting at the terminal.

Nothing here is specific to any operator or vendor — it's the general shape of the problem.
```

**最終行（`Nothing here is specific to any operator or vendor`）を必ず残す。** 守秘義務の観点で、自分と読者の両方への明示になる。

---

# 3. メーリングリスト（JANOG / NANOG）— **宣伝は明確に禁止**

| ML | 宣伝の可否 | 使い方 | 出典 |
|---|---|---|---|
| **JANOG**（日本・約7,700名） | ❌ **明らかに営業活動を目的とした参加は認められていない** | 技術的な質問への**回答のみ**。署名欄にURLも入れない。参加前に JANOG Comment 10（ML運用ポリシー）と Comment 11（行動規範）を読む | [JANOG Mailing List](https://www.janog.gr.jp/mailinglist/) / [JANOG Comment Index](https://www.janog.gr.jp/doc/janog-comment/) |
| **NANOG**（北米・英語） | ❌ **「NANOGメーリングリストを私的なマーケティング活動や、いかなる種類の製品マーケティングにも使うことは禁止」** | 同上 | [NANOG Mailing-List Usage Guidelines](https://nanog.org/resources/usage-guidelines/) |

> **この2つのMLは「集客の場」ではなく「ネタ源」。**
> 「今みんなが何に困っているか」の一次情報が、日本語圏で最も濃く流れている場所。**読むだけでも価値がある。**
> 週次ルーティンには入れない（読むのは任意）。
