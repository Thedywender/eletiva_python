from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("1", "BAIXO"),
        ("2", "MÉDIO"),
        ("3", "ALTO"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
