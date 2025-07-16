from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField("ID de Usuario")
    title = models.CharField("Título", max_length=255)
    completed = models.BooleanField("¿Completado?", default=False)

    def __str__(self):
        return self.title