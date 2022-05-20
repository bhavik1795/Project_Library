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
        fields = [ 'id', 'student_id', 'issued_date', 'book']




class ReturnBookSerializer(WritableNestedModelSerializer):
    
    class Meta:
        model = ReturnBook
        # fields = '__all__'

        fields = [ 'student_id', 'issuebook_id', 'book', 'return_date']





