# Generated by Django 4.1.5 on 2023-01-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electron', '0005_fileinfo_err_alter_fileinfo_cont'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='val',
            field=models.FloatField(default=1),
        ),
    ]
