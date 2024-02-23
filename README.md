# zfl-analytics

DjangoのWebフレームワークで開発された分析アプリです。

分析データはGoogleアナリティクスから収集したデータを活用します。


-----

**目次**
- [インストール](#インストール)
- [設定](#設定)
- [開発](#開発)
- [パッケージの組み込みテスト](#パッケージの組み込みテスト)
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

## 設定


## 開発


## パッケージの組み込みテスト



## License

`zfl-analytics` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
