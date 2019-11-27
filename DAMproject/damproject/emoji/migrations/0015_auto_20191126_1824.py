# Generated by Django 2.2.6 on 2019-11-26 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0014_auto_20191126_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(default='', max_length=500)),
                ('image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='emoji.Image')),
            ],
        ),
    ]