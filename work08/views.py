from django.shortcuts import render, redirect
from .models import Memo
from django.shortcuts import get_object_or_404


def top(request):
    memos = Memo.objects.all()
    return render(request, "work08/top.html", {"memos": memos})


def edit(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    if request.method == "POST":
        memo.title = request.POST.get("title", memo.title)
        memo.content = request.POST.get("content", memo.content)
        memo.save()
        return redirect("work08:top")
    return render(request, "work08/edit.html", {"memo": memo})


def create_memo(request):
    memo = Memo.objects.create(title="no title", content="")
    return redirect("work08:edit", memo_id=memo.id)


# 編集画面用のビュー関数


def edit(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)

    if request.method == "POST":
        memo.title = request.POST.get("title", memo.title)
        memo.content = request.POST.get("content", memo.content)
        memo.save()
        return redirect("work08:top")  # 保存したら一覧に戻る

    return render(request, "work08/edit.html", {"memo": memo})


# 削除用のビュー関数
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()  # データベースから削除
    return redirect("work08:top")  # 一覧画面に戻る
