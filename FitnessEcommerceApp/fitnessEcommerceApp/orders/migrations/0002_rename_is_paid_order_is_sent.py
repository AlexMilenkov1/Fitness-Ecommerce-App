# Generated by Django 5.1.3 on 2024-12-01 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_paid',
            new_name='is_sent',
        ),
    ]
