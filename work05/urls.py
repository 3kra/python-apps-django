from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # トップページ
    path("list/", views.list, name="list"),  # リストページ
]
