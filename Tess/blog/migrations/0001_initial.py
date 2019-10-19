# Generated by Django 2.2.5 on 2019-10-19 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('document', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]