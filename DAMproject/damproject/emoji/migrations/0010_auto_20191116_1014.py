# Generated by Django 2.2.6 on 2019-11-16 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0009_auto_20191116_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.CreateModel(
            name='Image2Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='emoji.Image')),
                ('tags', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='emoji.Tag')),
            ],
        ),
    ]
