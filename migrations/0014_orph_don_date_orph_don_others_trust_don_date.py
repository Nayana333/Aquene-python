# Generated by Django 4.0.5 on 2022-11-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquene_app', '0013_remove_sponsor_trust_sponsor_firm'),
    ]

    operations = [
        migrations.AddField(
            model_name='orph_don',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='orph_don',
            name='others',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='trust_don',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
