# Lazygit 使い方ガイド

> このドキュメントは公式ドキュメント、FreeCodeCamp、Zenn等の情報を元に作成（2025年1月）

## 1. Lazygitとは

Lazygitは**Go言語で書かれたターミナルベースのGit TUI（テキストユーザーインターフェース）クライアント**です。複雑なGitコマンドを覚える必要なく、キーボードショートカットだけでほとんどのGit操作を完結できます。

### 主な特徴

- **視覚的な操作**: 変更内容、ブランチ、コミットログなどが一目で確認可能
- **キーボード中心**: Vim風のキーバインドに対応
- **高速**: ターミナル上で動作するため軽量で高速
- **クロスプラットフォーム**: Windows、macOS、Linux対応

---

## 2. インストール方法

### macOS (Homebrew)

```bash
brew install lazygit
```

### Windows (Scoop)

```bash
scoop bucket add extras
scoop install lazygit
```

### Linux

**Arch Linux:**
```bash
sudo pacman -S lazygit
```

**Ubuntu/Debian:**
```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | grep -Po '"tag_name": "v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/latest/download/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit /usr/local/bin
```

**Fedora/RHEL:**
```bash
sudo dnf install lazygit
```

### Go経由

```bash
go install github.com/jesseduffield/lazygit@latest
```

### インストール確認

```bash
lazygit --version
```

---

## 3. 基本的な使い方

### 起動

Gitリポジトリ内で以下を実行:

```bash
lazygit
```

### 画面構成

Lazygitは6つの主要パネルで構成されています:

| パネル | 説明 | 切替キー |
|--------|------|----------|
| Status | リポジトリ情報 | `1` |
| Files | 変更ファイル一覧 | `2` |
| Branches | ローカル/リモートブランチ | `3` |
| Commits | コミット履歴 | `4` |
| Stash | スタッシュ一覧 | `5` |
| Preview | 右側に差分等の詳細表示 | - |

### ナビゲーション

| キー | 動作 |
|------|------|
| `h` / `l` または `←` / `→` | パネル間移動 |
| `j` / `k` または `↓` / `↑` | リスト内移動 |
| `[` / `]` | パネル内タブ切替 |
| `?` | キーバインド一覧表示 |
| `q` | 終了 |

---

## 4. 基本操作（キーバインド）

### ファイル操作（Filesパネル）

| キー | 動作 |
|------|------|
| `<space>` | ファイルのステージング/アンステージング切替 |
| `a` | 全ファイルのステージング/アンステージング切替 |
| `c` | ステージングした変更をコミット |
| `A` | 直前のコミットに変更を追加（amend） |
| `d` | ファイルの変更を破棄 |
| `e` | ファイルをエディタで開く |
| `s` | スタッシュに保存 |
| `S` | スタッシュオプション表示 |
| `<enter>` | 差分表示（行単位ステージング画面へ） |

### 行単位ステージング（差分表示時）

| キー | 動作 |
|------|------|
| `<space>` | 選択行をステージング/アンステージング |
| `v` | 範囲選択モード開始 |
| `a` | 現在のhunk全体を選択 |

### ブランチ操作（Branchesパネル）

| キー | 動作 |
|------|------|
| `<space>` | 選択ブランチにチェックアウト |
| `n` | 新規ブランチ作成 |
| `d` | ブランチ削除 |
| `R` | ブランチ名変更 |
| `M` | マージオプション表示 |
| `r` | リベース |
| `w` | ワークツリー作成 |

### コミット操作（Commitsパネル）

| キー | 動作 |
|------|------|
| `s` | スカッシュ（下のコミットと統合、メッセージ結合） |
| `f` | フィックスアップ（下のコミットと統合、メッセージ破棄） |
| `r` | コミットメッセージ編集 |
| `d` | コミット削除（drop） |
| `e` | コミット編集開始 |
| `<ctrl+j>` / `<ctrl+k>` | コミット順序を上下に移動 |
| `C` | チェリーピック（コピー） |
| `V` | チェリーピック（ペースト） |

### インタラクティブリベース

| キー | 動作 |
|------|------|
| `i` | インタラクティブリベース開始 |
| `m` | リベースオプションメニュー表示 |

### Push/Pull操作

| キー | 動作 |
|------|------|
| `p` | プル |
| `P` | プッシュ |

### スタッシュ操作（Stashパネル）

