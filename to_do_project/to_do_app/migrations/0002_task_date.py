# Generated by Django 5.0.1 on 2024-01-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-3-4'),
            preserve_default=False,
        ),
    ]
