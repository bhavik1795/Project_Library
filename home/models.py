from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from .managers import CustomUserManager  
from django.utils.translation import gettext_lazy as _

# from django.dispatch import receiver
# from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.core.mail import send_mail


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



#----------------------- StudyGyan (Reset Password Email) ----------------------------------------------
# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Some website title"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email]
#     )    
