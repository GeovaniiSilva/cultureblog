# Generated by Django 2.2.5 on 2019-09-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190906_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=30, unique=True, verbose_name='Slug'),
        ),
    ]
