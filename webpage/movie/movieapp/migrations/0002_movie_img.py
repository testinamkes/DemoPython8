# Generated by Django 4.2.8 on 2023-12-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='wwww', upload_to='pics'),
            preserve_default=False,
        ),
    ]
