from django.urls import path
from . import views


app_name = 'analytics'

urlpatterns = [
        path('', views.HomePageView.as_view(), name='index'),
        path('pulldown/', views.pulldown, name='pulldown'),
        path('update/', views.update, name='update')
]

