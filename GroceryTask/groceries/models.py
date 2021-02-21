from django.db import models

# Create your models here.

class GroceryItem(models.Model):

    title=models.CharField(max_length=255)
    description=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.FloatField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Grocery Items'