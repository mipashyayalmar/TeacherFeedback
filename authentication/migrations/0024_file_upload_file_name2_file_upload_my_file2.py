# Generated by Django 4.2.5 on 2023-10-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_myuploadfile_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_upload',
            name='file_name2',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='file_upload',
            name='my_file2',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]