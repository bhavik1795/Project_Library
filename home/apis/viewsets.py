from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import UserAccount, Book, IssueBook, ReturnBook
from home.apis.serializers import UserAccountSerializer, BookSerializer, IssueBookSerializer , ReturnBookSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404




class UserAccountViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]



class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

class IssueBookViewset(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    
    def create(self, request, *args, **kwargs):
        print("request-------------------------", request.data)       #---> # {'csrfmiddlewaretoken': ['1mOnnVOFvqYwQmdtDKXBZ0dJHvMS5n7vdl9Gbg27Q2'], 'student_id': ['3'], 'book': ['2']}

        serializer = self.get_serializer(data=request.data)
        print("serializer-------------------------", serializer)      #---> # get_serializer returns the serializer instance that is used for validation & deserializing i/p and for serializing o/p

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)          # "perform_create" method is used for saving a new object instance.
        
        headers = self.get_success_headers(serializer.data)
        #  Location header that points to the URL of the new resource (newly created via POST Method)

        print("request.data.get('book')-------------------------", request.data.get('book')) #  books requested by the user 
        books= request.data.get('book')

        for book_id in books:
            print("book-------------------------", book_id)
            book = Book.objects.get(pk=book_id)
            print("book data-------------------------", book.book_count)
            book.book_count = book.book_count-1
            print("book data111-------------------------", book.book_count)
            book.save()

        # book = get_object_or_404(books, id=id)
        # book.book_count = book.book_count - 1
        # book.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def get_queryset(self):
        user = self.request.user
        return IssueBook.objects.filter(student_id=user)


class ReturnBookViewset(viewsets.ModelViewSet):
    
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Ret_book= request.data.get('book')
        for book_id in Ret_book:
                book = Book.objects.get(pk=book_id)
                book.book_count = book.book_count-1
                book.save()
        return Response(serializer.data)


#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]


#     def update(self, request, *args, **kwargs):
#         print("request-------------------------", request.data)
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         # print("request-----------------------------------------", request.data.get('book'))
#         Ret_book = request.data.get('book')
#         for book_id in Ret_book:
#                 book = Book.objects.get(pk=book_id)
#                 book.book_count = book.book_count+1
#                 book.save()
#         return Response(serializer.data)


#     def get_queryset(self):
#         user= self.request.user
#         return IssueBook.objects.filter(student_id=user)



class ViewIssuedBookViewset(viewsets.ModelViewSet):
    queryset = IssueBook.objects.all()
    serializer_class = IssueBookSerializer

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id']



class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        user = self.request.user
        return UserAccount.objects.filter(email=user)