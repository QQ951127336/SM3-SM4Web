# Generated by Django 2.0.5 on 2018-05-22 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileServer', '0003_file_hashhex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='fileServer/static/files'),
        ),
    ]
