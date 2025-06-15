from django.db import models

# Create your models here.
class FleaItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flea/images/')
    is_sold = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name