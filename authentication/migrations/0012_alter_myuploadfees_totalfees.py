# Generated by Django 4.2.5 on 2023-10-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_myuploadfees_totalfees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuploadfees',
            name='totalfees',
            field=models.CharField(max_length=10),
        ),
    ]
