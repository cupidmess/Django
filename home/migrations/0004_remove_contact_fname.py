# Generated by Django 5.0.7 on 2024-08-03 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_fname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='fname',
        ),
    ]
