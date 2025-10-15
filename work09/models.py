from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)  # タスク名
    description = models.TextField(blank=True, null=True)  # 詳細（任意）
    due_date = models.DateField()  # 期限日
    is_completed = models.BooleanField(default=False)  # 完了フラグ
    created_at = models.DateTimeField(auto_now_add=True)  # 登録日（自動追加）

    def __str__(self):
        return self.title