| キー | 動作 |
|------|------|
| `<space>` | スタッシュを適用（残す） |
| `g` | スタッシュをポップ（適用して削除） |
| `d` | スタッシュを削除 |
| `n` | スタッシュから新規ブランチ作成 |

### その他便利なキー

| キー | 動作 |
|------|------|
| `z` | 直前の操作を取り消し（Undo） |
| `Z` | 取り消しをやり直し（Redo） |
| `R` | 画面リフレッシュ |
| `@` | コマンドログ表示 |
| `:` | カスタムコマンド実行 |

---

## 5. 便利な機能

### コミット順序の変更

Commitsパネルで `Ctrl+J` / `Ctrl+K` を使うと、インタラクティブリベースの煩雑さなしにコミット順序を入れ替えられます。

### Cherry-Pick操作

1. コピーしたいコミットで `Shift+C`
2. 貼り付け先のブランチに移動
3. `Shift+V` でペースト

### 行単位ステージング

1. Filesパネルでファイルを選択
2. `<enter>` で差分表示
3. `<space>` で行単位、`a` でhunk単位のステージング

### Bisect（バグ検出）

二分探索でバグが混入したコミットを特定できます。Commitsパネルで `b` キーから開始。

### ブランチのマージ

別ブランチの変更を現在のブランチに取り込む方法です。

**手順:**

1. **Branchesパネルに移動** → `3` キー
2. **マージ先ブランチにチェックアウト** → マージ先を選択して `<space>`
3. **マージ元ブランチを選択** → マージしたいブランチにカーソルを合わせる
4. **マージ実行** → `M` キーでマージオプション表示 → `merge` を選択

**マージオプション:**

| オプション | 説明 |
|------------|------|
| merge | 通常のマージ（マージコミットが作成される） |
| rebase | 現在のブランチをマージ元にリベース |
| squash | コミットを1つにまとめてマージ |

**コンフリクトが発生した場合:**

1. Filesパネル（`2`）にコンフリクトファイルが赤く表示される
2. ファイルを選択して `<enter>` で差分表示
3. 編集して解決後、`<space>` でステージング
4. 全て解決したら `m` → `continue` でマージ完了

**要約:**
```
マージ先にチェックアウト → マージ元で M → merge
```

---

## 6. 設定ファイル

### 設定ファイルの場所

| OS | パス |
|----|------|
| Linux | `~/.config/lazygit/config.yml` |
| macOS | `~/Library/Application Support/lazygit/config.yml` |
| Windows | `%LOCALAPPDATA%\lazygit\config.yml` |

環境変数 `LG_CONFIG_FILE` または起動時オプション `--use-config-file` で変更可能。

### 設定例

```yaml
gui:
  # テーマ設定
  theme:
    activeBorderColor:
      - green
      - bold
    inactiveBorderColor:
      - white
  # マウスサポート
  mouseEvents: true
  # 表示言語
  language: "auto"

git:
  # 自動フェッチ
  autoFetch: true
  # コミットメッセージ長の警告
  commitLength:
    show: true

# キーバインドのカスタマイズ
keybinding:
  universal:
    quit: 'q'
    return: '<esc>'
```

### エディタ設定

`editPreset` で vim、nvim、vscode、sublime等を選択可能:

```yaml
os:
  editPreset: "nvim"
```

---

## 7. クイックリファレンス（よく使う操作）

```
基本フロー:
  lazygit          → 起動
  2                → Filesパネルへ
  <space>          → ファイルをステージング
  c                → コミット（メッセージ入力）
  P                → プッシュ

ブランチ作成:
  3                → Branchesパネルへ
  n                → 新規ブランチ作成
  <space>          → ブランチ切替

困ったとき:
  ?                → キーバインド一覧
  z                → 直前の操作を取り消し
  q                → 終了
```

---

## 8. 参考リンク

- [公式GitHubリポジトリ](https://github.com/jesseduffield/lazygit)
- [公式キーバインドドキュメント](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md)
- [設定ドキュメント](https://github.com/jesseduffield/lazygit/blob/master/docs/Config.md)
- [FreeCodeCamp - How to Use Lazygit](https://www.freecodecamp.org/news/how-to-use-lazygit-to-improve-your-git-workflow/)
- [Zenn - Git操作を爆速化するlazygit](https://zenn.dev/aishift/articles/d1a0551a444317)
- [Zenn - モテるGit管理](https://zenn.dev/mozumasu/articles/mozumasu-lazy-git)
