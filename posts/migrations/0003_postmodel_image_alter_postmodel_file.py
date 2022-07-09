# Generated by Django 4.0.6 on 2022-07-05 14:52

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postmodel_sees'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]