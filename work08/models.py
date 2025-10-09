from django.db import models

# Create your models here.


class Memo(models.Model):
    title = models.CharField(max_length=100, default="no title")  # タイトル
    content = models.TextField(blank=True)  # メモ本文
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時
    image = models.ImageField(upload_to="images/", blank=True, null=True)  # 写真

    def __str__(self):
        return self.title
