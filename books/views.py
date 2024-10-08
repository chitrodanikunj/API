from rest_framework import generics
from .models import book
from .serializers import bookSerializer

class bookList(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class = bookSerializer

class bookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = book.objects.all()
    serializer_class = bookSerializer

