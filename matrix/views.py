from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import TaskForm
from .models import Quadrant, Task


def board(request):
    grouped_tasks = {quadrant: Task.objects.filter(quadrant=quadrant) for quadrant, _ in Quadrant.choices}
    context = {
        "grouped_tasks": grouped_tasks,
        "quadrants": Quadrant.choices,
    }
    return render(request, "matrix/board.html", context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created.")
            return redirect("board")
    else:
        form = TaskForm()
    return render(request, "matrix/task_form.html", {"form": form, "action": "Create"})


def update_task(request, task_id: int):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated.")
            return redirect("board")
    else:
        form = TaskForm(instance=task)
    return render(request, "matrix/task_form.html", {"form": form, "action": "Update", "task": task})


def toggle_complete(request, task_id: int):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed", "updated_at"])
    return redirect(reverse("board"))


def delete_task(request, task_id: int):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        messages.info(request, "Task deleted.")
        return redirect("board")
    return render(request, "matrix/task_confirm_delete.html", {"task": task})
