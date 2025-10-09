from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="work07_top"),  # トップページ
    path("omikuji/", views.omikuji, name="omikuji"),  # おみくじページ
    path("janken/", views.janken, name="janken"),  # ジャンケンページ
    path("hi_low/", views.hi_low, name="hi_low"),  # High & Lowページ
]
