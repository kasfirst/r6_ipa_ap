# ベースイメージとしてPython 3を指定
FROM python:3.9-slim

# vscode ユーザーの作成
RUN useradd -ms /bin/bash vscode

# 作業ディレクトリを設定
WORKDIR /workspace

# Pythonパッケージのキャッシュを活用して、依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# デフォルトのコマンド
# CMD ["python"]
