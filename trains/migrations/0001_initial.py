# Generated by Django 2.2.4 on 2019-08-17 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.User')),
            ],
            options={
                'ordering': ['-date', 'users'],
                'get_latest_by': 'date',
            },
        ),
    ]
