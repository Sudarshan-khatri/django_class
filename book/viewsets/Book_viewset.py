from rest_framework import viewsets
from ..models import Book
from ..serializer.book_serializer import *
from ..utilities.pagination import PageNumberPagination


#class for viewsets:
class bookViewer(viewsets.ModelViewSet):
    serializer_class=BookListSerializers
    queryset=Book.objects.all().order_by('-id')
    pagination_class=PageNumberPagination





    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return BookWriteSerializer
        elif self.action =='retrieve':
            return BookRetrieveSerializers
        return super().get_serializer_class()