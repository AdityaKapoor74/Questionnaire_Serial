# Generated by Django 2.2.6 on 2019-10-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneByOne', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userresponses',
            options={'verbose_name_plural': 'User Responses'},
        ),
        migrations.AddField(
            model_name='userresponses',
            name='iteration',
            field=models.IntegerField(default=1),
        ),
    ]
