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

# セットアップ
ここで示す手順はすべて本リポジトリのルート直下(以降、プロジェクトディレテクトリとします)で実行し、確認したものです。

## 仮想環境( `.venv` )の作成先を設定する
仮想環境の設定を確認してください。

```bash
% poetry config --list        # 設定を確認
(省略)
virtualenvs.in-project = null # 仮想環境がプロジェクトディレクトに作成されない
(省略)
```

仮想環境をプロジェクトディレクトリに設定します。
```bash
% poetry config virtualenvs.in-project true
% poetry config --list
virtualenvs.in-project = true # 仮想環境がプロジェクトディレクトに作成される
```

### 補足
`virtualenvs.in-project = null` の状態ですでに後述の `poetry install` を行っていた場合、仮想環境は [デフォルト PATH](https://python-poetry.org/docs/configuration/#virtualenvspath) ( `{cache-dir}/virtualenvs` ) に作成されています。
次のコマンドで作成済みの仮想環境を削除してください。

```bash
# 仮想環境を確認する
% poetry env list
(環境が表示されます)
% poetry env remove ${表示された環境を指定してくだい}

# もういちど `poetry env list` を実行してみる
% poetry env list
(削除した環境は表示されません)
```

## 仮想環境の作成
仮想環境を作成します。
下記コマンドを実行することで、 [pyproject.toml](./pyproject.toml) に登録された package がインストールされた仮想環境が作成されます。

```bash
% poetry install
Installing dependencies from lock file

Package operations: 52 installs, 0 updates, 0 removals

(省略)

Installing the current project: streamlit-work (0.1.0)
```

プロジェクトディレクトリに仮想環境( `.venv` ) が作成されていることを確認します。
```bash
% ls -la
(省略)
drwxrwxr-x 6 ksh ksh  4096  9月  4 12:29 .venv
```

### 補足
Streamlit は次のコマンドで予め [pyproject.toml](./pyproject.toml) に登録ずみです。

```bash
% poetry add streamlit
```

# アプリケーションの起動
起動用のスクリプトを用意しております。
次のコマンドを実行して起動してください。

```bash
% ./run.sh 

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.2.183:8501
```

上記 URL にブラウザからアクセスすると Streamlit で作成したページが確認できます。


