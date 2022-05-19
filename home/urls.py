from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.apis.viewsets import UserAccountViewset, BookViewset, IssueBookViewset, ReturnBookViewset, UserProfileViewset, ViewIssuedBookViewset
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'accounts', UserAccountViewset, basename="accounts")
router.register(r'book', BookViewset, basename="book")
router.register(r'issuebook', IssueBookViewset, basename="issuebook")
router.register(r'userprofile', UserProfileViewset, basename="userprofile")
router.register(r'viewissuedbook', ViewIssuedBookViewset, basename="viewissuedbook")
router.register(r'returnbook', ReturnBookViewset, basename="returnbook")


urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/gettoken/', obtain_auth_token),
]