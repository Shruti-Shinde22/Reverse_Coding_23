# Generated by Django 4.1.1 on 2023-05-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_RC', '0015_remove_profile_curr_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='is_junior',
            field=models.BooleanField(default=True),
        ),
    ]
