from django.db import models

# Create your models here.
class Boardgame(models.Model):
  name = models.CharField(max_length=100)
  background = models.CharField(max_length=300)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=100)
  boardgame = models.ForeignKey(
    Boardgame, related_name="categories", on_delete=models.CASCADE
  )

  def __str__(self):
    return self.name
