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
    ("Personal spending", "Personal spending"),
    ("Medical", "Medical"),
    ("Insurance", "Insurance"),
    ("Banking", "Banking"),
    ("Other", "Other")

]

class Profile(models.Model):
    status_list = (
        ('1', 'Active'),
        ('2', 'Deactive'),
        ('3', 'Delete')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=50, choices=status_list, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
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
