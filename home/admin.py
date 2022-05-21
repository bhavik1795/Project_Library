from django.contrib import admin 
from home.models import UserAccount, Book, IssueBook, ReturnBook
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  


class CustomUserAdmin(BaseUserAdmin):    
  
    list_display = ( 'id', 'email', 'user_type', 'is_staff', 'is_active', 'date_joined', 'first_name', 'last_name', 'phone_number')  
    list_filter = ('user_type', 'is_staff',)  
    fieldsets = (  
        ('User Credentials', {'fields': ('email', 'password')}),  
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'date_joined')}),  
        ('Permissions', {'fields': ('user_type', 'is_staff', 'is_active')}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'date_joined', 'password1', 'password2', 'is_staff', 'user_type', 'is_active',)}  
        ),  
    )  
    search_fields = ('email',)  
    ordering = ('email', 'id')  
    filter_horizontal = () 

admin.site.register(UserAccount, CustomUserAdmin)  

admin.site.register(Book)  
admin.site.register(IssueBook)  
admin.site.register(ReturnBook)  
