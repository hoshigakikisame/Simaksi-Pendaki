# Generated by Django 3.0.2 on 2020-12-13 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pendakian', '0002_auto_20201214_0150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='provinisi',
            new_name='provinsi',
        ),
        migrations.RenameField(
            model_name='solo',
            old_name='provinisi',
            new_name='provinsi',
        ),
    ]