# Generated by Django 4.1.3 on 2022-11-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customuser_biotext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='biotext',
            field=models.TextField(default=None, max_length=300, null=True),
        ),
    ]
