# Generated by Django 2.2.1 on 2019-05-13 06:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_remove_product_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='upvotes',
            field=models.ManyToManyField(default=None, related_name='products_product_related', related_query_name='products_products', to=settings.AUTH_USER_MODEL),
        ),
    ]