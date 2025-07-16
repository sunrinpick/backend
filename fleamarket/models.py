from django.db import models

# Create your models here.
class FleaItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=1024)
    is_sold = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name