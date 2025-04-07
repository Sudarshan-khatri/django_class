from rest_framework import serializers
from ..models import Book


#listseralizer
class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','book_name','book_type','slug' ,'author','vol','book_publication','book_review','language']



class BookRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','book_name','book_type','slug' ,'author''vol','book_publication','book_review','language']


class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"