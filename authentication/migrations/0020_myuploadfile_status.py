# Generated by Django 4.2.5 on 2023-10-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_myuploadfile_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfile',
            name='status',
            field=models.CharField(max_length=12, null=True),
        ),
    ]