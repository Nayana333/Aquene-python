# Generated by Django 4.0.4 on 2022-05-14 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aquene_app', '0008_orph_don_orph_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orph_don',
            old_name='orph_id',
            new_name='orph',
        ),
    ]