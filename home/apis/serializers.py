from rest_framework import serializers
from home.models import UserAccount, Book, IssueBook, ReturnBook
from drf_writable_nested.serializers import WritableNestedModelSerializer



class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ['id','email', 'first_name', 'last_name', 'date_joined', 'user_type', 'is_staff', 'is_active', 'password']
        
    def create(self, validated_data):
            user = UserAccount.objects.create_user(**validated_data)
            return user

    

class BookSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'author_name', 'book_count', 'date_publisheded', 'date_created']
        




class IssueBookSerializer(WritableNestedModelSerializer):

    class Meta:
        model = IssueBook
        fields = [ 'student_id', 'issued_date', 'book']




class ReturnBookSerializer(WritableNestedModelSerializer):
    class Meta:
        model = ReturnBook
        fields = '__all__'

        

    # def create(self, validated_data, *args, **kwargs):
    #     user = super(IssueBookSerializer, self).create(validated_data)
    #     user.save()
    #     return user




