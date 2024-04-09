from django.db import models

# Create your models here.
class sliderModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_img/',blank=True,null=True)

    def __str__(self):
        return self.title
    
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    msg = models.TextField()

    def __str__(self):
        return self.name
    