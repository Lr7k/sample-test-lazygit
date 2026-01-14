# Helix Editor 使い方ガイド（改訂版）

> 公式ドキュメントの内容を反映しつつ、既存ガイドの良い点を整理しました。

## 1. Helixとは

Helixは**Rust製のポストモダンなモーダルテキストエディタ**です。Vimに近い操作感を持ちつつ、Kakoune由来の**選択 → 操作**モデルを採用しています。

### 主な特徴

- LSP/Tree-sitter/テーマが標準搭載
- 選択優先モデル（対象を選んでから操作）
- 複数選択・複数カーソルが標準機能

---

## 2. インストール

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

### Cargo (Rustユーザー向け)

```bash
cargo install --git https://github.com/helix-editor/helix helix-term --locked
```

---

## 3. はじめに（公式ドキュメント準拠）

### 起動とチュートリアル

```bash
hx {file}
hx --tutor
```

または起動後に `:tutor`。

### モード

- Normal: 移動・編集の中心
- Insert: 文字入力（`i`）
- Select/Extend: 選択拡張（`v`）

補足: インサートの変更は、Normalに戻るタイミングでUndo単位になる。

### 重要な考え方

- **選択 → 操作**が基本
- カーソルは「幅1の選択」
- 複数選択で一括編集ができる

---

## 4. 基本操作（要点）

### 移動

- `h` `j` `k` `l`: 左/下/上/右
- `w` `b` `e`: 単語移動
- `f{char}` `t{char}` `F{char}` `T{char}`: 文字検索（行を跨ぐ）
- `Ctrl-f` / `Ctrl-b`: ページ移動
- `Ctrl-d` / `Ctrl-u`: 半ページ移動

### 選択・複数カーソル

- `v`: Select/Extendモード
- `x`: 行選択（2回目で次行へ拡張）
- `%`: ファイル全体を選択
- `;`: 選択をカーソルに縮小
- `,`: 主選択のみ残す
- `C`: 次の行にカーソルを追加
- `Alt-C`: 前の行にカーソルを追加

### 編集

- `i` `a` `I` `A`: 挿入
- `o` `O`: 下/上に行を開く
- `d`: 削除
- `c`: 変更（削除してInsert）
- `y` / `p` / `P`: ヤンク/ペースト
- `u` / `U`: Undo/Redo
- `=`: フォーマット（LSPが必要）
- `Ctrl-c`: コメントの切り替え

### 検索

- `/` `?`: 検索/逆検索
- `n` `N`: 次/前の検索結果
- `*`: 選択を検索パターンに（単語境界）
- `Alt-*`: 選択を検索パターンに
- `Space /`: ワークスペース全体検索

---

## 5. マイナーモード

### Gotoモード（`g`）

- `g g`: 先頭
- `g e`: 末尾
- `g h` / `g l`: 行頭/行末
- `g s`: 行の最初の非空白
- `g d`: 定義へ（LSP）
- `g r`: 参照へ（LSP）
- `g i`: 実装へ（LSP）

### Matchモード（`m`）

- `m m`: 対応括弧へ
- `m s <char>`: 囲む
- `m r <from><to>`: 囲み置換
- `m d <char>`: 囲み削除
- `m a <obj>` / `m i <obj>`: テキストオブジェクト

### Viewモード（`z`）

- `z t` / `z c` / `z b`: 上/中央/下に揃える
- `z j` / `z k`: 画面スクロール

### Windowモード（`Ctrl-w`）

- `Ctrl-w v`: 縦分割
- `Ctrl-w s`: 横分割
- `Ctrl-w q`: 分割を閉じる
- `Ctrl-w h/j/k/l`: 分割移動

### Spaceモード（`Space`）

- `Space f`: ファイルピッカー
- `Space b`: バッファピッカー
- `Space s`: シンボル
- `Space S`: ワークスペースシンボル
- `Space ?`: コマンドパレット
- `Space /`: グローバル検索

---

## 6. コマンドモード（`:`）

- `:w` / `:q` / `:wq`: 保存/終了/保存して終了
- `:o {path}`: ファイルを開く
- `:buffer-next` / `:buffer-previous`: バッファ移動
- `:format` / `:fmt`: フォーマット
- `:theme {name}`: テーマ変更
- `:lsp-restart`: LSP再起動
- `:tutor`: チュートリアル
- `:config-open`: 設定ファイルを開く
- `:config-reload`: 設定再読み込み
- `:set` / `:toggle`: 設定の変更

---

## 7. 設定ファイル

- Linux/macOS: `~/.config/helix/config.toml`
- Windows: `%AppData%\helix\config.toml`

関連コマンド:
- `:config-open` で設定を開く
- `:config-reload` で再読み込み
- `hx -c path/to/custom-config.toml` で任意設定を使用
- リポジトリ内の `.helix/config.toml` はプロジェクト設定として統合される

---

## 8. Vimユーザー向けポイント

- **選択 → 操作**が基本（Vimは操作 → 対象）
- `x` は行選択（文字削除ではない）
- 末尾へは `g e`（Gotoモード）
- まず対象を選び、`d`/`c`/`y` を当てる

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
  Alt-C            → カーソルを上に追加

困ったとき:
  Space ?          → コマンドパレット
  :tutor           → チュートリアル
```

---

## 10. 公式ドキュメント

- https://docs.helix-editor.com/usage.html
- https://docs.helix-editor.com/keymap.html
- https://docs.helix-editor.com/commands.html
- https://docs.helix-editor.com/configuration.html
