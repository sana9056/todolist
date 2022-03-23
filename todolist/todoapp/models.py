from django.db import models

from userapp.models import User


class todoapp(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100, unique=True)
    repository = models.URLField(blank=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}'


class todolist(models.Model):
    project = models.ForeignKey(todoapp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description}'