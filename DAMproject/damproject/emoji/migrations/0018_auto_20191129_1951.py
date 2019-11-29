# Generated by Django 2.2.6 on 2019-11-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0017_user_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='path',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='like_images',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='portrait',
            field=models.CharField(default='', max_length=5000000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]