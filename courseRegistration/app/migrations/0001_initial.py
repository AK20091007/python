# Generated by Django 4.1.3 on 2022-11-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.IntegerField(verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('instructor', models.CharField(max_length=150, verbose_name='Instructor')),
                ('capacity', models.IntegerField(verbose_name='Capacity')),
                ('openSeats', models.IntegerField(verbose_name='Openseats')),
            ],
        ),
    ]