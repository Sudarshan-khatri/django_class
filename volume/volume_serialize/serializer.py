from rest_framework  import serializers
from ..models import Volume


class VolumeListSerializer(serializers.ModelSerializer):
    class meta:
        model=Volume
        fields=[ 'v_name','created_date','update_date']





#class to retrieve from the models:
class VolumeRetrieveSerializer(serializers.ModelSerializer):
    class meta:
        model=Volume
        fields=['v_name','created_date']

#class to write from the models
class VolumeWriteSerializer(serializers.ModelSerializer):
    class meta:
        model=Volume
        fields='_all_'