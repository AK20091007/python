# Generated by Django 2.2.5 on 2022-11-10 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='student name')),
                ('pwd', models.CharField(max_length=32, verbose_name='student pwd')),
                ('age', models.IntegerField(verbose_name='student age')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='student balance')),
                ('enrollment_date', models.DateField(verbose_name='student enrollment date')),
                ('gender', models.BinaryField(choices=[(1, 'male'), (0, 'female')], verbose_name='student gender')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Department')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
