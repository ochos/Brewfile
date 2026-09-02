# Zenn への配置

## なぜ別リポジトリにするのか

**このリポジトリ（Brewfile）に Zenn を繋がないでください。** 理由は3つ。

1. **有料本のリポジトリは Private 必須**（`research/05-zenn-publishing.md`）。
   このリポジトリの公開状態は未確認で、Public なら**本の中身が誰でも読める**
2. **Zenn は1つのリポジトリとしか連携できない。** 繋いだ時点で、このリポジトリの用途が固定される
3. このリポジトリの本来の用途は Homebrew のパッケージリスト

→ **Zenn 用の Private リポジトリを新しく作る。**

---

## 原本はどこか

**`side-business/drafts/` が唯一の原本です。**

```
drafts/book-01/*.md      ← 本文。ここを編集する
publish/zenn/config-dwdm-intro.yaml  ← 本のメタ情報
```

**Zenn リポジトリ側を直接編集しないでください。** 二重管理になり、必ずズレます。
編集は常に `drafts/` で行い、`assemble.py` で配置し直します。

---

## 手順

### 1. Zenn 用の Private リポジトリを作る

GitHub で新規作成。**必ず Private。** 名前は何でもよい（例: `zenn-content`）。

### 2. 手元にクローンする

```bash
git clone git@github.com:<あなた>/zenn-content.git
```

### 3. 組み立てる

```bash
# 検証だけ
python3 side-business/publish/zenn/assemble.py --check

# 配置
python3 side-business/publish/zenn/assemble.py /path/to/zenn-content
```

`books/dwdm-intro/` に `config.yaml` と6章が配置されます。

### 4. Zenn と連携する

`publish/SETUP.md` の手順に従う。**STEP 7 の確認事項（住所開示の要否など）を必ず先に済ませること。**

### 5. 公開

```bash
cd /path/to/zenn-content
git add . && git commit -m "Add DWDM intro book" && git push
```

**push 成功 ≠ 公開成功。** Zenn の `/dashboard/deploys` で結果を確認する。

---

## `assemble.py` が検証すること

配置の前に、Zenn が弾く条件を先に潰します。実際に異常系でテスト済み。

| 検証 | 落ちる例 |
|---|---|
| `price` の型 | `price: "500"` ← クオートは型エラー |
| `price` の値 | `price: 550` ← 100円単位でない（0 または 200〜5000） |
| `chapters` と実ファイルの一致 | config に無い章は**同期されない**（気づきにくい） |
| `free` の型 | `free: "true"` ← 文字列は型エラー |
| `title` の長さ | 70字超 |
| チャプター slug | 50字超 |

---

## 公開前の最終確認

- [ ] `assemble.py --check` が通る
- [ ] `published: false` のまま配置し、Zenn 上で表示を確認してから `true` にする
- [ ] 無料公開章が意図どおりか（第1章・第3章）
- [ ] 本文中の `<!-- ▼ 筆者確認 ▼ -->` コメントを**全て削除した**
- [ ] `SETUP.md` STEP 7 の確認事項が済んでいる（**住所開示の要否**）
- [ ] リポジトリが **Private** である
