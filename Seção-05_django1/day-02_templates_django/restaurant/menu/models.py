from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="menu/img/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.ingredients[:20]} - {self.instructions[:20]} - {self.created_at} - {self.updated_at} - {self.image}"
