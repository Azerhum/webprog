# Generated by Django 5.0.6 on 2024-06-19 02:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_accountuser_account_user_id'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='accountuser',
            new_name='myapp_accou_account_d6f119_idx',
            old_name='myapp_accou_account_5d0f2f_idx',
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='account_user_related_user',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
