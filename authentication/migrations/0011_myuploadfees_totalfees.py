# Generated by Django 4.2.5 on 2023-10-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_myuploadfees'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfees',
            name='totalfees',
            field=models.IntegerField(default=None, max_length=9),
        ),
    ]
