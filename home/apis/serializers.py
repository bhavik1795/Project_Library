from dataclasses import field
from pyexpat import model
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



class ChangePasswordSerializer(serializers.Serializer):

    password = serializers.CharField(max_length=250, style={'input_type':'password'}, write_only=True)

    class Meta:
        fields = ['password']

    def validate(self,attrs):
        password = attrs.get('password')
        print("password-------------------------",password)

        # print("self.context------------------------",self.context)
        user = self.context.get('student_id')
        print("user------------------------",user)
        user.set_password(password)
        user.save()
        return attrs

    def create(self, validated_data):
        return UserAccount.objects.create(**validated_data)





#-----------------------StudyGyan---------------------------------------------

# class ChangePasswordSerializer(serializers.Serializer):

    # model = UserAccount

    # old_password = serializers.CharField(required=True)
    # new_password = serializers.CharField(required=True)


#------------------------------------gutsytechster----------------------------------------------------

# class PasswordChangeSerializer(serializers.Serializer):

#     current_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

#     def validate_current_password(self, value):
#         if not self.context['request'].user.check_password(value):
#             raise serializers.ValidationError('Current password does not match')
#         return value

#     def validate_new_password(self, value):
#         password_validation.validate_password(value)
#         return value