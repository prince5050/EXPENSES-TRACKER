from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User

SELECT_CATEGORY_CHOICES = [
    ("Food", "Food"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Entertainment", "Entertainment"),
    ("Other", "Other")
]


class Expense(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=120, unique=True)
    Category = models.CharField(max_length=20, choices=SELECT_CATEGORY_CHOICES, default='Food')
    # expense_type = models.CharField(max_length=120)
    amount = models.CharField(max_length=120)
    mode_of_payment = models.CharField(max_length=120)
    date_of_expense = models.DateTimeField(auto_now_add=False)
    month_of_expense = models.CharField(max_length=120,default=False)
    year_of_expense = models.CharField(max_length=120,default=False)
    def __str__(self):
        return self.expense_name
