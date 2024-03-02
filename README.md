# zfl-analytics

DjangoのWebフレームワークで開発した分析アプリです。

分析データはGoogleアナリティクスから収集した「date」ディメンションからなる「activeusers」「newusers」「pageview」「sessions」「totaladrevenue」「publisshaadimpression」のデータを活用します。

以下は「zfl-analytics」において使用しているデータ名一覧です。

|カラム名|内容|
|----|----|
|date|日付|
|activeusers|特定の期間にアクセスしたユーザー数|
|newusers|新規ユーザー|
|pageview|ページが開かれた回数|
|sessions|アクセスされてサイトから離脱するまでに行った移動数|
|totaladrevenue|広告収益額|
|publissheradimpression|広告が表示された回数|


-----

**目次**
- [インストール](#インストール)
- [License](#license)

## インストール


```console
$ python3 -m venv .venv && . .venv/bin/activate

$ pip install --upgrade pip

$ pip install zfl-analytics
```


データベースを初期化してアプリを起動します。

```console
$ python3 manage.py migrate

$ python3 manage.py runserver
```

アナリティクスデータ更新コマンド

```console
$ python3 manage.py update_analyticsdata
GoogleAnalytics4の設定が完了しておりません
```

...

```console
$ python3 manage.py update_analyticsdata
アナリティクスアプリのデータベース更新完了
```

## License

`zfl-analytics` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
