from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),  # 一覧
    path("add/", views.todo_add, name="todo_add"),  # 新規作成
    path("edit/<int:todo_id>/", views.todo_edit, name="todo_edit"),  # 編集
    path("delete/<int:todo_id>/", views.todo_delete, name="todo_delete"),  # 削除
    path(
        "toggle/<int:todo_id>/", views.todo_toggle, name="todo_toggle"
    ),  # 完了・未完了切替
]
