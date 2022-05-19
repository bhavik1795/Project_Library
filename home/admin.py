from django.contrib import admin 
from home.models import UserAccount, Book, IssueBook, ReturnBook


admin.site.register(UserAccount)  
admin.site.register(Book)  
admin.site.register(IssueBook)  
admin.site.register(ReturnBook)  
