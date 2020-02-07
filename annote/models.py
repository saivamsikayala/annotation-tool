from django.db import models

# Create your models here.
class AnnoteModel(models.Model):
    image = models.ImageField(upload_to="media/",null=True)
    filename = models.CharField(max_length=50,default="image.jpg")
    xcoordinate = models.IntegerField(default=0)
    ycoordinate = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    #shape = models.CharField(max_length=30,default="rect")
    attribute = models.CharField(max_length=30,default="trash")
    garbage = models.CharField(max_length=30,default="Garbage")
