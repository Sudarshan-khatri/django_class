from rest_framework import serializers
from ..models import Publication



#class to list the attribute of the models publication
class PublicationListSerializer(serializers.ModelSerializer):
    class meta:
        model=Publication
        fields=[ 'name','rating','book_name','description','created_date','updated_date']


#class to retrieve the attribute of the model :
class PublicationRetrieveSerializer(serializers.ModelSerializer):
    class meta:
        model=Publication
        fields=[ 'name','rating','book_name']


#class to 
#class to write from the models
class PublicationWriteSerializer(serializers.ModelSerializer):
    class meta:
        model=Publication
        fields='_all_'