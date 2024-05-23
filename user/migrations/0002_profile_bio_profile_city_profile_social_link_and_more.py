# Generated by Django 4.2.1 on 2023-06-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default='', max_length=200),
        ),
    ]
