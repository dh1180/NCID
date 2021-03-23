# Generated by Django 3.1 on 2021-03-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NCID', '0005_npc_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npc',
            name='images',
        ),
        migrations.AddField(
            model_name='npc',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
