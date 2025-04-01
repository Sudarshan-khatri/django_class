from rest_framework import serializers
from ..models import Book


#listseralizer
class BookListSerializers(serializers.ModelSerializer):
    class meta:
        model=Book
        fields=['id','book_name','book_type','slug' ,'author''vol','book_publication','book_review','language']



class BookRetrieveSerializers(serializers.ModelSerializer):
    class meta:
        model=Book
        fields=['id','book_name','book_type','slug' ,'author''vol','book_publication','book_review','language']


class BookWriteSerializer(serializers.ModelSerializer):
    class meta:
        fields='_all_'