from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="recipe-image")
    price=models.BigIntegerField(default=100)

    def __str__(self):
        return self.name 

class Orders(models.Model):
    order = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    cost=models.BigIntegerField(default=200)

    def __str__(self) -> str:
        return self.order.name
