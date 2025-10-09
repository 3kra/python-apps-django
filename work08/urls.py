from django.urls import path
from . import views

app_name = "work08"

urlpatterns = [
    path("", views.top, name="top"),  # メモ一覧画面
    path("edit/<int:memo_id>/", views.edit, name="edit"),  # 編集画面
    path("create/", views.create_memo, name="create_memo"),  # 新規作成用
    path("delete/<int:memo_id>/", views.delete_memo, name="delete_memo"),  # 削除用
]
