# Generated by Django 2.2.6 on 2019-11-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0016_user_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='path',
            field=models.CharField(default='', max_length=200),
        ),
    ]