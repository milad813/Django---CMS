from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Authors(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField(upload_to='images/')
    counter_view = models.IntegerField(default=0)
    author_id = models.ForeignKey(Authors, on_delete=models.SET_NULL, null=True)
    category_id = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

class Comments(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    text=models.TextField()

