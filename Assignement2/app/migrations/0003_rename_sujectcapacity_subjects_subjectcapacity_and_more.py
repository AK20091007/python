# Generated by Django 4.1.3 on 2022-11-30 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_subjects_sujectcapacity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='sujectcapacity',
            new_name='subjectcapacity',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='sujectid',
            new_name='subjectid',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='sujectinstructor',
            new_name='subjectinstructor',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='sujectopenseats',
            new_name='subjectopenseats',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='sujecttitle',
            new_name='subjecttitle',
        ),
    ]
