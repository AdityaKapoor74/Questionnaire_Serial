# Generated by Django 2.2.6 on 2019-10-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneByOne', '0010_auto_20191013_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stimuli',
            name='stimuli',
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_1',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_10',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_2',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_3',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_4',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_5',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_6',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_7',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_8',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='stimuli',
            name='stimuli_9',
            field=models.ImageField(default='Contrast00.png', upload_to='images/'),
        ),
    ]
