# Generated by Django 4.1.5 on 2023-02-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_expense_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_of_expense',
            field=models.DateTimeField(),
        ),
    ]
