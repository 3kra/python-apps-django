from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from datetime import date


# 一覧表示
def todo_list(request):
    todos = Todo.objects.all().order_by("due_date")  # 期限順
    today = date.today()
    return render(request, "work09/todo_list.html", {"todos": todos, "today": today})


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
