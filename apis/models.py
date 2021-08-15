from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from users.models import User
# Create your models here.


# class ParentCategory(models.Model):
#     ''' Class to interact with db.sqlite3 and creates the category table'''

#     category = models.CharField(("Category"), max_length=50)
#     posted_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-posted_on']

#     def __str__(self):
#         return self.category


# class SubCategory(models.Model):
#     ''' Class to interact with db.sqlite3 and creates the sub_category table'''

#     sub_category = models.CharField(("sub_category"), max_length=50)

class Product(models.Model):
    ''' Class to interact with db.sqlite3 and creates the Product table'''

    title = models.CharField(("Name"), max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.TextField("Description")
    measure = models.CharField(("Measure"), max_length=50)
    price = models.DecimalField(("Price"), max_digits=7, decimal_places=2)
    slug = models.SlugField(("slug"), max_length=200, unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey("ParentCategory", verbose_name=("Category"), on_delete=models.CASCADE)
    category = models.CharField(("category"), max_length=20)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title


class Order(models.Model):
    title = models.CharField(("Name"), max_length=100)
    description = models.TextField("Description")
    total_price = models.DecimalField(("Price"), max_digits=13, decimal_places=2)
    ordered_on = models.DateTimeField(auto_now_add=True)
    order_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING, blank=True, null=True)


