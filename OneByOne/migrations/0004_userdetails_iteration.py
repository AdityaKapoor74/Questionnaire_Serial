# Generated by Django 2.2.6 on 2019-10-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneByOne', '0003_auto_20191010_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='iteration',
            field=models.IntegerField(default=1),
        ),
    ]
