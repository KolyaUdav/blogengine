# Generated by Django 2.1.5 on 2019-02-06 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190207_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='tags',
        ),
    ]
