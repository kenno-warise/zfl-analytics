# zfl-analytics

- gif画像

PythonのWebフレームワークであるDjangoで開発した分析アプリです。

現在の仕様はGoogleアナリティクスのデータに特化した分析アプリとなっています。


-----

**目次**
- [使い方](#使い方)
- [License](#license)

## 使い方

以下のバージョンでの使用を検討してください。

|名前|バージョン|
|----|----|
|Python|3.7.0|
|Django|2.2.5|

```console
$ pip install zfl-analytics
```

Djangoプロジェクトの設定ファイルを開いて「INSTALLED_APPS」にアプリを設定します。

```python
# settings.py

...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'analytics',  # 追加
]
```

Djangoプロジェクトのパス設定ファイルを開いてアプリのパスを設定します。

```python
# urls.py

...

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
    path('', include('analytics.urls'))  # 追加
]
```

データベースを初期化して管理画面に入る為のスーパーユーザーを作成しDjangoプロジェクトを起動します。

```console
$ python3 manage.py migrate

$ python3 manage.py createsuperuser

$ python3 manage.py runserver
```

管理画面にアクセスして、「Googleアナリティクス4の構成」を追加してください。

この構成はデータを更新する際にGoogleアナリティクス４のAPIを使用するときに必要です。

※APIキーは環境変数に設定します。

- 画像


ログインした状態でアプリのページにアクセスすると、ナビゲーションバーに「設定」マークと「更新」マークが表示されます。

- 画像

更新ボタンをクリックすると、Googleアナリティクス4のAPIを通じてデータを取得します。

データを取得する範囲は、「Googleアナリティクス4の構成」の「days\_ago」で設定されている値の範囲です。「7」であれば過去7日間のデータを取得することになります。注:現在取得できる範囲は過去30日間までとなっています。


コマンドによるデータの更新は以下の方法です。

```console
# 設定が完了していない場合
$ python3 manage.py update_analyticsdata
GoogleAnalytics4の設定が完了しておりません

# 設定が完了している場合
$ python3 manage.py update_analyticsdata
アナリティクスアプリのデータベース更新完了
```

テンプレートファイルの設定は管理画面から行えます。

Djangoプロジェクトの直下に「templates/base.html」が存在していれば自動的に読み込まれますが、存在していなかったりファイル名が「base.html」でない場合は独立したHTMLファイルを使用します。

それらベースのテンプレートファイルの設定やBootstrapのグリッドシステムの設定は「アナリティクスアプリの設定」から行えます。

- 画像


## License

`zfl-analytics` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
