from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "quadrant",
                    models.CharField(
                        choices=[
                            ("DO", "Urgent + Important (Do)"),
                            ("DECIDE", "Not Urgent + Important (Schedule)"),
                            ("DELEGATE", "Urgent + Not Important (Delegate)"),
                            ("DELETE", "Not Urgent + Not Important (Eliminate)"),
                        ],
                        default="DO",
                        max_length=20,
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
                ("due_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["is_completed", "due_date", "-created_at"]},
        ),
    ]
