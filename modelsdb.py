# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllaboutfeetBrand(models.Model):
    bname = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_brand'


class AllaboutfeetCart(models.Model):
    user = models.OneToOneField('AuthUser', models.DO_NOTHING, primary_key=True)
    id = models.AutoField()
    pid = models.ForeignKey('AllaboutfeetProducts', models.DO_NOTHING, db_column='pid')
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_cart'
        unique_together = (('user', 'pid'),)


class AllaboutfeetCategory(models.Model):
    cname = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_category'


class AllaboutfeetColors(models.Model):
    color = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_colors'


class AllaboutfeetProducts(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=25)
    price = models.IntegerField()
    dprice = models.IntegerField(blank=True, null=True)
    desciption = models.CharField(max_length=100, blank=True, null=True)
    imagename = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_products'


class AllaboutfeetProductsizes(models.Model):
    id = models.AutoField()
    pid = models.OneToOneField(AllaboutfeetProducts, models.DO_NOTHING, db_column='pid', primary_key=True)
    size = models.ForeignKey('AllaboutfeetSizes', models.DO_NOTHING, db_column='size')

    class Meta:
        managed = False
        db_table = 'allaboutfeet_productsizes'
        unique_together = (('pid', 'size'),)


class AllaboutfeetProductsubs(models.Model):
    pid = models.OneToOneField(AllaboutfeetProducts, models.DO_NOTHING, db_column='pid', primary_key=True)
    bname = models.ForeignKey(AllaboutfeetBrand, models.DO_NOTHING, db_column='bname', blank=True, null=True)
    cname = models.ForeignKey(AllaboutfeetCategory, models.DO_NOTHING, db_column='cname', blank=True, null=True)
    sname = models.ForeignKey('AllaboutfeetStyle', models.DO_NOTHING, db_column='sname', blank=True, null=True)
    color = models.ForeignKey(AllaboutfeetColors, models.DO_NOTHING, db_column='color', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_productsubs'


class AllaboutfeetSizes(models.Model):
    size = models.CharField(primary_key=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_sizes'


class AllaboutfeetStyle(models.Model):
    sname = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'allaboutfeet_style'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
