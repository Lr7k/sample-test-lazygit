# Helix Editor 使い方ガイド

> このドキュメントは公式ドキュメント、Qiita、Zenn等の情報を元に作成（2025年1月）

## 1. Helixとは

Helixは**Rust製のポストモダンなモーダルテキストエディタ**です。Vimに似た操作性を持ちながら、Kakouneの「選択優先」モデルを採用しています。

### 主な特徴

- **バッテリー同梱**: LSP、シンタックスハイライト、テーマがデフォルトで利用可能
- **プラグイン不要**: 設定なしですぐに使える
- **選択優先モデル**: 先に対象を選択し、その後アクションを実行
- **Tree-sitter統合**: 高精度なシンタックスハイライトとテキストオブジェクト
- **複数カーソル**: 同時編集が標準機能

### こんな人におすすめ

- Vim/Neovimのライトユーザー
- プラグイン管理に疲れた人
- VSCodeが重いと感じる人
- モーダルエディタ初心者

---

## 2. インストール方法

### macOS (Homebrew)

```bash
brew install helix
```

### Windows (Scoop)

```bash
scoop install helix
```

### Linux

**Arch Linux:**
```bash
sudo pacman -S helix
```

**Ubuntu/Debian:**
```bash
sudo add-apt-repository ppa:maveonair/helix-editor
sudo apt update
sudo apt install helix
```

**Fedora:**
```bash
sudo dnf install helix
```

### Cargo経由（Rustユーザー向け）

```bash
cargo install --git https://github.com/helix-editor/helix helix-term --locked
```

### インストール確認

```bash
hx --version
```

### チュートリアル起動

```bash
hx --tutor
```

または起動後に `:tutor` コマンド

---

## 3. 基本概念

### Vimとの最大の違い：選択優先モデル

| エディタ | モデル | 例（単語削除） |
|----------|--------|----------------|
| Vim | 操作 → 対象 | `dw`（削除 → 単語） |
| Helix | 対象 → 操作 | `wd`（単語選択 → 削除） |

Helixでは**移動 = 選択**です。`w`キーを押すと次の単語に移動しつつ、その範囲が選択されます。

### モード一覧

| モード | 説明 | 切替キー |
|--------|------|----------|
| Normal | ナビゲーション・編集（デフォルト） | `Esc` |
| Insert | テキスト入力 | `i`, `a`, `o` 等 |
| Select | 選択拡張 | `v` |
| Command | コマンド実行 | `:` |

### マイナーモード（重要）

| モード | キー | 用途 |
|--------|------|------|
| Space | `Space` | ファイルピッカー、シンボル検索等 |
| Match | `m` | テキストオブジェクト操作 |
| Goto | `g` | ナビゲーション |
| Window | `Ctrl-w` | ウィンドウ操作 |
| View | `z` / `Z` | 画面スクロール |

---

## 4. 基本操作（キーバインド）

### 移動（ノーマルモード）

| キー | 動作 | Vimとの違い |
|------|------|-------------|
| `h`/`j`/`k`/`l` | 左/下/上/右 | 同じ |
| `w` | 次の単語の先頭へ | 単語の直前に移動 |
| `b` | 前の単語の先頭へ | 同じ |
| `e` | 単語の末尾へ | 同じ |
| `f{char}` | 文字検索（前方） | 行をまたいで検索 |
| `t{char}` | 文字検索（手前まで） | 行をまたいで検索 |
| `gg` | ファイル先頭へ | 同じ |
| `ge` | ファイル末尾へ | Vimは`G` |
| `Ctrl-f`/`Ctrl-b` | ページ移動 | 同じ |
| `Ctrl-d`/`Ctrl-u` | 半ページ移動 | 同じ |

### 選択

| キー | 動作 |
|------|------|
| `v` | 選択モード開始 |
| `x` | 行全体を選択 |
| `%` | ファイル全体を選択 |
| `;` | 選択を解除（カーソルに縮小） |
| `,` | 複数選択を解除 |
| `s` | 選択内を検索して複数選択 |
| `C` | カーソルを下に追加（複数カーソル） |
| `Alt-c` | カーソルを上に追加 |

### 編集

| キー | 動作 |
|------|------|
| `i` | 選択の前に挿入 |
| `a` | 選択の後に挿入 |
| `o` / `O` | 下/上に行を追加して挿入 |
| `d` | 選択を削除 |
| `c` | 選択を削除して挿入モード |
| `y` | ヤンク（コピー） |
| `p` / `P` | 後/前にペースト |
| `r{char}` | 選択を文字で置換 |
| `u` | アンドゥ |
| `U` | リドゥ |
| `>` / `<` | インデント増減 |
| `=` | フォーマット |
| `Ctrl-c` | 行コメント切替 |

### よく使う操作パターン

| 操作 | Vim | Helix |
|------|-----|-------|
| 行削除 | `dd` | `xd` |
| 行コピー | `yy` | `xy` |
| 単語削除 | `dw` | `wd` |
| 単語内選択して削除 | `diw` | `miwd` |
| 関数内選択 | - | `mif` |

---

## 5. マイナーモード詳細

### Spaceモード（`Space`）

| キー | 動作 |
|------|------|
| `f` | ファイルピッカー |
| `F` | カレントディレクトリのファイルピッカー |
| `b` | バッファピッカー |
| `s` | シンボルピッカー |
| `S` | ワークスペースシンボル |
| `/` | グローバル検索 |
| `?` | コマンドパレット |
| `w` | ウィンドウモード |
| `y` | クリップボードへヤンク |
| `p` | クリップボードからペースト |

### Matchモード（`m`）

Tree-sitterベースのテキストオブジェクト操作：

