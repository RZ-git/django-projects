# django-projects
Django 3.0.7 ~ プロジェクト



-- 前提
1. Pythonのインストール


-- 手順
①IDEで開発用のフォルダに移動
②githubからソースをコピー（zip解凍の場合は要git接続）
    >> git clone <url>
③仮想環境作成
    >> python -m venv venv
④仮想環境内のPythonをProject Interpreterに設定
⑤pipのアップデート（任意）
    >> python -m pip install --upgrade pip
⑥whlファイルをダウンロードして、mysqlclientをインストール。ルートディレクトリに配置。
    ファイル名：mysqlclient-1.4.6-cp38-cp38-win32.whl（環境によって異なる場合有り）
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
    >> pip install mysqlclient-1.4.6-cp38-cp38-win32.whl
⑦必要なライブラリをインストール
    >> pip install -r requirements.txt
⑧ MySQL Server 8.0.20その他MySQL関連ツールのインストール
    https://dev.mysql.com/downloads/installer/
    ※自分の名前でユーザーを一人追加しておく。（rootユーザーしかないと接続エラーになることがある。）
    ※基本的にオプション選択は開発用に使う最小の設定
    ※InnoDBは使いません。インスタンスが最低3台いるそうなので。
    rootユーザーのパスワードは config\settings.py 参照
    Executeポチポチして、MySQL ShellとMySQL Workbenchウィンドウが開いたら完了
⑨ MySQL（Windows） の初期設定と日本語化等
    https://style.potepan.com/articles/19084.html
    ※設定ファイルは my.cnf じゃなく C:\ProgramData\MySQL\MySQL Server 8.0\my.ini
    ※rootユーザーではなく、個別にDBユーザーを作らないとコネクションエラーが起きる
    mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
⑩チャットアプリ用のデータベース作成
    MysSQL 8.0 Command Line Clientを起動して下記コマンドを実施
    >> CREATE DATABASE chat_db CHARACTER SET utf8mb4;
    >> use chat_db;

⑪初期モデルのマイグレ（gitからソースを取得した場合はマイグレーションファイル作成不要）
    >> python manage.py migrate
