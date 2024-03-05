import pandas as pd

from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django_pandas.io import read_frame

from .models import DimensionDate

class HomePageView(TemplateView):
    template_name = "analytics/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        df = read_frame(DimensionDate.objects.all())
        # 日付データを「年月」のフォーマットに変換
        df['dates'] = df['dates'].apply(lambda df: df.strftime("%Y年%m月"))
        # 日付データを元に日付以外のデータを集約する
        df = df.drop('id', axis=1).groupby(df["dates"]).sum()
        # テーブルに渡す用に、日付を降順にソートしたデータフレームを作成
        df_descending = df.sort_values('dates', ascending=False)
        # テンプレートへ渡すコンテキストデータに格納
        context["data_graph"] = df
        context["data_graph_subtitle"] = f"{df.index[0]} - {df.index[-1]}"
        context["data_table"] = df_descending
        return context


def pulldown(request):
    data_name = request.GET.get('data_name')
    date_value = request.GET.get('date_value')
    dd_obj_all = DimensionDate.objects.all()
    
    # フィールドのバーボスネーム取得
    for field in dd_obj_all.first()._meta.get_fields():
        if field.name == data_name:
            verbose_name = field.verbose_name
    
    df = read_frame(dd_obj_all)
    # 日付データを「年月」のフォーマットに変換
    df['dates'] = df['dates'].apply(lambda df: df.strftime("%Y年%m月"))
    # 日付データを元に日付以外のデータを集約する
    df = df.drop('id', axis=1).groupby(df["dates"]).sum()
    
    # グラフ用の処理 ----------------------------------------------
    # 日付の設定値を変える処理
    if date_value == '2':
        df = df[-12:]
    elif date_value == '3':
        df = df[-6:]

    # jsresponse用にリストを作成
    graph_data = [[index,data] for index, data in zip(df.index, df[data_name])]
    
    # テーブル用の処理 ---------------------------------------------
    # テーブルに渡す用に、日付を降順にソートしたデータフレームを作成
    df_descending = df.sort_values('dates', ascending=False)
    
    # 日付の設定値を変える処理
    if date_value == '2':
        df_descending = df_descending[:12]
    elif date_value == '3':
        df_descending = df_descending[:6]
    
    # jsresponse用にリストを作成
    ls_data = [[index,data] for index, data in zip(df_descending.index, df_descending[data_name])]
    
    return JsonResponse({
                'data_table_head': verbose_name,
                'data_table': ls_data,
                'data_graph': graph_data,
            }, status=200)

