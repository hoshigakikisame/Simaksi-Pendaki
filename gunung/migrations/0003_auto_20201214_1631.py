# Generated by Django 3.0.2 on 2020-12-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gunung', '0002_auto_20201214_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gunung',
            name='thumbnail',
            field=models.ImageField(default='/123.jpg', upload_to='documents/'),
        ),
    ]
