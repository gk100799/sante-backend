from django.db import models

# Create your models here.
class Products(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=25)
    price = models.IntegerField()
    dprice = models.IntegerField(blank=True, null=True)
    desciption = models.CharField(max_length=100, blank=True, null=True)
    imagename = models.CharField(max_length=20, blank=False)

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
    size = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_sizes'

class Productbrand(models.Model):
    pid = models.ForeignKey('Products', models.DO_NOTHING, db_column='pid', blank=True, null=True)
    bname = models.ForeignKey('Brand', models.DO_NOTHING, db_column='bname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_productbrand'

