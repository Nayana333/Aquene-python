# Generated by Django 3.0.5 on 2022-05-14 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aquene_app', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]