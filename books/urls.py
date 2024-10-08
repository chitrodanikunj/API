from django.urls import path
from .views import bookList, bookDetail

urlpatterns = [
    path('books/', bookList.as_view(), name='book_list'),
    path('books/<int:pk>/', bookDetail.as_view(), name='book_detail'),
]
