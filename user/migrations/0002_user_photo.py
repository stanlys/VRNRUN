# Generated by Django 2.2.4 on 2019-08-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=123456, upload_to=''),
            preserve_default=False,
        ),
    ]
