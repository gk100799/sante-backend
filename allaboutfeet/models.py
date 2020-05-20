from django.db import models
from django.conf import settings


# Create your models here.
class Products(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=50)
    price = models.IntegerField()
    dprice = models.IntegerField(blank=True, null=True)
    desciption = models.CharField(max_length=500, blank=True, null=True)
    imagename = models.CharField(max_length=90, blank=False)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_products'


class Category(models.Model):
    cname = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_category'

class Brand(models.Model):
    bname = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_brand'

class Style(models.Model):
    sname = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_style'

class Colors(models.Model):
    color = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_colors'


class Sizes(models.Model):
    size = models.CharField(primary_key=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_sizes'

class ProductSubs(models.Model):
    pid = models.ForeignKey('Products', models.DO_NOTHING, db_column='pid',primary_key=True, blank=True, null=False)
    bname = models.ForeignKey('Brand', models.DO_NOTHING, db_column='bname', blank=True, null=True)
    cname = models.ForeignKey('Category', models.DO_NOTHING, db_column='cname', blank=True, null=True)
    sname = models.ForeignKey('Style', models.DO_NOTHING, db_column='sname', blank=True, null=True)
    color = models.ForeignKey('Colors', models.DO_NOTHING, db_column='color', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_productsubs'

class ProductSizes(models.Model):
    pid = models.ForeignKey('Products', models.DO_NOTHING, db_column='pid')
    size = models.ForeignKey('Sizes', models.DO_NOTHING, db_column='size')
    
    class Meta:
        managed = False
        db_table = 'allaboutfeet_productsizes'
        unique_together = (('pid', 'size'),)


class Cart(models.Model):
    user_id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_cart'
        unique_together = (('user_id', 'pid'),)


class ProductDetails(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=25)
    price = models.IntegerField()
    dprice = models.IntegerField(blank=True, null=True)
    desciption = models.CharField(max_length=100, blank=True, null=True)
    imagename = models.CharField(max_length=20, blank=False)
    bname = models.CharField(max_length=20)
    cname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    color = models.CharField(max_length=20)


    class Meta:
        managed = False
        db_table = 'productdetails'


class Orders(models.Model):
    user_id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_orders'
        unique_together = (('user_id', 'pid'),)