

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_profile_city_profile_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AlterField(
            model_name='expense',
            name='Category',
            field=models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Entertainment', 'Entertainment'), ('Personal spending', 'Personal spending'), ('Medical', 'Medical'), ('Insurance', 'Insurance'), ('Banking', 'Banking'), ('Other', 'Other')], default='Food', max_length=20),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_name',
            field=models.CharField(max_length=120),
        ),
    ]
