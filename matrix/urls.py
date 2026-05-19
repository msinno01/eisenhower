from django.urls import path
from . import views

urlpatterns = [
    path("", views.board, name="board"),
    path("tasks/new/", views.create_task, name="create_task"),
    path("tasks/<int:task_id>/edit/", views.update_task, name="update_task"),
    path("tasks/<int:task_id>/toggle/", views.toggle_complete, name="toggle_complete"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
]
