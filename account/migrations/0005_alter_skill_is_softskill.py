# Generated by Django 3.2.9 on 2022-07-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_skill_is_softskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='is_softskill',
            field=models.BooleanField(),
        ),
    ]
