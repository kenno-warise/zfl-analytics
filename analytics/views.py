import pandas as pd

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
