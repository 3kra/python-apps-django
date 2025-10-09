from django.shortcuts import render
from django.http import HttpResponse


# トップページ：index.htmlを表示
def index(request):
    return render(request, "work05/index.html")


# listページ：仮のメッセージを表示
def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")