| キー | 動作 |
|------|------|
| `m` | 対応する括弧へジャンプ |
| `s{char}{char}` | サラウンドで囲む |
| `r{from}{to}` | サラウンド置換 |
| `d{char}` | サラウンド削除 |
| `a` + オブジェクト | オブジェクト全体を選択 |
| `i` + オブジェクト | オブジェクト内部を選択 |

**テキストオブジェクト:**

| キー | オブジェクト |
|------|--------------|
| `w` | 単語 |
| `p` | 段落 |
| `(` / `)` | 括弧 |
| `{` / `}` | 波括弧 |
| `[` / `]` | 角括弧 |
| `<` / `>` | 山括弧 |
| `"` / `'` / `` ` `` | 引用符 |
| `f` | 関数 |
| `c` | クラス |
| `a` | 引数 |

### Gotoモード（`g`）

| キー | 動作 |
|------|------|
| `g` | ファイル先頭 |
| `e` | ファイル末尾 |
| `h` | 行頭 |
| `l` | 行末 |
| `s` | 最初の非空白文字 |
| `d` | 定義へジャンプ |
| `r` | 参照へジャンプ |
| `i` | 実装へジャンプ |
| `t` | 型定義へジャンプ |
| `.` | 最後の編集位置 |

---

## 6. インサートモード

| キー | 動作 |
|------|------|
| `Esc` / `Ctrl-[` | ノーマルモードへ |
| `Ctrl-x` | オートコンプリート |
| `Ctrl-w` | 前の単語を削除 |
| `Ctrl-u` | 行頭まで削除 |
| `Ctrl-k` | 行末まで削除 |
| `Ctrl-s` | スニペット展開 |

---

## 7. コマンドモード

`:` でコマンドモードに入ります。

### ファイル操作

| コマンド | 動作 |
|----------|------|
| `:w` | 保存 |
| `:w {path}` | 名前を付けて保存 |
| `:q` | 終了 |
| `:q!` | 強制終了 |
| `:wq` / `:x` | 保存して終了 |
| `:o {path}` | ファイルを開く |
| `:bc` | バッファを閉じる |
| `:n` | 新規バッファ |

### 設定

| コマンド | 動作 |
|----------|------|
| `:theme {name}` | テーマ変更 |
| `:config-reload` | 設定再読み込み |
| `:tutor` | チュートリアル起動 |

### LSP

| コマンド | 動作 |
|----------|------|
| `:lsp-restart` | LSP再起動 |
| `:format` | フォーマット |

---

## 8. 設定ファイル

### 設定ファイルの場所

| OS | パス |
|----|------|
| Linux/macOS | `~/.config/helix/config.toml` |
| Windows | `%AppData%\helix\config.toml` |

### 基本設定例

```toml
theme = "onedark"

[editor]
line-number = "relative"
mouse = true
bufferline = "multiple"
color-modes = true

[editor.cursor-shape]
insert = "bar"
normal = "block"
select = "underline"

[editor.indent-guides]
render = true

[editor.lsp]
display-messages = true
display-inlay-hints = true

[editor.statusline]
left = ["mode", "spinner", "file-name", "file-modification-indicator"]
right = ["diagnostics", "selections", "position", "file-encoding", "file-line-ending", "file-type"]

[editor.file-picker]
hidden = false

[keys.normal]
# カスタムキーバインド例
C-s = ":w"
```

### 言語設定（languages.toml）

```toml
[[language]]
name = "python"
auto-format = true

[[language]]
name = "rust"
auto-format = true
```

---

## 9. クイックリファレンス

```
起動:
  hx {file}        → ファイルを開く
  hx --tutor       → チュートリアル

基本フロー:
  i                → 挿入モード
  Esc              → ノーマルモード
  :w               → 保存
  :q               → 終了

選択と編集:
  w                → 次の単語を選択
  x                → 行を選択
  d                → 選択を削除
  c                → 選択を変更
  y                → ヤンク
  p                → ペースト

ファイル操作:
  Space f          → ファイルピッカー
  Space b          → バッファピッカー
  Space /          → グローバル検索

複数カーソル:
  C                → カーソルを下に追加
  ,                → 複数選択を解除

困ったとき:
  Space ?          → コマンドパレット
  :tutor           → チュートリアル
```

---

## 10. Vimユーザー向け移行ガイド

### 心構え

1. **選択が常に可視化される** - 移動すると自動で選択範囲が表示される
2. **`;`で選択を解除** - カーソルのみに戻したいときに使用
3. **`x`は行選択** - 文字削除ではない（`d`と組み合わせて`xd`で行削除）

### 主な操作の違い

| 操作 | Vim | Helix |
|------|-----|-------|
| 行削除 | `dd` | `xd` |
| 行コピー | `yy` | `xy` |
| 末尾へ | `G` | `ge` |
| 単語内選択 | `viw` | `miw` |
| ビジュアルモード | `v` → 移動 → 操作 | 移動 → 操作（常に選択表示） |
| ウィンドウ分割 | `Ctrl-w v` | `Ctrl-w v` または `Space w v` |

---

## 11. 参考リンク

- [公式サイト](https://helix-editor.com/)
- [公式ドキュメント](https://docs.helix-editor.com/)
- [GitHubリポジトリ](https://github.com/helix-editor/helix)
- [キーマップドキュメント](https://docs.helix-editor.com/keymap.html)
- [設定ドキュメント](https://docs.helix-editor.com/configuration.html)
- [Qiita - Helix Editorのモードと基本操作](https://qiita.com/GreasySlug/items/8a2c58e39ab345660722)
- [Zenn - Helixでモーダルエディタに触れてみる](https://zenn.dev/kairkarigohan/articles/9d8f2e79e823ef)
