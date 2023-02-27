from django.db import models
from users.models import Users
class CategoryPost(models.Model):
    category = models.CharField(max_length=150,unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category
class Post(models.Model):
    name = models.CharField(max_length=160)
    text = models.TextField()
    photo = models.ImageField(upload_to='basket_post',blank=False)
    cat = models.ForeignKey(CategoryPost,on_delete=models.CASCADE)
    author = models.ForeignKey(Users,on_delete=models.CASCADE)

    def __str__(self):
        return self.name