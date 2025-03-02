from django.db import models

# Create your models here.


class Blog_Category(models.Model):
    category = models.CharField(max_length=50)


    def __str__(self):
        return self.category



class Blog_Post(models.Model):
    category = models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()





    
