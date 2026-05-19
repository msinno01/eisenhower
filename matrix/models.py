from django.db import models


class Quadrant(models.TextChoices):
    DO = "DO", "Urgent + Important (Do)"
    DECIDE = "DECIDE", "Not Urgent + Important (Schedule)"
    DELEGATE = "DELEGATE", "Urgent + Not Important (Delegate)"
    DELETE = "DELETE", "Not Urgent + Not Important (Eliminate)"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quadrant = models.CharField(max_length=20, choices=Quadrant.choices, default=Quadrant.DO)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["is_completed", "due_date", "-created_at"]

    def __str__(self) -> str:
        return self.title
