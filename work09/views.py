from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from datetime import date
from datetime import date, datetime


def todo_list(request):
    sort = request.GET.get("sort", "due_date")
    filter_status = request.GET.get("filter", "all")  # ← フィルター追加

    todos = Todo.objects.all()

    # フィルタ処理
    if filter_status == "completed":
        todos = todos.filter(is_completed=True)
    elif filter_status == "incomplete":
        todos = todos.filter(is_completed=False)

    # ソート処理
    if sort == "created_at":
        todos = todos.order_by("created_at")
    else:
        todos = todos.order_by("due_date")

    today = date.today()
    return render(
        request,
        "work09/todo_list.html",
        {"todos": todos, "today": today, "sort": sort, "filter_status": filter_status},
    )


# 新規作成
def todo_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        Todo.objects.create(title=title, due_date=due_date)
        return redirect("todo_list")
    return redirect("todo_list")


# 編集
def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.due_date = request.POST.get("due_date")
        todo.is_completed = "is_completed" in request.POST
        todo.save()
        return redirect("todo_list")
    return render(request, "work09/todo_edit.html", {"todo": todo})


# 削除
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todo_list")


# 完了・未完了の切り替え
def todo_toggle(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect("todo_list")
