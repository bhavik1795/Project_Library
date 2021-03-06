from os import stat
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import UserAccount, Book, IssueBook, ReturnBook
from home.apis.serializers import UserAccountSerializer, BookSerializer, IssueBookSerializer, ReturnBookSerializer , ChangePasswordSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.views import APIView

class UserAccountViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]


class UserRegistrationViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def list(self, request, *args, **kwargs):
        pass
        return Response({'msg' : 'Fill the below form to register'}, status=status.HTTP_400_BAD_REQUEST)



class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

class IssueBookViewset(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        
        # user = self.request.user
        # print("user_id----------------------",user.id)
        # stu_id = request.data.get('student_id')
        # print("stu_id----------------------",stu_id)
        # u_id = user.id
        # if stu_id==u_id:

            print("request-------------------------", request.data)       #---> # {'csrfmiddlewaretoken': ['1mOnnVOFvqYwQmdtDKXBZ0dJHvMS5n7vdl9Gbg27Q2'], 'student_id': ['3'], 'book': ['2']}
            serializer = self.get_serializer(data=request.data) #, context={'student_id':request.user.id})
            # print("serializer-------------------------", serializer)      #---> # get_serializer returns the serializer instance that is used for validation & deserializing i/p and for serializing o/p
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)          # "perform_create" method is used for saving a new object instance.
            headers = self.get_success_headers(serializer.data)
            # print("headers-------------------------", headers)      #---> # get_serializer returns the serializer instance that is used for validation & deserializing i/p and for serializing o/p
            #  Location header that points to the URL of the new resource (newly created via POST Method)

        

            # print("request.data.get('book')-------------------------", request.data.get('book')) #  books requested by the user 
            books= request.data.get('book')

            for book_id in books:
                # print("book-------------------------", book_id)
                book = Book.objects.get(pk=book_id)
                # print("book data-------------------------", book.book_count)
                book.book_count = book.book_count-1
                # print("book data111-------------------------", book.book_count)
                book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # return Response({'msg' : 'Selected Wrong Student_id'}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        user = self.request.user
        print("Self_User--------------------------", user.id, user)
        return IssueBook.objects.filter(student_id=user)


class ReturnBookViewset(viewsets.ModelViewSet):
    
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
    
        print('All_data----------------------', request.data)

        Ret_book= request.data.get('book')
        print('data----------------------', request.data.get('book'))
        for book_id in Ret_book:
                book = Book.objects.get(pk=book_id)
                book.book_count = book.book_count+1
                book.save()


        delete_id = request.data.get('issuebook_id')
        print('**_id----------------------', delete_id)
        delete_record = IssueBook.objects.filter(id=delete_id)
        delete_record.delete()

        return Response(serializer.data, headers=headers)

    # def get_queryset(self):
    #     user= self.request.user
    #     return ReturnBook.objects.filter(student_id=user)



class ViewIssuedBookViewset(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id']

    def get_queryset(self):
        user = self.request.user
        return IssueBook.objects.filter(student_id=user)



class ViewReturnedBookViewset(viewsets.ModelViewSet):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['student_id']



class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserAccount.objects.filter(email=user)

class StudentIssuedBooksViewset(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id']





class ChangePasswordViewset(viewsets.ModelViewSet):

    queryset = UserAccount.objects.all()
    serializer_class = ChangePasswordSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'student_id':request.user})
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'msg':'Password changed successfully'}, status=status.HTTP_200_OK, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








#--------------------------GeekyShow-------------------------------

# class ChangePasswordViewset(APIView):
#     def post(self, request, format=None):
#         serializer = ChangePasswordSerializer(data=request.data, context={'student_id':request.user})
#         if serializer.is_valid(raise_exception=True):
#             return Response({'msg':'Password changed successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#--------------------------StudyGyan----------------------------------


# class ChangePasswordViewset(viewsets.ModelViewSet): #  (generics.UpdateAPIView) 

#     queryset = UserAccount.objects.all()
#     serializer_class = ChangePasswordSerializer

#     # serializer_class = ChangePasswordSerializer
#     # model = UserAccount
#     # permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }

#             return Response(response)

#          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#--------------------------gutsytechster-------------------------------

# class AuthViewSet(viewsets.GenericViewSet):
#     serializer_class = PasswordChangeSerializer


#     @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
#     def password_change(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         request.user.set_password(serializer.validated_data['new_password'])
#         request.user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)