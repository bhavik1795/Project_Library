from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import UserAccount, Book, IssueBook, ReturnBook
from home.apis.serializers import UserAccountSerializer, BookSerializer, IssueBookSerializer , ReturnBookSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend



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
        # stu_id = request.data.get('student_id')
        # print("stu_id----------------------",stu_id)
        # if stu_id==user.id:

            # print("request-------------------------", request.data)       #---> # {'csrfmiddlewaretoken': ['1mOnnVOFvqYwQmdtDKXBZ0dJHvMS5n7vdl9Gbg27Q2'], 'student_id': ['3'], 'book': ['2']}
            serializer = self.get_serializer(data=request.data)
            # print("serializer-------------------------", serializer)      #---> # get_serializer returns the serializer instance that is used for validation & deserializing i/p and for serializing o/p
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)          # "perform_create" method is used for saving a new object instance.
            headers = self.get_success_headers(serializer.data)
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
        # else:
        #     return Response({'msg' : 'Selected Wrong Student_id'}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        user = self.request.user
        print("Self_User--------------------------", user.id, user)
        return IssueBook.objects.filter(student_id=user)


class ReturnBookViewset(viewsets.ModelViewSet):
    
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
        
        # for id in delete_record:
        #     print("issued_id---------------------", id)
        #     # i_book = IssueBook.objects.get(student_id=id)
        #     i_book = IssueBook.objects.filter(id=id)
        #     # print("i_book---------------------", i_book)
        #     i_book.delete()


    # def get_queryset(self):
    #     user= self.request.user
    #     return ReturnBook.objects.filter(student_id=user)



class ViewIssuedBookViewset(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id']

    def get_queryset(self):
        user= self.request.user
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserAccount.objects.filter(email=user)