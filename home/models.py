from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from .managers import CustomUserManager  
from django.utils.translation import gettext_lazy as _



class UserAccount(AbstractBaseUser, PermissionsMixin):
    GEEKS_CHOICES =(
    ("student", "student"),
    ("superadmin", "superadmin"),
    )
    
    username = None
    email = models.EmailField(_('email_address'), unique=True, max_length = 200) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    phone_number = models.IntegerField(default=0)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=50, choices=GEEKS_CHOICES)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'date_joined', 'user_type']  

    objects = CustomUserManager()

    def __str__(self):  
        return self.email  


class Book(models.Model):
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50, default=None)
    book_count = models.IntegerField(default=0)
    date_publisheded = models.DateField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)      # +" ["+str(self.id)+']'


class IssueBook(models.Model):
    student_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    issued_date = models.DateField(auto_now_add=True)
    

class ReturnBook(models.Model):
    issuebook_id = models.IntegerField()
    student_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    return_date = models.DateField(auto_now_add=True)


# class ReturnBook(models.Model):
#     issuebook_id = models.ForeignKey(IssueBook, on_delete=models.CASCADE)
#     book = models.ManyToManyField(Book)
#     return_date = models.DateField(auto_now_add=True)


    
