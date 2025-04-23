# AtCoder Language Update テスト用 Dockerfile

[2025 年言語アップデート](https://atcoder.jp/posts/1342) の Haskell 環境のテスト用です。

## テストの実行手順

1. `installscript.toml` を設定 ([toyboot4e/submission](https://github.com/toyboot4e/submission) で自動生成 + 手作業したものをコピー)
2. [gksato/haskell-atcoder-server-gen](https://github.com/gksato/haskell-atcoder-server-gen) で生成した `CheckSource.sh` をリポジトリのこの直下にコピー (上書き)
3. `./run.sh` を実行

