# Generated by Django 4.2.5 on 2023-10-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_myuploadfees_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuploadfile',
            name='f_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
