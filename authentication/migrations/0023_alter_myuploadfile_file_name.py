# Generated by Django 4.2.5 on 2023-10-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_rename_f_desc_myuploadfile_file_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuploadfile',
            name='file_name',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
