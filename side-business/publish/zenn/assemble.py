#!/usr/bin/env python3
"""Zenn リポジトリに配置できる形に組み立てる。

drafts/ を唯一の原本とし、そこから Zenn の構造を作る。
drafts を直接編集し、公開前にこれを実行する（内容の二重管理をしない）。

使い方:
    python3 publish/zenn/assemble.py ../zenn-content     # 出力先を指定
    python3 publish/zenn/assemble.py --check             # 検証のみ
"""
import argparse, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent   # side-business/
DRAFTS = ROOT / "drafts"
CONFIG = ROOT / "publish" / "zenn" / "config-dwdm-intro.yaml"
BOOK_SLUG = "dwdm-intro"

# Zenn の制約（research/05-zenn-publishing.md より）
SLUG_RE_ARTICLE = re.compile(r"^[0-9a-z\-_]{12,50}$")
TITLE_MAX = 70


def check_chapter(path: pathlib.Path) -> list[str]:
    """チャプター1本を検証し、問題のリストを返す。"""
    problems = []
    text = path.read_text(encoding="utf-8")

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return [f"{path.name}: frontmatter がない"]
    fm = m.group(1)

    tm = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M)
    if not tm:
        problems.append(f"{path.name}: title がない")
    elif len(tm.group(1)) > TITLE_MAX:
        problems.append(f"{path.name}: title が {len(tm.group(1))} 字（上限 {TITLE_MAX}）")

    fr = re.search(r"^free:\s*(\S+)\s*$", fm, re.M)
    if fr and fr.group(1) not in ("true", "false"):
        problems.append(f"{path.name}: free は真偽値のみ（'{fr.group(1)}' は型エラー）")

    if len(path.stem) > 50:
        problems.append(f"{path.name}: チャプター slug が 50 字超")

    return problems


def read_chapters_from_config() -> list[str]:
    text = CONFIG.read_text(encoding="utf-8")
    body = text.split("chapters:", 1)[1]
    return [l.strip().lstrip("- ").strip() for l in body.strip().splitlines() if l.strip().startswith("-")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dest", nargs="?", help="Zenn リポジトリのパス")
    ap.add_argument("--check", action="store_true", help="検証のみ")
    args = ap.parse_args()

    src = DRAFTS / "book-01"
    if not src.is_dir():
        print(f"原本が見つかりません: {src}", file=sys.stderr)
        return 1

    listed = read_chapters_from_config()
    found = sorted(p.stem for p in src.glob("*.md"))

    problems: list[str] = []

    # config に書かれていないチャプターは同期されない
    for stem in found:
        if stem not in listed:
            problems.append(f"{stem}.md が config.yaml の chapters に無い（同期されません）")
    for stem in listed:
        if stem not in found:
            problems.append(f"config.yaml の '{stem}' に対応する .md が無い")

    for p in sorted(src.glob("*.md")):
        problems.extend(check_chapter(p))

    # price の検証
    cfg = CONFIG.read_text(encoding="utf-8")
    pm = re.search(r"^price:\s*(.+)$", cfg, re.M)
    if pm:
        raw = pm.group(1).strip()
        if not raw.isdigit():
            problems.append(f"price はクオート無しの半角数字にすること（現在: {raw}）")
        else:
            v = int(raw)
            if not (v == 0 or (200 <= v <= 5000 and v % 100 == 0)):
                problems.append(f"price は 0 または 200〜5000 の100円単位（現在: {v}）")

    free = [p.stem for p in sorted(src.glob("*.md"))
            if re.search(r"^free:\s*true\s*$", p.read_text(encoding="utf-8"), re.M)]

    if problems:
        print("問題あり:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(f"検証 OK  チャプター {len(listed)}本 / 無料公開 {len(free)}本 ({', '.join(free)})")

    if args.check or not args.dest:
        return 0

    dest_book = pathlib.Path(args.dest) / "books" / BOOK_SLUG
    dest_book.mkdir(parents=True, exist_ok=True)
    shutil.copy(CONFIG, dest_book / "config.yaml")
    for stem in listed:
        shutil.copy(src / f"{stem}.md", dest_book / f"{stem}.md")
    print(f"配置しました: {dest_book}")
    print("  次に: git add / commit / push → Zenn の /dashboard/deploys で結果を確認")
    return 0


if __name__ == "__main__":
    sys.exit(main())
