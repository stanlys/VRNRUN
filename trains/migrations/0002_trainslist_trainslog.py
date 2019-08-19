# Generated by Django 2.2.4 on 2019-08-19 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_unreguser'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Дата проведения тренировки')),
                ('comment', models.CharField(help_text='Коментарий к тренировке', max_length=100)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='TrainsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trains_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trains.TrainsLog')),
                ('unreguser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.UnRegUser')),
            ],
            options={
                'ordering': ['-trains_id'],
            },
        ),
    ]
