# Generated by Django 2.2.1 on 2019-05-13 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_upvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='upvote',
        ),
    ]
