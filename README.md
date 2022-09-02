# streamlit-work
Python の Web フレームワーク [Streamlit](https://streamlit.io/) を使った学習用リポジトリ

- Streamlit の公式ドキュメントは [こちら](https://docs.streamlit.io/)
- 上記から [Get started](https://docs.streamlit.io/library/get-started) や [API reference](https://docs.streamlit.io/library/api-reference) を参照できます。

# 環境
本リポジトリの内容は次の環境で確認しております。

| 環境 | バージョン | 備考 |
| ---- | ---------- | ---- |
| Python | 3.10.6 | python --version |
| Poetry | 1.1.15 | poetry --version |
| Streamlit | ^1.12.2 | pyproject.toml から | 

# 事前準備
## Poetry のインストール
このリポジトリで扱うアプリは `Poetry` でパッケージ管理を行っています。
事前に `Poetry` をインストールしてください。

- Poetry の公式ページは [こちら](https://python-poetry.org/)
- Poetry の GitHub は [こちら](https://github.com/python-poetry/poetry)

## セットアップ
次のコマンドを実行し環境をセットアップしてください。

```bash
% poetry install
Installing dependencies from lock file

Package operations: 52 installs, 0 updates, 0 removals

  • Installing six (1.16.0)
  ...
  ...
  ...
Installing the current project: streamlit-work (0.1.0)
```

## 補足
Streamlit は次のコマンドで予め [pyproject.toml](./pyproject.toml) に登録ずみです。
(実行時のログ含めて記載しています)

```bash
% poetry add streamlit
Using version ^1.12.2 for streamlit

Updating dependencies
Resolving dependencies... (2.7s)

Writing lock file

Package operations: 0 installs, 2 updates, 0 removals

  • Updating jsonschema (4.14.0 -> 4.15.0)
  • Updating pandas (1.4.3 -> 1.4.4)
```

# 実行
起動用のスクリプトを用意しております。
次のコマンドを実行して起動してください。

```bash
% ./run.sh 

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.2.183:8501
```

上記 URL にブラウザからアクセスすると Streamlit で作成したページが確認できます。


