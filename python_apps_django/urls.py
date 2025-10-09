from django.contrib import admin
from django.urls import path, include
from work05 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("work05/", include("work05.urls")),
    path("work06/", include("work06.urls")),
    path("work07/", include("work07.urls")),
    path("work08/", include("work08.urls")),
    path("", views.index, name="index"),
]
