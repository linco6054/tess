# Generated by Django 2.2.5 on 2019-10-19 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_admin_post_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_post',
            old_name='date',
            new_name='start_date',
        ),
    ]
