from django.db import models

# Create your models here.

class ParentCategory(models.Model):
    ''' Class to interact with db.sqlite3 and creates the category table'''

    category = models.CharField(("Category"), max_length=50)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    ''' Class to interact with db.sqlite3 and creates the sub_category table'''

    sub_category = models.CharField(("sub_category"), max_length=50)

class Product(models.Model):
    ''' Class to interact with db.sqlite3 and creates the Product table'''

    name = models.CharField(("Name"), max_length=50)
    measure = models.CharField(("Measure"), max_length=50)
    price = models.IntegerField(("Price"))
    slug = models.SlugField(("slug"), max_length=200, unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("ParentCategory", verbose_name=("Category"), on_delete=models.CASCADE)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.name


