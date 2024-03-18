from django.db import models

class NATO_Member(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='member_photos/')  # Здесь указываем путь для сохранения изображений


class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='country_photos')

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class InfoNATO(models.Model):
    photo = models.ImageField(upload_to='info_nato_photos')  
    name = models.CharField(max_length=100)  
    description = models.TextField()  

    def __str__(self):
        return self.name
    
class Story(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title