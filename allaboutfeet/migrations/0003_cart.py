# Generated by Django 3.0.5 on 2020-04-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allaboutfeet', '0002_auto_20200429_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'allaboutfeet_cart',
                'managed': False,
            },
        ),
    ]
