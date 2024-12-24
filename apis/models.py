from django.db import models
from  django.core.validators import EmailValidator
from django.db.models.functions import Now
from django.core.exceptions import ValidationError

# Create your models here



class User(models.Model):
    Name = models.CharField(max_length=254, null=False)
    Admin = models.BooleanField(db_default=False)
    Email = models.CharField(unique=True, max_length=254, null=False)
    Password = models.TextField(null=False)
    Profile_Picture = models.BinaryField(null=False)
    Created_At = models.DateTimeField(db_default=Now())

    class Meta:
        db_table = 'users'

class Category(models.Model):
    Category_Name = models.CharField(max_length=256, unique=True)
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_At = models.DateTimeField(db_default=Now())

    class Meta:
        db_table = 'categories'

class Subcategory(models.Model):
    SubCategory_Name = models.CharField(max_length=256)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_At = models.DateTimeField(db_default=Now())

    class Meta:
        db_table = 'subcategories'


class Applications(models.Model):
    App_Name = models.CharField(max_length=254, null=False)
    App_link = models.URLField(blank=True, null=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    Subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=False)
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Description = models.TextField(blank=True, null=False)
    Points = models.IntegerField(null=False)
    Application_Picture = models.BinaryField( null=False)
    Created_At = models.DateTimeField(db_default=Now())
    Screenshots = models.JSONField(default=dict)

    class Meta:
        db_table = 'applications'
