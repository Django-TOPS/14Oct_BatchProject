# Generated by Django 3.1.4 on 2021-01-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('myfile', models.FileField(upload_to='upload')),
                ('comment', models.TextField()),
            ],
        ),
    ]