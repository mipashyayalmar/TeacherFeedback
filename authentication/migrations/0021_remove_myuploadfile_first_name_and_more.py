# Generated by Django 4.2.5 on 2023-10-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_myuploadfile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadfile',
            name='first_name',
        ),
        migrations.AddField(
            model_name='myuploadfile',
            name='full_name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
