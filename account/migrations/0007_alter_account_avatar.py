# Generated by Django 4.0.6 on 2022-07-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='C:\\PROJECTS\\Backend\\devtools\\media\x07vatars\\IMG_20220114_104710_103.JPG', upload_to='avatars/'),
        ),
    ]
