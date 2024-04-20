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
    
class BlogCategory(models.Model):
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title
class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog_img/')
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
LAVELCHOSE = (
    ('Begineer','Begineer'),
    ('Intermedate','Intermedate'),
    ('Expert','Expert'),
)
class ReceipePost(models.Model):
    title = models.CharField(max_length=200)
   
    preparation_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    yield_items = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    lavel = models.CharField(choices=LAVELCHOSE,default='Begineer',max_length=50)
    featured_item = models.BooleanField(default=False)
    def __ser__(self):
        return self.title
    

class ReceipeImage(models.Model):
    receipe_post = models.ForeignKey(ReceipePost,on_delete=models.CASCADE ,related_name='receipe_post_set' )
    image = models.ImageField(upload_to='receipe_img/')

    

class RecipeContentSection(models.Model):
    post = models.ForeignKey(ReceipePost, on_delete=models.CASCADE,related_name='post_set')
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
    

class Ingredient(models.Model):
    post = models.ForeignKey(ReceipePost, on_delete=models.CASCADE, null=True, blank=True,related_name='post_set_ingd')
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['name']





class Feedback(models.Model):
    message = models.TextField()
    rating = models.IntegerField(default=0)  # New field for storing the rating
    created_at = models.DateTimeField(auto_now_add=True)
   