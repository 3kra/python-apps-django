from django.contrib import admin
from django.urls import path, include
from work05 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("work05/", include("work05.urls")),
    path("work06/", include("work06.urls")),
    path("work07/", include("work07.urls")),
    path("work08/", include("work08.urls")),
    path("work09/", include("work09.urls")),
    path("", views.index, name="index"),
]

# 画像アップロード用の設定（MEDIA_URL でアクセスされた時に MEDIA_ROOT を参照）
if settings.DEBUG:  # 開発中のみ
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
