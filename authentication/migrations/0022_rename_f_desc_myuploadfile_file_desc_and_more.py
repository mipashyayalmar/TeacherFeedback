# Generated by Django 4.2.5 on 2023-10-28 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_remove_myuploadfile_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuploadfile',
            old_name='f_desc',
            new_name='file_desc',
        ),
        migrations.RenameField(
            model_name='myuploadfile',
            old_name='f_name',
            new_name='file_name',
        ),
        migrations.AlterField(
            model_name='myuploadfile',
            name='date_field',
            field=models.DateField(auto_now=True),
        ),
    ]
