from .models import waifu
from rest_framework import serializers


class waifuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = waifu
        fields = ('name','age','id','type','gender','url','img','orName'
                  ,'roName','placeOf','dateBirth','height','weight',"bust",'hip'
                  ,'waist','bloodType','description'
                  ,'popularity','like','trash','likeCount','trashCount','isWaifu','serie')
class imageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = waifu
        fields = ('id','name')
