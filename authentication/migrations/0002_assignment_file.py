# Generated by Django 4.2.5 on 2023-10-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment_file',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('file_name1', models.CharField(max_length=255)),
                ('my_file1', models.FileField(upload_to='')),
            ],
        ),
    ]
