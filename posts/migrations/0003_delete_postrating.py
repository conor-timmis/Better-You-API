# Generated by Django 4.2 on 2024-10-21 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postrating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostRating',
        ),
    ]
