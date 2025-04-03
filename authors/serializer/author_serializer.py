from rest_framework  import serializers
from ..models import Author


class AuthorListSerializer(serializers.ModelSerializer):
    class meta:
        model=Author
        fields=['name','address','contact','email','book_published','bio','created_date','updated_date']





#class to retrieve from the models:
class AuthorsRetrieveSerializer(serializers.ModelSerializer):
    class meta:
        model=Author
        fields=['name','address','contact','email']

#class to write from the models
class AuthorsWriteSerializer(serializers.ModelSerializer):
    class meta:
        model=Author
        fields='_all_'