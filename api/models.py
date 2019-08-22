from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Seller(get_user_model()):
    county = models.CharField(max_length=150)
    store_name = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name


class Buyer(get_user_model()):
    phone_number = models.IntegerField(max_length=12)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent_id = models.ForeignKey('Category', null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=150)
    parent_id = models.ForeignKey('Brand', on_delete=models.DO_NOTHING, null=True, blank=True)
    logo_image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    short_description = models.TextField()
    long_description = models.TextField()
    unit_cost = models.FloatField()
    featured_image_url = models.ImageField(upload_to="product_images", max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class OrderProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()


class WishList(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

