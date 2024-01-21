# Generated by Django 5.0.1 on 2024-01-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_usertype_alter_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('customer', 'Customer'), ('vendor', 'Vendor')], max_length=20),
        ),
    ]
