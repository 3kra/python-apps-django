from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # トップページ
    path("reiwa/", views.reiwa, name="reiwa"),  # 令和変換ページ
    path("bmi/", views.bmi, name="bmi"),  # BMI計算ページ
    path("warikan/", views.warikan, name="warikan"),  # 割り勘計算ページ
    path("chokin/", views.chokin, name="chokin"),  # 貯金計算ページ
    path("calculator/", views.calculator, name="calculator"),  # 計算機ページ
]
