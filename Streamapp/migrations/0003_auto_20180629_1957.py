# Generated by Django 2.0.6 on 2018-06-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Streamapp', '0002_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
