# Generated by Django 4.2.5 on 2023-11-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_rename_myuploadfile_myuploadjournels'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclassnote',
            name='comments',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
