# システムの実行方法

このドキュメントでは、`main-script.py`スクリプトの実行方法について説明します。

## 必要条件

このスクリプトを実行するには、Python 3.7.9またはそれ以上のバージョンがインストールされている必要があります。

## 実行コマンド

スクリプトはコマンドラインから以下の形式で実行します：

```bash
py .\main-script.py [テンプレートID] [カスタムコード]
```

- `[テンプレートID]`：使用するテンプレートのIDを指定します。＊必須
- `[カスタムコード]`：テンプレート内のtitleに含まれる@@@を置換する文字列を指定します。＊任意

例えば、テンプレートIDが`0001`で、カスタムコードが`7`の場合、以下のようにコマンドを実行します：

```bash
py .\main-script.py 0001 7
```

このコマンドは、ID `0001`のテンプレートを使用し、テンプレート内のtitleに含まれる@@@を`7`置換するためのものです。